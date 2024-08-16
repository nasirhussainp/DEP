import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://en.wikipedia.org/wiki/Elon_Musk'  # Replace with the URL of the website you want to scrape
response = requests.get(url)

# Step 4: Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')


headings = soup.find_all('h2')  # Replace 'h2' with the appropriate HTML tag you're interested in

# Extracting text from the headings
data = []
for heading in headings:
    data.append(heading.text)


df = pd.DataFrame(data, columns=['Headings'])
df.to_csv('scraped_data.csv', index=False)

print("Data has been successfully scraped and saved to 'scraped_data.csv'")
