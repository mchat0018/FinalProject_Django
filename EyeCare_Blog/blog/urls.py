from django.urls import path
from . import views


urlpatterns = [
    path('home/',views.BlogHome.as_view(),name='blogs-home'),
    path('category/<int:id>',views.CategoryBlogPosts.as_view(),name='category-posts'),
    path('<int:pk>/',views.blogDetail,name='blog_detail'),
]