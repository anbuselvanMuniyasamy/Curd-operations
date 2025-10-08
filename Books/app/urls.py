from django.urls import path
from .views import (
    BookViewSet,
    book_list_template,
    book_create_template,
    book_update_template,
    book_delete_template
)

# DRF API endpoints
book_list_api = BookViewSet.as_view({'get': 'list', 'post': 'create'})
book_detail_api = BookViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})

urlpatterns = [
    # API URLs
    path('api/books/', book_list_api, name='book-list-api'),
    path('api/books/<int:pk>/', book_detail_api, name='book-detail-api'),

    # Template URLs
    path('', book_list_template, name='book-list-template'),
    path('books/create/', book_create_template, name='book-create-template'),
    path('books/<int:pk>/update/', book_update_template, name='book-update-template'),
    path('books/<int:pk>/delete/', book_delete_template, name='book-delete-template'),
]
