import sqlite3

import xlrd as xlrd

# Deschidem fisierul excel
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect

from category.models import Category


@login_required()
@permission_required('category.import_data')
def import_data(request):
    open_by_excel_category = xlrd.open_workbook('category/All_categories.xls')
    sheet = open_by_excel_category.sheet_by_name('Sheet1')

    database = sqlite3.connect('../db.sqlite3')

    for row in range(1, sheet.nrows):
        get_name = str(sheet.cell(row, 0).value)
        get_description = str(sheet.cell(row, 1).value)
        get_active = bool(sheet.cell(row, 2).value)

        # new_category = Category()
        # new_category.name = get_name
        # new_category.description = get_description
        # new_category.active = get_active
        # new_category.save()

        Category.objects.create(name=get_name,
                                description=get_description,
                                active=get_active)

    return redirect('list_of_categories')
