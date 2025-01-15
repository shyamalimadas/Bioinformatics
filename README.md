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
pip install requests pandas seaborn matplotlib cobra escher
