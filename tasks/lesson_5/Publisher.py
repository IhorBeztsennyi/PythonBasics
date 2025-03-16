from tasks.lesson_5.Entities import News, PrivateAd, JokeOfTheDay, NewsFeed
import random


def main():
    feed = NewsFeed()
    while True:
        print("Select record type to add:")
        print("1 - News")
        print("2 - Private Ad")
        print("3 - Joke of the Day")
        print("4 - Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            text = input("Enter news text: ")
            city = input("Enter city: ")
            feed.add_record(News(text, city))
        elif choice == "2":
            text = input("Enter ad text: ")
            exp_date = input("Enter expiration date (YYYY-MM-DD): ")
            feed.add_record(PrivateAd(text, exp_date))
        elif choice == "3":
            joke_text = input("Enter a joke: ")
            print("Select joke category:")
            for i, category in enumerate(JokeOfTheDay.CATEGORIES, 1):
                print(f"{i} - {category}")

            while True:
                category_index = int(input("Enter category number: "))
                if category_index in range(1, len(JokeOfTheDay.CATEGORIES) + 1):
                    break
                else:
                    print("Invalid category number. Please enter a valid number.")

            feed.add_record(JokeOfTheDay(joke_text, category_index))
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
