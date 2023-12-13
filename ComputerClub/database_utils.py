import psycopg2
from typing import Union


def con():
    try:
        connection = psycopg2.connect(
            user="admin",
            password="admin!",
            host="localhost",
            port="5432",
            database="ComputerClub"
        )
        if not connection:
            return None
    except psycopg2.OperationalError:
        return None
    return connection


BUTTONS_TABLES = {
    'btn_reservation': 'reservation',
    'btn_users': 'users',
    'btn_computer': 'computer',
    'btn_tariff': 'tariff'
}

LIST_BUTTON_TABLE = [
    'btn_reservation',
    'btn_users',
    'btn_computer',
    'btn_tariff'
]
