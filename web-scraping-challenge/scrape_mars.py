from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
from bs4 import BeautifulSoup as bs
import time

def scrape():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)

    ## News title and teaser
    url_news = 'https://mars.nasa.gov/news/'
    browser.visit(url_news)

    html = browser.html
    soup = bs(html, 'html.parser')
    time.sleep(4)
    news_title = soup.find('div', class_='content_title')
    news_title = news_title.text
    news_p = soup.find('div', class_='article_teaser_body')
    news_p = news_p.text

    ## JPL Mars Space Images - Featured Image
    url_feat_img = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url_feat_img)

    html = browser.html
    soup = bs(html, 'html.parser')

    featured_image_url = 'https://www.jpl.nasa.gov' + soup.find('a', id='full_image')['data-fancybox-href']

    ## Mars Weather
    url_mars_weather = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url_mars_weather)

    html = browser.html
    soup = bs(html, 'html.parser')

    for tweet in soup.find_all('div', class_='js-tweet-text-container'):
        if (tweet.p.text[:11] == 'InSight sol'):
            mars_weather = tweet.p.text
            break

    ## Mars Facts
    url_mars_facts = 'https://space-facts.com/mars/'
    browser.visit(url_mars_facts)

    html = browser.html
    soup = bs(html, 'html.parser')

    mars_facts_table = f"{soup.find('table', id='tablepress-p-mars-no-2')}"

    ## Mars Hemispheres

    url_mars_hemis = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url_mars_hemis)

    html = browser.html
    soup = bs(html, 'html.parser')

    hemisphere_image_urls = []
    for link in soup.find_all('div', class_='description'):
        hemisphere_image_urls.append({"title": link.h3.text[:-9]})
        img_page = browser.visit('https://astrogeology.usgs.gov' + link.a['href'])
        html = browser.html
        img_soup = bs(html, 'html.parser')
        for each in img_soup.find_all('a'):
            if (each.text == 'Sample'):
                img_url = each['href']
                break
        hemisphere_image_urls.append({"img_url": img_url})

    data = {'news_title': news_title,
            'news_p': news_p,
            'featured_image_url': featured_image_url,
            'mars_weather': mars_weather,
            'mars_facts_table': f'{mars_facts_table}',
            'hemisphere_image_urls': hemisphere_image_urls}
    return data    