from db.run_sql import run_sql

from models.country import Country
from models.city import City
import repositories.city_repository as city_repository

def save(country):
    sql = "INSERT INTO countries (country_name, visited) VALUES (%s, %s) RETURNING *"
    values = [country.country_name, country.visited]
    results = run_sql(sql, values)
    id = results[0]['id']
    country.id = id
    return country
