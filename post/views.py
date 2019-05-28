from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic import UpdateView, DeleteView, CreateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import RegisterForm  # , ProfileForm
from .models import Profil


class HomeView(TemplateView):
    template_name = "home.html"


def my_admin(request):
    template_name = "post/admin.html"
    users = User.objects.all()
    profiles = Profil.objects.all()
    return render(request, template_name,
                  {'users': users, 'profiles': profiles, })

# the login an logout and register views


def user_register(request):
    # if this is a POST request we need to process the form data
    template = 'auth/register.html'

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                messages.error(request, "Le nom d'utilisateur existe deja !")
                return render(request, template, {
                    'form': form,
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                messages.error(request, "L'email existe deja !")
                return render(request, template, {
                    'form': form,
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                messages.error(
                    request, "Les deux mots de passe ne sont pas identiques !")
                return render(request, template, {
                    'form': form,
                })
            else:
                # Create the user:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.save()

                # redirect to login page:
                return redirect('/unly/login/')

   # No post data availabe, let's just show the page.
    else:
        form = RegisterForm()

    return render(request, template, {'form': form})


def user_login(request):
    if request.POST:
        email = request.POST.get('email')
        password = request.POST.get('password')
        # retrieve the username according to the given email
        supposed_user = User.objects.filter(email=email)[0]
        username = supposed_user.username
        user = authenticate(username=username, password=password)
        if user:  # and user.is_staff for admin user
            if user.is_active:
                login(request, user)
                # return render(request, settings.LOGIN_REDIRECT_URL, {})
                if request.POST.get('next') is not '':
                    return redirect(request.POST.get('next'))
                else:
                    return redirect('/unly/')
            # the else statement
            return HttpResponse("You're account is disabled.")
        # the else statement
        messages.add_message(request, messages.WARNING, 'Credentials invalid')
    return render(request, 'auth/login.html', locals())


class LogoutView(TemplateView):
    template_name = 'auth/login.html'  # wish to change it with home.html

    def get(self, request, **kwargs):
        logout(request)
        return render(request, self.template_name)


class UserList(ListView):
    model = User
    template_name = 'post/user/user_list.html'
    context_object_name = 'users'


class UserDetail(DetailView):
    model = User
    template_name = 'post/users/user_detail.html'
    context_object_name = 'user'


class UserCreate(CreateView):
    model = User
    template_name = 'post/users/user_new_edit.html'
    fields = ['username', 'email', 'password', 'is_staff']
    success_url = reverse_lazy('my_admin')


class UserUpdate(UpdateView):
    model = User
    template_name = 'post/users/user_new_edit.html'
    fields = ['username', 'email', 'password', 'is_staff']
    success_url = reverse_lazy('my_admin')


class UserDelete(DeleteView):
    model = User
    template_name = 'post/users/user_delete.html'
    success_url = reverse_lazy('my_admin')
    context_object_name = 'user'


class ProfileDetail(DetailView):
    model = Profil
    template_name = 'post/profile/profile_detail.html'
    context_object_name = 'profile'


class ProfileCreate(CreateView):
    model = Profil
    template_name = 'post/profile/profile_new_edit.html'
    fields = '__all__'
    success_url = reverse_lazy('my_admin')
