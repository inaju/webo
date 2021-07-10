from rest_framework import serializers
from webo_app.models import ResearchPaperDetail


class ResearchPaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchPaperDetail
        fields = "__all__"
