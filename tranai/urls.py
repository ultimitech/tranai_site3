# from rest_framework_nested import routers
from .views import DocumentViewSet, TranslationViewSet
from django.urls import path, re_path, include
# from django.conf.urls import include
from . import views
from django.conf import settings
from django.conf.urls.static import static

# router = routers.SimpleRouter()
# router.register(r'documents', DocumentViewSet, basename='documents')

# documents_router = routers.NestedSimpleRouter(router, r'documents', lookup='document')
# documents_router.register(r'translations', TranslationViewSet, basename='translations')

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:year>/<str:month>/', views.home, name='home'),

    # Document
    # path('new_document', views.create_document, name='create-document'),
    path('create_document', views.create_document, name='create-document'),
    # path('documents/create', views.create_document, name='create-document'),
    # path('index_documents', views.index_documents, name='index-documents'),
    path('documents/', views.index_documents, name='index-documents'),
    path('documents/<document_id>/', views.show_document, name='show-document'),
    # path('show_document/<document_id>', views.show_document, name='show-document'),
    # path('documents/<document_id>/update', views.update_document, name='update-document'),
    path('documents/<document_id>', views.update_document, name='update-document'),
    path('documents/<document_id>', views.destroy_document, name='destroy-document'),
    path('delete_document/<document_id>', views.delete_document, name='delete-document'),
    path('update_document/<document_id>', views.update_document, name='update-document'),

    # Translation
    # path('translations', views.all_translations, name='list-translations'),
    path('create_translation', views.create_translation, name='create-translation'),
    path('translations/', views.index_translations, name='index-translations'),
    # path('translations/<translation_id>/', views.show_translation, name='show-translation'),
    path('documents/<document_id>/translations/new', views.create_document_translation, name='create-document-translation'),
    path('documents/<document_id>/translations/', views.show_document_translations, name='show-document-translations'),
    path('documents/<document_id>/translations/<translation_id>/', views.show_document_translation, name='show-document-translation'),
    # path('documents/<document_id>/translations/<translation_id>', views.show_translation, name='show-translation'),

    # re_path(r'^', include(router.urls)),
    # re_path(r'^', include(documents_router.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns = patterns('',
#     url(r'^', include(router.urls)),
#     url(r'^', include(documents_router.urls)),
# )