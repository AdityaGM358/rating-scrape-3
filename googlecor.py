import streamlit as st
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests
import os

# Get the absolute path of the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))
requirements_file = os.path.join(current_directory, "requirements.txt")

def main():
    st.title("Location Details Finder")

    # Input for coordinates
    coordinates = []
    
    lat = st.number_input(f"Enter Latitude for Coordinate:",format="%.6f")
    lon = st.number_input(f"Enter Longitude for Coordinate:",format="%.6f")
    radial = st.number_input(f"Enter radius: ",min_value=10,value=1000)
    coordinates.append((lat, lon))

    if st.button("Find Details"):
        # Scrape location details for the given coordinates
        scraped_locations = scrape_location_details(coordinates,radial)

        # Display the scraped location details in Streamlit
        if scraped_locations:
            st.write("Scraped Location Details:")
            location_table = []
            #chrome_options = Options()
            #chrome_options.add_argument("--headless")
            #driver = webdriver.Chrome(options=chrome_options)
            for location in scraped_locations:
                location_data = location.split("   ")
                name = location_data[0][len("Name: "):]
                rating = float(location_data[1][len("Rating: "):])
                user_ratings_total = int(location_data[2][len("Total Reviews: "):])
                address = location_data[3][len("Address: "):]
                map_link = f"https://www.google.com/maps?q={lat},{lon}"
                #driver.get(map_link)


                location_table.append((name, rating, user_ratings_total, address,map_link))
            df = pd.DataFrame(location_table, columns=["Name", "Rating", "Total Reviews", "Address", "Map Link"])
            st.dataframe(df)
        else:
            st.write("No location details found within the specified coordinates.")

        #driver.quit()

def scrape_location_details(coordinates,radial):
    # Set up the Selenium web driver (you need to download the appropriate driver for your browser)
    # For Chrome, download the chromedriver executable: https://sites.google.com/a/chromium.org/chromedriver/downloads
    #chrome_options = Options()
    #chrome_options.add_argument("--headless")  # To run Chrome in headless mode
    #driver = webdriver.Chrome(options=chrome_options)

    # API key for Google Maps
    headers = {
        "authorization": st.secrets["AUTH_KEY"],
        "content-type": "application/json",
    }

    # Implement the logic for scraping location details within the provided coordinates
    base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    location_details = []

    for lat, lon in coordinates:
        # Send API request to Google Maps API
        params = {
            "location": f"{lat},{lon}",
            "radius": radial,  # 1000 meters (adjust the radius as needed)
            "key": st.secrets["AUTH_KEY"],
        }
        response = requests.get(base_url, params=params)

        # Wait for the API response (you might need to add a longer wait time based on your internet speed)
        time.sleep(5)

        # Process the API response and extract location details
        if response.status_code == 200:
            data = response.json()
            if data["status"] == "OK":
                for result in data["results"]:
                    name = result["name"]
                    rating = result.get("rating", 0)
                    user_ratings_total = result.get("user_ratings_total", 0)
                    if rating < 4 and user_ratings_total > 1000:
                        address = result.get("vicinity", "")
                        location_details.append(f"[Name: {name}   Rating: {rating}   Total Reviews: {user_ratings_total}   Address: {address}]")
                    
            else:
                print("Error:", data["status"])
        else:
            print("Failed to fetch location details.")
    
    # Close the browser
    #driver.quit()

    # Return the list of scraped location details
    return location_details

if __name__ == "__main__":
    main()