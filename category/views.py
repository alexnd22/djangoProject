from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from category.filters import CategoryFilter
from category.forms import CategoryForm, CategoryFormUpdate
from category.models import Category


# TemplateView, CreateView, ListView
class CategoryCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'category/create_category.html'  # template-ul unde va fi randat formularul
    model = Category  # modelul pe care il folosim pentru a randa formularul si a salva datele
    form_class = CategoryForm
    success_url = reverse_lazy('list_of_categories')  # dupa salvarea formularului vom fi redirectionati
    # pe pagina de home sau dupa caz list of categories
    permission_required = 'category.add_category'


class CategoryListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'category/list_of_categories.html'
    model = Category
    context_object_name = 'all_categories'
    permission_required = 'category.view_category'

    def get_context_data(self, **kwargs):
        data = super(CategoryListView, self).get_context_data(**kwargs)
        all_categories = Category.objects.all()
        my_filter = CategoryFilter(self.request.GET, queryset=all_categories)
        all_categories = my_filter.qs
        data['all_categories'] = all_categories
        data['filters'] = my_filter
        return data


class CategoryUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'category/update_category.html'
    model = Category
    form_class = CategoryFormUpdate
    success_url = reverse_lazy('list_of_categories')
    permission_required = 'category.change_category'


# UPDATEVIEW()
# 1. VIEWS.PY- veti crea clasa CategoryUpdateView impreuna cu (template_name, model, form_class, success_url)
# 2. In templates veti crea fisierul html, unde veti avea formularul pentru a va actuliza informatiile
# despre categoria respectiva
# 3 in URLS.PY veti defini url pentru clasa creata din views.py.

class CategoryDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'category/delete_category.html'
    model = Category
    success_url = reverse_lazy('list_of_categories')
    permission_required = 'category.delete_category'


@login_required()
@permission_required('category.delete_category_by_popup')
def delete_category_with_popup(request, pk):
    current_category = Category.objects.filter(id=pk)
    current_category.delete()
    return redirect('list_of_categories')


class CategoryDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'category/detail_category.html'
    model = Category
    permission_required = 'category.view_category'


@login_required()
@permission_required('category.detail_category_by_popup')
def details_category_with_popup(request, pk):
    current_details_category = Category.objects.get(id=pk)
    return render(request, 'category/list_of_categories.html', current_details_category)

# ListView - afisati toate datele din tabela repectiva intr-un fisier HTML
# CreateView - adaugam si salvam o inregistrare in tabela respectiva bazat pe un formular
# UpdateView - actualizam datele unei inregistrari salvate in tabela noastra
# DeleteView - stergem o inregistrare din tabela respectiva
# DetailView - afisam detaliile din tabela respectiva
