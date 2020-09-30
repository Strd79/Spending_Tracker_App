from db.run_sql import run_sql
from models.transaction import Transaction
from models.merchant import Merchant
from models.tag import Tag

import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository

# CRUD Functions

def save(transaction):
    sql = "INSERT INTO transactions (merchant_id, date, amount, tag_id) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [transaction.merchant.id, transaction.date, transaction.amount, transaction.tag.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    transaction.id = id 

def select_all():
    transactions = []
    sql = "SELECT * FROM transactions ORDER BY date DESC"
    results = run_sql(sql)
    for row in results:
        merchant = merchant_repository.select(row["merchant_id"])
        tag = tag_repository.select(row["tag_id"])
        transaction = Transaction(merchant, row["date"], row["amount"], tag, row["id"])
        transactions.append(transaction)
    return transactions

def select(id):
    sql = "SELECT * FROM transactions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    merchant = merchant_repository.select(result["merchant_id"])
    tag = tag_repository.select(result["tag_id"])
    transaction = Transaction(merchant, result["date"], result["amount"], tag, result["id"])
    return transaction 

def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM transactions WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(transaction):
    sql = "UPDATE transactions SET (merchant_id, date, amount, tag_id) = (%s, %s, %s, %s) WHERE id = %s"
    values = [transaction.merchant.id, transaction.date, transaction.amount, transaction.tag.id, transaction.id]
    run_sql(sql, values)

# ADDITIONAL Functions

def amounts_total():
    total = []
    sql = "SELECT amount FROM transactions"
    results = run_sql(sql)
    for row in results:
        amount = row["amount"]
        total.append(amount)
    return sum(total)

def sort_all_by_merchant_a2z():
    transactions = []
    sql = "select t.* from transactions as t join merchants as m on m.id = t.merchant_id order by m.name ASC"
    results = run_sql(sql)
    for row in results:
        merchant = merchant_repository.select(row["merchant_id"])
        tag = tag_repository.select(row["tag_id"])
        transaction = Transaction(merchant, row["date"], row["amount"], tag, row["id"])
        transactions.append(transaction)
    return transactions

def sort_all_by_merchant_z2a():
    transactions = []
    sql = "select t.* from transactions as t join merchants as m on m.id = t.merchant_id order by m.name DESC"
    results = run_sql(sql)
    for row in results:
        merchant = merchant_repository.select(row["merchant_id"])
        tag = tag_repository.select(row["tag_id"])
        transaction = Transaction(merchant, row["date"], row["amount"], tag, row["id"])
        transactions.append(transaction)
    return transactions

def sort_all_by_tag_a2z():
    transactions = []
    sql = "select t.* from transactions as t join tags as tg on tg.id = t.tag_id order by tg.name ASC"
    results = run_sql(sql)
    for row in results:
        merchant = merchant_repository.select(row["merchant_id"])
        tag = tag_repository.select(row["tag_id"])
        transaction = Transaction(merchant, row["date"], row["amount"], tag, row["id"])
        transactions.append(transaction)
    return transactions

def sort_all_by_tag_z2a():
    transactions = []
    sql = "select t.* from transactions as t join tags as tg on tg.id = t.tag_id order by tg.name DESC"
    results = run_sql(sql)
    for row in results:
        merchant = merchant_repository.select(row["merchant_id"])
        tag = tag_repository.select(row["tag_id"])
        transaction = Transaction(merchant, row["date"], row["amount"], tag, row["id"])
        transactions.append(transaction)
    return transactions