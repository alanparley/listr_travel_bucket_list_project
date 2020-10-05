from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    cities = city_repository.select_all()
    return render_template("countries/index.html", all_countries = countries, cities = cities)

@countries_blueprint.route("/countries/new", methods=['GET'])
def new_country():
    countries = country_repository.select_all()
    return render_template("countries/new.html", all_countries = countries)


@countries_blueprint.route('/countries', methods=['POST'])
def create_country():
    country_name = request.form['country_name']
    visited = request.form['visited']
    country = Country(country_name, visited)
    country_repository.save(country)
    return redirect('/countries')

@countries_blueprint.route("/countries/<id>", methods=['GET'])
def show_country(id):
    country = country_repository.select(id)
    return render_template('countries/show.html', country = country)

@countries_blueprint.route("/countries/<id>/edit", methods=['GET'])
def edit_country(id):
    country = country_repository.select(id)
    cities = city_repository.select_all()
    return render_template('countries/edit.html', country = country, all_cities = cities)

@countries_blueprint.route("/countries/<id>", methods=['POST'])
def update_country(id):
    country = country_repository.select(id)
    visited = request.form['visited']
    country = Country(country.country_name, visited, id)
    country_repository.update(country)
    return redirect('/countries')

@countries_blueprint.route("/countries/<id>/delete", methods=['POST'])
def delete_country(id):
    country_repository.delete(id)
    return redirect('/countries')