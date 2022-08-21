from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from cart.models import Cart
from cart.serializers import CartSerializer


class CartView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartDetailView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
