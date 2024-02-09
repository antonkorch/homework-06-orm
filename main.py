import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
from os import getenv
from models import Publisher, Book, Shop, Stock, Sale
from create_db import create_db

create_db()

engine = sq.create_engine(getenv('DSN'))

session = (sessionmaker(bind=engine))()

pub_id = input('Enter publisher id or name: ')

results = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale) \
        .join(Publisher, Publisher.id == Book.id_publisher) \
        .join(Stock, Stock.id_book == Book.id) \
        .join(Shop, Shop.id == Stock.id_shop) \
        .join(Sale, Sale.id_stock == Stock.id)

if pub_id.isdigit():
    results = results.filter(Publisher.id == pub_id).all()
else:
    results = results.filter(Publisher.name == pub_id).all()

for result in results:
    print(f'{result[0]:<40} | {result[1]:<10} | {result[2]:<6} | {result[3]}')

session.commit()
session.close()