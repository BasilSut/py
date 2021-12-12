#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# получить стоимость одной норвежской кроны(NOK) в венгерских форинтах (HUF)

import requests 
from lxml import etree 


def resp(id):
    xml_response = etree.fromstring(requests.get("http://www.cbr.ru/scripts/XML_daily.asp").text.encode("1251"))
    nominal = int(xml_response.find("Valute[@ID='"+ id +"']/Nominal").text)
    name = xml_response.find("Valute[@ID='"+ id +"']/Name").text
    curs = float(xml_response.find("Valute[@ID='"+ id +"']/Value").text.replace(',', '.'))
    print(f"{nominal} {name} = {curs} рублей")
    curs_for_1 = float(curs/nominal)
    print(f"{name}(1) = {curs_for_1:.5f} рублей")
    return curs_for_1


HUF = resp("R01135") 
NOK = resp("R01535")    
cross_course = NOK/HUF
print(f"1 NOK = {cross_course:.5f} HUF")