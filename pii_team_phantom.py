import re
import spacy
from presidio_analyzer import AnalyzerEngine, RecognizerRegistry, PatternRecognizer, Pattern
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

def anonymize(text):
    instagram_p = Pattern(name="Instagram",regex=r'(?<!\S)@[\w._]{1,30}',score=0.9)
    amex_p = Pattern(name="Amex", regex=r'\d{4}\-\d{6}\-\d{5}', score=0.9)
    mastercard_p = Pattern(name="MASTERCARD", regex=r'\d{4}-\d{4}-\d{4}-\d{4}', score=0.9)


    instagram_recognizer = PatternRecognizer(supported_entity="INSTAGRAM_HANDLE", supported_language="en", patterns=[instagram_p])
    instagram_recognizer.analyze(text,entities="INSTAGRAM_HANDLE")

    amex_recognizer = PatternRecognizer(supported_entity="AMEX", supported_language="en", patterns=[amex_p])
    amex_recognizer.analyze(text, entities="AMEX")

    mastercard_recognizer = PatternRecognizer(supported_entity="MASTERCARD", supported_language="en", patterns=[mastercard_p])
    mastercard_recognizer.analyze(text, entities="AMEX")

    registry = RecognizerRegistry()
    registry.load_predefined_recognizers()
    registry.add_recognizer(instagram_recognizer)
    registry.add_recognizer(amex_recognizer)
    registry.add_recognizer(mastercard_recognizer)
    analyzer = AnalyzerEngine(registry=registry)

    detect_types = ['US_SSN', 'PHONE_NUMBER', 'EMAIL_ADDRESS', 'AMEX', 'INSTAGRAM_HANDLE', 'MASTERCARD', 'PERSON']

    results = analyzer.analyze(text=text,entities=detect_types,   language="en")
    engine = AnonymizerEngine()
    result = engine.anonymize(text=text,analyzer_results= results)
    return result


if __name__ == '__main__':
    print(anonymize(
'John Edwards called the help desk for help with their credit card 4095-3434-2424-1414.'
+ ' They provided their ssn 750-12-1234 and phone number 919-555-1212 which were used to verify their account.'
+ ' They also provided their email address je2@edwards.com and their social medial handle @jon_edwards for future contact.'
+ ' They would like future charges billed to an amex account 1234-567890-12345'
    ))



