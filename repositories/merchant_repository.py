from db.run_sql import run_sql
from models.merchant import Merchant


def save(merchant):
    sql = "INSERT INTO merchants (name, street, city) VALUES (%s, %s, %s) RETURNING id"
    values = [merchant.name, merchant.street, merchant.city]
    results = run_sql(sql, values)
    id = results[0]['id']
    merchant.id = id

def select_all():
    merchants = []
    sql = "SELECT * FROM merchants ORDER BY name ASC"
    results = run_sql(sql)
    for row in results:
        merchant = Merchant(row["name"], row["street"], row["city"], row["id"])
        merchants.append(merchant)
    return merchants

def select(id):
    sql = "SELECT * FROM merchants WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    merchant = Merchant(result["name"], result["street"], result["city"], result["id"])
    return merchant

def delete_all():
    sql = "DELETE FROM merchants"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM merchants WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(merchant):
    sql = "UPDATE merchants SET (name, street, city) = (%s, %s, %s) WHERE id = %s"
    values = [merchant.name, merchant.street, merchant.city, merchant.id]
    run_sql(sql, values)
