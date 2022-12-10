from django.urls import path
from . import views 

urlpatterns = [

    path('cheout/',views.cheout,name='cheout'),
]