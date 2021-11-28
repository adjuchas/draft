"""Draft URL Configuration

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

from django.urls import path
from .views import callback_code, get_accesstoken, logout, get_info


urlpatterns = [
    path('app215/', callback_code, name='app215'),

    path('get_accesstoken/', get_accesstoken, name='get_access_token'),

    path('logout/', logout, name='logout'),

    path('get_info/', get_info, name='get_info')
]
