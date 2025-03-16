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
        return f"Piece of News:\n{self.text}\n{self.city}, {self.date}"


class PrivateAd(Record):
    def __init__(self, text, expiration_date):
        self.text = text
        self.expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d")
        self.days_left = (self.expiration_date - datetime.now()).days

    def publish(self):
        return f"Private Advertisement:\n{self.text}\nExpires on: {self.expiration_date.strftime('%Y-%m-%d')}, {self.days_left} days left"


class JokeOfTheDay(Record):
    CATEGORIES = ["Knock-knock", "Dark humor", "Absurd", "Political"]

    def __init__(self, joke_text, category_index):
        if category_index not in range(1, len(self.CATEGORIES) + 1):
            raise ValueError("Invalid category number. Please select a valid number.")

        self.joke_text = joke_text
        self.category = self.CATEGORIES[category_index - 1]

    def publish(self):
        return f"Joke of the Day ({self.category}):\n{self.joke_text}"


class NewsFeed:
    def __init__(self, filename="news_feed.txt"):
        self.filename = filename

    def add_record(self, record):
        with open(self.filename, "a", encoding="utf-8") as file:
            file.write(record.publish() + "\n\n")