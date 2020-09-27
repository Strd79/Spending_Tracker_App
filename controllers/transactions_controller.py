from flask import Blueprint, Flask, redirect, render_template, request

from models.transaction import Transaction

import repositories.transaction_repository as transaction_repository
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository
import repositories.user_repository as user_repository

transactions_blueprint = Blueprint("transactions", __name__)

# INDEX
@transactions_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repository.select_all()
    return render_template("transactions/index.html", transactions = transactions)