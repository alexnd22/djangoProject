import xlrd
from django.shortcuts import redirect

from category.models import Category


def update_excel_category(request):
    update_categories = xlrd.open_workbook('category/All_categories.xls')
    sheet = update_categories.sheet_by_name('Sheet2')

    col = 0
    for row in range(1, sheet.nrows):
        get_id = int(sheet.cell(row, col).value)
        get_name = sheet.cell(row, col + 1).value
        get_description = sheet.cell(row, col + 2).value
        Category.objects.filter(id=get_id).update(name=get_name, description=get_description)

    return redirect('list_of_categories')
