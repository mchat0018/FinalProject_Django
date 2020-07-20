from django.urls import path
from . import views


urlpatterns = [
    path('home/',views.BlogHome.as_view(),name='blogs-home'),
    path('category/<str:field>',views.CategoryBlogPosts.as_view(),name='category-posts'),
    path('detail/<int:pk>/',views.PostDetail.as_view(),name='blog_detail'),
]