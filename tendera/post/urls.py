from django.urls import path
from . import views
from .views import PostListView, PostDetailView, post_create, post_update, PostDeleteView, UserPostListView, UserDashboard, UserDashboardAds, PaymentView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', PostListView.as_view(), name='post-home'),
    path('<str:order_by>', PostListView.as_view(), name='post-home'),
    # path('<str:order_by>', PostListViewSorted.as_view(), name='post-home-sort'),
 	path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
 	path('user/dashboard/<str:username>', UserDashboard.as_view(), name='user-dashboard'),
    path('user/dashboardads/<str:username>', UserDashboardAds.as_view(), name='user-dashboardads'),
    path('<int:pk>/', PaymentView.as_view(), name='payment'),
    path('payment/<int:pk>/', PostDetailView, name='post-detail'),
    
    path('new/', post_create, name='post-create'),
    path('<int:pk>/update/', post_update, name='post-update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='post-about'),
]