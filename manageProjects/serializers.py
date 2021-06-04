from django.db import models
from rest_framework import serializers
from .models import Project


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
