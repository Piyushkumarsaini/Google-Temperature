from django.urls import path,include
from . import views
urlpatterns = [
    path("temperature/<str:city>/",views.TemperatureScrap),
    path("user_input/",views.user_input,name='user_input')
]
