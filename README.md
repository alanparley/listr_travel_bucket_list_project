# travel bucket list project

I have built a full stack web-app to track someone's travel adventures.
The app allows a user to track countries and cities they want to visit and those they have visited.
It allows the user to create, edit and delete countries and cities, and to associate cities with countries.
The app allows the user to mark countries and cities as visited or still to see.

This app has been built using Python, Flask, PostgreSQL and the psycopg, HTML and CSS.

It demonstrates:
* Interacting with a PostgreSQL database (CRUD)
* Object oriented programming with Python
* Web Programming (REST, MVC)
* Interacting with a PostgreSQL database (CRUD)
* Using Jinja as a web template engine for Python

To run this app in VSCode, you must in run the folowing commands in terminal:
1. createdb bucket_list 
2. psql -d bucket_list -f db/bucket_list.sql
3. python3 console.py
4. flask run
