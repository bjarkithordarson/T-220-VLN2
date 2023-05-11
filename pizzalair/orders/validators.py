from django.core.exceptions import ValidationError

def credit_card_number_validator(value):
    if not value.isdigit():
        raise ValidationError('Credit card number must be all digits')
    if len(value) != 16:
        raise ValidationError('Credit card number must be 16 digits long')

def cvc_validator(value):
    if not value.isdigit():
        raise ValidationError('CVC must be all digits')
    if len(value) != 3:
        raise ValidationError('CVC must be 3 digits long')

def expiry_month_validator(value):
    if not value.isdigit():
        raise ValidationError('Expiry month must be all digits')
    if len(value) != 2:
        raise ValidationError('Expiry month must be 2 digits long')
    if int(value) < 1 or int(value) > 12:
        raise ValidationError('Expiry month must be between 1 and 12')

def expiry_year_validator(value):
    if not value.isdigit():
        raise ValidationError('Expiry year must be all digits')
    if len(value) != 4:
        raise ValidationError('Expiry year must be 4 digits long')
    if int(value) < 2020:
        raise ValidationError('Expiry year must be in the future')

