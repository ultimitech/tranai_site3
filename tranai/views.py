from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Translation, Document, TranslationSerializer
from .forms import DocumentForm
from rest_framework import viewsets
# import sys

class DocumentViewSet(viewsets.ModelViewSet):
  # serializer_class = DocumentSerializer
  # permission_classes = (permissions.IsAuthenticated, AccountPermission)

  def get_queryset(self):
    # queryset = Document.objects.all()
    return Document.objects.filter(document=self.kwargs['document_pk'])

class TranslationViewSet(viewsets.ModelViewSet):
  serializer_class = TranslationSerializer
  # permission_classes = (permissions.IsAuthenticated, AccountPermission)

  def get_queryset(self):
    # return Translation.objects.filter(translation=self.kwargs['translation_pk'])
    return Translation.objects.filter(translation=self.kwargs['pk'])

def show_translation(request, document_id, translation_id):
  document = Document.objects.get(pk=document_id)
  translation = Translation.objects.get(pk=translation_id)
  return render(request, 'tranai/show_translation.html', {'document': document, 'translation': translation})

def update_document(request, document_id):
  document = Document.objects.get(pk=document_id)
  return render(request, 'tranai/show_document.html', {'document': document})

def show_document(request, document_id):
  document = Document.objects.get(pk=document_id)
  translations = document.translations
  # print (sys.stderr, translations)
  return render(request, 'tranai/show_document.html', {'document': document, 'translations': translations})

def index_documents(request):
  document_list = Document.objects.all()
  return render(request, 'tranai/document.html', {'document_list': document_list})

def create_document(request):
  submitted = False
  if request.method == 'POST':
    form = DocumentForm(request.POST)
    # validation
    if form.is_valid():
      form.save()
      return  HttpResponseRedirect('/add_document?submitted=True')
  else:
    form = DocumentForm
    if 'submitted' in request.GET:
        submitted = True
  return render(request, 'tranai/add_document.html', {'form': form, 'submitted': submitted})

def all_translations(request):
  translation_list = Translation.objects.all()
  return render(request, 'tranai/translation_list.html', {'translation_list': translation_list})

def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
  name = 'John'
  month = month.capitalize()
  # conver month from naem to number
  month_number = list(calendar.month_name).index(month)
  month_number = int(month_number)
  # 
  cal = HTMLCalendar().formatmonth(year, month_number)
  # get current year
  now = datetime.now()
  current_year = now.year

  return render(request, 'tranai/home.html', {
    'name': name,
    'year': year,
    'month': month,
    'month_number': month_number,
    'cal': cal,
    'current_year': current_year,
  })