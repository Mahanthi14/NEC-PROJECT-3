from utils.database import get_connection

def login_user(username, password, role):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM users
    WHERE username=? AND password=? AND role=?
    """, (username, password, role))

    user = cursor.fetchone()
    conn.close()

    return user