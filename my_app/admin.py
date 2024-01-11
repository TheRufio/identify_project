from django.contrib import admin
from .models import MyUsers, Blogs

admin.site.register((MyUsers, Blogs))