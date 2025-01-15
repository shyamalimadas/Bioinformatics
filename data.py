import requests

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
