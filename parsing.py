#!/usr/bin/env python
from entities import Route, Itinerary, Trajectory

def get_routes(soup):
    select = soup.find('select', {'name':'SelLinhas'})
    options = select.find_all('option')
    code2name = (
            ( int(option['value']),  option.text.strip() )
             for option in options
    )

    return [ Route(code, name) for code, name in code2name if code ]

def get_itineraries(soup):
    select = soup.find('select', {'name':'SelNomeItinerario'})
    options = select.find_all('option')
    code2name = (
            ( int(option['value']),  option.text.strip() )
             for option in options
    )

    return [ Itinerary(code, name) for code, name in code2name if code ]

def get_active_itinerary(soup):
    select = soup.find('select', {'name':'SelNomeItinerario'})
    option = select.find('option', selected=True)
    code, name = int(option['value']),  option.text.strip()

    return Itinerary(code, name)

def get_price(soup):
    label_element = soup.find('b', text=re.compile(r'Tarifa\s*:'))
    value_element = label_element.parent.find_next_sibling()
    value = value_element.text

    return float(value.replace('R$','').replace(',','.').strip())

def get_company(soup):
    label_element = soup.find('b', text=re.compile(r'Empresa\s*:'))
    value_element = label_element.parent.find_next_sibling()
    value = value_element.text

    return value.strip()

def get_info(soup):
    price_element = soup.find('b', text=re.compile(r'Tarifa\s*:'))
    table = price_element.parent.parent
    cell = table.find_all('td')[2]

    return cel.text.strip()

def get_going_trajectory(soup):
    title_cell = soup.find('td', text=re.compile(r'TERMINAL/PONTO DE RETORNO'))
    outer_table = title_cell.parent.parent
    inner_talbe = outer_table.find('table')
    cells = (
        row.find_all('td')
            for row in inner_talbe.find_all('tr')[2:]
            if len(row.find_all('td')) == 3
    )

    places = [
        Place(municipality.text.strip(), location.text.strip())
            for location, _, municipality in cells
    ]

    return Trajectory(places)

def get_coming_trajectory(soup):
    title_cell = soup.find('td', text=re.compile(r'PONTO DE RETORNO/TERMINAL'))
    outer_table = title_cell.parent.parent
    inner_talbe = outer_table.find('table')
    cells = (
        row.find_all('td')
            for row in inner_talbe.find_all('tr')[2:]
            if len(row.find_all('td')) == 3
    )

    places = [
        Place(municipality.text.strip(), location.text.strip())
            for location, _, municipality in cells
    ]

    return Trajectory(places)


