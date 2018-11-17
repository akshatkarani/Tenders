from django.urls import path
from . import views
from .views import AdvertListView, AdvertDetailView, AdvertDeleteView, advert_create, advert_update
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', AdvertListView.as_view(), name='advert-home'),
    path('<str:order_by>', AdvertListView.as_view(), name='advert-home'),
    path('new/', advert_create, name='advert-create'),
    path('<int:pk>/', AdvertDetailView.as_view(), name='advert-detail'),
    path('<int:pk>/update/', advert_update, name='advert-update'),
    path('<int:pk>/delete/', AdvertDeleteView.as_view(), name='advert-delete'),
    path('about/', views.about, name='advert-about'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)