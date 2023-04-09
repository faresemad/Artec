from rest_framework.routers import SimpleRouter
from .views import StudentViewSet, McqAnswerViewSet, HandDrawingAnswerViewSet, DigitalDrawingAnswerViewSet, PracticeDrawingAnswerViewSet

router = SimpleRouter()
router.register(r'students', StudentViewSet)
router.register(r'mcq', McqAnswerViewSet)
router.register(r'hand-drawing', HandDrawingAnswerViewSet)
router.register(r'digital-art', DigitalDrawingAnswerViewSet)
router.register(r'practice-drawing', PracticeDrawingAnswerViewSet)
urlpatterns = router.urls