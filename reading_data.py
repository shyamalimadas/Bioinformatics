import cobra
import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import webbrowser

# Step 1: Fetch Gene Data from NCBI

# Define the query
query = "Escherichia coli[Organism] AND gene[Filter]"

# Define the URL for the E-utilities API
url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"

# Send the request
response = requests.get(url, params={"db": "gene", "term": query, "retmode": "json"})

# Parse the JSON response
data = response.json()

# Get the list of gene IDs
gene_ids = data["esearchresult"]["idlist"]

# Define the URL for the E-utilities API to fetch the gene data
fetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

# Send the request to fetch the gene data
fetch_response = requests.get(fetch_url, params={"db": "gene", "id": ",".join(gene_ids), "retmode": "xml"})

# Save the data to a file
with open("gene_data.xml", "w") as file:
    file.write(fetch_response.text)

# Step 2: Perform Metabolic Modeling with COBRApy

# Load the BIGG model
model = cobra.io.load_model("e_coli_core")

# Fetch KEGG pathway data with SSL verification disabled
kegg_url = "https://rest.kegg.jp/get/hsa00010"
response = requests.get(kegg_url, verify=False)
pathway_data = response.text

print("KEGG Pathway Data:")
print(pathway_data)

# Perform FBA
solution = model.optimize()
print("Flux Balance Analysis (FBA) Solution:")
print(solution)

# Visualization with Escher
import escher
from escher import Builder

builder = Builder(model_name='e_coli_core')
builder.save_html('e_coli_core_map.html')

# Open the HTML file in your default web browser
webbrowser.open('e_coli_core_map.html')

# Step 3: Analyze and Visualize Gene Data

# For demonstration purposes, let's assume your gene data is similar to this format
# and has been saved in a CSV file named 'ecoli.csv'

# Load the ecoli data
ecoli_data = pd.read_csv('ecoli.csv', delim_whitespace=True, header=None)

# Set column names
ecoli_data.columns = ['Gene'] + [f'Value_{i}' for i in range(1, 8)] + ['Annotation']

# Display the first few rows of the DataFrame
print("E. coli Data:")
print(ecoli_data.head())

# Perform some analysis
# Example: Summary statistics
summary_stats = ecoli_data.describe()
print("Summary Statistics:")
print(summary_stats)

# Normalize data (excluding 'Gene' and 'Annotation' columns)
values_data = ecoli_data.iloc[:, 1:8]
normalized_values = values_data.apply(lambda x: x / x.sum(), axis=1)

# Combine normalized data with 'Gene' and 'Annotation' columns
normalized_ecoli_data = pd.concat([ecoli_data[['Gene', 'Annotation']], normalized_values], axis=1)
print("Normalized E. coli Data:")
print(normalized_ecoli_data.head())

# Visualize the normalized data
sns.heatmap(normalized_values, cmap='viridis')
plt.xlabel('Values')
plt.ylabel('Genes')
plt.title('Heatmap of Normalized E. coli Data')
plt.show()

# Scatter plot of two selected columns (example: Value_1 vs Value_2)
plt.figure(figsize=(10, 6))
plt.scatter(ecoli_data['Value_1'], ecoli_data['Value_2'], alpha=0.5)
plt.xlabel('Value 1')
plt.ylabel('Value 2')
plt.title('Scatter Plot of Value 1 vs. Value 2')
plt.show()
