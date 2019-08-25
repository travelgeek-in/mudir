from django.core.validators import RegexValidator


phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                             message="Contact number must be entered in the format: '+999999999")
