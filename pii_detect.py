import re


def find_city_state(text) -> list:
    """Finds all occurrences of a city and state abbreviation in a text string"""
    # match a one word or a two word city name followed by a comma and state abbreviation
    return re.findall(r'\b[A-Z][a-z]+(?: [A-Z][a-z]+)?, [A-Z]{2}\b', text)


def find_account_number(text) -> list:
    """Finds all occurrences of a bank account number in a text string"""
    # match a 10 digit bank account number
    return re.findall(r'\b\d{10}\b', text)


def show_aggie_pride() -> list:
    """Returns a list of favorite aggie slogans"""
    # python lists
    # https://developers.google.com/edu/python/lists
    slogan_list = ['Aggie Pride - Worldwide',
                   'Aggies Do!',
                   'Go Aggies',
                   'We are Aggies!',
                   'Thats on 1891!',
                   'Thats What Aggies Do!',
                   'Lets Go Aggies!',
                   'Aggies skate, Aggies grind!',
                   'Show em what Aggies do',
                   'Aggie born, Aggie bred',
                   'Aggies stick together',
                   'Never Ever Underestimate An Aggie. Move Forward With Purpose.',
                   'Aggie For Life!',
                   'Go Aggie Pride!',
                   'Aggie Nation!',
                   'Aggies Achieve!',
                   'Aggies Go!',
                   'Aggie what? Pride what give me that, give me that',
                   'Aggies are periodt ahh, Eagles are periodt ugh',
                   'It\'s GHOE Babyyy!',
                   'Aggies are periodt ahh, Eagles are periodt ugh',
                   'Aggies Rule, Eagles Drool',
                   'A G G I E what!',
                   'Aggie PRIDE!',
                   'Gig em, Aggies! Fight em, Aggies! Farmers fight!',
                   'And when I die, I am Aggie Dead!',
                   'Aggies Learn',
                   'Aggieee Prideee!',
                   'Aggies Lead!']

    return slogan_list


if __name__ == '__main__':
    print(show_aggie_pride())
