from django.urls import path
from .views import GetAllData, PostModelData
from . import views

urlpatterns = [
    path('api/v1/mobileinfos/', GetAllData.as_view()),
    path('api/v1/post-model/', PostModelData.as_view()),
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('', views.home, name="home"),
]
