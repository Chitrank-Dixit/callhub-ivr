# from rest_framework import serializers

# from .models import User, IvrData

from django.contrib.auth import update_session_auth_hash

from rest_framework import serializers

from django.contrib.auth.models import User


class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    #confirm_password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name' , 'password',
                  'date_joined', 'last_login')
        read_only_fields = ('date_joined', 'last_login',)

        def create(self, validated_data):
            return User.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.username = validated_data.get('username', instance.username)
            #instance.tagline = validated_data.get('tagline', instance.tagline)

            instance.save()

            password = validated_data.get('password', None)
            #confirm_password = validated_data.get('confirm_password', None)

            if password:
                instance.set_password(password)
                instance.save()

            update_session_auth_hash(self.context.get('request'), instance)

            return instance