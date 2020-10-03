import pdb
from models.city import City
from models.country import Country

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

city_repository.delete_all()
country_repository.delete_all()

country1 = Country("Germany")
country_repository.save(country1)
country2 = Country("France")
country_repository.save(country2)
country3 = Country("Italy")
country_repository.save(country3)


city_1 = City("Berlin", country1)
city_repository.save(city_1)
city_2 = City("Paris", country2)
city_repository.save(city_2)
city_3 = City("Rome", country3)
city_repository.save(city_3)
city_4 = City("Hamburg", country1)
city_repository.save(city_4)
city_5 = City("Milan", country3)
city_repository.save(city_5)

# city_2 = City("Leon", country2, True, id=2)
# city_repository.update(city_2)

# city_repository.delete(id=3)



pdb.set_trace()
