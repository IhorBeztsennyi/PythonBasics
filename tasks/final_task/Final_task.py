import sqlite3
import math

__Earth_radius_in_km__ = 6371


def distance_calc(latitude1,longitude1, latitude2, longitude2):
    phi1 = math.radians(latitude1)
    phi2 = math.radians(latitude2)
    delta_phi = math.radians(latitude2 - latitude1)
    delta_lambda = math.radians(longitude2 -longitude1)

    a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return __Earth_radius_in_km__ * c


class CityDB:
    def __init__(self, db_name='cities.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS cities (
                name TEXT PRIMARY KEY,
                latitude REAL,
                longitude REAL
            )
        """)
        self.conn.commit()

    def get_coordinates(self, city):
        self.cursor.execute('SELECT latitude, longitude FROM cities WHERE name = ?', (city,))
        result = self.cursor.fetchone()
        return result if result else None

    def add_city(self, name, latitude, longitude):
        self.cursor.execute('INSERT OR REPLACE INTO cities (name, latitude, longitude) VALUES (?, ?, ?)',
                            (name, latitude, longitude))
        self.conn.commit()

    def add_or_update_city(self, name, latitude, longitude):
        self.cursor.execute('INSERT OR REPLACE INTO cities (name, latitude, longitude) VALUES (?, ?, ?)',
                            (name, latitude, longitude))
        self.conn.commit()

    def close(self):
        self.conn.close()


def get_city_coordinates(db, city_name):
    coords = db.get_coordinates(city_name)
    if coords:
        print(f"Coordinates for '{city_name}' found: Latitude={coords[0]}, Longitude={coords[1]}")
        update = input("Do you want to update these coordinates? (y/n): ").strip().lower()
        if update == 'y':
            latitude = float(input(f"Enter new latitude for {city_name}: "))
            longitude = float(input(f"Enter new longitude for {city_name}: "))
            db.add_or_update_city(city_name, latitude, longitude)
            return latitude, longitude
        else:
            return coords
    else:
        print(f"Coordinates for '{city_name}' not found.")
        latitude = float(input(f"Enter latitude for {city_name}: "))
        longitude = float(input(f"Enter longitude for {city_name}: "))
        db.add_or_update_city(city_name, latitude, longitude)
        return latitude, longitude


def main():
    db = CityDB()

    try:
        city1 = input("Enter the starting city name: ").strip().title()
        city2 = input("Enter the ending city name: ").strip().title()

        lat1, lon1 = get_city_coordinates(db, city1)
        lat2, lon2 = get_city_coordinates(db, city2)

        distance = distance_calc(lat1, lon1, lat2, lon2)
        print(f"The straight-line distance between {city1} and {city2} is {distance:.2f} km")
    finally:
        db.close()


if __name__ == "__main__":
    main()
