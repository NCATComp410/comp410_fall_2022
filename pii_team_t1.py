import re
import spacy
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


def anonymize_pii(text):
    # an account number is 3 or 4 digits followed by a dash and 5 digits
    account_pattern = Pattern(name='account_pattern', regex=r'\d{3,4}-\d{5}', score=0.9)
    account_recognizer = PatternRecognizer(supported_entity='ACCOUNT_NUMBER', patterns=[account_pattern])

    # a credit card is 4 sets of 4 digits seperated by dashes
    credit_pattern = Pattern(name='credit_pattern', regex=r'\d{4}-\d{4}-\d{4}-\d{4}', score=0.9)
    credit_recognizer = PatternRecognizer(supported_entity='CREDIT_CARD', patterns=[credit_pattern])
    
    #an amex card number is a set of 4 digits, 6 digits, and 5 digits, separated by dashes
    amex_number_pattern = Pattern(name='amex_number', regex=r'\d{4}-\d{6}-\d{5}', score=0.9)
    amex_recognizer = PatternRecognizer(supported_entity='AMEX_NUMBER', patterns=[amex_number_pattern])
    
     # an instagram handle is a string of 1 to 30 characters beginning with an at '@' symbol
    ig_handle_pattern = Pattern(name='Instagram_handle', regex=r"(@[\w]{1,30}\b)", score=0.9)
    ig_handle_recognizer = PatternRecognizer(supported_entity='IG_HANDLE', patterns=[ig_handle_pattern])

    # Initialize the recognition registry
    registry = RecognizerRegistry()
    registry.load_predefined_recognizers()

    # Add custom recognizers
    registry.add_recognizer(account_recognizer)
    registry.add_recognizer(credit_recognizer)
    registry.add_recognizer(amex_recognizer)
    registry.add_recognizer(ig_handle_recognizer)

    # Set up analyzer with our updated recognizer registry
    analyzer = AnalyzerEngine(registry=registry)

    # List of entities to detect
    detect_types = ['US_SSN', 'PHONE_NUMBER', 'EMAIL_ADDRESS', 'PERSON', 'CREDIT_CARD', 'ACCOUNT_NUMBER', 'IG_HANDLE', 'AMEX_NUMBER']

                    


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


if __name__ == '__main__':
    print(anonymize_pii('John Edwards called the help desk for help with their credit card 4095-3434-2424-1414. ' +
                        'They provided their ssn 750-12-1234 and phone number 919-555-1212 which were used to verify their account. ' +
                        'They also provided their email address je2@edwards.com and their social medial handle @jon_edwards for future contact. ' +
                        'They would like future charges billed to an amex account 1234-567890-12345'))
