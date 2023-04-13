from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, McqAnswerViewSet, HandDrawingAnswerViewSet, DigitalDrawingAnswerViewSet, PracticeDrawingAnswerViewSet

router = DefaultRouter()
router.register(r'list', StudentViewSet, basename='students')
router.register(r'mcq', McqAnswerViewSet, basename='mcqAnswer')
router.register(r'hand-drawing', HandDrawingAnswerViewSet, basename='hand-drawingAnswer')
router.register(r'digital-art', DigitalDrawingAnswerViewSet, basename='digital-drawingAnswer')
router.register(r'practice-drawing', PracticeDrawingAnswerViewSet, basename='practice-drawingAnswer')
urlpatterns = router.urls