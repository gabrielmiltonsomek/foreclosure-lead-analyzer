# Foreclosure Lead Analyzer

Foreclosure Lead Analyzer is a Python-based data processing project designed to clean, filter, and evaluate foreclosure lead data.

The project simulates how a real estate investor or data analyst might organize raw property records, remove low-quality leads, estimate potential property value, and prepare data for decision-making.

---

## Features

* Filters foreclosure lead data from CSV files
* Removes incomplete or low-quality records
* Detects likely apartments, condos, and HOA-related properties
* Uses structured validation logic to qualify leads
* Simulates comparable sales analysis
* Estimates potential investment spread
* Includes a simple HTML dashboard for presenting cleaned lead data

---

## Tech Stack

* Python
* CSV Processing
* HTML
* CSS
* Basic Data Analysis

---

## Project Structure

```
foreclosure-lead-analyzer/
├── app.py
├── comps_analysis.py
├── dashboard.html
├── README.md
├── LICENSE
└── .gitignore
```

---

## File Overview

### `app.py`

Main script for filtering foreclosure leads.

* Loads raw CSV data
* Validates each record
* Removes low-quality leads
* Outputs a cleaned dataset
* Displays summary statistics

---

### `comps_analysis.py`

Simulates comparable property analysis.

* Calculates price per square foot
* Estimates property value
* Compares value against purchase price
* Calculates potential investment spread

---

### `dashboard.html`

Lightweight dashboard for visualizing processed lead data.

* Displays summary metrics
* Shows example lead data
* Demonstrates how results could be presented

---

## How It Works

1. Load foreclosure lead data from a CSV file
2. Validate each record for required fields
3. Remove incomplete or low-quality entries
4. Filter out apartment and HOA-related properties
5. Save qualified leads to a cleaned dataset
6. Use comparable analysis to estimate property value
7. View results in a simple dashboard

---

## Example Usage

Run the lead filtering script:

```
python app.py sample_leads.csv filtered_leads.csv
```

Run comparable analysis:

```
python comps_analysis.py
```

Open the dashboard:

```
dashboard.html
```

---

## Why I Built This

I built this project to demonstrate how software engineering can be applied to real-world data processing workflows.

It reflects my interest in combining programming with practical, data-driven decision making.

---

## What This Project Demonstrates

* Clean Python code structure
* Data validation and filtering
* Use of dataclasses and type hints
* Modular function design
* Real-world problem solving
* Basic data visualization concepts

---

## Future Improvements

* Add database integration
* Implement automated lead scoring
* Build a web interface for uploading data
* Integrate real property data APIs
* Add exportable reports

---

## Author

Gabriel Milton Somek
