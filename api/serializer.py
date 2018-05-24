from rest_framework import serializers

from codelab.models import Codelab


class CodelabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Codelab
        fields = '__all__'
