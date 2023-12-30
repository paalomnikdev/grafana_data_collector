import os
from dotenv import dotenv_values
import click
import requests
import pymysql.cursors
from pprint import pprint as pp

config = dotenv_values('.env')
connection = pymysql.connect(
    host=config.get('DB_HOST'),
    user=config.get('DB_USER'),
    password=config.get('DB_PASS'),
    database=config.get('DB_NAME'),
)

@click.group()
def cli():
    pass

@cli.command()
def collect_etcmc():
    by_country = {}
    res = requests.get('https://api.etcnodes.org/peers')
    nodes = res.json()
    
    total_nodes_count = len(nodes)

    for n in nodes:
        country = n.get('ip_info').get('countryCode')
        if not by_country.get(country):
            by_country[country] = 1
        else:
            by_country[country] += 1

    pp(by_country)

    with connection:
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO `global_nodes_count` (`count`) VALUES (%s)",
                (total_nodes_count,)
            )
            cursor.execute(
                "INSERT INTO `etc_node_map` (`country_code`,`value`,`timestamp`) VALUES (%s, %s, now())",
                [(c, by_country[c]) for c in by_country]
            )

        connection.commit()

if __name__ == '__main__':
    cli()
