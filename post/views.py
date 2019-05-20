from django.shortcuts import render
from django.views.generic import TemplateView

from django.contrib.auth.models import User


class HomeView(TemplateView):
    template_name = "home.html"

# the login an logout views


def user_login(request):
    if request.POST:
        email = request.POST.get('email')
        password = request.POST.get('password')
        # retrieve the username according to the given email
        supposed_user = User.objects.filter(email=email)
        username = supposed_user.username
        user = authenticate(username=username, password=password)
        if user and user.is_staff:
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
