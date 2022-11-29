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

def find_us_phone_number(text) -> list:
    """Finds all occurrences of a US phone number in a text string"""
    # match a 10 digit phone number with area code
    return re.findall(r'\d{3}-\d{3}-\d{4}', text)


def find_visa_mastercard(text) -> list:
    """Finds all occurrences of a visa / mastercard number in a text string"""
    # match a 16 digit credit card number
    match1 = r'4\d{3}-\d{4}-\d{4}-\d{4}'
    match2 = r'5\d{3}-\d{4}-\d{4}-\d{4}'

    if re.search(match1,text):
        return re.findall(match1,text)
    elif re.search(match2,text):
        return re.findall(match2,text)
    else:
        print("Given text in not an occurance of a visa/mastercard number")
        return []

    


def find_amex(text) -> list:
    """Finds all occurrences of an amex number in a text string"""
    # match a 15 digit credit card number

    return re.findall(r'\d{4}-\d{6}-\d{5}', text)



def find_us_ssn(text) -> list:
    """Finds all occurrences of a US social security number in a text string"""
    return re.findall(r'\d{3}-\d{2}-\d{4}',text)



def find_email(text) -> list:
    """Finds all occurrences of an email address in a text string"""
    # match an email address
    return re.findall(r'[\w\.-]+@[\w\.-]+', text)


def find_instagram_handle(text) -> list:
    """Finds all occurrences of an instagram handle in a text string"""
    # match an instagram handle
    return re.findall(r'(@[\w]{1,30})', text)


def anonymize_pii(text):
    # Create an additional pattern to detect an account number
    amex_pattern = Pattern(name='amex_pattern', regex=r'\d{4}-\d{6}-\d{5}', score=0.9)
    ames_recognizer = PatternRecognizer(supported_entity='AMEX_NUMBER', patterns=[amex_pattern])

    #Create an additional pattern to detect social media
    instagram_pattern = Pattern(name='instagram',regex=r'(@[\w]{1,30})',score=0.9)
    instagram_recognizer = PatternRecognizer(supported_entity='SOCIAL_MEDIA',patterns=[instagram_pattern])

    # Initialize the recognition registry
    registry = RecognizerRegistry()
    registry.load_predefined_recognizers()

    # Add custom recognizers
    registry.add_recognizer(amex_recognizer)
    registry.add_recognizer(instagram_recognizer)

    # Set up analyzer with our updated recognizer registry
    analyzer = AnalyzerEngine(registry=registry)

    # Show all entities that can be detected for debuggng
    # print(analyzer.get_supported_entities())

    # List of entities to detect
    detect_types = ['US_SSN', 'PHONE_NUMBER', 'EMAIL_ADDRESS', 'PERSON', 'CREDIT_CARD',
                    'AMEX_NUMBER','SOCIAL_MEDIA']

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
     text = 'John Edwards called the help desk for help with their credit card 4095-3434-2424-1414. They provided their ssn 750-12-1234 and phone number 919-555-1212 which were used to verify their account. They also provided their email address je2@edwards.com and their social medial handle @jon_edwards for future contact. They would like future charges billed to an amex account 1234-567890-12345'
     print(anonymize_pii(text))