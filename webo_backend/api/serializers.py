from rest_framework import serializers
from webo_app.models import ResearchPaperDetail, ResearchField


class ResearchPaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchPaperDetail
        fields = "__all__"


class ResearchFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchField
        fields = "__all__"
