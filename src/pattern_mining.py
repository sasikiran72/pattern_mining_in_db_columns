# Install the pyECLAT package
#!pip install pyECLAT

# Import necessary libraries
import re
import pandas as pd
from pyECLAT import ECLAT

# Read data from CSV file into a DataFrame
data = pd.read_csv('datafiles/train.csv')
data = data.iloc[:10]
df = pd.DataFrame(data)

# Function to extract column names from SQL queries using REGEX
def extract_column_names(query):
    pattern = r'SELECT\s+(?:COUNT|MAX|MIN|AVG|SUM)?\s*(.*?)\s+FROM|\b(?:WHERE|AND)\s+(.*?)(?:\s*=\s*(?:\'[^\']*\'|\"[^\"]*\"))?(?=\s*(?:AND|ORDER BY|GROUP BY|\Z))'
    matches = re.findall(pattern, query, re.IGNORECASE)

    column_names = []
    for match in matches:
        for group in match:
            if group.strip():
                match_obj = re.search(r"(?:'(.*?)'|`(.*?)`|\b(\w+(?:\s*[/\-\w]+)*)\b)", group.strip())
                if match_obj:
                    column_names.append(match_obj.group(1) or match_obj.group(2) or match_obj.group(3))
    return list(set(column_names))

# Extract column names from SQL queries in the DataFrame
queries = df['sql']
transactions = []
for query in queries:
    column_names = extract_column_names(query)
    transactions.append(column_names)
    # the below can be uncommented to see all the query and column names one by one
    # if column_names:
    #     print(f"Column Names in Query '{query}':", column_names)
    # else:
    #     print(f"No column names found in the query: '{query}'")
print(transactions)
print("Number of Transactions sent to the Algorithm: ", len(transactions))

df_transactions = pd.DataFrame(transactions)
#print(df_transactions)

# Create an instance of the ECLAT algorithm with verbose mode enabled
eclat_instance = ECLAT(data=df_transactions, verbose=True)
# Fit the ECLAT algorithm to find frequent itemsets with a minimum support of 0.05
frequent_itemsets = eclat_instance.fit(min_support=0.05)

# Print the frequent itemsets
print("Frequent Itemsets:")
print(frequent_itemsets[0])

# Extract support values for the frequent itemsets and sorting in decsending order of support
support_values = frequent_itemsets[1]
sorted_support_values = dict(sorted(support_values.items(), key=lambda item: item[1], reverse=True))

# Print the sorted support values
print("Support values: ")
print(sorted_support_values)

# Define a function to extract column names from a group of SQL queries
def q_trans(qs):
  column_g = []
  for query in qs:
    column_names = extract_column_names(query)
    #print(column_names)
    for nam in column_names:
      column_g.append(nam)
  return column_g

# Initialize an empty list to store group transactions
group_transactions = []

# Calculate the number of queries
q_len = len(queries)

# Process queries in batches of 5
for i in range(0,q_len-4,5):
  q_set = queries[i:i+5]
  col_grp = q_trans(q_set)
  group_transactions.append(col_grp)

# Print the group transactions
print(group_transactions)
print("Number of Transactions sent to the Algorithm: ", len(group_transactions))

# Create a DataFrame from the group transactions
df_transactions = pd.DataFrame(group_transactions)

# Create an instance of the ECLAT algorithm with verbose mode enabled
eclat_instance = ECLAT(data=df_transactions, verbose=True)
frequent_itemsets = eclat_instance.fit(min_support=0.05)

# Fit the ECLAT algorithm to find frequent itemsets with a minimum support of 0.05
print("Frequent Itemsets:")
print(frequent_itemsets[0])

# Extract support values for the frequent itemsets and sorting in decsending order of support
support_values = frequent_itemsets[1]
sorted_support_values = dict(sorted(support_values.items(), key=lambda item: item[1], reverse=True))

# Print the sorted support values
print("Support values: ")
print(sorted_support_values)