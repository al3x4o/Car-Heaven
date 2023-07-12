from django.core import validators, exceptions
from django.db import models


class Profile(models.Model):
    MIN_USERNAME_LEN = 2
    MAX_USERNAME_LEN = 15

    MIN_AGE = 18
    MAX_PASSWORD_LEN = 30
    MIN_PASSWORD_LEN = 6
    MAX_FIRSTNAME_LEN = 30
    MAX_LASTNAME_LEN = 30

    username = models.CharField(
        max_length=MAX_USERNAME_LEN,
        blank=False,
        null=False,
        validators=(
            validators.MinLengthValidator(MIN_USERNAME_LEN, message="The username must be a minimum of 2 chars"),
        )
    )
    first_name = models.CharField(
        max_length=MAX_FIRSTNAME_LEN,
        blank=False,
        null=False,
    )

    last_name = models.CharField(
        max_length=MAX_LASTNAME_LEN,
        blank=True,
        null=True,
    )
    email = models.EmailField(
        blank=False,
        null=False
    )

    age = models.IntegerField(
        blank=False,
        null=False,
        validators=(
            validators.MinValueValidator(MIN_AGE),
        )
    )

    password = models.CharField(
        blank=False,
        null=False,
        max_length=MAX_PASSWORD_LEN,
        validators=[
            validators.MinLengthValidator(MIN_PASSWORD_LEN, message="Must contain at LEAST 6 symbols")
        ]
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )


class Car(models.Model):
    MAX_TYPE_LEN = 10
    MAX_SPEED_LEN = 10
    MAX_SPEED = 500
    MIN_SPEED = 1
    MAX_MODEL_LEN = 20
    MIN_MODEL_LEN = 2
    MIN_PRICE = 1
    MIN_YEAR = 1980
    MAX_YEAR = 2049

    SPORTS_CAR = "Sports Car"
    PICKUP = "Pickup"
    CROSSOVER = "Crossover"
    MINIBUS = "Minibus"
    OTHER = "Other"

    CARS = (
        (SPORTS_CAR, SPORTS_CAR),
        (PICKUP, PICKUP),
        (CROSSOVER, CROSSOVER),
        (MINIBUS, MINIBUS),
        (OTHER, OTHER)
    )

    type = models.CharField(
        max_length=MAX_TYPE_LEN,
        blank=False,
        null=False,
        choices=CARS,
    )

    model = models.CharField(
        blank=False,
        null=False,
        max_length=MAX_MODEL_LEN,
        validators=(
            validators.MinLengthValidator(MIN_MODEL_LEN),
        )
    )
    speed = models.IntegerField(
        blank=True,
        null=True,
        max_length=MAX_SPEED_LEN,
        validators=(
            validators.MaxValueValidator(MAX_SPEED),
            validators.MinValueValidator(MIN_SPEED),
        )
    )

    year = models.IntegerField(
        blank=False,
        null=False,
        validators=(
            validators.MaxValueValidator(MAX_YEAR, "Year must be between 1980 and 2049"),
            validators.MinValueValidator(MIN_YEAR, "Year must be between 1980 and 2049"),
        )
    )

    image_url = models.URLField(
        blank=False,
        null=False,
    )

    price = models.FloatField(
        blank=False,
        null=False,
        validators=(
            validators.MinValueValidator(MIN_PRICE),
        )
    )
