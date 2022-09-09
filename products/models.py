from django.db import models
from django.utils import timezone

class SinglePics (models.Model):
  name = models.CharField(max_length=100)
  image = models.ImageField(upload_to="profile/", blank=False)
  get_image_str = models.CharField(max_length=255, blank=True)
  date_added = models.DateTimeField(default=timezone.now)

  class Meta:
    ordering = ("-date_added",)
    abstract = True

  def get_image(self):
    return "http://127.0.0.1:8000" + self.image.url
  def __str__(self):
    return self.name

class Background (SinglePics):
  image = models.ImageField(upload_to="background/", blank=False)
  class Meta(SinglePics.Meta):
    verbose_name_plural = "background_pics"

# Create your models here.
class Profile (SinglePics):
  class Meta(SinglePics.Meta):
    verbose_name_plural = "profile_pics"

class CommonInfo (models.Model):
  name = models.CharField(max_length=255)
  slug = models.SlugField()
  description = models.TextField(default="")
  price = models.DecimalField(max_digits=6, decimal_places=2)
  image = models.ImageField(upload_to='products/', blank=False)
  thumbnail = models.ImageField(upload_to='products/', blank=True, null=True)
  date_added = models.DateTimeField(auto_now_add=True)
  get_image_str = models.CharField(max_length=255, blank=True)

  def get_image(self):
    return "http://127.0.0.1:8000" + self.image.url

  class Meta:
    ordering = ("name",)
    abstract = True

  def __str__(self):
    return self.name + " : " + self.description

class Product(CommonInfo):
  class Meta(CommonInfo.Meta):
    verbose_name_plural = "Products_galore"

class SelectedProduct (CommonInfo):
  image = models.ImageField(upload_to='selectedProducts/', blank=False)
  class Meta(CommonInfo.Meta):
    verbose_name_plural = "SelecProducts_galore"

class CustomerDetail (models.Model):
  name = models.CharField(max_length=255, blank=False)
  deliveryTime = models.DateTimeField(blank=False)
  mkuStudent = models.BooleanField(blank=False)
  deliveryPoint = models.CharField(max_length=255, blank=False)
  def __str__(self):
    return self.name + "to receive at" + self.deliveryTime + " : " + self.deliveryPoint
  class Meta:
    ordering = ("deliveryTime",)
