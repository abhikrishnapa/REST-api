from django.urls import path
from workapp import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.apiOverview, name='api-Overview'),

    #Login and Register
    path('login/',obtain_auth_token,name='login'),
    path('register/',views.register.as_view(),name='register'),
    path('welcome/',views.welcome.as_view(),name='welcome'),
    path('paginationApi/', views.paginationApi.as_view(), name='paginationApi'),
    
    #CRUD
    path('create/', views.create,name='create'),
    path('read/<str:pk>/', views.read,name='read'),
    path('readAll/', views.readAll,name='readAll'),
    path('update/<str:pk>/', views.update,name='update'),
    path('delete/<str:pk>/', views.delete,name='delete'),
    path('deleteAll/', views.deleteAll,name='deleteAll'),

]

