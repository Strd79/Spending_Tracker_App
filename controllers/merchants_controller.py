from flask import Blueprint, Flask, redirect, render_template, request

from models.merchant import Merchant

import repositories.merchant_repository as merchant_repository
import repositories.user_repository as user_repository

merchants_blueprint = Blueprint("merchants", __name__)

# INDEX
@merchants_blueprint.route("/merchants")
def merchants():
    merchants = merchant_repository.select_all()
    return render_template("merchants/index.html", merchants = merchants)