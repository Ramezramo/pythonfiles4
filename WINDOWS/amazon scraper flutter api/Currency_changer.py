import requests
from bs4 import BeautifulSoup
import json

class exchange_main:
	def exchange(self,from_currency):
		file_name = 'country_currency.json'
		f = open (file_name, "r")
		data = json.loads(f.read())
		
		
		
		
		the_currency_from = data[from_currency]

		
		#from_currency ='USD'
		#to_currency = str(input("Enter in the currency you'd like to convert to: ")).upper()
#		print(f'message from currency module = ==== the currency from ====== {the_currency_from}')
		to_currency = 'EGP'
		#amount = input("Enter in the amount of money: ")
		#amount = 1
		
		ammount = 1
		link =  f"https://www.xe.com/currencyconverter/convert/?Amount={ammount}&From={the_currency_from}&To={to_currency}"
		
		response = requests.get(link)
		
		src = response.content
		soup = BeautifulSoup(src, "lxml")
		product_titles = soup.find('p',{"class": "result__BigRate-sc-1bsijpp-1 iGrAod"}).text
		
		#("class":"result__BigRate-sc-1bsijpp-1 iGrAod")
		#<p class="result__BigRate-sc-1bsijpp-1 iGrAod">135.37<span class="faded-digits">406</span> Egyptian Pounds</p>
		
		#print('message from the currency module ====',product_titles[:5])
		
		#print(link)
		return product_titles[:5]
		
