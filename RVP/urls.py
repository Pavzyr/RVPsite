from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('general_stats.urls', namespace='general_stats')),
    path('admin/', admin.site.urls),
]
