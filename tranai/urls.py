from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:year>/<str:month>/', views.home, name='home'),
    path('translations', views.all_translations, name='list-translations'),
    # path('new_document', views.create_document, name='create-document'),
    path('create_document', views.create_document, name='create-document'),
    path('index_documents', views.index_documents, name='index-documents'),
    path('show_document/<document_id>', views.show_document, name='show-document'),
]
