from django.urls import path
from . import views

urlpatterns = [
    # Қауіпсіз форма (CSRF + XSS тәжірибесі)
    path('comments/', views.comment_view, name='comment_list'),

    # CSRF жоқ форма (403 тәжірибесі үшін)
    path('no-csrf/', views.no_csrf_view, name='no_csrf'),
]
