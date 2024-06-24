import sqlite3
from datetime import datetime

conn = sqlite3.connect('instance\site.db')

cursor = conn.cursor()

movies = [
    (1, 'Терминатор', 'https://upload.wikimedia.org/wikipedia/ru/c/ca/Terminator_poster.jpg', 1984, 1),
    (2, 'Идея тебя', 'https://sun9-10.userapi.com/impg/u2MEeZSc45Bpnc2L1lgMrh9j7SCAs-RUs5z0yQ/2-NYHoC7a1w.jpg?size=396x604&quality=95&sign=82cb5e549eaa31076312fc65e4944b08&c_uniq_tag=vaaQefh7SfZRsa7F5twr5inkNooEKh6_9hxOavKLdHU&type=album', 2024, 2),
    (3, 'Тихое место', 'https://upload.wikimedia.org/wikipedia/ru/4/45/%D0%9F%D0%BE%D1%81%D1%82%D0%B5%D1%80_%D1%84%D0%B8%D0%BB%D1%8C%D0%BC%D0%B0_%C2%AB%D0%A2%D0%B8%D1%85%D0%BE%D0%B5_%D0%BC%D0%B5%D1%81%D1%82%D0%BE%C2%BB.jpg',2020, 3),
    (4, 'В космосе', 'https://ru-images.kinorium.com/movie/1080/2596309.jpg?1705412895', 2024, 4),
    (5, 'Поиск', 'https://upload.wikimedia.org/wikipedia/ru/2/23/%D0%9F%D0%BE%D1%81%D1%82%D0%B5%D1%80_%D1%84%D0%B8%D0%BB%D1%8C%D0%BC%D0%B0_%C2%AB%D0%9F%D0%BE%D0%B8%D1%81%D0%BA%C2%BB.jpg', 2018, 5),
]

cursor.executemany('''
    INSERT INTO Movie(id, title, url, release_date, genre_id) VALUES(?,?,?,?,?)
''', movies)

conn.commit()
conn.close()
