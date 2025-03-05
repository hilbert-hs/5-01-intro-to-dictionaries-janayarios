# 5.01 Internet Slang

internet_slang = {
    'nbd': 'No big deal',
    'smh': 'shaking my head',
    'btw': 'by the way',
    'imo': 'in my opinion'
}


for term in internet_slang:
    print(f'{term} means {internet_slang[term]}')

while True:
    term = input('What abbreviation would you like to look up?: ')
    if term in internet_slang:
        print(f"{term} means {internet_slang[term]}")
    else:
        print("That isn't a term I know.")
        add_to = input("\nWould you like to add it? (Y/N): ")
        if add_to.lower() == "y":
            definition = input(f"What does {term} mean?")
            internet_slang[term] = definition
        else:
            print("goodbye")