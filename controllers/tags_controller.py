from flask import Blueprint, Flask, redirect, render_template, request

from models.tag import Tag

import repositories.tag_repository as tag_repository

tags_blueprint = Blueprint("tags", __name__)

# INDEX
@tags_blueprint.route("/tags")
def tags():
    tags = tag_repository.select_all()
    return render_template("tags/index.html", tags = tags)
