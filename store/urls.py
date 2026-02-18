from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('products',views.ProductViewSet, basename= 'product')
router.register('collections',views.CollectionViewSet)
router.register('promotions',views.PromotionsViewSet)
router.register('customers', views.CustomerViewSet)
router.register('carts', views.CartViewSet, basename='cart')
router.register('orders', views.OrderViewSet, basename='orders') 

products_router = routers.NestedDefaultRouter(router, 'products', lookup = 'products')
products_router.register('reviews', views.ReviewViewSet, basename= 'products-reviews')
cart_router = routers.NestedDefaultRouter(router, 'carts', lookup = 'cart' )
cart_router.register('items', views.cartItemViewSet, basename= 'cart-items')
urlpatterns = router.urls + products_router.urls + cart_router.urls
