# -*- coding: utf-8 -*-

import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "prueba.db")

class CurrencyManager(object):
    def __init__(self, database=None):
        if not database:
            database = ':memory:'
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()

    def insert(self, obj):
        query = 'INSERT INTO currency VALUES ("{}","{}","{}")'.format(obj.code, obj.name, obj.symbol)
        self.cursor.execute(query)
        self.conn.commit()

class Currency(object):
    "Currency Model"
    objects = CurrencyManager(DB_PATH)

    def __init__(self, code, name, symbol):
        self.code = code
        self.name = name
        self.symbol = symbol

    def __repr__(self):
        return u'{}'.format(self.name)

peso_arg = Currency(code='ARS', name='Pesos (Arg)', symbol='$')
dolar = Currency(code = 'USD', name='Dolar', symbol='U$S')
euro = Currency(code = 'EUR', name = 'Euro', symbol='€')

Currency.objects.insert(peso_arg)
Currency.objects.insert(dolar)
Currency.objects.insert(euro)

