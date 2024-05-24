from django.urls import path

from . import views


urlpatterns = [
    # path('notes/', views.notes),                        # localhost:8000/api/notes/
    # path('notes/<uuid:id>/', views.note),               # localhost:8000/api/notes/edit/:id

    # path('users/', views.users),                        # localhost:8000/api/users/
    # path('users/<int:id>/', views.user),                # localhost:8000/api/users/1
    
    
    # localhost:8000/api/users/
    path('users/',views.UserViewSet.as_view({
        'get':'list',
        'post':'create',

    })),
    
    # localhost:8000/api/users/1
    path('users/<int:pk>/',views.UserViewSet.as_view({
        'put':'update',
        'patch':'partial_update',
        'get':'retrieve',
        'delete':'destroy'
    })),
    # localhost:8000/api/notes/
    path('notes/',views.NoteViewSet.as_view({
        'get':'list',
        'post':'create',

    })),
    
    # localhost:8000/api/notes/id
    path('notes/<uuid:pk>/',views.NoteViewSet.as_view({
        'put':'update',
        'patch':'partial_update',
        'get':'retrieve',
        'delete':'destroy'
    })),
]
