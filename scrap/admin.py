from django.contrib import admin

# Register your models here.
from .models import Category,Scraps
admin.site.register(Category)
admin.site.register(Scraps)