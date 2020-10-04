import pdb
from models.city import City
from models.country import Country

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

city_repository.delete_all()
country_repository.delete_all()

country_1 = Country("Germany", True)
country_repository.save(country_1)
country_2 = Country("France", False)
country_repository.save(country_2)
country_3 = Country("Italy", True)
country_repository.save(country_3)


city_1 = City("Berlin", country_1)
city_repository.save(city_1)
city_2 = City("Paris", country_2)
city_repository.save(city_2)
city_3 = City("Rome", country_3)
city_repository.save(city_3)
city_4 = City("Hamburg", country_1)
city_repository.save(city_4)
city_5 = City("Milan", country_3)
city_repository.save(city_5)

# city_2 = City("Leon", country2, True, id=2)
# city_repository.update(city_2)

# city_repository.delete(id=3)



pdb.set_trace()
