import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# engine = create_engine(os.getenv("DATABASE_URL"))
engine = create_engine("postgres://ufahdppxmwmnfk:e0c55691f4045b71ca10ca5fad61e91027d9131fb8c7904142dcb0677f2a4a2e@ec2-23-21-13-88.compute-1.amazonaws.com:5432/d2vbqq75absh07")
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("books.csv")
    reader = csv.reader(f)
    for isb, titl, auth, yr in reader:    #reads csv line by line#

        db.execute("INSERT INTO books_table (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
                    {'isbn': isb, 'title': titl, 'author': auth, "year": yr})
        print(f"Added to books_table, {isb}, {titl}, {auth}, {yr}.")
    db.commit()

if __name__ == "__main__":
    main()
