#ARGUMENTS:
# loc = location in the word search // int
# word = word that we want to find // string
# word_search = the word search matrix // a really long string

def check_north(loc, word, word_search):
    try: #Need this to check if we are not going out of bounds (HANDLING "EDGE" CASE :p)
        for x in word[1:]:
            if word_search[loc - 1] != x: #check if the next letter matches the next letter of the word
                return False
            loc = loc - 1 #increment the locaiton of the letter to keep checking in the same direction
        return True
    except IndexError:
        return False

def check_north_east(loc, word, word_search, row_size):
    try:
        for x in word[1:]:
            if word_search[loc - 1 + row_size] != x:#check if the next letter matches the next letter of the word
                return False
            loc = loc - 1 + row_size #increment the locaiton of the letter to keep checking in the same direction
        return True
    except IndexError:
        return False

def check_north_west(loc, word, word_search, row_size):
    try:
        for x in word[1:]:
            if word_search[loc - 1 - row_size] != x:#check if the next letter matches the next letter of the word
                return False
            loc = loc - 1 - row_size #increment the locaiton of the letter to keep checking in the same direction
        return True
    except IndexError:
        return False

def check_south(loc, word, word_search):
    try:
        for x in word[1:]:
            if word_search[loc + 1] != x: #check if the next letter matches the next letter of the word
                return False
            loc = loc + 1 #increment the locaiton of the letter to keep checking in the same direction
        return True
    except IndexError:
        return False

def check_south_east(loc, word, word_search, row_size):
    try:
        for x in word[1:]:
            if word_search[loc + 1 + row_size] != x:#check if the next letter matches the next letter of the word
                return False
            loc = loc + 1 + row_size #increment the locaiton of the letter to keep checking in the same direction
        return True
    except IndexError:
        return False

def check_south_west(loc, word, word_search, row_size):
    try:
        for x in word[1:]:
            if word_search[loc + 1 - row_size] != x:#check if the next letter matches the next letter of the word
                return False
            loc = loc - 1 - row_size #increment the locaiton of the letter to keep checking in the same direction
        return True
    except IndexError:
        return False

def check_east(loc, word, word_search, row_size):
    try:
        for x in word[1:]:
            if word_search[loc + row_size] != x:#check if the next letter matches the next letter of the word
                return False
            loc = loc + row_size #increment the locaiton of the letter to keep checking in the same direction
        return True
    except IndexError:
        return False

def check_west(loc, word, word_search, row_size):
    try:
        for x in word[1:]:
            if word_search[loc - row_size] != x:#check if the next letter matches the next letter of the word
                return False
            loc = loc - row_size #increment the locaiton of the letter to keep checking in the same direction
        return True
    except IndexError:
        return False


#main:

#To input a word search, start with the leftmost column and input the letters as you travel down the column. I realise that this is terrible, improved method coming later. . .
word_search = ["T","N","V","P","E","M","A","R","V","A","B","C", #column1 (where "T" is the top left most corner and top of the column)
               "F","T","A","I","B","S","K","C","E","S","I","G", #column 2 (Where "F" is the top of the column)
               "R","I","S","K","T","S","H","I","R","T","K","S", #and so on . . .
               "L","P","U","W","R","O","P","O","S","W","I","M",
               "K","Y","N","J","I","L","A","D","R","M","N","O",
               "I","B","N","U","C","M","S","I","M","T","I","W",
               "T","T","Y","A","W","I","M","V","A","R","S","E",
               "E","R","B","F","O","C","Y","I","K","P","D","W",
               "G","I","S","V","K","H","L","N","N","E","H","A",
               "N","X","T","E","N","I","R","G","L","G","C","R",
               "U","F","Q","T","P","S","D","N","O","Y","A","M",
               "F","S","I","C","E","C","R","E","A","M","P","K"]
dimensions = (12,12) #In order for the math to work, you must start counting at 1. Thus the top left corner of the word search is (1,1)
word_bank = ["BIKINI", "CABIN", "DIVING", "ICECREAM",
             "BUTTHOLE", "KITE", "PAIL", "SHORTS", "SUNNY",
             "SWIM", "SWIMMING", "TSHIRT", "WARM", "WENIS"]

def main(word_search, dimensions, word_bank):
    LOCATION_DICTIONARY = dict()
    RES_DICT = dict()
    for loc,val in enumerate(word_search): #create a dictionary with the locations of all of the letters in the form (letter: [location])
        if val in LOCATION_DICTIONARY.keys():
            LOCATION_DICTIONARY[val] = LOCATION_DICTIONARY[val] + [loc]
        else:
            LOCATION_DICTIONARY[val] = [loc]
    print(LOCATION_DICTIONARY)

    for word in word_bank:
        print(word)
        if word[0] in LOCATION_DICTIONARY:
            for loc in LOCATION_DICTIONARY[word[0]]:
                if (check_north(loc, word, word_search) or #Logic check: if any function returns True than we know that the word was found
                    check_south(loc, word, word_search) or
                    check_west(loc, word, word_search, dimensions[0]) or
                    check_east(loc, word, word_search, dimensions[0]) or
                    check_north_west(loc, word, word_search, dimensions[0]) or
                    check_north_east(loc, word, word_search, dimensions[0]) or
                    check_south_west(loc, word, word_search, dimensions[0]) or
                    check_south_east(loc, word, word_search, dimensions[0])) == True:
                    RES_DICT[word] = True
                    break #need this break so that the boolean value is not overwritten by a later one i.e. once we find a word, we know its in the word search so no need to search anymore
                else:
                    RES_DICT[word] = False
    return RES_DICT

word_search_result = main(word_search, dimensions, word_bank)
print(word_search_result)
