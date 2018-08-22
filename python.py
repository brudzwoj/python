#print("hello")
def remove_chars(sentence):

    sentence = sentence[1:-1]

    return sentence
    print(sentence)


assert remove_chars("country") == "ountr", "failed testcase"


def return_half(sentence):

    lenght = len(sentence)

    return sentence[:lenght//2]


assert return_half("Tieto") == "Ti", "failed"


def append_to_string(sentence):


    if 5 <= len(sentence):
        w = " World"
        sentence += w
    else:
        h = "Welcome, "
        sentence = h + sentence

    return sentence

#print(append_to_string("Hello"))

assert append_to_string("Hello") == "Hello World", "Wrong"
assert append_to_string("Hi") == "Welcome, Hi", "Wrong"

def shortest_string():

    print("string 1")
    str1 = input()
    print("string 2")
    str2 = input()

    alphabet = [str1, str2]

    print(sorted(alphabet)[0])

#shortest_string()

def filter_list(list):

    new_list = []
    for elem in list:
        if type(elem) is int:
            new_list.append(elem)

#   print(new_list)

    return new_list


assert filter_list([1,5,'A',30,'Hello',50,2.75]) == [1,5,30,50], "bad filtering"

def who_likes_it(list_of_likes):

    if len(list_of_likes) == 0:
        output = "no one likes this"

    elif len(list_of_likes) > 3:
        output = f"{list_of_likes[0]}, {list_of_likes[1]} and {len(list_of_likes[2:])} others like this"

    elif len(list_of_likes) == 3:
        output = f"{list_of_likes[0]}, {list_of_likes[1]} and {list_of_likes[2]} like this"

    elif len(list_of_likes) == 2:
        output = f"{list_of_likes[0]} and {list_of_likes[1]} like this"

    elif len(list_of_likes) == 1:
        output = f"{list_of_likes[0]} likes this"

    print(output)

    return output


assert who_likes_it([]) == "no one likes this", "Wrong like count!"
assert who_likes_it(["Ryszard"]) == "Ryszard likes this", "Wrong like count!"
assert who_likes_it(["Marcin", "Michal"]) == "Marcin and Michal like this", "Wrong like count!"
assert who_likes_it(["Edyta", "Igor", "Kamil"]) == "Edyta, Igor and Kamil like this", "Wrong like count!"
assert who_likes_it(["Michal", "Maciej", "Bartosz", "Przemek"]) == "Michal, Maciej and 2 others like this", "Wrong like count!"

def count_duplicates(sentence, how_many_times):
    '''
    Function checks how many times a letter is present in a string.
    Return only those letters.
    See test cases for examples
    '''
    import numpy as np

    sentence = list(sentence)
    print(sentence)
    unique_elements, count_elements = np.unique(sentence, return_counts=True)
    print(np.asarray((unique_elements, count_elements)))
    unique_ = []
    for i, elem in enumerate(count_elements):
        if elem == how_many_times:
            unique_ += unique_elements[i]
            unique = "".join(unique_)

    return f"{unique}"

print(count_duplicates("Karima", 1))

assert count_duplicates("aabcdddee", 2) == "ae", "Failed to count!"  # only 'a' end 'e' were present 2 times
assert count_duplicates("indivisibility", 6) == "i", "Failed to count!"
#assert count_duplicates("Karima", 1) == "Krim", "Failed to count!"


def dictionary():
    my_dict = {

        "Ryszard": 1,
        "Michał": 2,
        "Patryk": 3

    }
    print(my_dict)

    if "Kamil" in my_dict:
        my_dict["Kamil"] += 1
    else:
        my_dict["Kamil"] = 1
    print(my_dict)

    if "Ryszard" in my_dict:
        my_dict.pop("Ryszard", None)
    print(my_dict)
#dictionary()

import nltk

def word_counter(sentence):

    words = nltk.word_tokenize(sentence)

    i = words
    dictio = {x: i.count(x) for x in i}
    print(dictio)

    print(words)
    return None

#answer = {"Ala": 2, "ma": 2, "kota": 1,".": 2, "psa": 1}
#assert word_counter("Ala ma kota. Ala ma psa.") == answer

import re

def validatePIN(PIN):

    if PIN == re.search(r"[^\d{4}]", PIN) and len(PIN) == 4:
        return True
    else:
        return False
    # ATM machines allow 4 digit PIN codes and PIN must contain only digits.
    # Validate if input is correct


assert validatePIN("1234") == True, "Wrong validation!"
assert validatePIN("12345") == False, "Wrong validation!"
assert validatePIN("a234") == False, "Wrong validation!"
