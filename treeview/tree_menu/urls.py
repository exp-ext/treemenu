from django.urls import path

from .views import PageView, post_detail

urlpatterns = [
    path('', PageView.as_view(), name='tree_menu'),
    path('<int:post_id>/', post_detail, name='post_detail'),
]
