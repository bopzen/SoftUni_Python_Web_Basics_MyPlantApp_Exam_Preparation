from django.core import validators


def validate_profile_names(value):
    if not value[0].isupper():
        raise validators.ValidationError("Your name must start with a capital letter!")


def validate_plant_name(value):
    for ch in value:
        if not ch.isalpha():
            raise validators.ValidationError("Plant name should contain only letters!")
