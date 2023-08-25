import requests
from bs4 import BeautifulSoup
import json

class exchange_main:
	def exchange(self,from_currency):
		file_name = 'country_currency.json'
		f = open (file_name, "r")
		data = json.loads(f.read())
		the_currency_from = data[from_currency]
		to_currency = 'EGP'
		ammount = 1
		link =  f"https://www.xe.com/currencyconverter/convert/?Amount={ammount}&From={the_currency_from}&To={to_currency}"
		while True:
			try:
				response = requests.get(link)
				
				src = response.content
				soup = BeautifulSoup(src, "lxml")
				product_titles = soup.find('p',{"class": "result__BigRate-sc-1bsijpp-1 iGrAod"}).text
				break
			except:
				print("there is a problem with internet connection +++ from(_1_1_currency changer)")
				input('for try again press eny key : ')
#		response = requests.get(link)
#		src = response.content
#		soup = BeautifulSoup(src, "lxml")
#		product_titles = soup.find('p',{"class": "result__BigRate-sc-1bsijpp-1 iGrAod"}).text
		return product_titles[:5]
		
