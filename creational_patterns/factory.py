"""
# Factory
Semelhante ao builder, mas no factory nao precisamos passar parametros

"""

import MySQLdb


class ConnectionFactory(object):
    def get_connection(self):
        # tratamento de erro omitido
        return MySQLdb.connect(
            host="localhost",
            user='root',
            passwd='',
            db='teste'
        )


if __name__ == '__main__':
    connection = ConnectionFactory().get_connection()

    cursor = connection.cursor()
    cursor.execute('SELECT * from cursos')

    for linha in cursor:
        print(linha)

    connection.close()
