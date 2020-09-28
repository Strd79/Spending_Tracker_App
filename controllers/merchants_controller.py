from flask import Blueprint, Flask, redirect, render_template, request

from models.merchant import Merchant

import repositories.merchant_repository as merchant_repository

merchants_blueprint = Blueprint("merchants", __name__)

# INDEX
@merchants_blueprint.route("/merchants")
def merchants():
    merchants = merchant_repository.select_all()
    return render_template("merchants/index.html", merchants = merchants)

# SHOW
@merchants_blueprint.route("/merchants/<id>")
def show_merchant(id):
    merchant = merchant_repository.select(id)
    transactions = merchant_repository.transactions(id)
    return render_template("merchants/show.html", merchant = merchant, transactions = transactions)

# NEW
@merchants_blueprint.route("/merchants/new")
def new_merchant():
    return render_template("merchants/new.html")

# CREATE
@merchants_blueprint.route("/merchants", methods=["POST"])
def create_merchant():
    name = request.form["name"]
    street = request.form["street"]
    city = request.form["city"]
    new_merchant = Merchant(name, street, city)
    merchant_repository.save(new_merchant)
    return redirect("/merchants")

# EDIT
@merchants_blueprint.route("/merchants/<id>/edit")
def edit_merchant(id):
    merchant = merchant_repository.select(id)
    return render_template("merchants/edit.html", merchant = merchant)

# UPDATE
@merchants_blueprint.route("/merchants/<id>", methods=["POST"])
def update_merchant(id):
    name = request.form["name"]
    street = request.form["street"]
    city = request.form["city"]
    merchant = Merchant(name, street, city, id)
    merchant_repository.update(merchant)
    return redirect("/merchants")

# DELETE
@merchants_blueprint.route("/merchants/<id>/delete", methods=["POST"])
def delete_merchant(id):
    merchant_repository.delete(id)
    return redirect("/merchants")