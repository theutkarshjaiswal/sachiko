"""assignment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from game.views import (Signup, Login, Logout, Home, CreateGame,
                        Play, UserView, UserViewDetail, GameList, GameDetail,
                        TransactionList, TransactionDetail, CategoryList,
                        CategoryDetail)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home,name = 'home'),
    path('signup/',Signup, name = 'signup'),
    path('login/',Login, name = 'login'),
    path('logout/',Logout,name = 'logout'),
    path('creategame/',CreateGame,name = 'creategame'),
    path('play/<int:pk>',Play,name = 'play'),
    path('user/',UserView.as_view(), name = "user"),
    path('user/<int:pk>/',UserViewDetail.as_view()),
    path('game/',GameList.as_view(), name = "game"),
    path('game/<int:pk>/',GameDetail.as_view()),
    path('category/',CategoryList.as_view(), name = "category"),
    path('category/<int:pk>/',CategoryDetail.as_view()),
    path('transaction/',TransactionList.as_view(), name = "transaction"),
    path('transaction/<int:pk>/',TransactionDetail.as_view()),
]
