import psycopg2
from faker import Faker

fake = Faker("ro_RO")

def generate_user():
    return [
        fake.first_name(),
        fake.last_name(),
        fake.email(),
        fake.user_name(),
        fake.password(),
        fake.date_between(start_date='-1y', end_date='today')
    ]

def insert_user(data):
    conn = psycopg2.connect(
        dbname="study_tracker",
        user="postgres",
        password="0504",  
        host="localhost",
        port=5432
    )
    cur = conn.cursor()

    sql = """
        INSERT INTO raw.users (
            first_name, last_name, email, username, password, registration_date
        ) VALUES (%s, %s, %s, %s, %s, %s);
    """

    cur.execute(sql, data)
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    for _ in range(20):  # inserează 20 de useri
        user = generate_user()
        insert_user(user)

    print("20 de utilizatori au fost inserați în raw.users.")
