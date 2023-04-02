import csv
import json
from datetime import date

# Define a Drug class to store information about drugs
class Drug:
    def __init__(self, atc_code, drug_name):
        self.atc_code = atc_code   # Anatomical Therapeutic Chemical (ATC) code for the drug
        self.drug_name = drug_name  # Name of the drug

# Define a Publication class to store information about publications related to drugs
class Publication:
    def __init__(self, id, title, date: date, journal):
        self.id = id   # Unique identifier for the publication
        self.title = title   # Title of the publication
        self.date=date   # Publication date
        self.journal = journal   # Name of the journal where the publication was published

# Define a ClinicalTrial class to store information about clinical trials related to drugs
class ClinicalTrial:
    def __init__(self, id,scientific_title,date: date ,journal):
        self.id = id   # Unique identifier for the clinical trial
        self.scientific_title = scientific_title   # Title of the clinical trial
        self.date=date   # Publication date
        self.journal = journal   # Name of the journal where the clinical trial was published
