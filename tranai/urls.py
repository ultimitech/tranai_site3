from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:year>/<str:month>/', views.home, name='home'),
    path('translations', views.all_translations, name='list-translations'),
    # path('new_document', views.create_document, name='create-document'),
    path('add_document', views.add_document, name='add-document'),
    path('list_documents', views.list_documents, name='list-documents'),
    path('show_document/<document_id>', views.show_document, name='show-document'),
]
