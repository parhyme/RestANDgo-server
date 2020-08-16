from django.urls import path
from .views import GetAllData, PostModelData
from . import views

urlpatterns = [
    path('get-all-data/', GetAllData.as_view()),
    path('post-model/', PostModelData.as_view()),
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('', views.home, name="home"),
]
