from json import JSONDecodeError
from django.http import JsonResponse
from .serializers import *
from rest_framework.parsers import JSONParser
from rest_framework import views, status
from rest_framework.response import Response
from .models import *


class CreatureCategoriesAPIView(views.APIView):
    """
    A simple APIView for creating contact entires.
    """
    serializer_class = CreatureCategoriesSerializer

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def post(self, request):
        try:
            data = JSONParser().parse(request)
            serializer = CreatureCategoriesSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except JSONDecodeError:
            return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)
    
    def get(self, request):
        data = CreatureCategories.objects.all()
        serializer = CreatureCategoriesSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)        

class CreaturesAPIView(views.APIView):
    """
    A simple APIView for creating contact entires.
    """
    serializer_class = CreaturesSerializer

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def post(self, request):
        try:
            data = JSONParser().parse(request)
            serializer = CreaturesSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except JSONDecodeError:
            return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)
        
    def get(self, request):
        data = Creatures.objects.all()
        serializer = CreaturesSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class HomePageAPIView(views.APIView):
    """
    A simple APIView for creating contact entires.
    """
    serializer_class = HomePageSerializer

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def post(self, request):
        try:
            data = JSONParser().parse(request)
            serializer = HomePageSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except JSONDecodeError:
            return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)
    
    def get(self, request):
        data = HomePage.objects.all()
        serializer = HomePageSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class BlogsAPIView(views.APIView):
    """
    A simple APIView for creating contact entires.
    """
    serializer_class = BlogsSerializer

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def post(self, request):
        try:
            data = JSONParser().parse(request)
            serializer = BlogsSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except JSONDecodeError:
            return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)

    def get(self, request):
        data = Blogs.objects.all()
        serializer = BlogsSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)