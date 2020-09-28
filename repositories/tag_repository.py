from db.run_sql import run_sql
from models.tag import Tag
from models.transaction import Transaction

import repositories.merchant_repository as merchant_repository

# CRUD Functions

def save(tag):
    sql = "INSERT INTO tags (name, description) VALUES (%s, %s) RETURNING id"
    values = [tag.name, tag.description]
    results = run_sql(sql, values)
    id = results[0]['id']
    tag.id = id

def select_all():
    tags = []
    sql = "SELECT * FROM tags ORDER BY name ASC"
    results = run_sql(sql)
    for row in results:
        tag = Tag(row["name"], row["description"], row["id"])
        tags.append(tag)
    return tags

def select(id):
    sql = "SELECT * FROM tags WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    tag = Tag(result["name"], result["description"], result["id"])
    return tag

def delete_all():
    sql = "DELETE FROM tags"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM tags WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(tag):
    sql = "UPDATE tags SET (name, description) = (%s, %s) WHERE id = %s"
    values = [tag.name, tag.description, tag.id]
    run_sql(sql, values)  

# ADDITIONAL Functions

def transactions(id):
    transactions = []
    sql = "SELECT * FROM transactions WHERE tag_id = %s ORDER BY date DESC"
    values = [id]
    results = run_sql(sql, values)
    for row in results:
        merchant = merchant_repository.select(row["merchant_id"])
        tag = select(row["tag_id"])
        transaction = Transaction(merchant, row["date"], row["amount"], tag, row["id"])
        transactions.append(transaction)
    return transactions

def amounts_total(id):
    total = []
    sql = "SELECT amount FROM transactions WHERE tag_id = %s"
    values = [id]
    results = run_sql(sql, values)
    for row in results:
        amount = row["amount"]
        total.append(amount)
    return sum(total)