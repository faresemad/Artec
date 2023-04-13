from rest_framework_nested.routers import NestedDefaultRouter, DefaultRouter
from .views import CollegeViewSet, CollegeDepartmentViewSet
from exams.views import *
router = DefaultRouter()

router.register(r'', CollegeViewSet, basename="colleges")

college_router = NestedDefaultRouter(router, r'', lookup='colleges')
college_router.register(r'departments', CollegeDepartmentViewSet, basename='colleges-departments')
college_router.register('mcq', McqViewSet, basename='college-mcq')
college_router.register('digital-drawing', DigitalDrawingViewSet, basename='digital-exam')
college_router.register('hand-drawing', HandDrawingViewSet, basename='hand-exam')
college_router.register('practice-drawing', PracticeDrawingViewSet, basename='practic-exam')
urlpatterns = router.urls + college_router.urls