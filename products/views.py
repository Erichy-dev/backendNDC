from django.views.generic import ListView, DetailView
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect
from .models import Product, Profile, SelectedProduct, Background

import json

# Create your views here.
class IndexView(View):
  def get(self, request):
    return render(request, "index.html")

class BackgroundView(ListView):
  def get(self, request):
    background = Background.objects.all()[:1]
    for prod in background:
      prod.get_image_str = prod.get_image()
    data = serializers.serialize("json", background)
    return HttpResponse(data)

class ProductsView(ListView):
  def get(self, request):
    products = Product.objects.all()
    # alter the value of "get_image_str" for every model object
    for prod in products:
      prod.get_image_str = prod.get_image()
    data = serializers.serialize("json", products)
    return HttpResponse(data)

class ProfileView(ListView):
  def get(self, request):
    profile = Profile.objects.all()[:1]
    for prod in profile:
      prod.get_image_str = prod.get_image()
    prof = serializers.serialize("json", profile)
    return HttpResponse(prof)

class SelectedProductsView(ListView):
  def get(self, request):
    params = request.GET
    paramsCopy = params.copy()
    param = paramsCopy.pop('selected')
    products = Product.objects.filter(slug__in=param)
    for prod in products:
      prod.get_image_str = prod.get_image()
    prof = serializers.serialize("json", products)
    return HttpResponse(prof)

@require_POST
# @csrf_protect
def confirmSelection(request):
  products = json.loads(request.body)
  for prod in products:
    pp = SelectedProduct()
    fields = prod['fields']
    pp.name = fields["name"]
    pp.slug = fields["slug"]
    pp.price = fields["price"]
    pp.image = fields["image"]
    pp.description = fields["description"]
    pp.thumbnail = fields["thumbnail"]
    pp.save()

  return HttpResponse("params")

class ThankYou (ListView):
  def get(self, request):
    return HttpResponse("Thank You For Choosing US")
