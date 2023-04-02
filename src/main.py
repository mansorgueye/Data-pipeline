import os  # Import the os module to interact with the operating system
import apache_beam as beam  # Import the Apache Beam module for data processing
from config import DRUGS_FILE, PUBMED_CSV_FILE, PUBMED_JSON_FILE, CLINICAL_TRIALS_FILE, OUTPUT_FILE, LOGS_DIR  # Import several file paths from the config.py file
from load_files import read_drugs, read_pubmed, read_pubmed_json, read_clinical_trials  # Import several functions from the load_files.py file
from pipeline import create_pipeline  # Import a function from the pipeline.py file
# Please uncommnent the following line to run the pipeline on with DataFlow
# from apache_beam.options.pipeline_options import PipelineOptions, GoogleCloudOptions, StandardOptions

from datetime import datetime  # Import the datetime module to work with dates and times
import logging  # Import the logging module for debugging and error logging

# Set up logging configuration
LOG_FILE_NAME = "Log_" + str(datetime.now()) + ".log"  # Create a log file name with the current timestamp
LOG_PATH = os.path.join(LOGS_DIR, LOG_FILE_NAME)  # Create the full path for the log file

logging.basicConfig(filename=LOG_PATH, level=logging.INFO)  # Set up the logging configuration to write to the log file

if __name__ == '__main__':
    drugs = read_drugs(DRUGS_FILE)  # Load the drugs data from a CSV file using the read_drugs function
    logging.info('Drugs file loaded')  # Log that the drugs file has been successfully loaded
    pubmed_csv = read_pubmed(PUBMED_CSV_FILE)  # Load the pubmed data from a CSV file using the read_pubmed function
    logging.info('Pubmed csv file loaded')  # Log that the pubmed CSV file has been successfully loaded
    pubmed_json = read_pubmed_json(PUBMED_JSON_FILE)  # Load the pubmed data from a JSON file using the read_pubmed_json function
    logging.info('Pubmed json file loaded')  # Log that the pubmed JSON file has been successfully loaded
    trials = read_clinical_trials(CLINICAL_TRIALS_FILE)  # Load the clinical trials data from a JSON file using the read_clinical_trials function
    logging.info('Clinical trials json file loaded')  # Log that the clinical trials file has been successfully loaded
    pubs = pubmed_csv + pubmed_json  # Merge the pubmed data from the CSV and JSON files
    logging.info('Clinical trials csv file and json file merge')  # Log that the pubmed CSV and JSON files have been merged
    logging.info('All data needed to run the pipeline is loaded')  # Log that all required data has been loaded
    options=None 
# Please uncommnent the following code block and update parameters to run the pipeline on with DataFlow 
#     options = PipelineOptions(
#     runner='DataflowRunner',
#     project=None',
#     region=None,
#     job_name=None,
#     temp_location=None,
#     staging_location=None,
#     setup_file=None
# )
    pipeline = create_pipeline(drugs, pubs, trials, OUTPUT_FILE,options=options)  # Create a Beam pipeline using the create_pipeline function
    run = pipeline.run()  # Run the pipeline
    logging.info('Pipeline running')  # Log that the pipeline is running
    run.wait_until_finish()  # Wait until the pipeline has finished
    logging.info('Pipeline completed successfully')  # Log that the pipeline has completed successfully
    logging.info('Path to the resulting json file:{} '.format(OUTPUT_FILE))  # Log the path to the resulting JSON file
