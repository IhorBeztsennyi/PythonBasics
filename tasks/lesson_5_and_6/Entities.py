from datetime import datetime
import os
from tasks.Lesson_3 import normalize_text



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


class FileRecordProvider:
    def __init__(self, file_path="input_records.txt"):
        self.file_path = file_path

    def process_file(self, feed):
        if not os.path.exists(self.file_path):
            print(f"File {self.file_path} does not exist.")
            return

        with open(self.file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        for line in lines:
            line = line.strip()
            if line.startswith("news"):
                _, text, city = line.split("|")
                feed.add_record(News(normalize_text(text), city))
            elif line.startswith("ad"):
                _, text, exp_date = line.split("|")
                feed.add_record(PrivateAd(normalize_text(text), exp_date))
            elif line.startswith("joke"):
                _, text, category_index = line.split("|")
                feed.add_record(JokeOfTheDay(normalize_text(text), int(category_index)))
            else:
                print(f"Invalid record format: {line}")

        os.remove(self.file_path)
        print(f"File {self.file_path} processed and deleted successfully.")
