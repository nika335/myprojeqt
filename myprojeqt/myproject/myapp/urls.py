from django.urls import path
from myapp.views import website, home, about, contact


urlpatterns = [
    path('', website),
    path('home', home),
    path('about', about),
    path('contact', contact)
]
