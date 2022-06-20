from django.urls import include, path

from rest_framework import routers

from users_api.views import UserViewSet

users_list = UserViewSet.as_view({
    'get': 'list',
})

add_user = UserViewSet.as_view({
    'post': 'create',
})

retrieve_user = UserViewSet.as_view({
    'get': 'retrieve',
})

delete_user = UserViewSet.as_view({
    'delete': 'destroy'
})

update_user = UserViewSet.as_view({
    'put': 'update'
})

urlpatterns = [
   path('users/', users_list, name='users-list'),
   path('add_user/', add_user, name='add-user'),
   path('users/<int:pk>/', retrieve_user, name='retrieve-user'),
   path('delete_user/<int:pk>/', delete_user, name='delete-user'),
   path('edit_user/<int:pk>/', update_user, name='update-user'),
]