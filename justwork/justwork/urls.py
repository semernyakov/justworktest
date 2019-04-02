"""justwork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from basetype import views
from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from rest_framework import routers
router = routers.DefaultRouter()

schema_view = get_swagger_view(title='Pages API')

urlpatterns = [
    path('', schema_view),
    path('', include(router.urls)),
    path('api/v1/pages/', views.PageList.as_view(), name="pages_list"),
    path('api/v1/page/<int:pk>/', views.PageDetail.as_view(), name="page_detail"),
    path('api/v1/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
