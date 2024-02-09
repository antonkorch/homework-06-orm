import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
from models import create_tables, Publisher, Book, Shop, Stock, Sale
import json
import os

def create_db():

    data = json.load(open('tests_data.json'))
    engine = sq.create_engine(os.getenv('DSN'))

    create_tables(engine)

    session = (sessionmaker(bind=engine))()

    for row in data:
        if row['model'] == 'publisher':
            session.add(Publisher(name=row['fields']['name']))
        
        elif row['model'] == 'book':
            session.add(Book(title=row['fields']['title'], 
                            id_publisher=row['fields']['id_publisher']))
        
        elif row['model'] == 'shop':
            session.add(Shop(name=row['fields']['name']))
        
        elif row['model'] == 'stock':
            session.add(Stock(id_book=row['fields']['id_book'], 
                            id_shop=row['fields']['id_shop'], 
                            count=row['fields']['count']))

        elif row['model'] == 'sale':
            session.add(Sale(price=row['fields']['price'], 
                            date_sale=row['fields']['date_sale'], 
                            id_stock=row['fields']['id_stock'], 
                            count=row['fields']['count']))
        

    session.commit()
    session.close()