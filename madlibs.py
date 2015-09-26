import random


placeholders = [['NOUN', 'PLACE', 'SILLY WORD', 'VERB', 'NOUN', 'VERB',
                 'ADJECTIVE', 'ADJECTIVE', 'NUMBER', 'ADJECTIVE', 'ADVERB',
                 'ADJECTIVE', 'ADJECTIVE', 'NUMBER', 'MEASURMENT OF TIME',
                 'ADJECTIVE', 'ADJECTIVE', 'ADJECTIVE', 'NOUN', 'NUMBER',
                 'NUMBER'],
                ['NOUN', 'NOUN', 'NOUN', 'OCCUPATION', 'VERB', 'PLACE',
                 'VERB ENDING IN "ED"', 'NOUN', 'VERB ENDING IN "ING"',
                 'NOUN (PLURAL)', 'NOUN', 'EMOTION'],
                ['COLOR', 'SUPERLATIVE (ENDING IS "EST")',
                 'ADJECTIVE', 'BODY PART (PLURAL)', 'BODY PART', 'NOUN',
                 'ANIMAL (PLURAL)', 'ADJECTIVE', 'ADJECTIVE', 'ADJECTIVE']]

# http://www.madtakes.com/
madlib = ["Is your %s making a mess of your %s? Try %s! It will %s your whole \
%s and %s to unbelievable levels! Watch, as we demonstrate, the %s capabilitie\
s of this %s product! Everyone should have at least %s of these! \n\nTo order,\
call the number on your screen. %s phone attendants will %s take your reques\
t. %s and %s service will be yours! Call within the next %s %s, and you will\
receive a %s, %s, %s %s as a bonus, absolutely free for an additional value\
of %s dollars, plus shipping and handling cost of %s dollars. Act Now!!", "It\
 was during the battle of %s when I was running through a %s when a %s went of\
f right next to my platoon. Our %s yelled for us to %s to the nearest %s we \
could find. When we got to the we %s to start a fire. As we were starting the\
 fire the enemy saw the %s from the fire and started %s %s at us. we all quic\
kly ducked behind the %s at the and returned fire. we quickly eliminated the\
 enemy and were %s that we had won the battle.", "The %s Dragon is the %s \
Dragon of all. It has %s %s, and a %s shaped like a %s. It loves to eat %s,\
 although it will feast on nearly anything. It is %s and %s. You must be %s\
 around it, or you may end up as its meal!"]


def play_game():
    rInt = random.randrange(0, len(placeholders))
    values = []
    for word in placeholders[rInt]:
        values.append(input('GIVE ME A ' + word + ': '))
    values = tuple(values)
    print(madlib[rInt] % values)

if __name__ == '__main__':
    play_game()
