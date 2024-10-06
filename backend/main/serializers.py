from . import models
from rest_framework import serializers
from rest_framework.fields import CharField, IntegerField, ImageField



class CreatureCategoriesSerializer(serializers.ModelSerializer):

	name = CharField(source="title", required=True)
	description = CharField(required=True)
	image = ImageField()
	class Meta:
		model = models.CreatureCategories
		fields = (
			'name',
			'description',
			'image',
		)
		


class CreaturesSerializer(serializers.ModelSerializer):

	name = CharField(source="title", required=True)
	description = CharField( required=True)
	category = IntegerField( required=True)
	image = ImageField()
	class Meta:
		model = models.Creatures
		fields = (
			'name',
			'description',
			'category',
			'image',
		)
		
class HomePageSerializer(serializers.ModelSerializer):
    name = CharField(source="title", required=True)
    description = CharField(required=True)
    image = ImageField()
    class Meta:
        model = models.HomePage
        fields = (
            'name',
            'description',
            'image',
        )
class BlogsSerializer(serializers.ModelSerializer):

    name = CharField(source="title", required=True)
    description = CharField(required=True)
    author = CharField(required=True)
    image = ImageField()
    class Meta:
        model = models.HomePage
        fields = (
            'name',
            'description',
            'author',
            'image',
        )
		

