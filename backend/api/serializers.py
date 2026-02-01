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

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"