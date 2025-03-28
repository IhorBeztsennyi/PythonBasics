from datetime import datetime
import os, csv
from tasks.Lesson_3 import normalize_text
from collections import Counter



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


class NewsFeedCSV(NewsFeed):
    def __init__(self, filename="news_feed.txt", csv_filename="word_count.csv", letter_csv_filename="letter_count_csv"):
        super().__init__(filename)
        self.csv_filename = csv_filename
        self.letter_csv_filename = letter_csv_filename

    def add_record(self, record):
        super().add_record(record)
        self.word_count_csv()
        self.letter_count_csv()

    def word_count_csv(self):
        if not os.path.exists(self.filename):
            return

        with open(self.filename, "r", encoding="utf-8") as file:
            text = file.read().lower()

        words = text.split()
        word_counts = Counter(words)

        with open(self.csv_filename, "w", encoding="utf-8", newline="") as csv_file:
            writer = csv.writer(csv_file, delimiter='-')
            for word, count in word_counts.items():
                writer.writerow([word, count])

    def letter_count_csv(self):
        if not os.path.exists(self.filename):
            return

        with open(self.filename, 'r', encoding='utf-8') as file:
            text = file.read()

        letter_counts = Counter(c.lower() for c in text if c.isalpha())
        upper_counts = Counter(c for c in text if c.isupper())
        total_letters = sum(letter_counts.values())

        with open(self.letter_csv_filename, "w", encoding="utf-8", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Letter", "Count_All", "Count_Uppercase", "Percentage"])
            for letter, count_all in letter_counts.items():
                count_upper = upper_counts.get(letter.upper(), 0)
                percentage = (count_all / total_letters) * 100 if total_letters > 0 else 0
                writer.writerow([letter, count_all, count_upper, f"{percentage:.2f}%"])