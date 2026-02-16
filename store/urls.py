from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('products',views.ProductViewSet, basename= 'products')
router.register('collections',views.CollectionViewSet)
router.register('promotions',views.PromotionsViewSet)
router.register('customers', views.CustomerViewSet)
router.register('cartItem', views.CartItemViewSet, basename='cartItem')

products_router = routers.NestedDefaultRouter(router, 'products', lookup = 'product')
products_router.register('reviews', views.ReviewViewSet, basename= 'products-reviews')
cartItem_router = routers.NestedDefaultRouter(router, 'cartItem', lookup = 'cart')
cartItem_router.register('cart', views.CartItemViewSet, basename='cartItem-ids')
urlpatterns = router.urls + products_router.urls + cartItem_router.urls
