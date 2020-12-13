#ARGUMENTS:
# loc = location in the word search // int
# word = word that we want to find // string
# word_search = the word search matrix // a really long string

def check_north(loc, word, word_search, colm_size):
    try: #Need this to check if we are not going out of bounds (HANDLING "EDGE" CASE :p)
        for x in word[1:]:
            if word_search[loc - colm_size] != x: #check if the next letter matches the next letter of the word
                return False
            loc = loc - colm_size #increment the locaiton of the letter to keep checking in the same direction
        return True
    except IndexError:
        return False

def check_north_east(loc, word, word_search, colm_size):
    try:
        for x in word[1:]:
            if word_search[loc + 1 - colm_size] != x:#check if the next letter matches the next letter of the word
                return False
            loc = loc + 1 - colm_size #increment the locaiton of the letter to keep checking in the same direction
        return True
    except IndexError:
        return False

def check_north_west(loc, word, word_search, colm_size):
    try:
        for x in word[1:]:
            if word_search[loc - 1 - colm_size] != x:#check if the next letter matches the next letter of the word
                return False
            loc = loc - 1 - colm_size #increment the locaiton of the letter to keep checking in the same direction
        return True
    except IndexError:
        return False

def check_south(loc, word, word_search, colm_size):
    try:
        for x in word[1:]:
            if word_search[loc + colm_size] != x: #check if the next letter matches the next letter of the word
                return False
            loc = loc + colm_size #increment the locaiton of the letter to keep checking in the same direction
        return True
    except IndexError:
        return False

def check_south_east(loc, word, word_search, colm_size):
    try:
        for x in word[1:]:
            if word_search[loc + 1 + colm_size] != x:#check if the next letter matches the next letter of the word
                return False
            loc = loc + 1 + colm_size #increment the locaiton of the letter to keep checking in the same direction
        return True
    except IndexError:
        return False

def check_south_west(loc, word, word_search, colm_size):
    try:
        for x in word[1:]:
            if word_search[loc - 1 + colm_size] != x:#check if the next letter matches the next letter of the word
                return False
            loc = loc - 1 + colm_size #increment the locaiton of the letter to keep checking in the same direction
        return True
    except IndexError:
        return False

def check_east(loc, word, word_search):
    try:
        for x in word[1:]:
            if word_search[loc + 1] != x:#check if the next letter matches the next letter of the word
                return False
            loc = loc + 1 #increment the locaiton of the letter to keep checking in the same direction
        return True
    except IndexError:
        return False

def check_west(loc, word, word_search):
    try:
        for x in word[1:]:
            if word_search[loc - 1] != x:#check if the next letter matches the next letter of the word
                return False
            loc = loc - 1 #increment the locaiton of the letter to keep checking in the same direction
        return True
    except IndexError:
        return False

def print_word_search(word_search, dimensions): #Prints the word search in the terminal
    i = 0
    while i < dimensions[1]:
        for x in word_search:
            if i == 0:
                i = i + 1
                print("|", x, end=" ")
            elif i == dimensions[1] - 1:
                i = 0
                print(x, "|\n", end=" ")
            else:
                i = i + 1
                print(x, end=" ")
        break

def print_result(word_search_result): #Prints each entry in the result dictionary (makes it readable instead of printing a whole dictionary into the terminal)
    for x in word_search_result:
        print(x, ":", word_search_result[x])
#main:

#To input a word search, start with the leftmost column and input the letters as you travel down the column. I realise that this is terrible, improved method coming later. . .
word_search =  ["T","F","R","L","K","I","T","E","G","N","U","F",
                "N","T","I","P","Y","B","T","R","I","X","F","S",
                "V","A","S","U","N","N","Y","B","S","T","Q","I",
                "P","I","K","W","J","U","A","F","V","E","T","C",
                "E","B","T","R","I","C","W","O","K","N","P","E",
                "M","S","S","O","L","M","I","C","H","I","S","C",
                "A","K","H","P","A","S","M","Y","L","R","D","R",
                "R","C","I","O","D","I","V","I","N","G","N","E",
                "V","E","R","S","R","M","A","K","N","L","O","A",
                "A","S","T","W","M","T","R","P","E","G","Y","M",
                "B","I","K","I","N","I","S","D","H","C","A","P",
                "C","G","S","M","O","W","E","W","A","R","M","K"]
dimensions = (12,12) #In order for the math to work, you must start counting at 1. Thus the top left corner of the word search is (1,1)
word_bank = ["BIKINI", "CABIN", "DIVING", "ICECREAM",
             "NOTINPUZZLE", "KITE", "PAIL", "SHORTS", "SUNNY",
             "SWIM", "SWIMMING", "TSHIRT", "WARM", "CAR"]

def main(word_search, dimensions, word_bank):
    LOCATION_DICTIONARY = dict()
    RES_DICT = dict()
    for loc,val in enumerate(word_search): #create a dictionary with the locations of all of the letters in the form (letter: [location])
        if val in LOCATION_DICTIONARY.keys():
            LOCATION_DICTIONARY[val] = LOCATION_DICTIONARY[val] + [loc]
        else:
            LOCATION_DICTIONARY[val] = [loc]

    for word in word_bank:
        if word[0] in LOCATION_DICTIONARY:
            for loc in LOCATION_DICTIONARY[word[0]]:
                if (check_north(loc, word, word_search, dimensions[1]) or #Logic check: if any function returns True than we know that the word was found
                    check_south(loc, word, word_search, dimensions[1]) or
                    check_west(loc, word, word_search) or
                    check_east(loc, word, word_search) or
                    check_north_west(loc, word, word_search, dimensions[1]) or
                    check_north_east(loc, word, word_search, dimensions[1]) or
                    check_south_west(loc, word, word_search, dimensions[1]) or
                    check_south_east(loc, word, word_search, dimensions[1])) == True:
                    RES_DICT[word] = True
                    break #need this break so that the boolean value is not overwritten by a later one i.e. once we find a word, we know its in the word search so no need to search anymore
                else:
                    RES_DICT[word] = False
    return RES_DICT

word_search_result = main(word_search, dimensions, word_bank)
print_result(word_search_result)
