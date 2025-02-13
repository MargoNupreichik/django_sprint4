from django.contrib import admin

# Из модуля models импортируем модель...
from .models import Post, Category, Location

# ...и регистрируем её в админке:
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Location)
