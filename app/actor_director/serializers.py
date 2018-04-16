from rest_framework import serializers
from actor_director.models import Member


class MemberDefaultListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = '__all__'


class MemberNameListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = (
            'name',
        )