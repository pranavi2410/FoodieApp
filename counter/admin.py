#from django.contrib import admin
# admin.py
from django.contrib import admin
from .models import Food

admin.site.register(Food)
