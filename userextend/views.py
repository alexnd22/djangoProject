from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from userextend.forms import UserExtendForm
from userextend.models import UserExtend


class UserExtendCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = UserExtend
    form_class = UserExtendForm
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        if form.is_valid() and not form.errors:
            user = form.save(commit=False)
            user.save()
            get_group = Group.objects.get(name='client')
            get_group.user_set.add(user.id)
            # send_mail()

        return redirect('login')
