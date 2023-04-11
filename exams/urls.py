from rest_framework_nested.routers import NestedDefaultRouter, DefaultRouter
from colleges.views import CollegeViewSet
from .views import *

router = DefaultRouter()
router.register('college', CollegeViewSet, basename='college-mcq')

exam_router = NestedDefaultRouter(router, 'college', lookup='college')
exam_router.register('mcq', McqViewSet, basename='college-mcq')
exam_router.register('digital-drawing', DigitalDrawingViewSet, basename='digital-exam')
exam_router.register('hand-drawing', HandDrawingViewSet, basename='hand-exam')
exam_router.register('practice-drawing', PracticeDrawingViewSet, basename='practic-exam')

urlpatterns = router.urls + exam_router.urls 