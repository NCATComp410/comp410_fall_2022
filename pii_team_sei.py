import re


def find_us_phone_number(text) -> list:
    """Finds all occurrences of a US phone number in a text string"""
    # match a 10 digit phone number with area code
    return []


def find_visa_mastercard(text) -> list:
    """Finds all occurrences of a visa / mastercard number in a text string"""
    # match a 16 digit credit card number
    return []


def find_amex(text) -> list:
    """Finds all occurrences of an amex number in a text string"""
    # match a 15 digit credit card number
    return []


def find_us_ssn(text) -> list:
    """Finds all occurrences of a US social security number in a text string"""
    SSN = raw_input("enter SSN (ddd-dd-dddd):")
    chunks = SSN.split('-')
    valid=False
    if len(chunks) ==3: 
     if len(chunks[0])==3 and len(chunks[1])==2 and len(chunks[2])==4:
       valid=True
    print valid
    return []


def find_email(text) -> list:
    """Finds all occurrences of an email address in a text string"""
    # match an email address
    return []


def find_instagram_handle(text) -> list:
    """Finds all occurrences of an instagram handle in a text string"""
    # match an instagram handle
    return []
