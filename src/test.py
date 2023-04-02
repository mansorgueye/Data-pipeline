# import necessary modules
from config import DRUGS_FILE, PUBMED_CSV_FILE, PUBMED_JSON_FILE, CLINICAL_TRIALS_FILE
from models import Drug, Publication, ClinicalTrial
from load_files import read_drugs, read_pubmed, read_pubmed_json, read_clinical_trials
import unittest

# define a class to test main functionality
class TestMain(unittest.TestCase):
    
    # set up initial variables
    def setUp(self):
        self.drugs_file = DRUGS_FILE
        self.pubmed_file = PUBMED_CSV_FILE
        self.pubmed_json_file = PUBMED_JSON_FILE
        self.trials_file = CLINICAL_TRIALS_FILE

    # test if drugs can be read from file and loaded into Drug objects
    def test_read_drugs(self):
        drugs = read_drugs(self.drugs_file)
        self.assertIsInstance(drugs, list)  # check if drugs are loaded into a list
        self.assertGreater(len(drugs), 0)  # check if the list has more than 0 drugs
        self.assertIsInstance(drugs[0], Drug)  # check if the first element of the list is a Drug object

    # test if publications can be read from CSV file and loaded into Publication objects
    def test_read_pubmed(self):
        pubmed = read_pubmed(self.pubmed_file)
        self.assertIsInstance(pubmed, list)  # check if publications are loaded into a list
        self.assertGreater(len(pubmed), 0)  # check if the list has more than 0 publications
        self.assertIsInstance(pubmed[0], Publication)  # check if the first element of the list is a Publication object
    
    # test if publications can be read from JSON file and loaded into Publication objects
    def test_read_pubmed_json(self):
        pubmed = read_pubmed_json(self.pubmed_json_file)
        self.assertIsInstance(pubmed, list)  # check if publications are loaded into a list
        self.assertGreater(len(pubmed), 0)  # check if the list has more than 0 publications
        self.assertIsInstance(pubmed[0], Publication)  # check if the first element of the list is a Publication object

    # test if clinical trials can be read from file and loaded into ClinicalTrial objects
    def test_read_clinical_trials(self):
        trials = read_clinical_trials(self.trials_file)
        self.assertIsInstance(trials, list)  # check if clinical trials are loaded into a list
        self.assertGreater(len(trials), 0)  # check if the list has more than 0 clinical trials
        self.assertIsInstance(trials[0], ClinicalTrial)  # check if the first element of the list is a ClinicalTrial object
      
# if the current file is being run as the main program, run the tests
if __name__ == '__main__':
    unittest.main()
