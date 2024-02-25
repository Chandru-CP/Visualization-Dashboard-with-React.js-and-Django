from rest_framework import serializers
from .models import Analysis, Impact

class AnalysisSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='name')

    class Meta:
        model = Analysis
        fields = ['title', 'likelihood', 'impact', 'relevance']

