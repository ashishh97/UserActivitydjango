from django.contrib import admin
from django.urls import path,include
from .views import ActivityView

urlpatterns = [
  path('api-auth',include('rest_framework.urls')),
  path('admin/', admin.site.urls),
  path('',ActivityView.as_view(), name='activity')
]