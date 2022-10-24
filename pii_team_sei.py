import re


def find_us_phone_number(text) -> list:
    """Finds all occurrences of a US phone number in a text string"""
    # match a 10 digit phone number with area code
    return []
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
    return []


def find_us_ssn(text) -> list:
    """Finds all occurrences of a US social security number in a text string"""
    return []
    regex = "^(?!666|000|9\\d{2})\\d{3}-(?!00)\\d{2}-(?!0{4})\\d{4}$";



def find_email(text) -> list:
    """Finds all occurrences of an email address in a text string"""
    # match an email address
    return []
    return re.findall(r'^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+', text)


def find_instagram_handle(text) -> list:
    """Finds all occurrences of an instagram handle in a text string"""
    # match an instagram handle
    return []

