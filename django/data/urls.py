from django.urls import path
from . import views

app_name = 'data'

urlpatterns = [
    path('', views.DataHomeView.as_view(), name='data-home'),
    path('sync/', views.DataSyncLandingView.as_view(), name='data-sync-landing'),
    path('sync/process/', views.DataSyncView, name='data-sync-process'),
    path('<slug:slug>/', views.DataFolderView.as_view(), name='data-folder')
]
