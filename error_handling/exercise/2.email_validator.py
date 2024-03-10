import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneAtSymbolError(Exception):
    pass


class NotValidNameError(Exception):
    pass


MIN_NAME_LENGTH = 4
name_pattern = r"([a-zA-Z\d]+[_\.\-]?[a-zA-Z\d]+)"
valid_domains = ['.com', '.bg', '.org', '.net']
domain_pattern = r'\.[a-z]+'


email = input()
while email != 'End':
    if "@" not in email:
        raise MustContainAtSymbolError("The email address must contain '@'")

    if email.count('@') > 1:
        raise MoreThanOneAtSymbolError("The email address cannot contain more than one '@'")

    name, domain = email.split('@')

    if re.findall(domain_pattern, email)[-1] not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: '.com', '.bg', '.org', '.net'")

    if len(name) <= MIN_NAME_LENGTH:
        raise NameTooShortError("Name must be more than 4 characters long")

    if re.findall(name_pattern, email)[0] != name:
        raise NotValidNameError("Name must contain only letters (a-z), numbers, underscores, periods, and dashes.\n"
                                "An underscore, period, or dash must be followed by one or more letter or number.")

    print('The email address is valid.')

    email = input()