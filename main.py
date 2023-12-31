import os
from dotenv import load_dotenv
import click
import requests
import pymysql.cursors
from pprint import pprint as pp

load_dotenv()

connection = pymysql.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASS'),
    database=os.getenv('DB_NAME'),
)

@click.group()
def cli():
    pass

@cli.command()
def health():
    print('health')

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

    print(by_country)

    with connection:
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO `global_nodes_count` (`count`) VALUES (%s)",
                (str(total_nodes_count),)
            )
            # cursor.executemany(
            #     "INSERT INTO `etc_node_map` (`country_code`,`value`) VALUES (%s, %s)",
            #     [(c, str(by_country[c])) for c in by_country]
            # )

        connection.commit()

if __name__ == '__main__':
    cli()
