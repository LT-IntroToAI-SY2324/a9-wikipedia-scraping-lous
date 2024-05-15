# some python libraries we'll be using
import re, string, calendar
from wikipedia import page
from bs4 import BeautifulSoup

from typing import List, Match
from utilities import *

# Assignment 8 Part II

def get_planet_radius(planet_name: str) -> str:
    """Gets the radius of the given planet

    Args:
        planet_name - name of the planet to get radius of

    Returns:
        radius of the given planet
    """
    infobox_text = clean_text(get_first_infobox_text(get_page_html(planet_name)))
    pattern = r"polar radius[^0-9]*([0-9,]+)\s*km"
    error_text = "Page infobox has no polar radius information"
    match = get_match(infobox_text, pattern, error_text)
    return match.group(1)


def get_birth_date(name: str) -> str:
    """Gets birth date of the given person

    Args:
        name - name of the person

    Returns:
        birth date of the given person
    """
    infobox_text = clean_text(get_first_infobox_text(get_page_html(name)))
    pattern = r"born[^0-9]*\((\d{4}-\d{2}-\d{2})\)"
    error_text = "Page infobox has no birth information (at least none in xxxx-xx-xx format)"
    match = get_match(infobox_text, pattern, error_text)
    return match.group(1)

if __name__ == "__main__":
    print("\n<<<<<<<<<<<<<< Testing Planet Radius >>>>>>>>>>>>>>")
    # should be 3,376.2
    print(f'Mars has a polar radius of {get_planet_radius("Mars")}km')
    # should be 6356.752
    print(f'Earth has a polar radius of {get_planet_radius("Earth")}km')
    # should be 66,854
    print(f'Jupiter has a polar radius of {get_planet_radius("Jupiter")}km')
    # should be 54,364
    print(f'Saturn has a polar radius of {get_planet_radius("Saturn")}km')

    print("\n<<<<<<<<<<<<<< Testing Birth Dates >>>>>>>>>>>>>>")
    # should be 1906-12-09
    print(format_birth(get_birth_date("Grace Hopper"), "Grace Hopper"))
    # should be 1912-06-23
    print(format_birth(get_birth_date("Alan Turing"), "Alan Turing"))
    # should be 1955-06-08
    print(format_birth(get_birth_date("Tim Berners-Lee"), "Tim Berners-Lee"))
    # should be 1949-01-17
    print(format_birth(get_birth_date("Anita Borg"), "Anita Borg"))
