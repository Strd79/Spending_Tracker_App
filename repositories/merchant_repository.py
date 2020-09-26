from db.run_sql import run_sql
from models.merchant import Merchant

def save(merchant):
    sql = "INSERT INTO merchants (name, location) VALUES (%s, %s) RETURNING id"
    values = [merchant.name, merchant.location]
    results = run_sql(sql, values)
    id = results[0]['id']
    merchant.id = id

