from db.run_sql import run_sql
from models.transaction import Transaction
from models.merchant import Merchant
from models.tag import Tag

import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository

def save(transaction):
    sql = "INSERT INTO transactions (merchant_id, date, amount, tag_id) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [transaction.merchant.id, transaction.date, transaction.amount, transaction.tag.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    transaction.id = id 