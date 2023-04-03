from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()
router.register('mcq', McqViewSet)
router.register('digital-drawing', DigitalDrawingViewSet)
router.register('hand-drawing', HandDrawingViewSet)
router.register('practice-drawing', PracticeDrawingViewSet)
urlpatterns = router.urls