from Browser import Browser
from selenium.webdriver.common.by import By
import os
import re
import sys
import time

# Sleeping time between refreshing
SLEEP = 5

# Helper
def create_folder_if_does_not_exist(path):
    isExist = os.path.exists(path)
    if not isExist:
        os.makedirs(path)

# Create an instance of 'Browser'. A ease-of-use wrapper for selenium
browser = Browser()

# Make folder for outputs
create_folder_if_does_not_exist('./jobs')

# URL is localhost here
URL = 'http://localhost:8000'

# Output-file
output_file = './jobs/jobs.txt'

browser.setUp()
browser.get(URL) # Establish connection

while True:

    print('Checking for jobs')
    
    jobs = []
    # Find all buttons on website
    job_buttons = browser.find_many(By.TAG_NAME, 'button')

    print('Found {} jobs'.format(len(job_buttons)))

    for btn in job_buttons:
        job_name = btn.get_attribute('innerHTML')
        job_id   = btn.get_attribute('id')
        jobs.append(job_id + ' ' + job_name + '\n')

        # Click job-button
        btn.click()
        
    # Write jobs to disk
    with open(output_file,'a') as f:
        f.writelines(jobs)

    # Wait for second between refreshing
    print('Sleeping for {} seconds'.format(SLEEP))
    time.sleep(SLEEP)