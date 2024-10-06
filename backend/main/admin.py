from django.contrib import admin
from .models import *


@admin.register(CreatureCategories)
class CreatureCategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')

@admin.register(Creatures)
class CreaturesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'category')

@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    
@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'modified', 'title', 'description', 'author')