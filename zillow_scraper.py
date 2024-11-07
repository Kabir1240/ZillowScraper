import requests
import re
from typing import Dict
from bs4 import BeautifulSoup


URL = "https://appbrewery.github.io/Zillow-Clone/"

class ZillowScraper:
    def __init__(self) -> None:
        """
        initializes scraper for Zillow and finds the photo cards
        """
        
        response = requests.get(URL)
        response.raise_for_status()
        
        self.soup = BeautifulSoup(response.text, 'html.parser')
        
        self.photo_cards = self.soup.find("ul", class_="List-c11n-8-84-3-photo-cards")\
        .find_all("li", class_="ListItem-c11n-8-84-3-StyledListCardWrapper")
        
    def get_property_info(self, attribute: str) -> list:
        """
        Generic function to return a list of specified attributes for each property on the page.
        
        :param attribute: The name of the attribute to retrieve (e.g., "link", "price", "address").
        :return: A list of the specified attribute for properties found on the page.
        :rtype: list
        """
        
        items = []
        for photo_card in self.photo_cards:
            if attribute.lower() == "link":
                link = photo_card.a.get("href")
                items.append(link)
                
            elif attribute.lower() == "price":
                price = photo_card.find("span", {'data-test': 'property-card-price'}).text
                
                pattern = r"\$\d{1,3}(?:,\d{3})*"
                match = re.search(pattern, price)
                if match:
                    items.append(match.group())
                
            elif attribute.lower() == "address":
                address = photo_card.address.text.rstrip().lstrip()
                items.append(address)
        
        return items
            
    def get_links(self) -> list:
        """
        returns a list of URLs for each property on the page

        :return: a list of URLs for properties found on Zillow
        :rtype: list
        """
        
        return self.get_property_info("link")
        
    def get_prices(self) -> list:
        """
        returns a list of prices for each property on the page

        :return: a list of prices for properties found on Zillow
        :rtype: list
        """
        
        return self.get_property_info("price")
    
    def get_addresses(self) -> list:
        """
        returns a list of addresses for each property on the page

        :return: a list of addresses for properties found on Zillow
        :rtype: list
        """
        
        return self.get_property_info("address")
    
    def get_zillow_dict(self) -> Dict[str, list]:
        """
        returns a dictionary with links, addresses and prices from the Zillow website properties

        :return: a dictionary with links, addresses and prices from the Zillow website properties
        :rtype: Dict[str, list]
        """
        
        zillow_dict = {
            "links":self.scraper.get_links,
            "addresses":self.scraper.get_addresses,
            "prices":self.scraper.get_prices
        }

        return zillow_dict
