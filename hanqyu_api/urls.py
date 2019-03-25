from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

import hanqyu_api.api_test.api

app_name='api_test'

router = routers.DefaultRouter()
router.register('api_tests', hanqyu_api.api_test.api.TestViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/doc', get_swagger_view(title='Rest API Document')),
    url(r'^api/v1/', include((router.urls, 'api_test'), namespace='api')),
]
