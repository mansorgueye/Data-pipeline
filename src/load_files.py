# Import necessary modules
from models import Drug, Publication, ClinicalTrial
import csv
import json
from datetime import datetime

# Function to read drugs from a CSV file and return a list of Drug objects
def read_drugs(file_path):
    # Open the file for reading
    with open(file_path, 'r') as f:
        # Create a CSV reader object from the file
        reader = csv.DictReader(f)
        # Iterate over the rows in the CSV file
        # and create a Drug object for each row
        drugs = [Drug(row['atccode'], row['drug']) for row in reader]
    # Return the list of Drug objects
    return drugs

# Function to read PubMed publications from a CSV file and return a list of Publication objects
def read_pubmed(file_path):
    # Open the file for reading
    with open(file_path, 'r') as f:
        # Create a CSV reader object from the file
        reader = csv.DictReader(f)
        # Create an empty list to hold the Publication objects
        pubmed=[]
        # Iterate over the rows in the CSV file
        for row in reader:
            # Check the format of the date field and convert it to a datetime object
            if '/' in row['date']:
                # Convert date in format dd/mm/yyyy
                date_obj = datetime.strptime(row['date'], '%d/%m/%Y')
            elif " " in row['date'] :
                # Convert date in format d Month yyyy
                date_obj = datetime.strptime(row['date'], '%d %B %Y')
            elif "-" in row['date'] : 
                # Convert date in format yyy-mm-dd
                date_obj = datetime.strptime(row['date'], '%Y-%m-%d')
            # Store the datetime object back to the CSV row
            row['date'] = date_obj.strftime('%Y-%m-%d')
            # Create a Publication object for the row and add it to the list
            pubmed.append(Publication(row['id'], row['title'], row['date'],row['journal']) )
    # Return the list of Publication objects
    return pubmed

# Define a function to read in JSON files containing PubMed data
def read_pubmed_json(file_path):
    
    # Open the JSON file
    with open(file_path, 'r') as f:
        # Load the JSON data
        pubmed_json = json.load(f)
        # Create an empty list to store PubMed publications
        pubmed=[]
        # Iterate over each row in the JSON data
        for row in pubmed_json:
            # Check if the date in the row contains a forward slash '/'
            if '/' in row['date']:
                # Convert date in format dd/mm/yyyy
                date_obj = datetime.strptime(row['date'], '%d/%m/%Y')
            # If the date contains a space ' ', assume it is in format d Month yyyy
            elif " " in row['date'] :
                # Convert date in format d Month yyyy
                date_obj = datetime.strptime(row['date'], '%d %B %Y')
            # If the date contains a hyphen '-', assume it is in format yyy-mm-dd
            elif "-" in row['date'] : 
                # Convert date in format yyy-mm-dd
                date_obj = datetime.strptime(row['date'], '%Y-%m-%d')
            # Store the datetime object back to the row with the date formatted as yyy-mm-dd
            row['date'] = date_obj.strftime('%Y-%m-%d')
            # Append the row as a Publication object to the pubmed list
            pubmed.append(Publication(row['id'], row['title'], row['date'],row['journal']))
    # Return the list of PubMed publications
    return pubmed

# Define a function to read in CSV files containing clinical trial data
def read_clinical_trials(file_path):
     
    # Open the CSV file
    with open(file_path, 'r') as f:
        # Use the csv module to read in the CSV data
        reader = csv.DictReader(f)
        # Create an empty list to store clinical trials
        trials=[]
        # Iterate over each row in the CSV data
        for row in reader:
            # Check if the date in the row contains a forward slash '/'
            if '/' in row['date']:
                # Convert date in format dd/mm/yyyy
                date_obj = datetime.strptime(row['date'], '%d/%m/%Y')
            # If the date contains a space ' ', assume it is in format d Month yyyy
            else:
                # Convert date in format d Month yyyy
                date_obj = datetime.strptime(row['date'], '%d %B %Y')
            # Store the datetime object back to the row with the date formatted as yyy-mm-dd
            row['date'] = date_obj.strftime('%Y-%m-%d')
            # Append the row as a ClinicalTrial object to the trials list
            trials.append(ClinicalTrial(row['id'], row['scientific_title'], row['date'],row['journal'])) 
    # Return the list of clinical trials
    return trials