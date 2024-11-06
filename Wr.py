import requests
import json
from degree import dgr_chr
import os
from datetime import datetime as dt
import time

if os.path.exists(os.getcwd()+'/weather_cities') == False:
	os.mkdir(os.getcwd()+'/weather_cities') 

class Weather:
	def __init__(self, x=None, api=None, url=False):
		self.__x = x
		self.__api = # api
		self.__main_sities = ['Tokio', 'Moscow', 'New York', 'London', 'Berlin', 'Pekin', 'Jerusalem']
		self.__url = f"https://api.openweathermap.org/data/2.5/" if url == False else url
	def start(self):
		responce = requests.get(self.__url+f'forecast?q={self.__x}&appid={self.__api}')
		
		if responce.status_code == 200 and self.__x:
			with open("responce.json","w") as file:
				obj = json.loads(responce.text)
				json.dump(obj,file)
		else:
			raise NameError
		
		with open("responce.json") as wee:
			obj = json.load(wee)
		adress = os.getcwd()+f'/weather_cities/{self.__x} - {dt.now().date()}.txt'

		with open(adress,"w") as file:
			file.write(self.__x+"\n\n")
			for k,i in enumerate(obj.get("list")):
				temps = dgr_chr(i.get("main").get("temp"))
				dts = i.get("dt_txt")
				print(f"{temps}C",*dts.split(),sep=" - ",file=file)
		return adress
	
	def main_city(self):
		for i in self.__main_sities:
			name = i
			responce = requests.get(self.__url+f'forecast?q={i}&appid={self.__api}')
			time.sleep(1)
			
			if responce.status_code == 200 and name:
				with open("responce.json","w") as file:
					obj = json.loads(responce.text)
					json.dump(obj,file)
			else:
				raise NameError
			
			with open("responce.json") as wee:
				obj = json.load(wee)
			adress = os.getcwd()+f'/weather_cities/{name} - {dt.now().date()}.txt'

			with open(adress,"w") as file:
				file.write(name+"\n\n")
				for k,i in enumerate(obj.get("list")):
					temps = dgr_chr(i.get("main").get("temp"))
					dts = i.get("dt_txt")
					print(f"{temps}C",*dts.split(),sep=" - ",file=file)
