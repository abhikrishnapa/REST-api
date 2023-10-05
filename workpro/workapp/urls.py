from django.urls import path
from workapp import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.apiOverview, name='api-Overview'),

    #Login and Register
    path('login/',obtain_auth_token,name='login'),
    path('register/',views.register.as_view(),name='register'),
    path('welcome/',views.welcome.as_view(),name='welcome'),
    path('paginationApi', views.paginationApi.as_view(), name='paginationApi'),
    
    #CRUD
    path('task-list/', views.tasklist,name='task-list'),
    path('task-detail/<str:pk>/', views.taskDetail,name='task-detail'),
    path('task-create/', views.taskCreate,name='task-create'),
    path('task-update/<str:pk>/', views.taskUpdate,name='task-update'),
    path('task-delete/<str:pk>/', views.taskDelete,name='task-delete')
]


