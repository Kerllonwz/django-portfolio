from django.contrib import admin
from django.urls import path
from blog.views import home, post_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
]
