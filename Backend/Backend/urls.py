from django.contrib import admin
from django.urls import path
from .api import api
from .apiPost import api_post
from .apiLogin import api_login
from .apiGet import api_get




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
    path('post_api/', api_post.urls),
    path('api_login/', api_login.urls),
    path('api_get/', api_get.urls)
     
]


