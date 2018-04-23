from rest_framework import serializers
from django.contrib.auth import get_user_model

from movie.models import UserToMovie, StillCut


User = get_user_model()

__all__ = (
    'UserSerializer',
    'UserEmailSerializer',
    'UserSimpleDetailSerializer',
    'UserMyPageTopSerializer',

)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'email',
            'username',
            'nickname',
            'img_profile',
            'first_name',
            'last_name',
        )
        read_only_fields = ('pk', 'username', 'email')


class UserEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'email',
            'username',
        )
        # read_only_fields = ('pk', 'username',)


class UserSimpleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'email',
            'nickname',
            'img_profile',
        )


class UserMyPageTopSerializer(serializers.ModelSerializer):
    total_running_time = serializers.SerializerMethodField()
    interesting_movie_cnt = serializers.SerializerMethodField()
    still_cut_img = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'pk',
            'email',
            'nickname',
            'img_profile',
            'total_running_time',
            'interesting_movie_cnt',
            'still_cut_img',
        )

    def get_total_running_time(self, obj):
        rt_sum = 0
        user_to_movie = UserToMovie.objects.filter(user=self.context['user'], user_watched_movie=True)
        for item in user_to_movie:
            rt_sum += item.movie.running_time
        return round(rt_sum / 60)

    def get_interesting_movie_cnt(self, obj):
        cnt = UserToMovie.objects.filter(user=self.context['user']).count()
        return cnt

    def get_still_cut_img(self, obj):
        try:
            user_to_movie = UserToMovie.objects.filter(user=self.context['user']).latest('rating')
            still_cut = StillCut.objects.filter(movie=user_to_movie.movie).latest('id')
            from movie.serializers import StillCutSerializer
            serializer = StillCutSerializer(still_cut)
            return serializer.data
        except:
            return None
