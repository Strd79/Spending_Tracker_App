from db.run_sql import run_sql
from models.tag import Tag

def save(tag):
    sql = "INSERT INTO tags (name, description) VALUES (%s, %s) RETURNING id"
    values = [tag.name, tag.description]
    results = run_sql(sql, values)
    id = results[0]['id']
    tag.id = id