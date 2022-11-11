from django.urls import path
from . import views
app_name="com"
urlpatterns=[
    path('home',views.home),
    path('placements',views.placements),
    path('blog',views.blog),
    path('gallery',views.gallery),
    path('enquire',views.enquire),
]