from rest_framework.routers import SimpleRouter
from .views import AboutViewSet

router = SimpleRouter()
router.register(r'about', AboutViewSet, basename='about')
router.register(r'about/(?P<college_pk>\d+)', AboutViewSet, basename='about-detail')
urlpatterns = router.urls