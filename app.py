from flask import Flask, render_template

from controllers.merchants_controller import merchants_blueprint
from controllers.tags_controller import tags_blueprint
from controllers.transactions_controller import transactions_blueprint

import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository

app = Flask(__name__)

app.register_blueprint(merchants_blueprint)
app.register_blueprint(tags_blueprint)
app.register_blueprint(transactions_blueprint)

@app.route('/')
def home():
    merchants = merchant_repository.select_all()
    tags = tag_repository.select_all()
    return render_template('index.html', merchants = merchants, tags = tags)

if __name__ == '__main__':
    app.run()