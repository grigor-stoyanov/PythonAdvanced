# Creating custom Exceptions
class NameTooShort(Exception):
    """email name less than 4 characters """
    pass


class MustCointainAt(Exception):
    """email doesn't contain @"""
    pass


class InvalidDomainError(Exception):
    """Domain is wrong"""
    pass


# Keeping domains as a constant and a list of errors as a global
ALLOWED_DOMAINS = ['com', 'org', 'net', 'bg']
errors = []


def validate_email(email):
    # validating for each error and adding it to the list
    if '@' not in email or '@@' in email:
        errors.append(MustCointainAt('Email must contain one "@" symbol'))
    else:
        # adding independent errors
        name, domain = email.split('@')
        if len(name) < 4:
            errors.append(NameTooShort('Username must be at least 4 characters long'))
        if '..' in domain or domain.split('.')[-1] not in ALLOWED_DOMAINS:
            errors.append(InvalidDomainError(f"Domain must be one of the following: {', '.join(ALLOWED_DOMAINS)}"))
    return errors


# executing the errors one at a time
def raise_errors(errs):
    if not errs:
        return 'Email is valid'
    try:
        raise errs.pop()
    except (NameTooShort, InvalidDomainError) as e:
        print(e)
    finally:
        raise_errors(errs)


def main():
    while not (email := input()) == 'End':
        errors = validate_email(email)
        # if the email is not valid result is none
        result = raise_errors(errors)
        if result:
            print(result)
        # while errors:
        #     try:
        #         errors.pop()
        #     except (NameTooShort, InvalidDomainError) as e:
        #         print(e)
        #     else:
        #         print('Email is Valid')


if __name__ == '__main__':
    main()
