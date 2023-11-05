import os
import requests

# Create a directory for the HTML files if it doesn't exist
if not os.path.exists("raw_html"):
    os.makedirs("raw_html")

# Define the base URL
base_url = "https://www.met.hu/eghajlat/magyarorszag_eghajlata/150_eves_eghajlati_adatsorok/Budapest/adatok/napi_adatok/main.php?"

# Iterate through years (1870 to 2020)
for year in range(1870, 2021):
    # Iterate through months (01 to 12)
    for month in range(1, 13):
        # Create the full URL with the year and month parameters
        url = f"{base_url}y={year}&m={month:02d}&ful=AKT_FUL#y{year}"

        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Get the content (HTML) from the response
            html_content = response.text

            # Specify the file path in the "raw_html" directory
            file_path = os.path.join("raw_html", f"met_hu_data_{year}_{month:02d}.html")

            # Write the HTML content to the file
            with open(file_path, "w", encoding="utf-8") as html_file:
                html_file.write(html_content)

            print(f"HTML content for year {year} and month {month:02d} saved to {file_path}")
        else:
            print(f"Failed to retrieve HTML for year {year} and month {month:02d}. Status code: {response.status_code}")
