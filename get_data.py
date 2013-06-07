#!/usr/bin/env python
import time

import requests
from bs4 import BeautifulSoup

from entities import Route, Itinerary, Trajectory
from parsing import get_routes, get_itineraries, get_active_itinerary, \
        get_company, get_price, get_info, \
        get_coming_trajectory, get_going_trajectory

ROUTES_URL = 'http://200.238.84.28/site/consulta/itinerarios.asp'
ROUTE_URL = 'http://200.238.84.28/site/consulta/itinerarios.asp?linha={route}'
ITINERARY_URL = ('http://200.238.84.28/site/consulta/itinerarios.asp?'
        'linha={route}&nomeitinerario={itinerary}')

if __name__ == "__main__":
    routes_result = requests.get(ROUTES_URL)
    soup = BeautifulSoup(routes_result.text)
    routes = get_routes(soup)
    
    indentation = ''

    for route in routes:
        time.sleep(3)
        route_result = requests.get(ROUTE_URL.format(route=route.code))
        soup = BeautifulSoup(route_result.text)

        route.company = get_company(soup)
        route.price = get_price(soup)
        route.info = get_info(soup)

        route.itineraries = get_itineraries(soup)
        current_itinerary = get_active_itinerary(soup)

        print indentation, route.name
        indentation += '\t'

        for itinerary in route.itineraries:
            time.sleep(3)
            if itinerary != current_itinerary:
                itinerary_result = requests.get(ITINERARY_URL.format(
                    route=route.code,
                    itinerary=itinerary.code
                ))
                soup = BeautifulSoup(itinerary_result.text)
            itinerary.going = get_going_trajectory(soup)
            itinerary.coming = get_coming_trajectory(soup)

            print indentation, itinerary.name

            indentation += '\t'
            print indentation, itinerary.coming.name
            indentation += '\t'
            for place in itinerary.coming.places:
                print indentation, place
            indentation = indentation[:-1]
            print indentation, itinerary.going.name
            indentation += '\t'
            for place in itinerary.going.places:
                print indentation, place
            indentation = indentation[:-2]
        indentation = indentation[:-1]
