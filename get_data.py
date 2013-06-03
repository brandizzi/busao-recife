#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup

from entities import Itinerary

ITINERARY_URL = 'http://200.238.84.28/site/consulta/itinerarios.asp'

def get_itineraries(soup):
    options = soup.find('select', {'name':'SelLinhas'}).find_all('option')
    code2name = {int(option['value']) : option.text.strip()
            for option in options if int(option['value'])}
    return (Itinerary(code, name) for code, name in code2name.items())

if __name__ == "__main__":
    itineraries_result = requests.get(ITINERARY_URL)
    soup = BeautifulSoup(itineraries_result.text)
    itineraries = get_itineraries(soup)
    for itinerary in itineraries:
        

