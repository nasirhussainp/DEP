import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 3: Send a request to the website
url = 'https://example.com'  # Replace with the URL of the website you want to scrape
response = requests.get(url)

# Step 4: Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Step 5: Extract the data you need
# Example: Extracting all headings from the webpage
headings = soup.find_all('h2')  # Replace 'h2' with the appropriate HTML tag you're interested in

# Extracting text from the headings
data = []
for heading in headings:
    data.append(heading.text)

# Step 6: Store the data in a CSV file
df = pd.DataFrame(data, columns=['this is my final task'])
df.to_csv('scraped_data.csv', index=False)

print("Data has been successfully scraped and saved to 'scraped_data.csv'")
