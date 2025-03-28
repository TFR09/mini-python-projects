
import pandas as pd
import matplotlib.pyplot as plt

bestsellers = pd.read_csv('bestsellers.csv')
bestsellers = bestsellers.drop_duplicates(subset='Name', keep='last')

number_of_books_written = bestsellers.groupby('Author')[['Name']].count()
print(number_of_books_written)
number_of_books_by_genre = bestsellers.groupby('Genre')[["Name", "Genre"]].count()
print(number_of_books_by_genre)
plt.pie(number_of_books_by_genre.Name, labels=number_of_books_by_genre.Genre)
plt.pie(number_of_books_by_genre.Name, labels=number_of_books_by_genre.Genre, autopct='%.2f')
plt.show()

