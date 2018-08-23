# noinspection PyUnresolvedReferences
import omdb
import re

omdb.set_default('apikey', '688763bc')

res = omdb.request(t='True Grit', y=1969, r='xml')
xml_content = res.content

# print("Order by :   ")

# order = str(input())

def add_movie():

    while True:

        print("'Enter' to continue, to end session type 'end!'")
        action = input()
        if action != "end!":
            print("Enter Movies Name")
            movies = []
            movie = input()
            splt_movie = movie.split(", ")
            order = movie.rsplit(None, 1)[-1]
            for i in range(len(splt_movie)):
                new_element = splt_movie[i]
                movies.append(new_element)
                print(movies)
            for each in movies:
                print(omdb.title(each))
        else:
            print("bye")
            break
add_movie()


    # for key, value in each.items():
    #   print(key, value)
    # if order == "ratings":
    #   for each_source in ["ratings"]:
    #      print(each_source)
# else:
#   print(, "=>", values)
