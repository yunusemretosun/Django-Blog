from django.urls import path
from .views import (BlogView,
                    BlogDetailView,
                    BlogCreateNew,
                    BlogUpdateView,
                    BlogDeleteView)

urlpatterns = [
    path('post/delete/<int:pk>', BlogDeleteView.as_view(), name='post_delete'),
    path('post/edit/<int:pk>', BlogUpdateView.as_view(), name='post_edit'),
    path('post/yeni/', BlogCreateNew.as_view(), name='post_yeni'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', BlogView.as_view(), name='anasayfa'),

]
