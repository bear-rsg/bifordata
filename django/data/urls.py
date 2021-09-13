from django.urls import path
from . import views

app_name = 'data'

urlpatterns = [
    path('', views.DataListView.as_view(), name='data-list'),
]
