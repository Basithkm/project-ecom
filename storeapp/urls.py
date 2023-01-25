from . import views
from rest_framework import routers



router=routers.DefaultRouter()

router.register('banner',views.BannerViewSet)
router.register('category',views.CategoryViewSet)
router.register('products',views.ProductViewSet)
router.register('cart',views.CartViewSet)

urlpatterns = router.urls
