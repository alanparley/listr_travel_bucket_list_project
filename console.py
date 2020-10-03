import pdb
from models.city import City
from models.country import Country

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

# city_repository.delete_all()
# country_repository.delete_all()

country1 = Country("Germany")
country_repository.save(country1)
country2 = Country("France")
country_repository.save(country2)

# country_repository.select_all()

city_1 = City("Berlin", country1)
city_repository.save(city_1)
city_2 = City("Paris", country2)
city_repository.save(city_2)

pdb.set_trace()
