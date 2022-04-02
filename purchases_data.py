class Purchases:
    def __init__(self, article_id, t_date, customer_id, id_price):
        self.article_id = article_id
        self.t_date = t_date
        self.customer_id = customer_id
        self.id_price = id_price

    def to_dct(self):
        return {'article_id': self.article_id, 't_date': self.t_date, 'customer_id': self.customer_id,'id_price': self.id_price}


class PurchasesDataAcces:
    def __init__(self, dbconnect):
        self.dbconnect = dbconnect

    def get_purchases(self):
        cursor = self.dbconnect.get_cursor()
        cursor.execute('SELECT d.article_id, d.t_date, d.customer_id, d.id_price FROM Purchases d') #Haalt uit de database
        user_objects = list()
        for row in cursor:
            user_object = Purchases(row[0], row[1], row[2], row[3])
            user_objects.append(user_object)

        return user_objects

    def get_popularity(self, start_date, end_date, top_K):
        cursor = self.dbconnect.get_cursor()

        sql = "SELECT article_id, COUNT(article_id) " \
              "FROM purchases t " \
              "WHERE t.t_date between '" + start_date + "' and '" + end_date + "' " \
              "GROUP BY article_id " \
              "ORDER BY COUNT(article_id) DESC " \
              "LIMIT " + str(top_K) + ";"

        cursor.execute(sql)

        articles = list()

        for row in cursor:
            article = Purchases(row[0], None, None, None)
            articles.append(article.article_id)

        return articles

    def add_purchase(self, purchase):
        cursor = self.dbconnect.get_cursor()
        try:

            cursor.execute('INSERT INTO Purchases(t_date, customer_id, article_id, id_price) VALUES(TO_DATE(%s, \'YYYY-MM-DD\'),%s,%s,%s)',
            (purchase.t_date, purchase.customer_id, purchase.article_id, purchase.id_price))

            self.dbconnect.commit()
            return purchase
        except:
            self.dbconnect.rollback()
            raise Exception("Unable to save the purchase!")
