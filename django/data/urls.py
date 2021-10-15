from django.urls import path
from . import views

app_name = 'data'

urlpatterns = [
    path('', views.DataHomeView.as_view(), name='data-home'),
    path('<slug:slug>/', views.DataFolderView.as_view(), name='data-folder'),
    path('sync/', views.DataSyncView, name='data-sync'),
]
