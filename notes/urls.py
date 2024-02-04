from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'note'

urlpatterns = [
    path('',  views.note_list, name='note_list'),
    path('create/',  views.create_note, name='create_note'),
    path('about/', views.about, name='about'),
    path('<int:note_id>/', views.note_detail, name='note_detail'),
    # path('create_note/', views.create_note, name='create_note'),
    # path('search_note/', views.search_note, name='search_note'),

]

