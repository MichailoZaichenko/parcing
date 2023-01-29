# -*- coding: utf-8 -*-
import bs4
import requests, sys, os
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
resp = requests.get('https://www.gismeteo.ua/weather-dnipro-5077/now/', headers=headers)
resp.encoding = 'utf'

if resp.status_code == 200:
    resp = resp.text
else:
    sys.exit()

soup = bs4.BeautifulSoup(resp, 'html.parser')
time = soup.find('div', class_="now-localdate").getText()
temp =  soup.find('span', class_='unit unit_temperature_c').getText()
filling = soup.find("div", class_="now-feel").find('span', class_='unit unit_temperature_c').getText()
weather = soup.find('div', class_="now-desc").getText()
wind = soup.find('div', class_="unit unit_wind_m_s").getText()
presure = soup.find('div', class_="unit unit_pressure_mm_hg_atm").getText()
humabiliti = soup.find('div', class_="now-info-item humidity").find('div', class_="item-value").getText()
eathequake = soup.find('div', class_="now-info-item gm").find('div', class_="item-value").getText()

print(time)
print(f'Температура: {temp}')
print(f'Відчувається: {filling}')
print(weather)
print(f"Вітер: {wind} м/с")
print(f"Давление: {presure}")
print(f"Вологість: {humabiliti}%")
print(f"Г/м активність: {eathequake} из 9")

