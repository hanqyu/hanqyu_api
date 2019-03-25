from .models import Test
from rest_framework import serializers, viewsets

class TestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Test
        fields = '__all__'

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
