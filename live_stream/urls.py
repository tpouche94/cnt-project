from .views import live
from django.urls import path


urlpatterns = [
    path('', live),
] 