from seleniumwire import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Prompt to ask for the Excel file
Tk().withdraw()  # We don't want a full GUI, so keep the root window from appearing
excel_file_path = askopenfilename(title="Select Excel file")

# Load the Excel file
df = pd.read_excel(excel_file_path)

def get_dash_xml_urls(teams_url):
    # Initialize the driver
    driver = webdriver.Chrome()
    driver.get(teams_url)

    # Login (you will need to modify selectors based on the actual page structure)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "loginfmt")))
    login_field = driver.find_element(By.NAME, "loginfmt")
    login_field.send_keys('XXX@abc.com') #Your login email address
    login_field.send_keys(Keys.RETURN)

    # Password input
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "i0118")))
    password_field = driver.find_element(By.ID, "i0118")
    password_field.send_keys('Password') #Your Password
    password_field.send_keys(Keys.RETURN)

    # Access the video element (this part is speculative and needs specific selectors)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "video")))

    # Find the requests with Content-Type 'application/dash+xml'
    dash_xml_urls = [request.url for request in driver.requests if request.response and request.response.headers.get('Content-Type') == 'application/dash+xml']

    # Close the driver
    driver.quit()

    return dash_xml_urls

# Process each row in the DataFrame
dash_xml_urls_list = []
for index, row in df.iterrows():
    teams_url = row['URL']
    dash_xml_urls = get_dash_xml_urls(teams_url)
    dash_xml_urls_list.append(','.join(dash_xml_urls))

# Add the 'V_URL' column to the DataFrame
df['V_URL'] = dash_xml_urls_list

# Save the updated DataFrame to a new Excel file
file_name_parts = excel_file_path.split('.')
updated_file_path = file_name_parts[0] + '_updated.' + file_name_parts[1]
df.to_excel(updated_file_path, index=False)