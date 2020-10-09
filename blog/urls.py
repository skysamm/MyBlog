from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path(r'contact/$', views.get_contact, name='contact'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]