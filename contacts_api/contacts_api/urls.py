"""
URL configuration for contacts_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# from django.urls import path
# from contacts.views import contact_list, contact_detail

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('contacts/', contact_list),
#     path('contacts/<int:pk>/', contact_detail)
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from contacts.views import CategoryViewSet, ContactViewSet, SignUpView, LoginView

router = DefaultRouter()
router.register(r'contacts', ContactViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls)),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
]