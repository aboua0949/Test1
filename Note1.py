def happy() :
    #return the same line
    return "happy birthday to you!\n"

def verseFor(person) :
    lyrics = happy()*2 + "Happy Birthday, dear " + person + ".\n" + happy()
    return lyrics

def main():
    for meow in ["Joseph", "Joe", "Seth"]:
        print(verseFor(meow))

main()

