import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# engine = create_engine(os.getenv("DATABASE_URL"))
engine = create_engine("postgres://ufahdppxmwmnfk:e0c55691f4045b71ca10ca5fad61e91027d9131fb8c7904142dcb0677f2a4a2e@ec2-23-21-13-88.compute-1.amazonaws.com:5432/d2vbqq75absh07")
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("flights.csv")
    reader = csv.reader(f)
    for o, des, dur in reader:    #reads csv line by line#
        db.execute("INSERT INTO flights (origin, destination, duration) VALUES (:origin, :destination, :duration)", #place holder fo origin, destination, duration#
                    {"origin": o, "destination": des, "duration": dur})
        print(f"Added flight from {o} to {des} lasting {dur} minutes.")
    db.commit()

if __name__ == "__main__":
    main()
