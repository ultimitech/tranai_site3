from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from .models import Translation, Document
from .forms import DocumentForm, TranslationForm
# from rest_framework import viewsets
# import sys

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

###############################################################################
# Document
###############################################################################
# class DocumentViewSet(viewsets.ModelViewSet):
#   serializer_class = DocumentSerializer
#   permission_classes = (permissions.IsAuthenticated, AccountPermission)
#   def get_queryset(self):
#     queryset = Document.objects.all()
#     return Document.objects.filter(document=self.kwargs['document_pk'])

def index_documents(request):
  document_list = Document.objects.all().order_by('title')#sort by date instead of title
  return render(request, 'tranai/index_documents.html', {'document_list': document_list})

def show_document(request, document_id):
  document = Document.objects.get(pk=document_id)
  translations = document.translations
  # print (sys.stderr, translations)
  return render(request, 'tranai/show_document.html', {'document': document, 'translations': translations})

def create_document(request):
  if request.method == 'POST':
    form = DocumentForm(request.POST)
    if form.is_valid():
      try:
        document = form.save()
        model = form.instance
        # return redirect('index-documents')
        return redirect(f'/documents/{document.id}/')
      except:
        pass
    # print('post')
    # return HttpResponse("<a class='dropdown-item' href='#'>Translations</a>")
  elif request.method == 'GET':
    form = DocumentForm()
    # print('get')
    return render(request, 'tranai/create_document.html', {'form': form})

# def update_document(request, document_id):
#   document = Document.objects.get(pk=document_id)
#   form = DocumentForm(request.POST or None, instance=document)
#   if form.is_valid():
#     form.save()
#     return redirect('index-documents')
#   return render(request, 'tranai/update_document.html', {'document': document, 'form': form})

def update_document(request, document_id):
  document = Document.objects.get(pk=document_id)
  form = DocumentForm(initial={'dod': document.dod, 'tod': document.tod, 'dow': document.dow, 'title': document.title, 'descriptor': document.descriptor})
  if request.method == 'POST':
    form = DocumentForm(request.POST, instance=document)
    if form.is_valid():
      try:
        form.save()
        model = form.instance
        print('Document id=' + document_id + ' updated successfully')
        return redirect(f'/documents/{document_id}/')
      except Exception as e:
        print('Document update failure: ' + e)
        pass
    else:
      print('form is not valid')
  elif request.method == 'GET':
    form = DocumentForm(initial={'dod': document.dod, 'tod': document.tod, 'dow': document.dow, 'descriptor': document.descriptor, 'title': document.title })
    return render(request, 'tranai/update_document.html', {'document': document, 'form': form})

# def delete_document(request, document_id):
#   document = Document.objects.get(pk=document_id)
#   document.delete()
#   return redirect('index-documents')

# def destroy_document(request, document_id):
#   document = Document.objects.get(pk=document_id)
#   document.delete()
#   return render(request, 'tranai/show_document.html', {'document': document})

def delete_document(request, document_id):
  document = Document.objects.get(pk=document_id)
  try:
    document.delete()
    print('Document delete success')
  except Exception as e:
    print('Document delete failure: ' + e)
    pass
  return redirect('index-documents')
  # return redirect(f'/documents/')

###############################################################################
# Translation
###############################################################################

# class TranslationViewSet(viewsets.ModelViewSet):
#   serializer_class = TranslationSerializer
#   permission_classes = (permissions.IsAuthenticated, AccountPermission)
#   def get_queryset(self):
#     # return Translation.objects.filter(translation=self.kwargs['translation_pk'])
#     return Translation.objects.filter(translation=self.kwargs['pk'])

def index_all_translations(request):
  translation_list = Translation.objects.all()
  return render(request, 'tranai/index_all_translations.html', {'translation_list': translation_list})

def index_translations(request):
  translation_list = Translation.objects.all()
  return render(request, 'tranai/all_translations.html', {'translation_list': translation_list})

def show_translation(request, translation_id):
  translation = Translation.objects.get(pk=translation_id)
  document = translation.document
  return render(request, 'tranai/show_document_translation.html', {'document': document, 'translation': translation})

def create_translation(request):
  if request.method == 'POST':
    form = TranslationForm(request.POST)
    if form.is_valid():
      try:
        form.save()
        model = form.instance
        return redirect('index-all-translations')
      except:
        pass
    # print('post')
    # return HttpResponse("<a class='dropdown-item' href='#'>Translations</a>")
  elif request.method == 'GET':
    form = TranslationForm()
    # print('get')
    return render(request, 'tranai/add_translation.html', {'form': form})


def show_document_translation(request, document_id, translation_id):
  # return redirect('/')
  # return HttpResponse("<a class='dropdown-item' href='#'>Translations</a>")
  # return redirect('show')
  document = Document.objects.get(pk=document_id)
  translation = Translation.objects.get(pk=translation_id)
  return render(request, 'tranai/show_document_translation.html', {'document': document, 'translation': translation})

def show_document_translations(request, document_id):
  document = Document.objects.get(pk=document_id)
  translations = document.translations.all
  # return redirect('/')
  return render(request, 'tranai/show_document.html', {'document': document, 'translations': translations})

def create_document_translation(request, document_id):
  if request.method == 'POST':
    form = TranslationForm(request.POST)
    if form.is_valid():
      try:
        # form.save()
        translation = form.save()
        document = Document.objects.get(pk=document_id)
        # translation = Translation.objects.get(pk=translation_id)
        translation = Translation.objects.get(pk=translation.id)
        translation.document_id = document_id
        translation.save()
        # model = form.instance
        # return redirect('index-translations')
        # document
        return render(request, 'tranai/show_document.html', {'document': document})
      except:
        pass
    # print('post')
    # return HttpResponse("<a class='dropdown-item' href='#'>Translations</a>")
  elif request.method == 'GET':
    form = TranslationForm()
    # print('get')
    return render(request, 'tranai/create_document_translation.html', {'form': form})

def update_document_translation(request, document_id, translation_id):
  translation = Translation.objects.get(pk=translation_id)
  document = Document.objects.get(pk=document_id)
  form = TranslationForm(initial={'lan': translation.lan, 'tran_title': translation.tran_title, 'eng_tran': translation.eng_tran, 'descrip': translation.descrip, 'blkc': translation.blkc, 'subc': translation.subc, 'senc': translation.senc, 'xcrip': translation.xcrip, 'li': translation.li, 'pubdate': translation.pubdate, 'version': translation.version })
  if request.method == 'POST':
    form = TranslationForm(request.POST, instance=translation)
    if form.is_valid():
      try:
        form.save()
        model = form.instance
        print('Translation id=' + translation_id + ' updated successfully')
        # return redirect(f'/documents/{document_id}/translations/{translation_id}/')
        return redirect(f'/documents/{document_id}/')
        # return render(request, 'tranai/show_document_translation.html', {'document': document, 'translation': translation})
        # return redirect('index-translations')
      except Exception as e:
        # print('Translation update failure: ' + e)
        pass
    else:
      print('form is not valid')  
  elif request.method == 'GET':
    form = TranslationForm(initial={'lan': translation.lan, 'tran_title': translation.tran_title, 'eng_tran': translation.eng_tran, 'descrip': translation.descrip, 'blkc': translation.blkc, 'subc': translation.subc, 'senc': translation.senc, 'xcrip': translation.xcrip, 'li': translation.li, 'pubdate': translation.pubdate, 'version': translation.version })
    return render(request, 'tranai/update_document_translation.html', {'document': document, 'translation': translation, 'form': form})

def delete_document_translation(request, document_id, translation_id):
  translation = Translation.objects.get(pk=translation_id)
  document = Document.objects.get(pk=document_id)
  try:
    translation.delete()
    print('Translation delete success')
  except Exception as e:
    print('Translation delete failure: ' + e)
  # return redirect(f'/documents/{document_id}/translations/')
  return redirect(f'/documents/{document_id}/')

###############################################################################
# Task
###############################################################################

