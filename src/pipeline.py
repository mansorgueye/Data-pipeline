import json
import apache_beam as beam

# Create a DoFn class to define the data transformation logic
class LinkGraph(beam.DoFn):
    def process(self, element ):
        # Extract the input data from the element tuple
        drug, pubs, trials= element
        # Initialize empty lists to store the drug mentions in publications, clinical trials, and journals
        journal_drug_mentions = []
        pub_drug_mentions = []
        trial_drug_mentions = []
        
        # Collect all drug mentions in each publication
        for pub in pubs:
            # Check if the drug name is mentioned in the publication title
            if drug.drug_name.lower() in pub.title.lower():
                # If so, add the publication ID, title, and date to the pub_drug_mentions list
                pub_drug_mentions.append({ "id": pub.id, "title":pub.title,"date": pub.date})
                # If this is the first time this drug was mentioned in this journal on this date, add the journal and date to the journal_drug_mentions list
                if {"journal": pub.journal,"date": pub.date} not in journal_drug_mentions:
                    journal_drug_mentions.append ({"journal": pub.journal,"date": pub.date}) 
        
        # Collect all drug mentions in each clinical trial
        for trial in trials:
            # Check if the drug name is mentioned in the scientific title of the trial
            if drug.drug_name.lower() in trial.scientific_title.lower() :
                # If so, add the trial ID, scientific title, and date to the trial_drug_mentions list
                trial_drug_mentions.append ({"id": trial.id, "scientific_title":trial.scientific_title, "date": trial.date}) 
                # If this is the first time this drug was mentioned in this journal on this date, add the journal and date to the journal_drug_mentions list
                if {"journal": trial.journal,"date": trial.date} not in journal_drug_mentions:
                    journal_drug_mentions.append ({"journal": trial.journal,"date": trial.date}) 

        # Construct the link graph for the drug
        link_graph={
            "atc_code": drug.atc_code,
            "drug_name": drug.drug_name,
            "pubmed": pub_drug_mentions,
            "clinical_trials": trial_drug_mentions,
            "journals": journal_drug_mentions
        }
        # Return the link graph as a generator object to the pipeline
        yield link_graph

# Create a function to define the Beam pipeline
def create_pipeline(drugs, pubs, trials, output_path, options):
    with beam.Pipeline(options=options) as p:
        # Create PCollections from lists of Objects 
        drugs_pcoll = p | "Create drugs PCollection" >> beam.Create(drugs)
        pubs_pcoll = p | "Create publications PCollection" >> beam.Create(pubs)
        trials_pcoll = p | "Create clinical trials PCollection" >> beam.Create(trials)
        
        # Create a drug-journal PCollection by joining the drugs, publications, and clinical trials, and processing the data with the LinkGraph DoFn
        drug_journal_pcoll = (drugs_pcoll | "Join drugs with journals" >>beam.Map(lambda drug: (drug, pubs, trials))
                             | "Join drug-journal" >> beam.ParDo(LinkGraph())
                             # Convert the PCollection to a single dictionary element
                             |'ToDist' >> beam.combiners.ToList()
                             |"Map" >> beam.Map(lambda x:{"drugs":x})
                            # Convert the PCollection to a JSON-formatted string
                             |'ToJson' >> beam.Map(json.dumps)
                             # Output the PCollection as a JSON file 
                             | "Write drug-journal links to file" >> beam.io.WriteToText(output_path,file_name_suffix='.json', shard_name_template='')
                             )
    return p
