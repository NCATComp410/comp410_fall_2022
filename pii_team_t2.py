import re
import spacy
from presidio_analyzer import AnalyzerEngine, RecognizerRegistry, PatternRecognizer, Pattern
from presidio_anonymizer import AnonymizerEngine

def find_us_phone_number(text) -> list:
    """Finds all occurrences of a US phone number in a text string"""
    # match a 10 digit phone number with area code
    num = re.findall(r'\d{3}[-\.\s]\d{3}[-\.\s]\d{4}', text)
    return num


def find_visa_mastercard(text) -> list:
    """Finds all occurrences of a visa / mastercard number in a text string"""
    # match a 16 digit credit card number
    return re.findall(r'\d{4}-\d{4}-\d{4}-\d{4}', text)


def find_amex(text) -> list:
    """Finds all occurrences of an amex number in a text string"""
    # match a 15 digit credit card number
    return re.findall(r'\d{4}-\d{6}-\d{5}', text)


def find_us_ssn(text) -> list:
    """Finds all occurrences of a US social security number in a text string"""
    # match a 9 digit social security number
    return re.findall(r'(\b\d{3}-?\d{2}-?\d{4}\b)', text)


def find_email(text) -> list:
    """Finds all occurrences of an email address in a text string"""
    # match an email address
    return re.findall(r'[\w\.-]+@[\w\.-]+', text)



def find_instagram_handle(text) -> list:
    """Finds all occurrences of an instagram handle in a text string"""
    # match an instagram handle
    return re.findall(r'@\b[\w.]+', text)


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
    

    amex_pattern = Pattern(name='amex_pattern', regex=r'\d{3,4}-\d{6}-\d{5}', score=0.9)
    amex_recognizer = PatternRecognizer(supported_entity='AMEX', patterns=[amex_pattern])
    
    instagram_pattern = Pattern(name='instagram_pattern', regex=r'@([A-Za-z0-9_](?:(?:[A-Za-z0-9_]|(?:\\.(?!\\.))){0,28}(?:[A-Za-z0-9_]))?)', score=0.9)
    instagram_recognizer = PatternRecognizer(supported_entity='INSTAGRAM_ACCOUNT', patterns=[instagram_pattern])
    
    account_pattern = Pattern(name='account_pattern', regex=r'\d{3,4}-\d{5}', score=0.9)
    account_recognizer = PatternRecognizer(supported_entity='ACCOUNT_NUMBER', patterns=[account_pattern])
    # Initialize the recognition registry
    registry = RecognizerRegistry()
    registry.load_predefined_recognizers()

    # Add custom recognizers
    registry.add_recognizer(amex_recognizer)
    registry.add_recognizer(instagram_recognizer)
    registry.add_recognizer(account_recognizer)
    # Set up analyzer with our updated recognizer registry
    analyzer = AnalyzerEngine(registry=registry)

    # Show all entities that can be detected for debuggng
    print(analyzer.get_supported_entities())

    # List of entities to detect
    detect_types = ['US_SSN', 'PHONE_NUMBER', 'EMAIL_ADDRESS', 'PERSON', 'CREDIT_CARD', 'AMEX', 'INSTAGRAM_ACCOUNT',
                    'ACCOUNT_NUMBER']

    results = analyzer.analyze(text=text,
                               entities=detect_types,
                               language='en')

    # Initialize the engine and anonymize the results
    engine = AnonymizerEngine()
    anon = engine.anonymize(
        text=text,
        analyzer_results=results,
    )

    return anon
print(anonymize_pii('John Edwards called the help desk for help with their credit card 4095-3434-2424-1414. They provided their ssn 750-12-1234 and phone number 919-555-1212 which were used to verify their account. They also provided their email address je2@edwards.com and their social medial handle @jon_edwards for future contact. They would like future charges billed to an amex account 1234-567890-12345'))

