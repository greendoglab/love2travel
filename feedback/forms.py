# -*- coding: utf-8 -*-
from django import forms
from django.forms.fields import ChoiceField, MultipleChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple


TYPETOUR_CHOICES = (
        ('свадебное путешествие, медовый месяц', 'свадебное путешествие, медовый месяц'),
        ('венчание', 'венчание'),
        ('символическая свадебная церемония', 'символическая свадебная церемония'),
        ('официальное бракосочетание', 'официальное бракосочетание'),
        ('романтический тур', 'романтический тур'),
        ('тур', 'тур'),
        ('другое', 'другое'),
    )
FLYCLASS_CHOICES = (
        ('Первый', 'Первый'),
        ('Бизнес', 'Бизнес'),
        ('Эконом', 'Эконом'),
    )
EATHOTEL_CHOICES = (
        ('OB', 'OB'),
        ('BB', 'BB'),
        ('HB', 'HB'),
        ('FB', 'FB'),
        ('AL', 'AL'),
        ('UAL', 'UAL'),
    )
GUESTPAY_CHOICES = (
        ('Да', 'Да'),
        ('Нет', 'Нет'),
        ('Другое', 'Другое'),
    )
ADVANCE_CHOICES = (
        ('свадебный координатор от нашей компании на месте проведения свадьбы',
         'свадебный координатор от нашей компании на месте проведения свадьбы'),
        ('помощь в организации мальчишника или девичника',
         'помощь в организации мальчишника или девичника'),
        ('помощь в организации расширенной шоу-программы',
         'помощь в организации расширенной шоу-программы'),
        ('Другое',
         'Другое'),
    )

class OrderForm(forms.Form):

    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=100)
    email = forms.EmailField("Email")
    date_married = forms.CharField(max_length=100, required=False)
    date_tour = forms.CharField(max_length=100)
    country = forms.CharField(max_length=100)
    budget = forms.CharField(max_length=100)
    hotel_stars = forms.CharField(max_length=100)
    guest = forms.CharField(max_length=100, required=False)
    best_place = forms.CharField(max_length=100, required=False)
    best_country = forms.CharField(max_length=100, required=False)
    full_budget = forms.CharField(max_length=100, required=False)

    type_tour = ChoiceField(widget=RadioSelect, choices=TYPETOUR_CHOICES, required=False)
    fly_class = ChoiceField(widget=RadioSelect, choices=FLYCLASS_CHOICES, required=False)
    eat_hotel = ChoiceField(widget=RadioSelect, choices=EATHOTEL_CHOICES, required=False)
    guest_pay = ChoiceField(widget=RadioSelect, choices=GUESTPAY_CHOICES, required=False)
    advance = ChoiceField(widget=RadioSelect, choices=ADVANCE_CHOICES, required=False)

    message = forms.CharField(widget=forms.Textarea, required=False)
    cc_myself = forms.BooleanField(required=False)