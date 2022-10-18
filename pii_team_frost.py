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
    # match a 9 digit social security number
    SSNRegex = re.compile(r'\d\d\d-\d\d-\d\d\d\d')
    MO = SSNRegex.search(text)
    result_list = []
    result_list.append(MO.group())
    return [result_list]


def find_email(text) -> list:
    """Finds all occurrences of an email address in a text string"""
    # match an email address
    return []


def find_instagram_handle(text) -> list:
    """Finds all occurrences of an instagram handle in a text string"""
    # match an instagram handle
    return []