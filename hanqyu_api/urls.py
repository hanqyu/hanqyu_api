from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from django.contrib.staticfiles.urls import static
from . import settings, api_test.api

app_name='api_test'

router = routers.DefaultRouter()
router.register('api_tests', api_test.api.TestViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/doc', get_swagger_view(title='Rest API Document')),
    url(r'^api/v1/', include((router.urls, 'api_test'), namespace='api')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
