
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', include('blogsite.urls')),
    path('crudapp/', include('crudapp.urls')),
    path('usuario/', include('usuario.urls')),


]
