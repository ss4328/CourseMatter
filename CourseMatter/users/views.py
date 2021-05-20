from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


# Create your views here.


def dashboard(request):
    return render(request, "users/userDashboard.html")


# def register(request):
#     if request.method == "GET":
#         return render(
#             request, "users/register.html",
#             {"form": CustomUserCreationForm}
#         )
#     elif request.method == "POST":
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect(reverse("dashboard"))

# def register(generic.CreateView):
#     form_class = SignUpForm
#     template_name = 'registration/edit_profile.html'
#     success_url = reverse_lazy('home')


class UserRegisterView(generic.CreateView):
    # form_class = UserCreationForm
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.CreateView):
    form_class = UserChangeForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')
