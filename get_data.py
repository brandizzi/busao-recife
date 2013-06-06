#!/usr/bin/env python
import re
import requests
from bs4 import BeautifulSoup

from entities import Route, Itinerary, Trajectory
from parsing import get_routes, get_itineraries, get_company, get_price

ROUTES_URL = 'http://200.238.84.28/site/consulta/itinerarios.asp'
ROUTE_URL = 'http://200.238.84.28/site/consulta/itinerarios.asp?linha={route}'
ITINERARY_URL = ('http://200.238.84.28/site/consulta/itinerarios.asp?'
        'linha={route}&nomeitinerario={itinerary}')

if __name__ == "__main__":
    routes_result = requests.get(ROUTES_URL)
    soup = BeautifulSoup(routes_result.text)
    routes = get_routes(soup)

    for route in routes:
        route_result = requests.get(ROUTE_URL.format(route=route.code))
        soup = BeautifulSoup(route_result.text)

        route.company = get_company(soup)
        route.price = get_price(soup)
        route.info = get_info(soup)

        route.itineraries = get_itineraries(soup)
        current_itinerary = get_active_itinerary(soup)

        print route

        for itinerary in route.itineraries:
            if itinerary != current_itinerary:
                itinerary_result = requests.get(ITINERARY_URL.format(
                    route=route.code,
                    itinerary=itinerary.code
                ))
                soup = BeautifulSoup(itinerary_result.text)
            itinerary.going = get_going_trajectory(soup)
            itinerary.coming = get_coming_trajectory(soup)
            print ' ' + str(itinerary)



    for route in routes: print route
