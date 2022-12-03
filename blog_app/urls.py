from django.conf.urls import (handler400, handler403, handler404, handler500)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('', include('posts.urls'))
]

handler404 = 'authentication.views.error_404'
handler500 = 'authentication.views.server_error'
