
#update[13.2] update name >(_adding comma to the price[23~)

#update[13.2] what i will do (i will add comma to the price)




#update[13.2] started in [09/02/2023 15:03]

# history >> (


#13.2 succesfuly added comma def and this function worked like a bullet
#and while i am writeing this notes i descovered a new keyboard and it is an ammazing one that i have seen before it contain a new tricks and new features i love it it will help me alot in programming with my phone i will write its name right now (unexpected keyboard) it was on my phone but i didnt now that it was here (4.5 pm)

#                     )
#i finshed it in [09/02/2023 4:30]®














from _1_1_setting_control_system import json_hi
from _1_1_currency_changer import exchange_main
from colorama import Fore,Back
from texttable import Texttable#8.3
from bs4 import BeautifulSoup
import requests
import json
import os
import webbrowser
import random
import html#4.6
import socket






def internet(host="8.8.8.8", port=53, timeout=3):#9.3
    try:#9.3
        socket.setdefaulttimeout(timeout)#9.3
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))#9.3
        return True #9.3
    except socket.error as ex:#9.3
        return False #9.3


if internet() == False:#9.3
	if_offline = ""#9
else:#9.3
	if_offline = "online"#9.3
#if_offline = 'hh'

def offline_contry_currency(country_name):#9
	offline_dict = {"egypt": "1.00","saudia": "5.231","emirates": "5.341","china": "2.708","france": "19.34","italy": "19.34","japan": "0.132","holand": "19.34","poland": "4.050","singapore": "13.86","espania": "19.34","swide": "1.751","jermany":"19.34"}
	return offline_dict[country_name]#9


file_name = 'E:\\programming\\programming\\ABC_my_python_files\\files 4\\amazon scraper flutter api\\links.json'
f = open (file_name, "r")
data = json.loads(f.read())


#from this line i deleted some of codes that i put to import the settings from the jeson file

def op(link_):
	webbrowser.open(f"{link_}")

big_calc = 0
def price_convertor (the_price,value_of_currency,country_name):
	country_name_ = country_name
	item_price = html.unescape(f"{the_price}")
	
	price_unscaped = ""
	for i in item_price:
		if i in ["1","2","3","4","5","6","7","8","9","0",",",'.']:
			price_unscaped += i
		else:
			continue
	found_in = price_unscaped[4:].find(price_unscaped[0:3])
	found_in_plus = found_in + 4
	price_redy_to_float = price_unscaped[:found_in_plus]
	if found_in == -1 :
		price_redy_to_float = price_unscaped
	if country_name == "japan":
		without_after_c = price_redy_to_float[:4]
		for i in price_redy_to_float[4:]:
			if i == ',':
				break
			without_after_c += i
	elif country_name != "japan":
		without_after_c = price_redy_to_float[:3]
		for i in price_redy_to_float[3:]:
			if i == ',':
				break
			without_after_c += i
	if '.' in without_after_c[2:]:#9.5
		without_after_c1 = ''#9.5
		for i in without_after_c:#9.5
			if i == '.':#9.5
				break #9.5
			without_after_c1 += i#9.5
	else:#9.5
		without_after_c1 = without_after_c#9.5
	price_replaced = without_after_c1.replace(",","")
	price_replaced2 = price_replaced.replace(".","")
	price_replaced3 = price_replaced2.replace(" ","")
	if country_name != "japan":
		try:
			price_floated = float(price_replaced3)
		except:
			price_floated = 0
			print("cant replace this")
	else:
		price_floated = float(price_replaced3)
	#print('price floated',price_floated)
	price_in_egy = price_floated * float(value_of_currency)
	return int(price_in_egy),f"{value_of_currency} \n=> ( {price_floated} ) * ( {float(value_of_currency)} ) = ( {price_in_egy} )", value_of_currency# up in 10.3


def searcher(amazon_link,the_word_search,country_name,currency_ammount):
	the_name_of_item = 0
	the_name_of_item += big_calc
	if if_offline != '':#9
		words = the_word_search.split()#4.0
		var = len(words)
		search_text_to_add_in_link = ""#4.0
		word_get_calc = 0
		for i in range(var):#4.0
			search_text_to_add_in_link += f"{words[word_get_calc]}+"
			word_get_calc += 1
		amazon_link1 = amazon_link+'s?k='+search_text_to_add_in_link[:-1]#4.0
		while True :
			try:
				result = requests.get(amazon_link1)
				break
			except:
				print('There is a Problem with Internet conection')
				input('press eny key for try again')
				continue
		if not result:#8.5
			for i in range (3):#8.5
				try:#8.5
					print('connecting again !!!')#8.5
					result = requests.get(amazon_link1)#8.5
					if not result:#8.5
						print('server timeout !!')#8.5
						continue #8.5
					else:#8.5
						print('successfull response !!')#8.5
						break #8.5
				except:#8.5
					print('There is a Problem with Internet conection')#8.5
					input('press eny key for try again')#8.5
					continue #8.5
		else:#8.5
			print('successfull response !!')#8.5
			pass#8.5
		src = result.content
		soup = BeautifulSoup(src, "lxml")
		product_titles = soup.find_all('div',{'class':'s-card-container s-overflow-hidden aok-relative puis-expand-height puis-include-content-margin puis s-latency-cf-section s-card-border'})
	else:
		print("in offline search i will outomatically search about (rtx)")
		the_folder = "Amazons_offline/"
		result = open(the_folder+str(country_name)+str(".html"),"r")
		soup = BeautifulSoup(result, "lxml")
		product_titles = soup.find_all('div',{'class':'s-card-container s-overflow-hidden aok-relative puis-expand-height puis-include-content-margin puis s-latency-cf-section s-card-border'})

	
	the_dict = {}
	for item in product_titles:
		the_name_of_item += 1
		product_titles2 = item.find('span',{"class": "a-price-whole"})
		try :
			the_price2 = product_titles2.text
			
			the_price = the_price2
		except :			
			the_price = "no price"		
		name = item.find('a',{'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
		name1 = name.text
		name = html.unescape(name1)#4.6
		link = item.find('a',{'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
		the_link = link['href']
		discount = item.find('span',{'class':'a-price a-text-price'})
		try :
			the_discount = discount.text
			discount2 = the_discount
		except:
			discount2 = 'no discount'
		link_for_delet_space = amazon_link[:-1],the_link
		the_final_link = ''

		for i in link_for_delet_space:
			if i == ' ':
				continue
			the_final_link += i
		def GetP(data2):
			m=3
			p= ""
			while len(p)!=m:
				v=random.choice(data2)
				p+=v
			return p
		data2 = ("1234567890")
		rand_num = GetP(data2)
		if discount2 != 'no discount':
			discount_egypt_convertor = price_convertor (discount2,currency_ammount,country_name)
			discount_egypt_convertor1 = discount_egypt_convertor[0]
		else :
			discount_egypt_convertor1 = 'no discount to convert'
		if the_price != "no price":
			price_egypt_convertor = price_convertor (the_price,currency_ammount,country_name)
			price_two = price_egypt_convertor[0]
			
		else :
			price_egypt_convertor = 'no price to convert'
			price_two = 'no price to convert'
		currency_ammount_will_view = price_egypt_convertor[2]
		country_dict = {f"{rand_num}":{"country_name":f"{country_name}","item name":f"{name}","price":the_price,"price_egypt_convertor":f"{price_two}","link":f"{the_final_link}","discount":f"{discount2}","discount_egypt_convertor":f"{discount_egypt_convertor1}",'currency today':currency_ammount_will_view}}
		the_dict.update(country_dict)
	return the_dict


def is_what_percent_of(num_a, num_b):#9.5
    return (num_a / num_b) * 100


the_big_dict = {}
user_favorets_dict = {}
def user_output(user_product_name,country):
	the_country_that_user_chose = value_dict[country]
	print(the_country_that_user_chose)
	link = (data[the_country_that_user_chose])
	link_updated = link
	if if_offline !='':#9
		currency_ammount = exchange_main.exchange(0,the_country_that_user_chose)
	else:#9
		currency_ammount = offline_contry_currency(the_country_that_user_chose)#9
	the_dict = searcher(link_updated,user_product_name,the_country_that_user_chose,currency_ammount)
	for key1,value1 in the_dict.items():
			the_big_dict.update(the_dict)
	for key,value in the_dict.items():#4.5 
		item_code = key
		item_price = value['price']
		item_link = value['link']
		item_country = value['country_name']
		item_discreption = value['item name']
		is_discount = value['discount']
		japan_first_num = ''
		the_price_in_egy = value['price_egypt_convertor']
		if item_country == "japan":#لان تحويل عملة اليابان فية بعض الصعوبة فقد قمت بجعل نتيجة سعر اليابان تظهر الوف فقط بدون كسور 
			
			for i in the_price_in_egy:
				if i == '.':
					break
				japan_first_num += i
			the_price_in_egy = japan_first_num
		else:
			the_price_in_egy = the_price_in_egy
		discount_in_egy = value['discount_egypt_convertor']
		currency_today = value['currency today']
		if is_discount == 'no discount':
			real_price_discount = None
			discount_pounded = None
		else:
			real_price_discount = html.unescape(is_discount)
			discount_pounded = discount_in_egy
			elfarq = int(discount_pounded) - int(the_price_in_egy)
		try:#9.5
			discount_percentage = is_what_percent_of(int(elfarq), int(discount_pounded))#9.5
		except:#9.5
			discount_percentage = '0'#9.5
		user_favorets_dict.update({item_code:{"item_country":item_country,"discount":real_price_discount,"item_num":big_calc,"discount_percentage ":f'{int(discount_percentage)}',"discount in egy":f'{discount_in_egy}',"price_before_discount":discount_pounded,"currency_today_value":currency_today,"item_discreption_":item_discreption,"item_price":item_price,"item_price_converted":the_price_in_egy,"item_link_":item_link}})
		
def read_settings_read():
	file_name = "E:\\programming\\programming\\ABC_my_python_files\\files 4\\amazon scraper flutter api\\_1_3_settings.json"
	f = open (file_name, "r")
	data = json.loads(f.read())
	#json_settings = data["view_discount_"]
	
	#view_discount_percentage = data["discount_percentage"]
	currency_today = data["currency_value"]
	item_link = data["item_link"]
	#discreption = data["item_discreption"]
	#currency_calculation = data["calculate_currency"]
	
	#print(ranking_discounts)
	return [currency_today,item_link]
	
	
json_settings = read_settings_read()
			
small_calc = 0
def adding_comma(_num):#added 13.2
	NUM_LEN =len(_num)
	if NUM_LEN == 4:
		num_added_comma = ""
		counter66 = 0
		for i in _num:
			if counter66 == 1:
				num_added_comma += ','
			num_added_comma += i
			counter66 += 1
	elif NUM_LEN == 5:
		num_added_comma = ""
		counter66 = 0
		for i in _num:
			if counter66 == 2:
				num_added_comma += ','
			num_added_comma += i
			counter66 += 1
	elif NUM_LEN == 6:
		num_added_comma = ""
		counter66 = 0
		for i in _num:
			if counter66 == 3:
				num_added_comma += ','
			num_added_comma += i
			counter66 += 1
	elif NUM_LEN == 7:
		num_added_comma = ""
		counter66 = 0
		for i in _num:
			if counter66 == 1:
				num_added_comma += ','
			num_added_comma += i
			counter66 += 1


	else:
		num_added_comma =_num
			
			
	return num_added_comma#added 13.2
			
			
def get_user_output(dict_will_appear):

	for key,value in dict_will_appear.items():
		item_code = key
		item_num = value["item_num"]
		item_price = value['item_price']
		
		item_link = value['item_link_']
		item_country = value['item_country']
		item_discreption = value['item_discreption_']
		is_discount = value['discount']
		
		the_price_in_egy = value['item_price_converted']
		the_price_in_egy = f'{adding_comma(the_price_in_egy)} '#added 13.2
		discount_percentage = value['discount_percentage ']#9.5
		currency_today = value['currency_today_value']
		discount_in_egy = value["discount in egy"]
		discount_in_egy = f'{adding_comma(discount_in_egy)} '#added 13.2
		def printer_ ():
			global small_calc
			small_calc += 1
			print(Fore.LIGHTCYAN_EX,item_country,Fore.RESET)
			print(f"\n{Back.BLACK}{Fore.LIGHTYELLOW_EX}{item_discreption}{Fore.RESET}{Back.RESET}")
			print(f"\nitem price in egy {Back.LIGHTGREEN_EX}{Fore.LIGHTRED_EX}{the_price_in_egy}{Fore.RESET}{Back.RESET}")
			
			if is_discount == 'no discount' or is_discount == None:
				print("")
			else:
				print(f"{Fore.LIGHTGREEN_EX}{is_discount}{Fore.RESET}")
				print(f'price before discount {Back.LIGHTRED_EX}{Fore.LIGHTGREEN_EX}{discount_in_egy}{Fore.RESET}{Back.RESET}')
				
				print(f'discount percentage ({discount_percentage}%)')#9.5
			if json_settings[0] == "on":
				print(f'\ncurrency value ({currency_today})')
			
			
			
			print(f"the foriegn price({item_price})")
			if json_settings[1] == "on":
				print(f"\n{Fore.BLUE}{item_link}{Fore.RESET}")
			print(f"\n{small_calc}=>> ×item code ({item_code}) ")

			print("_"*60)
			print("_"*60)
			print(" ")
		printer_()



def search_in_range():
	try :
		user_ranges = None
		for i in range(100):
			try:
				print('\n type your range in thousands')
				range_from0 = int(input('search from : '))
				range_from = f"{range_from0}000"
				range_to0 = int(input('search to '))
				range_to = f"{range_to0+1}000"#updated in 10.2
				user_ranges = {"from":f"{int(range_from)}","to":f"{int(range_to)}"}
				break
			except:
				print("please type a vaild num")
	except:
		print('the error in here')
	return user_ranges

def view_discount_def(dict,print_or_no):
		discount_dict = {}
		for key, value in dict.items():
			if value["discount"] != None :
				discount_dict.update({key:value})
		if print_or_no == "y":
				get_user_output(discount_dict)
		return discount_dict
				
		
def ranges(dict):
	discount_dict = {}
	ranges = search_in_range()
	for key,value in dict.items():
		try:
			if value["item_price_converted"] == 'no price to convert':
				continue
			if int(value["item_price_converted"]) >= int(ranges["from"]) and int(value["item_price_converted"])<= int(ranges["to"]) :
				discount_dict.update({key:value})
		except:
			continue
	return discount_dict


def ranges_discount(dict,print_or_no):
	discount_ranges_dict = {}
	ranges = search_in_range()
	for key,value in dict.items():
		try:
			if value["item_price_converted"] == 'no price to convert':
				continue
			if int(value["item_price_converted"]) >= int(ranges["from"]) and int(value["item_price_converted"])<= int(ranges["to"]) :
					discount_ranges_dict.update({key:value})
		except:
			continue
	if print_or_no == "y":
		get_user_output(discount_ranges_dict)
	return discount_ranges_dict


def ranking(dict):
		result_ranked = {}
		name_price_dict = {}
		for key,value in dict.items():
			the_price__ = value["item_price_converted"]
			if the_price__  == 'no price to convert':
				continue
			else:
				name_price_dict.update({key:int(the_price__)})
		sorted_x = sorted(name_price_dict.items(), key=lambda kv: kv[1])
		for i in sorted_x:
			for i2 in i :
				the_value_ = dict[i2]
				result_ranked.update({i2:the_value_})
				break
		get_user_output(result_ranked)
			
			
def ranking_discounts(dict):
		result_ranked = {}
		name_price_dict = {}
		for key,value in dict.items():
			the_price__ = value["item_price_converted"]
			if the_price__  == 'no price to convert':
				continue
			else:
				name_price_dict.update({key:int(the_price__)})
		sorted_x = sorted(name_price_dict.items(), key=lambda kv: kv[1])
		for i in sorted_x:
			for i2 in i :
				the_value_ = dict[i2]
				result_ranked.update({i2:the_value_})
				break
		get_user_output(result_ranked)
def sort_by_percentage(dict):#9.6
		result_ranked = {}
		name_price_dict = {}
		for key,value in dict.items():
			the_percentage = value["discount_percentage "]
			if the_percentage  == 'no price to convert':
				continue
			else:
				name_price_dict.update({key:int(the_percentage)})
		sorted_x = sorted(name_price_dict.items(), key=lambda kv: kv[1])
		try:#9.6
			counter = 1#9.6
			for i in sorted_x:#9.6
				
				for i2 in sorted_x[-counter] :
					the_value_ = dict[i2]
					result_ranked.update({i2:the_value_})
					break
				counter += 1#9.6
		except:#9.6
			pass #9.6
		get_user_output(result_ranked)


while True :
	
	user_favorets_dict = {}
	value_dict = {}
	contry_num = []
	new_ = []#8.3
	main = True
	while main:
		calc = 0
		new_.clear()#8.3
		new_.append(["country num","country name"])#8.3
		for key, value in data.items():
			calc += 1
			new_.append([f"{str(calc)} =>",key])#8.3
			value_dict.update({calc:key})
			contry_num.append(str(calc))
		new_.append(["enter => ","search in all"])
		t = Texttable()#8.3
		t.add_rows(new_)#8.3
		print(f"{Fore.LIGHTYELLOW_EX}")
		print(t.draw())#8.3
		print(f"{Fore.RESET}")
		print(Fore.LIGHTCYAN_EX,"="*57,Fore.RESET)#8.6
		if if_offline == "":#9
			print(f"{Fore.LIGHTRED_EX} you are in offline mode{Fore.RESET}")#9
		else:#9
			print(f'{Fore.LIGHTGREEN_EX} you are in online mode {Fore.RESET}')#9
		print(Fore.LIGHTCYAN_EX,"="*57,Fore.RESET)#8.6
#from this line i deleted some of codes that i put to import the settings from the jeson file
		print(f"for enter the settings type [{Fore.LIGHTYELLOW_EX}s{Fore.RESET}]")
		input_1 = input(f'\nfor search in all amazons press {Fore.LIGHTYELLOW_EX}enter{Fore.RESET}!!!\nplease input {Fore.LIGHTYELLOW_EX}country num {Fore.RESET}: ').lower()#4.4 ,, 10.2 + [.lower()]
		if input_1 in contry_num:
			while True:#4.1
				try:#4.1
					the_country_that_user_chose = value_dict[int(input_1)]
					break
				except:#4.1
					print('please input a correct country num ')
					input_1 = None#4.4
					continue
			print(Fore.LIGHTCYAN_EX,"\n",the_country_that_user_chose,Fore.RESET)
		
			if if_offline != "":#9
				user_product_name = input('product name !? ')
			else:
				user_product_name = 'rtx'
			user_output(user_product_name,int(input_1))
			ranking(user_favorets_dict)
			print(Fore.LIGHTMAGENTA_EX,"$" *119,Fore.RESET)#adding [11]
			
			smaall_dict_local = {"1":"sort results","2":"search in range","3":"view discounts only","4":"view discounts in range","5":"sort discounts by pecentage"}#adding[11.1]
			
			for i in range (10):#adding [11]#11.4 edit
				print("""
1 - sort results 
2 - search in range 
3 - view discounts only 
4 - view discounts in range
5 - sort discounts by pecentage
	""")#adding11#11.4 edit
				veiwing_results_user_choise = input('[x] for open product amazon page \n[s] for settings\nenter the num of your sorting results method : ')#adding [11]
				if veiwing_results_user_choise == '3':#edit [11]
					print(Fore.LIGHTMAGENTA_EX,"$" *119,Fore.RESET)
					discounts_dict = view_discount_def(user_favorets_dict,"n")
					
					ranking_discounts(discounts_dict)
					
				elif veiwing_results_user_choise == "2":#3.2,#edit [11]
					print(Fore.LIGHTMAGENTA_EX,"$" *119,Fore.RESET)#adding [11]
					ranges = ranges(user_favorets_dict)#9.1
					ranking(ranges)#9.1
				elif veiwing_results_user_choise == "4":#edit [11]
					print(Fore.LIGHTMAGENTA_EX,"$" *119,Fore.RESET)
					discounts_dict = view_discount_def(user_favorets_dict,"n")
					ranges_discounts = ranges_discount(discounts_dict,"n")
					
					print(ranking(ranges_discounts))
					
				elif veiwing_results_user_choise == "1":#edit [11]
					print(Fore.LIGHTMAGENTA_EX,"$" *119,Fore.RESET)
					ranking(user_favorets_dict)
				elif veiwing_results_user_choise == "5":#edit [11]
					print(Fore.LIGHTMAGENTA_EX,"$" *119,Fore.RESET)
					discounts_dict = view_discount_def(user_favorets_dict,"n")#9.6
					sort_by_percentage(discounts_dict)#9.6
	
				elif veiwing_results_user_choise == "x":#adding [11]
					break#adding [11]
					
				elif veiwing_results_user_choise == "s":#adding [11]
					json_hi.edit_json(9)
					json_settings = read_settings_read()
					continue
				else:#adding [11]
					print("\nerror :(")#adding [11]
					continue #adding [11]
				print("i sorted the results to you in [[", smaall_dict_local[veiwing_results_user_choise],"]]method")#adding[11.1]
				print(Fore.LIGHTMAGENTA_EX,"$" *119,Fore.RESET)#adding [11]
				continue #adding [11]
			
			
			while True :
				input_item_code = input(f'For exit [{Fore.LIGHTYELLOW_EX}x{Fore.RESET}] \nInput Item Code for Product review: ')
				if input_item_code != 'x':
					try:
						value = the_big_dict[input_item_code]
						print(value['link'])
						op(value['link'])
					except:
						continue
				elif input_item_code == 'x':
					main = False
					break
				else:
					print('\nnot found \n')
					continue
		elif input_1 == '' :#4.4
			print(f'{Fore.LIGHTCYAN_EX}searching in all amazons...{Fore.RESET}')#4.4
			if if_offline != "":#9
				user_product_name = input('product name !? ')
			else:
				user_product_name = 'rtx'
			for key, value in value_dict.items():
				print(key,"searching in ")
				user_output(user_product_name,key)							
			ranking(user_favorets_dict)
			print(Fore.LIGHTMAGENTA_EX,"$" *119,Fore.RESET)#edit [11]
			smaall_dict_local = {"1":"sort results","2":"search in range","3":"view discounts only","4":"view discounts in range","5":"sort discounts by pecentage"}#adding[11.1]
			for i in range (10):#adding [11]#11.4 edit
				print("""
1 - sort results 
2 - search in range 
3 - view discounts only 
4 - view discounts in range
5 - sort discounts by pecentage
	""")#adding11#11.4 edit
				veiwing_results_user_choise = input('[x] for open product amazon page \n[s] for settings\nenter the num of your sorting results method : ')#adding [11]
				if veiwing_results_user_choise == '3':#editing[11]
					print(Fore.LIGHTMAGENTA_EX,"$" *119,Fore.RESET)#adding [11]
					discounts_dict = view_discount_def(user_favorets_dict,"n")
					
					ranking_discounts(discounts_dict)
				elif veiwing_results_user_choise == "2":#3.2#editing11
					print(Fore.LIGHTMAGENTA_EX,"$" *119,Fore.RESET)#adding11
					ranges = ranges(user_favorets_dict)#9.1
					ranking(ranges)#9.1
				elif veiwing_results_user_choise == "4":#editing11
					print(Fore.LIGHTMAGENTA_EX,"$" *119,Fore.RESET)
					discounts_dict = view_discount_def(user_favorets_dict,"n")
					ranges_discounts = ranges_discount(discounts_dict,"n")
					
					print(ranking(ranges_discounts))
				elif veiwing_results_user_choise == "1":#editing11
					print(Fore.LIGHTMAGENTA_EX,"$" *119,Fore.RESET)
					ranking(user_favorets_dict)
					
				elif veiwing_results_user_choise == "5":#editing11
					print(Fore.LIGHTMAGENTA_EX,"$" *119,Fore.RESET)
					discounts_dict = view_discount_def(user_favorets_dict,"n")#9.6
					sort_by_percentage(discounts_dict)#9.6
				elif veiwing_results_user_choise == "x":#edding11
					break#adding [11]
				elif veiwing_results_user_choise == "s":#adding [11]
					json_hi.edit_json(9)
					json_settings = read_settings_read()
					continue
				else:#adding [11]
					print("\nerror :(")#adding [11]
					continue #adding [11]
				print("i sorted the results in [[", smaall_dict_local[veiwing_results_user_choise],"]]method")#adding[11.1]
				print(Fore.LIGHTMAGENTA_EX,"$" *119,Fore.RESET)#adding [11]
				continue #adding [11]
			while True :
				input_item_code = input(f'For exit [{Fore.LIGHTYELLOW_EX}x{Fore.RESET}] \nInput Item Code for Product review: ')
				if input_item_code != 'x':
					try:
						value = the_big_dict[input_item_code]
						print(value['link'])
						op(value['link'])
					except:
						continue
				elif input_item_code == 'x':
					
					main = False
					break
				else:
					print('\nnot found \n')
					continue
		elif input_1 == "s" :
			json_hi.edit_json(9)
			json_settings = read_settings_read()
			continue
		else:
			os.system("clear")#8.3
			print('error')
			continue