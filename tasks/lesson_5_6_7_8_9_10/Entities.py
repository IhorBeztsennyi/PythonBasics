from datetime import datetime
import os, csv, json
from tasks.Lesson_3 import normalize_text
from collections import Counter
import xml.etree.ElementTree as ET
import sqlite3


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


class JSONRecordProvider:
    def __init__(self, file_path="input_records.json"):
        self.file_path = file_path

    def process_json(self, feed):
        if not os.path.exists(self.file_path):
            print(f"File {self.file_path} does not exist.")
            return

        with open(self.file_path, "r", encoding="utf-8") as file:
            records = json.load(file)

        for record in records:
            record_type = record.get("type")
            text = normalize_text(record.get("text", ""))

            if record_type == "news":
                feed.add_record(News(text, record.get("city", "")))
            elif record_type == "ad":
                feed.add_record(PrivateAd(text, record.get("expiration_date", "")))
            elif record_type == "joke":
                feed.add_record(JokeOfTheDay(text, int(record.get("category_index", 1))))
            else:
                print(f"Invalid record format: {record}")

        os.remove(self.file_path)
        print(f"File {self.file_path} processed and deleted successfully.")


class XMLRecordProvider:
    def __init__(self, file_path="input_records.xml"):
        self.file_path = file_path

    def process_xml(self, feed):
        if not os.path.exists(self.file_path):
            print(f"File {self.file_path} does not exist.")
            return

        try:
            tree = ET.parse(self.file_path)
            root = tree.getroot()

            for record in root.findall("record"):
                record_type = record.get("type")
                text = normalize_text(record.find("text").text)

                if record_type == "news":
                    city = record.find("city").text
                    feed.add_record(News(text, city))
                elif record_type == "ad":
                    expiration_date = record.find("expiration_date").text
                    feed.add_record(PrivateAd(text, expiration_date))
                elif record_type == "joke":
                    category_index = int(record.find("category_index").text)
                    feed.add_record(JokeOfTheDay(text, category_index))
                else:
                    print(f"Invalid record type: {record_type}")

            os.remove(self.file_path)
            print(f"File {self.file_path} processed and deleted successfully.")

        except Exception as e:
            print(f"Error processing XML file: {e}")


class DatabaseRecordSaver:
    def __init__(self, db_name="records.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS News (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT,
                city TEXT,
                date TEXT,
                UNIQUE(text, city, date)
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Advertising (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT,
                expiration_date TEXT,
                days_left INTEGER,
                UNIQUE(text, expiration_date)
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS JokeOfTheDay (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT,
                category TEXT,
                UNIQUE(text, category)
            )
        ''')
        self.conn.commit()

    def save_news(self, news: News):
        try:
            self.cursor.execute('''
                INSERT INTO News (text, city, date) VALUES (?, ?, ?)
            ''', (news.text, news.city, news.date))
            self.conn.commit()
        except sqlite3.IntegrityError:
            print("The record already exists (News).")

    def save_ad(self, ad: PrivateAd):
        try:
            self.cursor.execute('''
                INSERT INTO Advertising (text, expiration_date, days_left) VALUES (?, ?, ?)
            ''', (ad.text, ad.expiration_date.strftime('%Y-%m-%d'), ad.days_left))
            self.conn.commit()
        except sqlite3.IntegrityError:
            print("The record already exists (Advertising).")

    def save_joke(self, joke: JokeOfTheDay):
        try:
            self.cursor.execute('''
                INSERT INTO JokeOfTheDay (text, category) VALUES (?, ?)
            ''', (joke.joke_text, joke.category))
            self.conn.commit()
        except sqlite3.IntegrityError:
            print("The record already exists (JokeOfTheDay).")

    def close(self):
        self.conn.close()


class NewsFeedDB(NewsFeedCSV):
    def __init__(self, db_saver, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.db_saver = db_saver

    def add_record(self, record):
        super().add_record(record)

        if isinstance(record, News):
            self.db_saver.save_news(record)
        elif isinstance(record, PrivateAd):
            self.db_saver.save_ad(record)
        elif isinstance(record, JokeOfTheDay):
            self.db_saver.save_joke(record)