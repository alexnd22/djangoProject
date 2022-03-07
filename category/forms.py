from django import forms
from django.forms import TextInput, Textarea, HiddenInput

from category.models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        # fields = '__all__' # formularul se va genera cu toate field-urile modelului Category
        fields = ['name', 'description', 'active']  # specificam ce field-uri din model vrem sa avem in formular
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Please enter category name', 'class': 'form-control'}),
            'description': Textarea(attrs={'placeholder': 'Please enter category description', 'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Your name'
        # self.fields['name'].widget = HiddenInput()

    def clean(self):
        cleaned_data = self.cleaned_data
        name_input = self.cleaned_data.get('name')  # iau textul pe care il scriu in input-ul name
        all_categories = Category.objects.all()  # interogam baza de date luand toate categoriile salvate in db
        for category in all_categories:  # parcurgem prin toate categoriile din db
            if name_input == category.name:
                msg = 'This name already exist in db!'
                self._errors['name'] = self.error_class([msg])

        return cleaned_data


class CategoryFormUpdate(forms.ModelForm):
    class Meta:
        model = Category
        # fields = '__all__' # formularul se va genera cu toate field-urile modelului Category
        fields = ['name', 'description', 'active']  # specificam ce field-uri din model vrem sa avem in formular
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Please enter category name', 'class': 'form-control'}),
            'description': Textarea(attrs={'placeholder': 'Please enter category description', 'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(CategoryFormUpdate, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Your name'
        # self.fields['name'].widget = HiddenInput()
