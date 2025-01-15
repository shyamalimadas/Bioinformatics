# E. coli Gene and Metabolic Data Analysis

This project performs gene data fetching from NCBI, metabolic modeling with COBRApy, and analysis and visualization of E. coli gene data using Python.

## Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
  - [Step 1: Fetch Gene Data from NCBI](#step-1-fetch-gene-data-from-ncbi)
  - [Step 2: Perform Metabolic Modeling with COBRApy](#step-2-perform-metabolic-modeling-with-cobrapy)
  - [Step 3: Analyze and Visualize Gene Data](#step-3-analyze-and-visualize-gene-data)
- [License](#license)

## Overview

This project automates the process of fetching gene data from NCBI, performing metabolic modeling with COBRApy, and analyzing gene data for E. coli. It includes steps for fetching gene data, performing flux balance analysis (FBA), and visualizing the data.

## Requirements

- Python 3.6+
- `requests`
- `pandas`
- `seaborn`
- `matplotlib`
- `cobra`
- `escher`

You can install the required libraries using pip:
```bash
pip install requests pandas seaborn matplotlib cobra escher '
```

## Setup
### Clone the Repository:

```bash
git clone https://github.com/yourusername/ecoli-gene-metabolic-analysis.git
cd ecoli-gene-metabolic-analysis
```
### Install Dependencies:

``` bash
pip install -r requirements.txt
```

### Prepare Data:

Save your gene data in a CSV file named ecoli.csv in the same directory.

### Usage
Run the script:

```bash
python analysis.py
```

## Code Explanation
### Step 1: Fetch Gene Data from NCBI
The script fetches gene data for Escherichia coli from the NCBI E-utilities API and saves it as an XML file.

### Step 2: Perform Metabolic Modeling with COBRApy
The script loads the E. coli core metabolic model, fetches KEGG pathway data, performs flux balance analysis (FBA), and visualizes the metabolic map using Escher.

### Step 3: Analyze and Visualize Gene Data
The script reads gene data from ecoli.csv, performs normalization, and creates visualizations such as heatmaps and scatter plots.

## License
This project is licensed under the MIT License.


Feel free to customize it further to fit your project's specific needs. If you need additional details or have any questions, feel free to ask!

