import requests
from bs4 import BeautifulSoup

# Enter your login credentials
username = "your_username"
password = "your_password"

# Login to the website
session = requests.Session()
login_url = "https://yourwebsite.com/login"
login_data = {"username": username, "password": password}
session.post(login_url, data=login_data)

# Navigate to the time sheet page
timesheet_url = "https://yourwebsite.com/timesheet"
timesheet_page = session.get(timesheet_url)

# Parse the HTML of the time sheet page
soup = BeautifulSoup(timesheet_page.content, "html.parser")

# Find the job number field and enter the job number
job_number_field = soup.find("input", {"name": "job_number"})
job_number_field["value"] = "123456"

# Find the number of hours field for Monday and enter the hours
monday_hours_field = soup.find("input", {"name": "monday_hours"})
monday_hours_field["value"] = "8"

# Repeat for the other days of the week
tuesday_hours_field = soup.find("input", {"name": "tuesday_hours"})
tuesday_hours_field["value"] = "8"

wednesday_hours_field = soup.find("input", {"name": "wednesday_hours"})
wednesday_hours_field["value"] = "8"

thursday_hours_field = soup.find("input", {"name": "thursday_hours"})
thursday_hours_field["value"] = "8"

friday_hours_field = soup.find("input", {"name": "friday_hours"})
friday_hours_field["value"] = "8"

# Submit the form
submit_button = soup.find("input", {"type": "submit"})
session.post(timesheet_url, data=submit_button)

print("Time sheet submitted successfully!")
