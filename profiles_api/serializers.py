from rest_framework import serializers as s

from profiles_api import models

class HelloSerializer(s.Serializer):
    """ Serializes a name field for testing our APIView """
    name = s.CharField(max_length=10)

class UserProfilesSerializer(s.ModelSerializer):
    """ Serializes a user profile Object """

    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }
    
    def create(self, validated_data):
        """ Create and Return a new User Object """
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user

class ProfileFeedItemSerializer(s.ModelSerializer):
    """ Serilizes profile feed items """

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}
        