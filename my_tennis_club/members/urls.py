from django.urls import path
from . import views
# from .views import MemberListCreate

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('test/', views.test, name='testing'),    
    path('name/', views.fun, name='name'),
    path('name2/', views.fun2, name='name2'),
    path('hell/', views.hell, name='hell'),
    
    # path('mem_post/', MemberListCreate.as_view(), name='member-list-create'),

    

]