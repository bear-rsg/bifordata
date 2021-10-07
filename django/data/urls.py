from django.urls import path
from . import views

app_name = 'data'

urlpatterns = [
    path('', views.DataHomeView.as_view(), name='data-home'),
    path('<pk>/', views.DataFolderView.as_view(), name='data-folder'),
]
