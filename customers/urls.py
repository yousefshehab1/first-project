from django.urls import path 
from . import views
urlpatterns=[

    path('',views.customers,name='customers'),
    path('mm',views.customers2,name='customers2'),
]