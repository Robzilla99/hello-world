from spellchecker import SpellChecker

spell = SpellChecker()

# find those words that may be misspelled
misspelled = spell.unknown(['something', 'is', 'hapenning', 'here'])

for word in misspelled:
    # Get the one `most likely` answer
    print(spell.correction(word))

    # Get a list of `likely` options
    print(spell.candidates(word))

import BioloJoke

# Get a random joke
# (returns a random joke):
print (BioloJoke.getJoke())

# Get a certain joke
# REQUIRES: passing int for joke number
print(BioloJoke.joke(2))




import beepy
beep(sound=1) # integer as argument
beep(sound='coin') # string as argumentimport beepy


           

