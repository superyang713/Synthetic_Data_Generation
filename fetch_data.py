from sqlalchemy import create_engine


address = 'postgresql+psycopg2://sharpestminds:abc123@35.222.59.78/manifold'
engine = create_engine(address)
print(engine.table_names())
