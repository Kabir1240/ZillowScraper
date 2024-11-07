from zillow_scraper import ZillowScraper
from fill_form import fill_form


# get data from scraper
scraper = ZillowScraper()
prices = scraper.get_prices()
addresses = scraper.get_addresses()
links = scraper.get_links()

# make sure the number of properties is consistent
if len(prices) != len(addresses) or len(prices) != len(links):
    raise ValueError("There should be an equal number of prices, addresses and links")

# fill out form with the scraped data
for index in range(len(prices)):
    fill_form(price=prices[index], address=addresses[index], link=links[index])
