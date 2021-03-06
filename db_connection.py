import psycopg2


class DBConnection:
    def __init__(self, dbname, dbuser):
        try:
            self.conn = psycopg2.connect("dbname='{}' user='{}'".format(dbname, dbuser))
        except:
            print('Error: unable to connect to the database:', dbname)
            raise

    def close(self):
        self.conn.close()

    def get_connection(self):
        return self.conn

    def get_cursor(self):
        return self.conn.cursor()

    def commit(self):
        return self.conn.commit()

    def rollback(self):
        return self.conn.rollback()
