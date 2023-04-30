from django.contrib import admin
from user_accounts.models import User
from .models import Musician, Album, Track, Listener, Listens, Purchase, Payments

my_models = [User, Musician, Album, Track, Listener, Listens, Purchase, Payments]

admin.site.register(my_models)
