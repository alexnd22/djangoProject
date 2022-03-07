from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from category.models import Category
from product.forms import ProductForm
from product.models import Product


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'product/create_product.html'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('list_of_products')
    permission_required = 'product.add_product'


class ProductListView(LoginRequiredMixin, ListView):
    template_name = 'product/list_of_products.html'
    model = Product
    context_object_name = 'all_products'


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'product/update_product.html'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('list_of_products')
    permission_required = 'product.change_product'


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'product/delete_product.html'
    model = Product
    success_url = reverse_lazy('list_of_products')
    permission_required = 'product.delete_product'


def delete_product_with_popup(request, pk):
    current_product = Product.objects.filter(id=pk)
    current_product.delete()
    return redirect('list_of_products')


class ProductDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'product/detail_product.html'
    model = Product
    permission_required = 'product.view_product'


def details_product_with_popup(request, pk):
    current_details_product = Product.objects.get(id=pk)
    return render(request, 'product/list_of_products.html', current_details_product)


@login_required()
def get_products_per_category(request, pk):
    products_per_category = Product.objects.filter(category_id=pk)
    get_category = Category.objects.get(id=pk)
    return render(request, 'product/products_per_category.html',
                  {'products_per_category': products_per_category, 'name_of_category': get_category})
