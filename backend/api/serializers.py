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

class CommentReadSerializer(serializers.ModelSerializer):
    author = UserSummarySerializer(read_only=True)    
    
    class Meta:
        model = Comment 
        fields = ["id", "content", "author", "posted_at"]
        

class JobSummarySerializer(serializers.ModelSerializer):
    employer = EmployerSummarySerializer(read_only=True)  
    
    class Meta:
        model = Job
        fields = ["id", "title", "posted_at", "location", "employer"]

class JobDetailSerializer(serializers.ModelSerializer):
    employer = EmployerSummarySerializer(read_only=True)
    comments = CommentReadSerializer(many=True, read_only=True)
    
    class Meta:
        model = Job
        fields = ["id", "title", "description", "posted_at", "location", "employer","comments"]

## ADD COMMENTWRITE, JOBPOST WRITE AND CANDIDATEPROFILE SERIALIZER 
class CommentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["content"]

class JobPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ["title", "description", "location"]