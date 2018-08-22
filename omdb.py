import omdb

omdb.set_default('apikey', "688763bc")



db_output = {'title': 'Deadpool', 'year': '2016', 'rated': 'R', 'released': '12 Feb 2016', 'runtime': '108 min',
               'genre': 'Action, Adventure, Comedy', 'director': 'Tim Miller', 'writer': 'Rhett Reese, Paul Wernick',
               'actors': 'Ryan Reynolds, Karan Soni, Ed Skrein, Michael Benyaer',
               'plot': 'A fast-talking mercenary with a morbid sense of humor is subjected to a rogue experiment that leaves him with accelerated healing powers and a quest for revenge.',
             'language': 'English', 'country': 'USA',
             'awards': 'Nominated for 2 Golden Globes. Another 27 wins & 73 nominations.',
             'poster': 'https://m.media-amazon.com/images/M/MV5BYzE5MjY1ZDgtMTkyNC00MTMyLThhMjAtZGI5OTE1NzFlZGJjXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SX300.jpg',
             'ratings': [{'source': 'Internet Movie Database', 'value': '8.0/10'},
                           {'source': 'Rotten Tomatoes', 'value': '83%'}, {'source': 'Metacritic', 'value': '65/100'}],
               'metascore': '65', 'imdb_rating': '8.0', 'imdb_votes': '748,845', 'imdb_id': 'tt1431045',
               'type': 'movie',
               'dvd': '10 May 2016', 'box_office': '$328,674,489', 'production': '20th Century Fox',
               'website': 'http://www.foxmovies.com/deadpool', 'response': 'True'}

print("Movie name  ( to end session type end )")

movie = input()

for keys, values in db_output.items():
    print(keys, "=>", values)
