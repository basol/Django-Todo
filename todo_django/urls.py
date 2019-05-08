"""todo_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from todo.views import home_page, login, register, update, delete, create_todo, import_todo, export_todo,user_profile, statistics_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('django.contrib.auth.urls')),
    path('register', register),
    path('profile/<int:id>', user_profile),
    path('update/<int:id>', update),
    path('delete/<int:id>', delete),
    path('create-todo', create_todo),
    path('import-todo', import_todo),
    path('export-todo', export_todo),
    path('statistics', statistics_page),
    path('', home_page),
]
