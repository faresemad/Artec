from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('mcq', McqViewSet, basename='mcq-exam')
router.register('digital-drawing', DigitalDrawingViewSet, basename='digital-exam')
router.register('hand-drawing', HandDrawingViewSet, basename='hand-exam')
router.register('practice-drawing', PracticeDrawingViewSet, basename='practic-exam')
urlpatterns = router.urls