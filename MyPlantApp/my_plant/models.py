from django.db import models
from django.core import validators
from MyPlantApp.my_plant.validators import validate_profile_names, validate_plant_name


class Profile(models.Model):
    MIN_USERNAME_LENGTH = 2
    MAX_USERNAME_LENGTH = 10
    MAX_NAME_LENGTH = 20
    username = models.CharField(
        max_length=MAX_USERNAME_LENGTH,
        validators=(
            validators.MinLengthValidator(MIN_USERNAME_LENGTH),
        ),
        null=False,
        blank=False
    )
    first_name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        validators=(
            validate_profile_names,
        ),
        null=False,
        blank=False
    )
    last_name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        validators=(
            validate_profile_names,
        ),
        null=False,
        blank=False
    )
    profile_picture = models.URLField(
        null=True,
        blank=True
    )


class Plant(models.Model):
    MIN_NAME_LENGTH = 2
    MAX_NAME_LENGTH = 20
    MAX_PLANT_TYPE_LENGTH = 14
    PLANT_TYPES = [
        ('Outdoor Plants', 'Outdoor Plants'),
        ('Indoor Plants', 'Indoor Plants'),
    ]
    plant_type = models.CharField(
        max_length=MAX_PLANT_TYPE_LENGTH,
        choices=PLANT_TYPES,
        null=False,
        blank=False
    )
    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        validators=(
            validators.MinLengthValidator(MIN_NAME_LENGTH),
            validate_plant_name
        ),
        null=False,
        blank=False
    )
    image_url = models.URLField(
        null=False,
        blank=False
    )
    description = models.TextField(
        null=False,
        blank=False
    )
    price = models.FloatField(
        null=False,
        blank=False
    )
