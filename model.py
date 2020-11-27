from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

engine = create_engine('sqlite:///expenses.db', echo=True)
meta = MetaData()

expenses = Table(
    'expenses', meta,
    Column('particulars', String, primary_key=True),
    Column('category', String),
    Column('amount', Integer),
    Column('date', String),
    Column('comments', String)
)
meta.create_all(engine)
