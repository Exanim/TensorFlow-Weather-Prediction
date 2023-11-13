import os
from bs4 import BeautifulSoup
import csv

# Create a directory for the CSV files if it doesn't exist
if not os.path.exists("csv_data"):
    os.makedirs("csv_data")


# data.append(["year", "month", "day", "temperature", "total_rainfall"])

csv_file_path = os.path.join("csv_data", f"szeged_data.csv")
with open(csv_file_path, "w", newline="", encoding="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["year", "month", "day", "temperature", "total_rainfall"])
csv_file.close()

# Iterate through each HTML file in the "raw_html" directory
for filename in os.listdir("raw_html"):
    if filename.endswith(".html"):
        # Construct the full path of the HTML file
        html_file_path = os.path.join("raw_html", filename)

        # Read the HTML content from the file
        with open(html_file_path, "r", encoding="utf-8") as html_file:
            html_content = html_file.read()

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_content, "html.parser")

        # Find the table element containing the data
        table = soup.find("table", {"class": "eas-tbl"})

        if table:

            # Extract the year from the filename
            year = int(filename.split("_")[3])
            # if you get confused by this and say this is not readable learn to read
            month = int(filename.split("_")[-1].split(".")[0])

            # Extract the data from the table
            # The first row of the table is just column metadata so we slice it
            data = []
            daily_data = table.find_all("tr")[1:]
            for day in range(len(daily_data)):
                tr = daily_data[day]

                row_data = [year, month, day+1]
                row_data.append(tr.find_all("td")[0].get_text(strip=True))
                row_data.append(tr.find_all("td")[1].get_text(strip=True))

                data.append(row_data)

            # Write the data to the CSV file
            with open(csv_file_path, "a", newline="", encoding="utf-8") as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerows(data)

            print(f"Data for year {year} extracted and saved to {csv_file_path}")
        else:
            print(f"No data found in {filename}. Check the HTML structure and update the selector.")
