import os
import aiohttp
import asyncio

# Create a directory for the HTML files if it doesn't exist
if not os.path.exists("raw_html"):
    os.makedirs("raw_html")

base_url = "https://www.met.hu/eghajlat/magyarorszag_eghajlata/150_eves_eghajlati_adatsorok/Szeged/adatok/napi_adatok/main.php?"


async def fetch_and_save_html(session, year, month, max_retries=3):
    url = f"{base_url}y={year}&m={month:02d}&ful=AKT_FUL#y{year}"

    for retry in range(max_retries):
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    html_content = await response.text()

                    file_path = os.path.join("raw_html", f"met_hu_data_{year}_{month:02d}.html")

                    with open(file_path, "w", encoding="utf-8") as html_file:
                        html_file.write(html_content)

                    print(f"HTML content for year {year} and month {month:02d} saved to {file_path}")
                    return
                elif response.status == 503 and retry < max_retries - 1:
                    # Retry after a delay
                    await asyncio.sleep(5)  # Adjust the delay time as needed
                    continue
                else:
                    print(f"Failed to retrieve HTML for year {year} and month {month:02d}. Status code: {response.status}")
                    return
        except Exception as e:
            print(f"Error during request for year {year} and month {month:02d}: {str(e)}")
            return


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_and_save_html(session, year, month) for year in range(1870, 2021) for month in range(1, 13)]
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
