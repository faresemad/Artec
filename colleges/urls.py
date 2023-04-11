from rest_framework_nested.routers import NestedDefaultRouter, DefaultRouter
from .views import CollegeViewSet, CollegeDepartmentViewSet

router = DefaultRouter()

router.register(r'', CollegeViewSet, basename="colleges")

college_router = NestedDefaultRouter(router, r'', lookup='colleges')
college_router.register(r'departments', CollegeDepartmentViewSet, basename='colleges-departments')

urlpatterns = router.urls + college_router.urls