import re
import spacy
from presidio_analyzer import AnalyzerEngine, RecognizerRegistry, PatternRecognizer, Pattern
from presidio_anonymizer import AnonymizerEngine


def anonymize_pii(text):
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
def find_us_phone_number(text) -> list:
    """Finds all occurrences of a US phone number in a text string"""
    # match a 10 digit phone number with area code
    return re.findall(r'\d{3}-\d{3}-\d{4}', text)


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
    return re.findall(r'\d{3}-\d{2}-\d{4}', text)


def find_email(text) -> list:
    """Finds all occurrences of an email address in a text string"""
    # match an email address
    return re.findall(r'[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+', text)

def find_instagram_handle(text) -> list:
    """Finds all occurrences of an instagram handle in a text string"""
    rgx_ig = r"(@[\w]{1,30}\b)"
    lst = re.findall(rgx_ig, text)
    return lst
