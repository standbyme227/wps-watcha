from rest_framework import serializers
from actor_director.models import Member


class MemberDefaultListSerializer(serializers.ModelSerializer):
    # type = serializers.ChoiceField(choices=[1])
    class Meta:
        model = Member
        fields = '__all__'


class MemberNameListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = (
            'name',
        )