from . import views
from django.urls import path

# app_name=''
urlpatterns = [


       # path('',views.students,name='form'),
       path('add/', views.person_create_view, name='person_add'),
       path('<int:pk>/', views.person_update_view, name='person_change'),
       path('ajax/load-course/', views.load_course, name='ajax_load_course'),  # AJAX
]

