from django.urls import path

from .views import UserView, UserDetailView

urlpatterns = [
    path('', UserView.as_view()),
    path('/<id>', UserDetailView.as_view())
]
