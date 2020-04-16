import glob

"""
***************************************************************************************
*
*                         __       ___,.-------..__        __
*                        //\\ _,-''                `'--._ //\\
*                        \\ ;'                           `: //
*                         `(         recipe reader!       )'
*                           :.                           ,;
*                            `.`--.___           ___.--','
*                              `.     ``-------''     ,'
*                                 -.               ,-
*                                    `-._______.-'      (woK r u lOoKiN aT???)
*                        
*  
*  DEVELOPER: Katelyn Biesiadecki
*  DATE: August 26, 2019
*  PROJECT NAME: Recipe Reader
*  DESCRIPTION: This script will parse through recipes in the current directory 
*               (specifically, recipe-*.txt files) and allow the user to filter
*               recipes based on their key ingredients, difficulty, type of 
*               cuisine, and total cooking time. 
*  WHY: Sometimes you want a specific type of food like Italian; sometimes you
*       really need to use up some questionably old chicken breasts; sometimes
*       you are too hungry to wait more than 30 minutes for a hot meal. But you will
*       ~always~ be too lazy to use your brain and mentally filter through your
*       recipes based on these different distinctions.
*  NOTE: Check out recipe-template.txt for an explanation of the formatting you will
*        need for this script to be useful in any capacity. 
* 
*  For simple checks, you can just use grep! 
*  
***************************************************************************************
"""

# ============================== FUNCTIONS =======================================

def parse_recipe(filepath):
    """ Parses a recipe file for key tags (difficulty, type of cuisine, etc.). """

    def get_next_value():
        """ Returns the value of the next item. """
        line = fp.readline()
        words = line.strip().split(' ')
        value = words[1:] if len(words) > 1 else "error"

        return value

    fp = open(filepath, 'r')
    fp.readline() # Discard header (filename and my name!).

    space = ' '
    cuisine = space.join(get_next_value())

    meal = get_next_value()

    difficulty = space.join(get_next_value())
    time = space.join(get_next_value())

    # Get key ingredients by searching for @<ingredient>.
    key_ingredients = []
    line = fp.readline()
    while line:
        if line[0] == '@':
            key_ingredients.append(line[2:].strip('\n'))
         
        line = fp.readline()

    fp.close() # Close file.
    return cuisine, meal, difficulty, time, key_ingredients


def peek_recipe(filepath):
    """ Prints out the contents of a recipe file. """
    fp = open(filepath, 'r')
    print(fp.read())
    fp.close()


def add_dict_set(dict, key, value):
    """ Adds value to set in a dictionary. """
    if key not in dict.keys():
        dict[key] = {value}
    else:
        dict[key].add(value)


# ================================ MAIN ==========================================

# SPLASH SCREEN
# TODO: make this into a cute sl-like gif
print("I'M HUNGRY")
print("... let's make food!")
print()

# MENU
    # MAKE SELECTION (have it be a satisfying gui-like thing)

# Use a dictionary:
#    cuisines = {french: {set of recipes}, italian: {ditto}}
#    meal = {breakfast: {}, lunch: {}, dinner: {}, snack: {}}
#    difficulty = {easy: {}, medium: {}, difficult}
# Design decision to make meal and difficulty categories into 
# dictionaries as well, despite being a "fixed size" (i.e. easy/medium/hard vs.
# every type of cuisine), for consistency.
# But would it be better to just make indvdl variables (e.g. snack_set = {})?
# Or does it really not matter?

# Time should be less than or equal to, right? And should be sorted from least -> greatest.

dict_cuisine    = {}
dict_meal       = {}
dict_difficulty = {}

# CHECK ALL FILES 
files = [f for f in glob.glob("recipe-*.txt", recursive=True)] 

for f in files:
    cuisine, meals, difficulty, time, key_ings = parse_recipe(f)
    add_dict_set(dict_cuisine, cuisine, f) 

    for m in meals: 
        add_dict_set(dict_meal, m.strip(','), f) 

    add_dict_set(dict_difficulty, difficulty, f) 
    
    print(f)
    print(cuisine)
    print(meals)
    print(difficulty)
    print(time)
    print(key_ings)
    print()

print(dict_cuisine)
print(dict_meal)
print(dict_difficulty)
#peek_recipe('recipe-template.txt')

# ====================================================================================

# What do you feel like -> How much time do you have
# How much energy do you have -> Do you have any ingredients you want to use up?
print("What kind of food do you feel like?")
for c in enumerate(dict_cuisine, start=1):
    print(str(c[0]) + ".", c[1])

choice = input("Enter your choice or none: ")
difficulty = input("Enter difficulty level (easy=1, med=2, hard=3): ")





