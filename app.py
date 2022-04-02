# TUTORIAL Len Feremans, Sandy Moens and Joey De Pauw
# see tutor https://code.tutsplus.com/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-22972
from flask import Flask, request, session, jsonify
from flask.templating import render_template

from config import config_data
from db_connection import DBConnection
from user_data_acces import DataScientist, UserDataAcces
from purchases_data import *
# import pandas as pd

import random

# INITIALIZE SINGLETON SERVICES
app = Flask('Tutorial ')
app.secret_key = '*^*(*&)(*)(*afafafaSDD47j\3yX R~X@H!jmM]Lwf/,?KT'
app_data = dict()
app_data['app_name'] = config_data['app_name']
connection = DBConnection(dbname=config_data['dbname'], dbuser=config_data['dbuser'])
user_data_access = UserDataAcces(connection)
purchases_acces = PurchasesDataAcces(connection)

DEBUG = False
HOST = "127.0.0.1" if DEBUG else "0.0.0.0"


# REST API
# See https://www.ibm.com/developerworks/library/ws-restful/index.html
# @app.route('/quotes', methods=['GET'])
# def get_quotes():
#     # Lookup row in table Quote, e.g. 'SELECT ID,TEXT FROM Quote'
#     quote_objects = quote_data_access.get_quotes()
#     # Translate to json
#     return jsonify([obj.to_dct() for obj in quote_objects])
#
#
# @app.route('/quotes/<int:id>', methods=['GET'])
# def get_quote(id):
#     # ID of quote must be passed as parameter, e.g. http://localhost:5000/quotes?id=101
#     # Lookup row in table Quote, e.g. 'SELECT ID,TEXT FROM Quote WHERE ID=?' and ?=101
#     quote_obj = quote_data_access.get_quote(id)
#     return jsonify(quote_obj.to_dct())
#
#
# # To create resource use HTTP POST
# @app.route('/quotes', methods=['POST'])
# def add_quote():
#     # Text value of <input type="text" id="text"> was posted by form.submit
#     quote_text = request.form.get('text')
#     quote_author = request.form.get('author')
#     # Insert this value into table Quote(ID,TEXT)
#     quote_obj = Quote(iden=None, text=quote_text, author=quote_author)
#     print('Adding {}'.format(quote_obj.to_dct()))
#     quote_obj = quote_data_access.add_quote(quote_obj)
#     return jsonify(quote_obj.to_dct())


#----------------- VIEW -----------------#
@app.route("/")
@app.route("/home")
def main():
    return render_template('home.html', app_data=app_data)


@app.route("/home", methods=['POST', 'GET'])
def mainGet():

    if request.method == "POST":
        purchases = purchases_acces.get_popularity('2020-01-01', '2020-01-30', 5)
        return jsonify(purchases)

    else:
        return render_template('home.html', app_data=app_data)



def addPurchases():

    for i in range(1000):
        a_id = 0
        date = ''

        a_id = random.randint(100000, 100020)
        month = random.randint(1,12)
        day = random.randint(1,28)
        date = '2020-' + str(month) + '-' + str(day)
        price_id = 159357
        cus_id = 951357
        purchase = Purchases(article_id=a_id, t_date=date, id_price=price_id, customer_id=cus_id)
        purchases_acces.add_purchase(purchase)


# RUN DEV SERVER
if __name__ == "__main__":
    app.run(HOST, debug=True)

