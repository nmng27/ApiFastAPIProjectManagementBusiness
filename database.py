import psycopg2


DATABASE_URL = "postgresql://postgres/projects@localhost/KingDavid"
conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()