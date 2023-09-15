# Zety Resume Data Extraction Script

This Python script is designed to extract data from a specific website (https://zety.com/resume-examples) that provides resume examples and categories. The script fetches and processes data from the website, including category and subcategory information, as well as HTML content for each subcategory.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Program Description](#program-description)
- [License](#license)

## Prerequisites

Before running the script, ensure you have the following prerequisites installed:

- Python (version 3.x)
- Required Python libraries (`requests`, `BeautifulSoup`, `json`)

You can install the required libraries using `pip`:

```bash
pip install requests beautifulsoup4 json
```

## Installation

1. Clone or download the script to your local machine.

```bash
git clone https://github.com/your-username/resume-data-extraction.git
```

2. Navigate to the script's directory.

```bash
cd resume-data-extraction
```

## Usage

To run the script, simply execute it using Python:

```bash
python resume_extraction.py
```

The script will start fetching and processing data from the specified website.

## Program Description

The script performs the following tasks:

1. Sends a GET request to the website (https://zety.com/resume-examples).

2. Parses the HTML content of the website using BeautifulSoup.

3. Extracts category and subcategory information, including category titles, subcategory text, and subcategory URLs.

4. Fetches HTML content for each subcategory URL.

5. Extracts the first line of HTML content for each subcategory.

6. Prints or saves the data, including category and subcategory information, and the first line of HTML content.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer
This script is provided for educational purposes only. It is intended to demonstrate web scraping and data extraction techniques. Ensure that you comply with all relevant laws and terms of service when using this script to scrape data from websites. Use this script responsibly and ethically.
