## Web Scraping

from bs4 import BeautifulSoup
import requests
from splinter import Browser
from selenium import webdriver
import pandas as pd
import pymongo

# Open Chrome Driver

def init_browser():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    

def scrape():
    browser = init_browser()


    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"

    browser.visit(url)

    # Creating A bs object

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    news_title = soup.find('div', class_='content_title').text
    news_p = soup.find('div', class_='article_teaser_body').text

    print(news_title)
    print('-------------------')
    print(news_p)


    # Mars Image URL

    images_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(images_url)

    # Getting Full Size Image

    browser.click_link_by_id('full_image')

    browser.click_link_by_partial_text('more info')

    # Creating Soup item for images url

    html_image = browser.html
    soup = BeautifulSoup(html_image, 'html.parser')

    image = soup.body.find('figure', class_='lede')

    # Extracting the image url

    link = image.find('a')
    href = link['href']

    main_url = "https://www.jpl.nasa.gov"

    # Featured URL

    featured_image_url = main_url + href
    print(featured_image_url)   
    
    mars_weather = 'InSight sol 457 (2020-03-10) low -95.7ºC (-140.3ºF) high -9.1ºC (15.6ºF) winds from the SSE at 6.5 m/s (14.5 mph) gusting to 21.0 m/s (46.9 mph) pressure at 6.30 hPa'


    # Mars Facts

    facts_url = "https://space-facts.com/mars/"
    browser.visit(facts_url)

    # Creating Soup Object

    html_facts = browser.html
    soup = BeautifulSoup(html_facts, 'html.parser')

    tables = pd.read_html(facts_url)
    tables

    mars_facts = tables[2]

    mars_facts.columns = ['Description', 'Details']
    mars_facts


    # Convering Mars Facts table to Html

    html_table_marsfacts = mars_facts.to_html()
    html_table_marsfacts
    
    # Mars Hemispheres
    
    hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif"},
    {"title": "Cerberus Hemisphere", "img_url": "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif"},
    {"title": "Schiaparelli Hemisphere", "img_url": "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif"},
    {"title": "Syrtis Major Hemisphere", "img_url": "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif"},
]


