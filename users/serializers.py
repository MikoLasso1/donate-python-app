from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import CustomUser, Feedback
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, authenticate
from django.conf import settings
from allauth.account.adapter import get_adapter
from rest_framework.response import Response
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm

UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    username = None
    # profile_pic = serializers.ImageField(required=False)
    dob = serializers.DateField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    address = serializers.CharField(required=False)
    masjid_id = serializers.IntegerField(required=False)
    gender = serializers.ChoiceField(
        choices=['male', 'female', 'transgender'],
        style={'base_template': 'radio.html'},
        required=False,
    )
    phone = serializers.CharField(
        max_length=100,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())],
        required=True
    )
    email = serializers.EmailField(
        max_length=100,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())],
        required=True
    )
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'dob', 'address', 'masjid_id','gender']



class RegisterUserSerializer(serializers.ModelSerializer):
    dob = serializers.DateField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    address = serializers.CharField(required=False)
    masjid_id = serializers.IntegerField(required=False)
    gender = serializers.ChoiceField(
        choices=['male', 'female', 'transgender'],
        style={'base_template': 'radio.html'},
        required=False,
    )
    phone = serializers.CharField(
        max_length=100,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())],
        required=False
    )
    email = serializers.EmailField(
        max_length=100,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())],
        required=False
    )
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'dob', 'address', 'masjid_id','gender','password']

        def create(self, validated_data):
            user = User.objects.create(
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
                email=validated_data['email'],
                phone=validated_data['phone'],
                dob=validated_data['dob'],
                address=validated_data['address'],
                masjid_name=validated_data['masjid_id'],
                unl_gender=validated_data['unl_gender'],
                gender=validated_data['gender'],
            )
            user.set_password(validated_data['password'])
            user.save()

            return user
            # return CustomUser.objects.create(**validated_data)

        def update(self, validated_data):
            return CustomUser.objects.update(**validated_data)


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'



class UpdateUserProfileSerializer(serializers.ModelSerializer):
    profile_pic = serializers.ImageField(required=True, use_url=False)
    class Meta:
        model = CustomUser
        fields = ['id', 'profile_pic']
        def update(self, validated_data):
            return CustomUser.objects.update(profile_pic=validated_data['profile_pic'],)