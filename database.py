
from sqlalchemy.orm import declarative_base,Session
from sqlalchemy import create_engine


url = "sqlite:///app.db"

base = declarative_base()

engine = create_engine(url=url,echo=True)

session = Session(bind=engine)



