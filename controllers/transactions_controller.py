from flask import Blueprint, Flask, redirect, render_template, request

from models.transaction import Transaction

import repositories.transaction_repository as transaction_repository
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository

transactions_blueprint = Blueprint("transactions", __name__)

# INDEX
@transactions_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repository.select_all()
    total_amounts = transaction_repository.amounts_total()
    return render_template("transactions/index.html", transactions = transactions, total_amounts = total_amounts)

@transactions_blueprint.route("/transactions/merchants_a2z")
def transactions_sorted_by_merchant_a2z():
    transactions = transaction_repository.sort_all_by_merchant_a2z()
    total_amounts = transaction_repository.amounts_total()
    return render_template("transactions/index.html", transactions = transactions, total_amounts = total_amounts)

@transactions_blueprint.route("/transactions/merchants_z2a")
def transactions_sorted_by_merchant_z2a():
    transactions = transaction_repository.sort_all_by_merchant_z2a()
    total_amounts = transaction_repository.amounts_total()
    return render_template("transactions/index.html", transactions = transactions, total_amounts = total_amounts)


# SHOW
@transactions_blueprint.route("/transactions/<id>")
def show_transaction(id):
    transaction = transaction_repository.select(id)
    return render_template("transactions/show.html", transaction = transaction)

# NEW
@transactions_blueprint.route("/transactions/new")
def new_transaction():
    merchants = merchant_repository.select_all()
    tags = tag_repository.select_all()
    return render_template("transactions/new.html", merchants = merchants, tags = tags)

# CREATE
@transactions_blueprint.route("/transactions", methods=["POST"])
def create_transaction():
    merchant_id = request.form["merchant_id"]
    merchant = merchant_repository.select(merchant_id)
    date = request.form["date"]
    amount = float(request.form["amount"])
    tag_id = request.form["tag_id"]
    tag = tag_repository.select(tag_id)
    new_transaction = Transaction(merchant, date, amount, tag)
    transaction_repository.save(new_transaction)
    return redirect("/transactions")

# EDIT
@transactions_blueprint.route("/transactions/<id>/edit")
def edit_transaction(id):
    transaction = transaction_repository.select(id)
    merchants = merchant_repository.select_all()
    tags = tag_repository.select_all()
    return render_template("transactions/edit.html", transaction = transaction, merchants = merchants, tags = tags)

# UPDATE
@transactions_blueprint.route("/transactions/<id>", methods=["POST"])
def update_transaction(id):
    merchant_id = request.form["merchant_id"]
    merchant = merchant_repository.select(merchant_id)
    date = request.form["date"]
    amount = request.form["amount"]
    tag_id = request.form["tag_id"]
    tag = tag_repository.select(tag_id)
    transaction = Transaction(merchant, date, amount, tag, id)
    transaction_repository.update(transaction)
    return redirect("/transactions")

# DELETE
@transactions_blueprint.route("/transactions/<id>/delete", methods=["POST"])
def delete_transaction(id):
    transaction_repository.delete(id)
    return redirect("/tranactions")