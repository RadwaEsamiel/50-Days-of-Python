import data_manager
import flight_search

class FlightData:
    def __init__(self):
        self.data_manager_data = data_manager.DataManager()
        self.flight_search_data = flight_search.FlightSearch()

    def data_structure(self):
        cities = self.data_manager_data.cities_data()
        dict_returned = self.flight_search_data.requesting_data(cities)

        for city_id, city_info in dict_returned.items():
            if city_info[1]:
                self.data_manager_data.update_cities(city_id, city_info[1])
