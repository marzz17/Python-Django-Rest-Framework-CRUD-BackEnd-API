from rest_framework import routers, serializers, viewsets
from .models import Employeeleave

class employeeleave_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employeeleave
        fields = ('first_name', 'last_name', 'Reason','leave_date')