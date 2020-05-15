from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name='blog'),
    path('<int:blog_id>', views.blog_detail, name='detail'),
    # path('blog/', include('blog.urls')),
]
