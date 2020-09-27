from db.run_sql import run_sql
from models.merchant import Merchant
from models.user import User

import repositories.user_repository as user_repository

def save(merchant):
    sql = "INSERT INTO merchants (name, street, city, user_id) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [merchant.name, merchant.street, merchant.city, merchant.user.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    merchant.id = id

def select_all():
    merchants = []
    sql = "SELECT * FROM merchants"
    results = run_sql(sql)
    for row in results:
        user = user_repository.select(row["user_id"])
        merchant = Merchant(row["name"], row["street"], row["city"], user, row["id"])
        merchants.append(merchant)
    return merchants

def select(id):
    sql = "SELECT * FROM merchants WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    user = user_repository.select(result["user_id"])
    merchant = Merchant(result["name"], result["street"], result["city"], user, result["id"])
    return merchant

def delete_all():
    sql = "DELETE FROM merchants"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM merchants WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(merchant):
    sql = "UPDATE merchants SET (name, street, city, user_id) = (%s, %s, %s, %s) WHERE id = %s"
    values = [merchant.name, merchant.street, merchant.city, merchant.user.id, merchant.id]
    run_sql(sql, values)
