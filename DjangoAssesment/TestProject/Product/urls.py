from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("/test-api", views.testProduct),
    path("/create-new-product", views.createNewProduct),
    path("/get-all-products-w-images", views.getAllProductsWImages),
    path("/create-new-product-image", views.createNewProductsWithImages),
    path("/add-product-to-cart/<int:unique_id>/<int:user_id>", views.addProductToCart),
    path("/test-upload-image", views.testUploadImage),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
