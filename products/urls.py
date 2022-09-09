from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "products"
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path("background/", views.BackgroundView.as_view()),
    path("profile/", views.ProfileView.as_view()),
    path("products/", views.ProductsView.as_view()),
    path("selectedProducts/", views.SelectedProductsView.as_view()),
    path("confirmSelection/", views.confirmSelection, name = "confirmSelection"),
    path("thankYou/", views.ThankYou.as_view(), name = "thankYou"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
