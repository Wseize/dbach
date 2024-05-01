from django.urls import path
from . import views


urlpatterns = [
    path('product-image/', views.ProductImageViewSet.as_view(({'get': 'list', 'post': 'create'}), name='gallery-image-list')),
    path('product-image/<int:pk>/', views.ProductImageViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='gallery-image-detail'),
    path('gallery/', views.ProductGalleryViewSet.as_view(({'get': 'list', 'post': 'create'}), name='gallery-image-list')),
    path('gallery/<int:pk>/', views.ProductGalleryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='gallery-image-detail'),
    path('categories/', views.CategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='category-list'),
    path('categories/<int:pk>/', views.CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='category-detail'),
    path('message/', views.SendMessageViewSet.as_view({'get': 'list','post': 'create'}), name='message'),
    path('messageList/', views.SendMessageListViewSet.as_view({'get': 'list','post': 'create'}), name='message'),
    path('logo/', views.LogoViewSet.as_view(({'get': 'list', 'post': 'create'}), name='logo-list')),
    path('logo/<int:pk>/', views.LogoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='logo-detail'),


    path('orders/', views.OrderViewSet.as_view({'get': 'list', 'post': 'create'}), name='order-list'),
    path('orders/<int:pk>/', views.OrderViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='order-detail'),

    path('ordered-products/', views.OrderedProductViewSet.as_view({'get': 'list', 'post': 'create'}), name='orderedproduct-list'),
    path('ordered-products/<int:pk>/', views.OrderedProductViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='orderedproduct-detail'),

    path('pub/', views.PubViewSet.as_view(({'get': 'list', 'post': 'create'}), name='pub-image-list')),
    path('pub/<int:pk>/', views.PubViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='pub-image-detail'),

]