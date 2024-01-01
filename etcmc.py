import requests
import pymysql.cursors


class Etcmc:
    _endpoint = 'https://api.etcnodes.org/peers'
    _nodes = {}

    def __init__(self, mysql_connection) -> None:
        self.load_nodes()
        self._mysql_connection=mysql_connection

    def load_nodes(self) -> None:
        self._nodes = requests.get('https://api.etcnodes.org/peers').json()

    def get_nodes_count(self) -> int:
        return len(self._nodes)

    def get_nodes_by_country(self) -> map:
        by_country = {}

        for n in self._nodes:
            country = n.get('ip_info').get('countryCode')
            if not by_country.get(country):
                by_country[country] = 1
            else:
                by_country[country] += 1

        return by_country
    
    def store_nodes_count(self):
        with self._mysql_connection:
            with self._mysql_connection.cursor() as cursor:
                cursor.execute(
                    'INSERT INTO `{prefix}global_nodes_count` (`count`) VALUES (%s)'.format(prefix=os.getenv('DB_PREFIX', '')),
                    (str(self.get_nodes_count()),)
                )

            self._mysql_connection.commit()

    def get_nodes_count_one_day_ago(self):
        nodes_count = 0
        with self._mysql_connection.cursor() as cursor:
            sql = "SELECT `count` FROM global_nodes_count WHERE time >= DATE_SUB(NOW(), INTERVAL 1 DAY) ORDER BY time DESC LIMIT 1;"
            cursor.execute(sql)
            result = cursor.fetchone()

            if result:
                nodes_count = result[0]

        return nodes_count

    def get_discord_message(self):
        current_nodes_online = self.get_nodes_count()
        before_nodes_online = self.get_nodes_count_one_day_ago()
        diff = current_nodes_online - before_nodes_online
        sign = '+'

        if diff < 0:
            sign = '-'

        message = """
{} nodes currently online({}{})
""".format(str(current_nodes_online), str(sign), str(diff))
        
        print(message)

        return message
