import re
from django.core.exceptions import ValidationError
password_pattern = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

def validate_password(password):
    error_message="In the password one special character,one number and one alphabat"
    p=re.fullmatch(password_pattern,password)
    if p:
        return password
    else:
        
        raise ValidationError(error_message,params={'password':password})


