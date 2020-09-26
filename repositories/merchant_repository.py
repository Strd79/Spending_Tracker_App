from db.run_sql import run_sql
from models.merchant import Merchant

def save(merchant):
    sql = "INSERT INTO merchants (name, street, city) VALUES (%s, %s, %s) RETURNING id"
    values = [merchant.name, merchant.street, merchant.city]
    results = run_sql(sql, values)
    id = results[0]['id']
    merchant.id = id

