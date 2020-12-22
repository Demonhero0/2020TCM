from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework.authtoken import views
from rest_framework.schemas import get_schema_view
from project.main.views.utils import UtilsViewSet, descriptionView
from project.main.views.users import UserViewSet
from project.main.views.students import StudentViewSet
from project.main.views.doctor import CheckViewSet,DiseaseViewSet,MedicineViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'', UtilsViewSet, basename="utils")
router.register(r'diseases', DiseaseViewSet, basename="disease")
router.register(r'medicines', MedicineViewSet, basename='medicine')
# router.register(r'users', UserViewSet, basename='user')
# router.register(r'students',StudentViewSet,basename='student')

urlpatterns = [
    path('', include(router.urls)),
    path('openapi', get_schema_view(
        title="DRF-Starter",
        description="API for DRF-Starter"
    ), name='openapi-schema'),
    path('docs/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
    path('check',CheckViewSet.as_view(),name='check')
]
