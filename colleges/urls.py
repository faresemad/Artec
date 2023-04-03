from rest_framework.routers import SimpleRouter
from .views import CollegeViewSet

router = SimpleRouter()
router.register(r'', CollegeViewSet, basename="colleges")
router.register(r'(?P<college_pk>\d+)', CollegeViewSet, basename="collegesDetails")
# router.register(r'(?P<college_pk>\d+)/departments', CollegeDepartmentViewSet, basename="collegesDepartments")
# router.register(r'(?P<college_pk>\d+)/departments/(?P<department_pk>\d+)', CollegeDepartmentViewSet, basename="collegesDepartmentsDetails")
urlpatterns = router.urls