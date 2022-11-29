import re
from presidio_analyzer import PatternRecognizer, RecognizerRegistry, AnalyzerEngine, Pattern
from presidio_anonymizer import AnonymizerEngine

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
    return re.findall(r'\d{4}\-\d{6}\-\d{5}', text)


def find_us_ssn(text) -> list:
    """Finds all occurrences of a US social security number in a text string"""
    # match a 9 digit social security number.


    
    return re.findall(r'\d{3}\-\d{2}\-\d{4}',text)




def find_email(text) -> list:
    """Finds all occurrences of an email address in a text string"""
    # match an email address
    return re.findall(r'[\w\.-]+@[\w\.-]+', text)


def find_instagram_handle(text) -> list:
    """Finds all occurrences of an instagram handle in a text string"""
    # match an instagram handle
    return re.findall(r'@[\w._]{1,30}', text)

def anonymize_instagram(text):
    instagram_p = Pattern(name="Instagram",regex=r'(?<!\S)@[\w._]{1,30}',score=0.9)
    instagram_pattern = ['r@[\w._]{1,30}']

    instagram_recognizer = PatternRecognizer(supported_entity="INSTAGRAM_HANDLE", supported_language="en", patterns=[instagram_p])
    instagram_recognizer.analyze(text,entities="INSTAGRAM_HANDLE")

    registry = RecognizerRegistry()
    registry.load_predefined_recognizers()

    # Add the recognizer to the existing list of recognizers
    registry.add_recognizer(instagram_recognizer)

    # Set up analyzer with our updated recognizer registry
    analyzer = AnalyzerEngine(registry=registry)

    results = analyzer.analyze(text=text,entities=['INSTAGRAM_HANDLE'],   language="en")
    engine = AnonymizerEngine()
    result = engine.anonymize(text=text,analyzer_results= results)
    return result


if __name__ == '__main__':
    print(anonymize_instagram( 'John Edwards called the help desk for help with their credit card 4095-3434-2424-1414.'
                                + ' They provided their ssn 750-12-1234 and phone number 919-555-1212 which were used to verify their account.'
                                + ' They also provided their email address je2@edwards.com and their social medial handle @jon_edwards for future contact.'
                                + ' They would like future charges billed to an amex account 1234-567890-12345' ))
