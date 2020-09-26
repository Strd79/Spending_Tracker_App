from db.run_sql import run_sql
from models.user import User

def save(user):
    sql = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s) RETURNING id"
    values = [user.name, user.email, user.password]
    results = run_sql(sql, values)
    id = results[0]['id']
    user.id = id