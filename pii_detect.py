import re
import spacy
from presidio_analyzer import AnalyzerEngine, RecognizerRegistry, PatternRecognizer, Pattern
from presidio_anonymizer import AnonymizerEngine

# make sure en_core_web_lg is loaded correctly
try:
    nlp = spacy.load("en_core_web_lg")
except OSError:
    from spacy.cli import download

    download("en_core_web_lg")
    nlp = spacy.load("en_core_web_lg")


def find_city_state(text) -> list:
    """Finds all occurrences of a city and state abbreviation in a text string"""
    # match a one word or a two word city name followed by a comma and state abbreviation
    return re.findall(r'\b[A-Z][a-z]+(?: [A-Z][a-z]+)?, [A-Z]{2}\b', text)


def find_account_number(text) -> list:
    """Finds all occurrences of a bank account number in a text string"""
    # match a 10 digit bank account number
    return re.findall(r'\b\d{10}\b', text)


def anonymize_pii(text):
    """Attempt to locate and anonymize personally identifiable information"""
    # https://microsoft.github.io/presidio/analyzer/

    # Create an additional pattern to detect an account number which
    # is not included with the default recognition types
    # an account number is 3 or 4 digits followed by a dash and 5 digits
    account_pattern = Pattern(name='account_pattern', regex=r'\d{3,4}-\d{5}', score=0.9)
    account_recognizer = PatternRecognizer(supported_entity='ACCOUNT_NUMBER', patterns=[account_pattern])

    # Initialize the recognition registry
    registry = RecognizerRegistry()
    registry.load_predefined_recognizers()

    # Add custom recognizers
    registry.add_recognizer(account_recognizer)

    # Set up analyzer with our updated recognizer registry
    analyzer = AnalyzerEngine(registry=registry)

    # Show all entities that can be detected for debuggng
    # print(analyzer.get_supported_entities())

    # List of entities to detect
    detect_types = ['US_SSN', 'PHONE_NUMBER', 'EMAIL_ADDRESS', 'PERSON', 'CREDIT_CARD',
                    'ACCOUNT_NUMBER']

    results = analyzer.analyze(text=text,
                               entities=detect_types,
                               language='en')

    # Initialize the engine and anonymize the results
    engine = AnonymizerEngine()
    anon = engine.anonymize(
        text=text,
        analyzer_results=results
    )

    return anon


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
    # print(show_aggie_pride())
    print(anonymize_pii('my name is John Smith and my email is js@gmail.com'))
