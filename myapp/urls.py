from  .import views
from django.urls import path

urlpatterns=[
    path('',views.index,name='index'),
    path('portfolio',views.portfolio,name='portfolio'),
    path('blog',views.blog,name='blog')
]