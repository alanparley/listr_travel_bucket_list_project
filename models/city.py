class City:
    def __init__ (self, city_name, country, visited = False, id = None):
        
        self.city_name = city_name
        self.country = country
        self.visited = visited
        self.id = id

        # country_id INT REFERENCES countries(id)