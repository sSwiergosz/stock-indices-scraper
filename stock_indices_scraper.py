''' This is a web scraper, which retrieves stock indices from the Bloomberg Quote website. '''
import sys
import re

from urllib.request import urlopen
from bs4 import BeautifulSoup

end = False
abbr_list = []

print('This is a web scraper, which retrieves stock indices from The Bloomberg Quote website. You can check the values and save it to csv file. If you want to use scraper for several different companies - enter the abbreviations separated with space.\n')

while end == False:
	abbreviation = input('Enter a company name abbreviation, which value you want to know.\nTip: use the abbreviation from the stock.\n\nI\'m looking for index of: ')

	abbr_list = [x.strip() for x in abbreviation.split()]

	for i in abbr_list:

		source_page = 'http://www.bloomberg.com/quote/{}:IND'.format(i)

		page = urlopen(source_page)

		soup = BeautifulSoup(page, 'html.parser')

		# look for particular class inside our site
		name_container = soup.find('h1', attrs={'class': 'name'})
		price_container = soup.find('div', attrs={'class': 'price'})
		# change_container = soup.find('div', attrs={'class': 'change-container'})

		name = name_container.text.strip()
		price = price_container.text

		print(name, '-', price)

	decision = input("\nDo you want to look for the other stock indices? [y/N]: ")
	if decision == 'N':
		end = True