from django.db import models
from django_extensions.db.models import (
	TimeStampedModel, 
	TitleDescriptionModel
)

class CreatureCategories(TitleDescriptionModel):
	
    image = models.ImageField(verbose_name="image", null=True)
    class Meta:
        verbose_name_plural = "CreatureCategories"

    def __str__(self):
	    return f'{self.title}'
    
class Creatures(TitleDescriptionModel):
	
    image = models.ImageField(verbose_name="image", null=True)
    category = models.ForeignKey(CreatureCategories, models.CASCADE, verbose_name="category")
    class Meta:
        verbose_name_plural = "Creatures"

    def __str__(self):
	    return f'{self.title}'
    
class HomePage(TitleDescriptionModel):
    image = models.ImageField(verbose_name="image", null=True)
	
    class Meta:
        verbose_name_plural = "HomePage"

    def __str__(self):
	    return f'{self.title}'
    
class Blogs(TitleDescriptionModel,TimeStampedModel):
    image = models.ImageField(verbose_name="image", null=True)
    author = models.TextField(verbose_name="author", blank=True, null=True)
    class Meta:
        verbose_name_plural = "Blogs"

    def __str__(self):
	    return f'{self.title}'