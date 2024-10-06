from django.urls import path
from django.contrib import admin
from rest_framework import routers
from main.views import * 
router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
    path('creaturecategories/', CreatureCategoriesAPIView.as_view()),
    path('creatures/', CreaturesAPIView.as_view()),
    path('homepage/', HomePageAPIView.as_view()),
    path('blogs/', BlogsAPIView.as_view()),
]