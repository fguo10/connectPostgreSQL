from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from db_app.db_cls import DB, db_obj


def index(request):
    db_names = db_obj.get_dbs()
    return render(request, 'index.html', context={'db_names': db_names})


def get_db_tablenames(request, db_name):
    try:
        db_obj.use_db(database=db_name)
        table_names = db_obj.get_tables()
    except Exception as e:
        return render(request, 'database.html', context={'db_name': db_name, 'table_names': []})
    return render(request, 'database.html', context={'db_name': db_name, 'table_names': table_names})


def get_table_datas(request, db_name, table_name):
    try:
        db_obj.use_db(database=db_name)
        table_attrs = db_obj.get_table_attrs(table_name=table_name)
        search_attr = request.GET.get('attr')
        search_value = request.GET.get('search')

        if search_attr and search_value:
            table_datas = db_obj.get_filter_table_datas(table_name=table_name,
                                                        attr=search_attr,
                                                        value=search_value
                                                        )
        else:
            table_datas = db_obj.get_table_datas(table_name=table_name)
        datas = []
        for data in table_datas:
            datas.append(dict(zip(table_attrs, data)))
    except Exception as e:
        print("error:", str(e))
        return render(request, 'table.html', context={'table_name': table_name, 'datas': []})
    return render(request, 'table.html', context={
        'db_name': db_name,
        'table_name': table_name,
        'datas': datas})
