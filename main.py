from uuid import uuid4
import time

import mysql.connector
from faker import Faker
import random
from datetime import datetime, timedelta

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="manyusers"
)

# Create a cursor object
cursor = db.cursor()

# Create a Faker instance
fake = Faker()

data = []
counter = 0


for _ in range(100_000):
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = f"{first_name.lower()}.{last_name.lower()}+{str(uuid4())[:8]}@example.com"
    birth_date = fake.date_of_birth(minimum_age=18, maximum_age=80)
    gender = random.choice(['M', 'F', 'O'])
    data.append((first_name, last_name, email, birth_date, gender))
    counter += 1
    if counter % 10000 == 0:
        print(counter)


batch_size = 10000
start_time = time.time()
for i in range(0, len(data), batch_size):
    batch = data[i:i+batch_size]
    sql = "INSERT INTO users (first_name, last_name, email, birth_date, gender) VALUES (%s, %s, %s, %s, %s)"
    cursor.executemany(sql, batch)
    db.commit()
    print(f"Inserted {i+batch_size} out of 40,000,000 records")

elapsed_time = time.time() - start_time
print(f"Elapsed time {elapsed_time}")

db.close()