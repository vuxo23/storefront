from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('products',views.ProductViewSet, basename= 'product')
router.register('collections',views.CollectionViewSet)
router.register('promotions',views.PromotionsViewSet)
router.register('customers', views.CustomerViewSet)
router.register('carts', views.CartViewSet, basename='cart')

products_router = routers.NestedDefaultRouter(router, 'products', lookup = 'products')
products_router.register('reviews', views.ReviewViewSet, basename= 'products-reviews')
urlpatterns = router.urls + products_router.urls
