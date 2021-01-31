from enum import Enum


class Regions(Enum):
    AFRICA = 'AFRICA'
    EUROPE = 'EUROPE'
    ASIA = 'ASIA'
    AUSTRALIA_SOUTH_PACIFIC = 'AUSTRALIA+AND+SOUTH+PACIFIC'
    CARIBBEAN = 'CARIBBEAN'
    SOUTH_AMERICA = 'SOUTH+AMERICA'
    MIDDLE_EAST = 'MIDDLE+EAST'
    NORTH_AMERICA = 'NORTH+AMERICA'


class Sectors(Enum):
    BASIC_INDUSTRIES = 'Basic Industries'
    CAPITAL_GOODS = 'Capital Goods'
    CONSUMER_DURABLES = 'Consumer Durables'
    CONSUMER_NON_DURABLES = 'Consumer Non-Durables'
    CONSUMER_SERVICES = 'Consumer Services'
    ENERGY = 'Energy'
    FINANCE = 'Finance'
    HEALTH_CARE = 'Health Care'
    MISCELLANEOUS = 'Miscellaneous'
    PUBLIC_UTILITIES = 'Public Utilities'
    TECHNOLOGY = 'Technology'
    TRANSPORTATION = 'Transportation'
