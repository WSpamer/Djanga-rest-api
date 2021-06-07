from django.db import models
from rest_framework import serializers
from .models import Project, Measurement, Section


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "pk",
            "name",
            "companyName",
            "site",
            "areaManager",
            "designType",
            "sections",
            "lowMaintananceCheck",
            "folderUrl",
            "infoUrl",
        ]
        extra_kwargs = {
            "lowMaintananceCheck": {"required": False},
        }


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = [
            "pk",
            "blockArea",
            "blockOmtrek",
            "blockLengte",
            "blockBreedte",
            "blockRy",
            "blockDwars",
            "blockHoeke",
            "blockHeight",
        ]


class SectionSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    measurement = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Section
        fields = [
            "pk",
            "project",
            "measurement",
        ]
