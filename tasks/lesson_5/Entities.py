from datetime import datetime
import random


class Record:
    def publish(self):
        raise NotImplementedError("Subclasses must implement publish method")


class News(Record):
    def __init__(self, text, city):
        self.text = text
        self.city = city
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def publish(self):
        return f"News:\n{self.text}\n{self.city}, {self.date}"


class PrivateAd(Record):
    def __init__(self, text, expiration_date):
        self.text = text
        self.expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d")
        self.days_left = (self.expiration_date - datetime.now()).days

    def publish(self):
        return f"Private Ad:\n{self.text}\nExpires on: {self.expiration_date.strftime('%Y-%m-%d')}, {self.days_left} days left"


class JokeOfTheDay(Record):
    CATEGORIES = ["Knock-knock", "Dark humor", "Absurd", "Political"]

    def __init__(self, joke_text):
        self.joke_text = joke_text
        self.category = random.choice(self.CATEGORIES)

    def publish(self):
        return f"Joke of the Day ({self.category}):\n{self.joke_text}"