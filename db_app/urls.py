from django.contrib import admin
from django.urls import path, include

from db_app.views import get_table_datas, index, get_db_tablenames

urlpatterns = [
    path('', index),
    path('dbs/<str:db_name>/', get_db_tablenames),
    path('<str:db_name>/tables/<str:table_name>/', get_table_datas),
]