#®
import os
import json
from colorama import Fore
class json_hi:

	def edit_json(self):
		def read_json():
			os.system('clear')
			file_name = "_1_2_settings_.json"
			f = open (file_name, "r")
			data = json.loads(f.read())
			file_name = "_1_2_settings_.json"
			f = open (file_name, "r")
			data = json.loads(f.read())
			dict = {}
			values_dict = {}
			counter = 0
			for key,value in data.items():
				counter += 1
				dict.update({counter:{key:value}})
				values_dict.update({str(counter):key})
			will_view1 = []
			for key,value in dict.items():
				will_view1.append(f"{value}---->{key}")
			for i in will_view1:
				finder = (i.find('off'))
				
				if finder == -1:
					print(f'{Fore.LIGHTGREEN_EX}{i}{Fore.RESET}')
				else:
					print(i)
		os.system('clear')
		file_name = "_1_2_settings_.json"
		f = open (file_name, "r")
		data = json.loads(f.read())
		dict = {}
		values_dict = {}
		counter = 0
		for key,value in data.items():
			counter += 1
			dict.update({counter:{key:value}})
			values_dict.update({str(counter):key})
			
		will_view = []
		for key,value in dict.items():
			
			will_view.append(f"{value}------>{key}")
		
		for i in will_view:
			finder = (i.find('off'))
			
			if finder == -1:
				print(f'{Fore.LIGHTGREEN_EX}{i}{Fore.RESET}')
			else:
				print(i)
		
		for i in range(12):
			user_input = input("\nfor end press enter\ninput a feature num for open or close it : ")
			if user_input == "":
				os.system('clear')
				break
			try:
				the_value = (values_dict[f"{user_input}"])
				f = open (file_name, "r+")
				data2 = json.load(f)
			
				if data2[str(the_value)] == "off":
					data2[str(the_value)] = 'on'
					f.seek(0)
					json.dump(data2, f)
					f.truncate()
					read_json()
				elif data2[str(the_value)] == "on":
					data2[str(the_value)] = 'off'
					f.seek(0)
					json.dump(data2, f)
					f.truncate()
					read_json()
				file_name = "_1_2_settings_.json"
				f = open (file_name, "r")
				data = json.loads(f.read())
				try:
					for key,value in data.items():
						if key == the_value:

							continue
						
						if value == "on":
							f = open (file_name, "r+")
							data2 = json.load(f)
							data2[str(key)] = 'off'
							f.seek(0)
							json.dump(data2, f)
							f.truncate()
							read_json()
				except :
					print('error')
			except :
				print('error')
			
			
				

		
#json_hi.edit_json(2)