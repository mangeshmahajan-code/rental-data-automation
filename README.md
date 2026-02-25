**Zillow Clone Scraper & Google Form Automation
**

This project scrapes rental property data from a Zillow clone website and automatically submits the extracted information into a Google Form using Selenium.

• It combines :
 
  - requests for fetching webpage data
 
  -BeautifulSoup for HTML parsing
  
  -Selenium for browser automation

**What This Project Does
**

Scrapes:

-Property address

-Rental price

-Property link

-Cleans and formats the extracted data

-Automatically fills and submits a Google Form for each listing

**Tech Stack**

-Python 3

-BeautifulSoup

-Requests

-Selenium

-Chrome WebDriver



**How It Works**

• Send HTTP request to the Zillow clone site.

• Parse the HTML using BeautifulSoup.

• Extract required data fields.

• Clean and format the scraped data.

• Use Selenium to:

• Open the Google Form

• Fill inputs dynamically

• Submit

• Repeat for all listings


**Notes**

-This project is built for educational purposes.

-Web scraping real-world websites may violate their terms of service.

-Always review a website’s policies before scraping.


**What I Learned**

• Handling dynamic elements using Selenium

• Using explicit waits to avoid ElementNotInteractableException

• Cleaning and structuring scraped data

• Automating repetitive browser tasks

---● **License** ●---

This project is licensed under the MIT License.
