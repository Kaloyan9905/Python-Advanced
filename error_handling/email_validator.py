class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


email = input()

emails = []

while email != "End":
    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    index = email.index("@")

    if len(email[:index + 1]) < 5:
        raise NameTooShortError("Name must be more than 4 characters")

    index = email.index(".")

    domain = email[index::]

    if domain not in [".com", ".bg", ".org", ".net"]:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")

    email = input()
