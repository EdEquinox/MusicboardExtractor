from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
import os
import csv
import time
from selenium.webdriver.common.keys import Keys



def process_form_data(url):
    # Set up Chrome options
    options = Options()
    options.add_argument("--headless")  # Ensure GUI is off
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome(options=options)

    try:
        
        # Go to the URL
        driver.get(str(url))

        # Wait for the page to load
        time.sleep(5)

        print("Page loaded successfully.")

        # Use a while loop to keep clicking the button as long as it exists
        while True:
            try:
                # Find the "View More" div by xPath
                element = driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/div/div/div/div[2]/div/div[1]/div/div[1]/div[7]/div")
                
                # Click the "View More" button using JavaScript
                driver.execute_script("arguments[0].click();", element)
                time.sleep(2)

            except Exception as e:
                # If the "View More" button can't be found, break the loop
                break

        # Get the HTML of the webpage
        html_content = driver.page_source
        driver.quit()

        # Parse the HTML content of the page with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find all the divs containing the data
        divs = soup.find_all('div', {'class': 'content-options-wrapper'})

        # Initialize an empty list to store the data
        data = []
        
        # Open the CSV file
        with open('listMusicboard.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Artist", "Image URL"])
            
        # Loop through the divs and extract the data
            for div in divs:
                title = div.find('h6', {'class': 'bigbackenditem_title__bSh2l'}).text
                artist = div.find('a', {'class': 'bigbackenditem_artistLink__2-oCg'}).text
                img_url = div.find('img', {'class': 'albumcover_cover__1egXq'})['src']

                # Write the data to the CSV file
                writer.writerow([title, artist, img_url])

        # Open the CSV file
        with open('listMusicboard.csv', 'r', newline='') as file:
            data = file.read()
            
        os.remove('listMusicboard.csv')

        print("CSV file created successfully.")
        
        return data

    except WebDriverException:
        print("WebDriverException occurred.")
    finally:
        if driver is not None:
            driver.quit()
            
def process_form_data_later(url):
    # Set up Chrome options
    options = Options()
    options.add_argument("--headless")  # Ensure GUI is off
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome(options=options)

    try:
        
        # Go to the URL
        driver.get(str(url))

        # Wait for the page to load
        time.sleep(5)

        print("Page loaded successfully.")
        
        # Get the initial page height
        last_height = driver.execute_script("return document.body.scrollHeight")

        # Use a while loop to keep clicking the button as long as it exists
        while True:
            # Scroll down to the bottom of the page
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)

            # Wait for new content to load
            time.sleep(2)

            # Calculate new scroll height and compare with the last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        # Get the HTML of the webpage
        html_content = driver.page_source
        driver.quit()

        # Parse the HTML content of the page with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find all the divs containing the data
        divs = soup.find_all('div', {'class': 'content-options-wrapper'})

        # Initialize an empty list to store the data
        data = []
        
        # Open the CSV file
        with open('listMusicboard.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Artist", "Image URL"])
            
        # Loop through the divs and extract the data
            for div in divs:
                title = div.find('h6', {'class': 'bigbackenditem_title__bSh2l'}).text
                artist = div.find('a', {'class': 'bigbackenditem_artistLink__2-oCg'}).text
                img_url = div.find('img', {'class': 'albumcover_cover__1egXq'})['src']

                # Write the data to the CSV file
                writer.writerow([title, artist, img_url])

        # Open the CSV file
        with open('listMusicboard.csv', 'r', newline='') as file:
            data = file.read()
            
        os.remove('listMusicboard.csv')

        print("CSV file created successfully.")
        
        driver.quit()
        
        return data

    except WebDriverException:
        print("WebDriverException occurred.")
    finally:
        if driver is not None:
            driver.quit()
            
def process_form_data_album(url):
    
    options = Options()
    options.add_argument("--headless")  # Ensure GUI is off
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome(options=options)
    
    try:
        # Go to the URL
        driver.get(str(url))

        # Wait for the page to load
        time.sleep(5)

        print("Page loaded successfully.")
        
        # Get the initial page height
        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to the bottom of the page
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)

            # Wait for new content to load
            time.sleep(2)

            # Calculate new scroll height and compare with the last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
            
         # Get the HTML of the webpage
        html_content = driver.page_source
        driver.quit()
        
        # Parse the HTML content of the page with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Find all the divs containing the data
        divs = soup.find_all('div', {'class': 'content-options-wrapper'})
                
        # Initialize an empty list to store the data
        data = []
        
        # Open the CSV file
        with open('listAlbunsMusicboard.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Rate", "Image URL"])
        
            # Loop through the divs and extract the data
            for div in divs:
                
                
                title = div.find('h6', {'class': 'bigbackenditem_title__bSh2l'}).text
                img_url = div.find('img', {'class': 'albumcover_cover__1egXq'})['src']
                writer.writerow([title, 0, img_url])

        # Open the CSV file
        with open('listAlbunsMusicboard.csv', 'r', newline='') as file:
            data = file.read()
        
        print("CSV file created successfully.")
            
        result = data
            
        os.remove('listAlbunsMusicboard.csv')

        
        return result

    except WebDriverException:
        print("WebDriverException occurred.")
    finally:
        if driver is not None:
            driver.quit()
            
def process_form_data_reviews(url):
    
    options = Options()
    options.add_argument("--headless")  # Ensure GUI is off
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome(options=options)
    
    try:
        # Go to the URL
        driver.get(str(url))

        # Wait for the page to load
        time.sleep(5)

        print("Page loaded successfully.")
        
        # Get the initial page height
        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to the bottom of the page
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)

            # Wait for new content to load
            time.sleep(2)

            # Calculate new scroll height and compare with the last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
            
         # Get the HTML of the webpage
        html_content = driver.page_source
        driver.quit()
        
        # Parse the HTML content of the page with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Find all the divs containing the data
        divs = soup.find_all('div', {'class': 'link-inner'})
                
        # Initialize an empty list to store the data
        data = []
        
        # Open the CSV file
        with open('listAlbunsMusicboard.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Target", "Artist", "Type", "Title" ,"Review"])
        
            # Loop through the divs and extract the data
            for div in divs:
                title = None
                review3 = None
                link_inner = div.find('div', {'class': 'link-inner'})
                if link_inner is not None:  # Check if 'link-inner' div is found
                    h5 = link_inner.find('h5')
                    if h5 is not None:  # Check if h5 is found
                        title = h5.get_text()
                target = div.find('h5', {'class': 'reviewitem_a__iuJDD'}).get_text() if div.find('h5', {'class': 'reviewitem_a__iuJDD'}) else None
                artist = div.find('a', {'class': 'reviewitem_artistLink__28F-G'}).get_text() if div.find('a', {'class': 'reviewitem_artistLink__28F-G'}) else None
                type = div.find('p', {'class': 'highDarkGrey'}).get_text() if div.find('p', {'class': 'highDarkGrey'}) else None
                review = div.find('div', {'class': 'truncate_container__3Xl3S'})
                if review is not None:  # Check if 'truncate_container' div is found
                    review2 = review.find('div')
                    if review2 is not None:
                        review3 = review2.find('p').get_text()
                writer.writerow([target, artist, type, title, review3])

        # Open the CSV file
        with open('listAlbunsMusicboard.csv', 'r', newline='', encoding='utf-8') as file:
            data = file.read()
        
        print("CSV file created successfully.")
            
        result = data
            
        os.remove('listAlbunsMusicboard.csv')

        
        return result

    except WebDriverException:
        print("WebDriverException occurred.")
    finally:
        if driver is not None:
            driver.quit()
