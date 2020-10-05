from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

cities_blueprint = Blueprint("cities", __name__)

@cities_blueprint.route("/cities")
def cities():
    cities = city_repository.select_all()
    return render_template("cities/index.html", all_cities = cities)

@cities_blueprint.route("/cities/new", methods=['GET'])
def new_city():
    cities = city_repository.select_all()
    countries = country_repository.select_all()
    print("countrrrrrrrrrrrrrrrries", countries[0].id)
    return render_template("cities/new.html", all_cities = cities, all_countries = countries)


@cities_blueprint.route('/cities', methods=['POST'])
def create_city():
    city_name = request.form['city_name']
    visited = request.form['visited']
    country_id = request.form['country_id']
    print("COUNTRYRYRY", country_id)
    country = country_repository.select(country_id)
    city = City(city_name, country, visited)

    city_repository.save(city)
    return redirect('/cities')



@cities_blueprint.route("/countries/<id>", methods=['GET'])
def show_city(id):
    city = city_repository.select(id)
    return render_template('countries/index.html', city = city)