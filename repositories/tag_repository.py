from db.run_sql import run_sql
from models.tag import Tag
from models.user import User

import repositories.user_repository as user_repository

def save(tag):
    sql = "INSERT INTO tags (name, description, user_id) VALUES (%s, %s, %s) RETURNING id"
    values = [tag.name, tag.description, tag.user.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    tag.id = id

def select_all():
    tags = []
    sql = "SELECT * FROM tags"
    results = run_sql(sql)
    for row in results:
        user = user_repository.select(row["user_id"])
        tag = Tag(row["name"], row["description"], user, row["id"])
        tags.append(tag)
    return tags

def select(id):
    sql = "SELECT * FROM tags WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    user = user_repository.select(result["user_id"])
    tag = Tag(result["name"], result["description"], user, result["id"])
    return tag

def delete_all():
    sql = "DELETE FROM tags"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM tags WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(tag):
    sql = "UPDATE tags SET (name, description, user_id) = (%s, %s, %s) WHERE id = %s"
    values = [tag.name, tag.description, tag.user.id, tag.id]
    run_sql(sql, values)  