from django.contrib import admin
from .models import Movie, Category

# Register your models here

admin.site.site_header = 'Welcome Movie World Dashboard'
admin.site.site_title = 'Login to Movie World'
admin.site.index_title = 'Welcome to the Movie World Admin Dashboard'


admin.site.register(Movie)
admin.site.register(Category)


