from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'', include(('learning_logs.urls','learning_logs'), namespace='learning_logs')),
    url(r'^users/', include(('users.urls', 'users'), namespace='users')),
]
