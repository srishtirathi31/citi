import psycopg2
from app.config import Config

conn = psycopg2.connect(Config.POSTGRES_URI)
cursor = conn.cursor()

def index_in_postgres(requirements: str):
    cursor.execute("INSERT INTO backlog (description) VALUES (%s)", (requirements,))
    conn.commit()
