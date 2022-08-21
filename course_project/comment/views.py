from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from .models import Comment
from .serializers import CommentSerializer


class CommentView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get(self, request, *args, **kwargs):
        product = request.GET.get('product')
        if product:
            self.queryset = Comment.objects.filter(product=product)
        return self.list(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        user = request.GET.get('user')
        if user:
            self.queryset = Comment.objects.filter(user=user)
        return self.list(request, *args, **kwargs)


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
