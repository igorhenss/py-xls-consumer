import psycopg2


def connect():
    connection = psycopg2.connect(user="postgres", password="postgres",
                                  host="localhost", port="5432", database="postgres")
    return connection, connection.cursor()


def disconnect(connection, cursor):
    cursor.close()
    connection.close()
