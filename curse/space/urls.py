from django.urls import path, include
from . import views
from .views import PostListView, PostDetailView, PostCreateView
from users import views as users_views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

router = routers.DefaultRouter()
router.register('reviews', views.PostView)

urlpatterns = [
	path('', views.main, name='space-main'),
	path('history/', views.history, name='space-history'),
	path('records/', views.records, name='space-records'),
	path('graph/', views.graph, name='space-graph'),
	path('comments/', PostListView.as_view(), name='space-comments'),
	# path('comments/post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
	path('comments/post/new/', PostCreateView.as_view(), name='post-create'),
	path('register/', users_views.register, name='space-register'),
	path('', include(router.urls))
]

