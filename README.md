 *Location Details Finder*

**Location Details Finder** is a Python-based web application that allows you to find location details within a specified radius of a set of coordinates. It utilizes Streamlit for the user interface, Selenium for web scraping, and the Google Maps API for location data retrieval.

## Table of Contents

- [Introduction]
- [Features]
- [Usage]
- [Installation]
- [How It Works]
- [Dependencies]
- [License]
## Introduction

Have you ever needed to quickly find location details such as names, ratings, user reviews, and addresses within a certain area defined by coordinates? **Location Details Finder** simplifies this task by allowing you to input latitude, longitude, and a radius, and then scraping location details using the Google Maps API. The results are displayed in an easy-to-read table format, making it convenient to find the information you need.

## Features

- Input latitude and longitude coordinates.
- Set a custom radius to define the search area.
- Scrape location details such as name, rating, user reviews, and address.
- Display results in a tabular format.
- Links to Google Maps for each location.

## Usage

1. Input the latitude and longitude for the coordinate you want to search around.
2. Define the search radius (in meters).
3. Click the "Find Details" button to initiate the location details search.
4. View the scraped location details in a table format.
5. Click on the "Map Link" to open Google Maps for each location.

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/location-details-finder.git
   ```

2. Navigate to the project directory:

   ```bash
   cd location-details-finder
   ```

3. Install the required Python libraries:

   ```bash
   pip install -r requirements.txt
   ```

4. [Set up your Google Maps API key](https://developers.google.com/maps/gmp-get-started) and add it as a secret in Streamlit Share (replace `st.secrets["AUTH_KEY"]` with your API key).

5. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

6. Access the app in your web browser at the provided URL :   

https://2uhms9mrzqtyealn8m8fpt.streamlit.app/

## How It Works

- The application uses Streamlit for the user interface, allowing you to input coordinates and a radius.
- It sends a request to the Google Maps API to retrieve location details within the specified radius of the coordinates.
- The application then processes the API response, extracting relevant information such as location names, ratings, user reviews, and addresses.
- Results are displayed in a tabular format using pandas DataFrames.
- Each location's "Map Link" provides a direct link to Google Maps for easy navigation.

## Dependencies

- [Streamlit](https://streamlit.io/): A popular Python library for creating web applications with minimal effort.
- [Pandas](https://pandas.pydata.org/): A data manipulation and analysis library.
- [Selenium](https://selenium-python.readthedocs.io/): A web testing framework used for web scraping in this application.
- [Requests](https://docs.python-requests.org/en/master/): A Python library for making HTTP requests.
- [Google Maps API](https://developers.google.com/maps/gmp-get-started): Provides location data used in this application.
