from .models import Job, Comment, EmployerProfile, CandidateProfile
from django.contrib.auth.models import User
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ["username", "email", "password"]
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class UserSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username"]

class EmployerSummarySerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="owner.username", read_only=True)
    
    class Meta:
        model = EmployerProfile
        fields = ["id", "username", "company_name"]

class JobSummarySerializer(serializers.ModelSerializer):
    employer = EmployerSummarySerializer
    
    class Meta:
        model = Job
        fields = ["id", "title", "posted_at", "location", "employer"]