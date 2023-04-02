# This script finds the journal that mentions the highest number of different drugs, along with the number of different drugs mentioned.

from  config import OUTPUT_FILE  # import the name of the output file and its extension
import json  # import the json module to read and write json files

# Open the json output file and load its content into the data variable
with open(OUTPUT_FILE+".json", 'r') as f:
        data= json.load(f)

# Create a dictionary to keep track of the count of drugs mentioned for each journal
journal_counts = {}

# Loop through each drug in the data
for drug in data["drugs"]:
    # Loop through each journal where the drug was mentioned
    for journal in drug["journals"]:
        # If the journal is not yet in the dictionary, add it and initialize its count to an empty set
        if journal["journal"] not in journal_counts.keys():
            journal_counts[journal["journal"]]= set()
        # Add the atc code of the drug to the set of drugs mentioned for the current journal
        journal_counts[journal["journal"]].add(drug["atc_code"])

# Initialize variables to keep track of the highest count and the journal with the highest count
highest_count = 0
highest_journal = None

# Loop through each journal in the dictionary and its corresponding drug set
for journal, drug_set in journal_counts.items():
    # Count the number of drugs mentioned for the current journal
    count = len(drug_set)
    # Update the highest count and highest journal if the current count is higher
    if count > highest_count:
        highest_count = count
        highest_journal = journal

# Print the name of the journal with the highest count and the count itself
print(f"The journal that mentioned the highest number of different drugs is '{highest_journal}', with {highest_count} different drugs mentioned.")
