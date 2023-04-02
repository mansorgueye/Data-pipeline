import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(ROOT_DIR, '..', 'data')
RESULTS_DIR = os.path.join(ROOT_DIR, '..', 'outputs')
LOGS_DIR = os.path.join(ROOT_DIR, '..', 'logs')

DRUGS_FILE = os.path.join(DATA_DIR, 'drugs.csv')
PUBMED_CSV_FILE = os.path.join(DATA_DIR, 'pubmed.csv')
PUBMED_JSON_FILE = os.path.join(DATA_DIR, 'pubmed.json')
CLINICAL_TRIALS_FILE = os.path.join(DATA_DIR, 'clinical_trials.csv')

OUTPUT_FILE = os.path.join(RESULTS_DIR, r'DRUGS_PUBS_TRIALS_JOURNALS_GRAPH_LINK')
