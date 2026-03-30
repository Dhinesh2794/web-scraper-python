import requests
from bs4 import BeautifulSoup
import csv

url = "https://realpython.github.io/fake-jobs/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

jobs = soup.find_all("div", class_="card-content")

# Ask user for keyword
keyword = input("Enter job keyword to search (e.g., python): ").lower()

with open("filtered_jobs.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Company", "Location"])

    print("\n--- Filtered Job Listings ---\n")

    found = False

    for job in jobs:
        title = job.find("h2", class_="title").text.strip()
        company = job.find("h3", class_="company").text.strip()
        location = job.find("p", class_="location").text.strip()

        if keyword in title.lower():
            print(f"{title} | {company} | {location}")
            writer.writerow([title, company, location])
            found = True

    if not found:
        print("No matching jobs found.")

print("\nFiltered data saved to filtered_jobs.csv ✅")