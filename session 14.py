# Python program for the URL https://restcountries.com/v3.1/all
import requests

class CountryInfo:
    def __init__(self, url):
        self.url = url
        self.data = self.fetch_data()

    def fetch_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch data: {response.status_code}")

    def display_countries_currencies(self):
        for country in self.data:
            name = country.get('name', {}).get('common', 'N/A')
            currencies = country.get('currencies', {})
            if currencies:
                for currency_code, currency_info in currencies.items():
                    print(f"Country: {name}, Currency: {currency_info.get('name', 'N/A')}, Symbol: {currency_info.get('symbol', 'N/A')}")
            else:
                print(f"Country: {name}, Currency: N/A, Symbol: N/A")

    def display_countries_with_dollar(self):
        dollar_countries = []
        for country in self.data:
            currencies = country.get('currencies', {})
            if any('dollar' in currency_info.get('name', '').lower() for currency_info in currencies.values()):
                dollar_countries.append(country.get('name', {}).get('common', 'N/A'))
        print("Countries that use Dollar as currency:")
        for country in dollar_countries:
            print(country)

    def display_countries_with_euro(self):
        euro_countries = []
        for country in self.data:
            currencies = country.get('currencies', {})
            if any(currency_info.get('name', '').lower() == 'euro' for currency_info in currencies.values()):
                euro_countries.append(country.get('name', {}).get('common', 'N/A'))
        print("Countries that use Euro as currency:")
        for country in euro_countries:
            print(country)

if __name__ == "__main__":
    url = "https://restcountries.com/v3.1/all"
    country_info = CountryInfo(url)
    
    print("Displaying countries, currencies and currency symbols:")
    country_info.display_countries_currencies()
    
    print("\nDisplaying countries with Dollar as currency:")
    country_info.display_countries_with_dollar()
    
    print("\nDisplaying countries with Euro as currency:")
    country_info.display_countries_with_euro()
#END

#Python program for the URL https://www.openbrewerydb.org/

import requests

class BreweryInfo:
    def __init__(self):
        self.base_url = "https://api.openbrewerydb.org/breweries"
        self.states = ['Alaska', 'Maine', 'New York']
        self.data = self.fetch_data()

    def fetch_data(self):
        all_data = []
        for state in self.states:
            response = requests.get(f"{self.base_url}?by_state={state}&per_page=50")
            if response.status_code == 200:
                all_data.extend(response.json())
            else:
                raise Exception(f"Failed to fetch data for {state}: {response.status_code}")
        return all_data

    def list_breweries(self):
        breweries_by_state = {state: [] for state in self.states}
        for brewery in self.data:
            if brewery['state'] in self.states:
                breweries_by_state[brewery['state']].append(brewery['name'])
        for state, breweries in breweries_by_state.items():
            print(f"Breweries in {state}:")
            for name in breweries:
                print(f"  - {name}")

    def count_breweries_by_state(self):
        count_by_state = {state: 0 for state in self.states}
        for brewery in self.data:
            if brewery['state'] in self.states:
                count_by_state[brewery['state']] += 1
        for state, count in count_by_state.items():
            print(f"Number of breweries in {state}: {count}")

    def count_brewery_types_by_city(self):
        brewery_types_by_city = {}
        for brewery in self.data:
            city = brewery['city']
            if city not in brewery_types_by_city:
                brewery_types_by_city[city] = {}
            brewery_type = brewery['brewery_type']
            if brewery_type not in brewery_types_by_city[city]:
                brewery_types_by_city[city][brewery_type] = 0
            brewery_types_by_city[city][brewery_type] += 1
        for city, types in brewery_types_by_city.items():
            print(f"Brewery types in {city}:")
            for brewery_type, count in types.items():
                print(f"  - {brewery_type}: {count}")

    def count_breweries_with_websites(self):
        breweries_with_websites = {state: 0 for state in self.states}
        for brewery in self.data:
            if brewery['state'] in self.states and brewery['website_url']:
                breweries_with_websites[brewery['state']] += 1
        for state, count in breweries_with_websites.items():
            print(f"Number of breweries with websites in {state}: {count}")

if __name__ == "__main__":
    brewery_info = BreweryInfo()

    print("Listing all breweries in Alaska, Maine, and New York:")
    brewery_info.list_breweries()

    print("\nCount of breweries in Alaska, Maine, and New York:")
    brewery_info.count_breweries_by_state()

    print("\nCount of brewery types in individual cities of Alaska, Maine, and New York:")
    brewery_info.count_brewery_types_by_city()

    print("\nCount of breweries with websites in Alaska, Maine, and New York:")
    brewery_info.count_breweries_with_websites()
#END