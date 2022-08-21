from django.urls import path

from .views import CommentView, CommentDetailView

urlpatterns = [
    path('', CommentView.as_view()),
    path('/<id>', CommentDetailView.as_view()),

]