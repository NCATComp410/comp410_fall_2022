# -*- coding: utf-8 -*-
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

def find_us_phone_number(text):
    """Finds all occurrences of a US phone number in a text string"""
    # match a 10 digit phone number with area code
    return re.findall(r'\d{3}-\d{3}-\d{4}', text)


def find_visa_mastercard(text):
    """Finds all occurrences of a visa / mastercard number in a text string"""
    # match a 16 digit credit card number
    return re.findall(r'\d{4}-\d{4}-\d{4}-\d{4}', text)

# All American Express account numbers must start with “37” or “34”.
def find_amex(text):
    """Finds all occurrences of an amex number in a text string"""
    # match a 15 digit credit card number
    return re.findall(r'^(34|37)\d{2}-\d{6}-\d{5}', text)


def find_us_ssn(text):
    """Finds all occurrences of a US social security number in a text string"""
    # match a 9 digit social security number
    return re.findall(r'\d{3}-\d{2}-\d{4}', text)


def find_email(text):
    """Finds all occurrences of an email address in a text string"""
    # match an email address
    return re.findall(r'[\w.\-+]+@(?:[\w-]+\.){1,2}[a-zA-Z]{2,4}$', text)


def find_instagram_handle(text):
    """Finds all occurrences of an instagram handle in a text string"""
    # match an instagram handle
    return re.findall(r'(?<!\S)@[\w\d.]{1,30}', text)

def find_account_number(text):
    """Finds all occurrences of a possible account number"""
    # match an account number
    return re.findall(r'\d{3,4}-\d{5}', text)



def anonymize_pii(text) :
    # dict for patterns and recognizers
    patterns = {
        "US_SSN": Pattern(name = 'SSN_pattern', regex = r'\d{3}-\d{2}-\d{4}', score = 0.9),
        "AMEX": Pattern(name = 'AMEX_pattern', regex = r'^3[4]|[7]\d{2}-\d{6}-\d{5}$', score = 0.9),
    }
    # SSN_pattern = Pattern(name = 'SSN_pattern', regex = r'\d{3}-\d{2}-\d{4}', score = 0.9)
    recognizers = {
        "SSN_recognizer": PatternRecognizer(supported_entity = 'US_SSN', patterns = [patterns['US_SSN']]),
        "AMEX_recognizer": PatternRecognizer(supported_entity = 'AMEX', patterns = [patterns['AMEX']]),
    }
    
    registry = RecognizerRegistry()
    registry.load_predefined_recognizers()

    #Add Custom Recognizers
    for pattern in recognizers:
        registry.add_recognizer(pattern)

    #Setup analyzer with updated recognizer registry
    analyzer = AnalyzerEngine (registry = registry)

    detect_types = ['US_SSN', 'AMEX']
    
    results = analyzer.analyze(text = text, entities = detect_types, language = 'en')

    # Initialize the engine and anonymize the results
    engine = AnonymizerEngine()
    anon = engine.anonymize(text = text, analyzer_results = results)

    return anon


if __name__ == '__main__' :
    
     print(anonymize_pii('John Edwards called the help desk for help with their credit card 4095-3434-2424-1414. '+
                         'They provided their ssn 750-12-1234 and phone number 919-555-1212 which were used to verify their account. '+
                         'They also provided their email address je2@edwards.com and their social medial handle @jon_edwards for future contact. '+
                         'They would like future charges billed to an amex account 1234-567890-12345'))