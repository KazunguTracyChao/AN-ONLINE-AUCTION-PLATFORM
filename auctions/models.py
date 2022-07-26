from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def age_validator(age):
    if age < 21:
        raise ValidationError(
            _('You need to be 21 years old!')
        )


GENDER_MALE = 'M'
GENDER_FEMALE = 'F'
GENDER_NOT_SPECIFIED = 'O'

GENDER_CHOICES = (
    (GENDER_MALE, _('male')),
    (GENDER_FEMALE, _('female')),
    (GENDER_NOT_SPECIFIED, _('not specified')),
)


class User(AbstractUser):
    name = models.CharField(max_length=100, default='username')
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(
        validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    address = models.CharField(max_length=100, default='')
    age = models.IntegerField(validators=[age_validator])
    gender = models.CharField(max_length=1,
                              choices=GENDER_CHOICES, default=GENDER_NOT_SPECIFIED)


class Bid(models.Model):
    bid = models.IntegerField(default=0)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='bid')

    def __str__(self):
        return f"{self.user} - {self.bid}"


class Listing(models.Model):
    title = models.CharField(max_length=32)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='listing', null=True, blank=True)
    is_closed = models.BooleanField(default=False, blank=True, null=True)
    description = models.CharField(max_length=400)
    bid = models.ForeignKey(
        Bid, on_delete=models.CASCADE, related_name='listing', default=None)
    url = models.CharField(
        max_length=2048, default="https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg", null=True, blank=True)
    watchlist = models.ManyToManyField(
        User, blank=True, related_name='watch_listings')
    category = models.CharField(max_length=400, null=True, blank=True)

    def __str__(self):
        return f"{self.category}"
