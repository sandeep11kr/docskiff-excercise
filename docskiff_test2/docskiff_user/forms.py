from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    FRUIT_CHOICES = [
        ('orange', 'Oranges'),
        ('cantaloupe', 'Cantaloupes'),
        ('mango', 'Mangoes'),
        ('honeydew', 'Honeydews'),
        ('apple', 'Apple'),
        ('pineapple', 'Pineapple'),
        ('banana', 'Banana')
    ]

    favorite_fruit = forms.MultipleChoiceField(label='What are your favorite fruits?',
                                               choices=FRUIT_CHOICES,
                                               widget=forms.SelectMultiple)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2', 'favorite_fruit']
