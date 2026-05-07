from psycopg2.extras import execute_batch
from db.connection import get_connection
from logs import logger

def insert_single(doc, embedding):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO documents (content, embedding) VALUES (%s, %s)",
        (doc, embedding)
    )

    conn.commit()
    cur.close()
    conn.close()


def insert_batch(records):
    conn = get_connection()
    cur = conn.cursor()

    execute_batch(
        cur,
        "INSERT INTO documents (content, embedding) VALUES (%s, %s)",
        records
    )

    conn.commit()
    cur.close()
    conn.close()