import requests

url = "https://ohiodnr.gov/static/documents/oil-gas/production/20210309_2020_1%20-%204.xls"

response = requests.get(url)

if response.status_code == 200:
    with open("Ohio_quarterly_production_2020.xls", "wb") as file:
        file.write(response.content)
    print("File downloaded successfully.")
else:
    print("Failed to download the file. Status code:", response.status_code)