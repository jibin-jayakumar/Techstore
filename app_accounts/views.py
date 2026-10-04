from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import RegisterForm


def register_view(request):
    if request.user.is_authenticated:
        return redirect('app_accounts:profile')
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('app_accounts:profile')
    return render(request, 'app_accounts/register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'app_accounts/login.html'
    redirect_authenticated_user = True


def logout_view(request):
    logout(request)
    return redirect('app_store:home')


@login_required
def profile_view(request):
    return render(request, 'app_accounts/profile.html', {'user': request.user})