from django.urls import include, path
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken import views
from project.main.views.utils import UtilsViewSet, descriptionView
from project.main.views.users import UserViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'', UtilsViewSet, basename="utils")
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('docs/', include_docs_urls(title='API docs')),
    path('description/', descriptionView)
]