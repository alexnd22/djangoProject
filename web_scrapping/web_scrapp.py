import requests
import bs4
import xlsxwriter
from django.shortcuts import redirect
import datetime


def get_data_web_scrapping(request):
    url = "https://www.emag.ro/laptopuri/c?ref=search_menu_category"
    result = requests.get(url)
    soup = bs4.BeautifulSoup(result.text, 'lxml')
    cases = soup.find_all('div', class_='card-v2')
    context = {'data': []}
    for case in cases:
        data = {}
        product_name = case.find('a', class_='card-v2-title semibold mrg-btm-xxs js-product-url').text
        product_price = case.find('p', class_='product-new-price').text
        price_before_the_discount = case.find('span', class_='rrp-lp30d-content').text
        if product_name is None:
            data['product_name'] = 'Not available'
        else:
            data['product_name'] = product_name
            data['product_price'] = product_price
            data['price_before_the_discount'] = price_before_the_discount

        context['data'].append(data)

    workbook = xlsxwriter.Workbook(f'Laptopuri {datetime.datetime.now().date()}.xlsx')
    worksheet = workbook.add_worksheet('Lista laptopuri')

    row = 0
    col = 0

    for i in context['data']:
        worksheet.write(row, col, i['product_name'])
        worksheet.write(row, col + 1, i['product_price'])
        worksheet.write(row, col + 2, i['price_before_the_discount'])
        row += 1

    workbook.close()
    return redirect('homepage')
