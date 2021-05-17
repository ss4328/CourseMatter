from django.conf.urls import include, url
# from .views import dashboard, register, UserEditView
from .views import UserRegisterView, UserEditView, dashboard

urlpatterns = [
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^dashboard/", dashboard, name="dashboard"),
    # url(r"^register/", register, name="register"),
    url(r"^edit_profile/", UserEditView.as_view(), name="edit_profile"),
    url(r"^register/", UserRegisterView.as_view(), name="register"),
]