from django.contrib import admin
from django.urls import path, include

from db_app.views import get_table_datas, index, get_db_tablenames, connect

urlpatterns = [
    path('', index),
    path('connect/', connect),
    path('dbs/<str:db_name>/', get_db_tablenames),
    path('<str:db_name>/tables/<str:table_name>/', get_table_datas),
]