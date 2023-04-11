from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, McqAnswerViewSet, HandDrawingAnswerViewSet, DigitalDrawingAnswerViewSet, PracticeDrawingAnswerViewSet

router = DefaultRouter()
router.register(r'list', StudentViewSet)
router.register(r'mcq', McqAnswerViewSet)
router.register(r'hand-drawing', HandDrawingAnswerViewSet)
router.register(r'digital-art', DigitalDrawingAnswerViewSet)
router.register(r'practice-drawing', PracticeDrawingAnswerViewSet)
urlpatterns = router.urls