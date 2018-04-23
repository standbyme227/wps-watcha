from rest_framework import serializers
from django.contrib.auth import get_user_model

from movie.models import UserToMovie, StillCut

User = get_user_model()

__all__ = (
    'UserStatisticsSerializer',
)


class UserStatisticsSerializer(serializers.ModelSerializer):
    rating_eval = serializers.SerializerMethodField()
    nation_statistics = serializers.SerializerMethodField()
    genre_statistics = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'pk',
            'email',
            'nickname',
            'rating_eval',
            'nation_statistics',
            'genre_statistics',
        )

    def get_genre_statistics(self, obj):
        user_to_movies = UserToMovie.objects.filter(user=self.context['user'], user_watched_movie=True)
        genre_movie_list_action = []
        genre_movie_list_roco = []
        genre_movie_list_mistery = []
        genre_movie_list_crime = []
        genre_movie_list_thriller = []
        genre_movie_list_drama = []
        genre_movie_list_family = []
        genre_movie_list_animation = []
        genre_movie_list_romance = []
        genre_movie_list_fantasy = []
        genre_movie_list_comedy = []
        genre_movie_list_documentary = []
        genre_movie_list_adventure = []
        genre_movie_list_suspense = []
        genre_movie_list_horror = []
        genre_movie_list_blackcomedy = []
        genre_movie_list_sf = []
        genre_movie_list_war = []
        genre_movie_list_musical = []
        genre_movie_list_noir = []
        genre_movie_list_narrative = []
        genre_movie_list_martial_arts = []

        l = 1

        for utm in user_to_movies:

            if utm.movie.movie_genre_list.filter(genre=1):
                total_rating = 0
                genre_movie_list_action.append(utm)
                l = len(genre_movie_list_action)
                for genre_movie in genre_movie_list_action:
                    total_rating += genre_movie.rating
                avg_rating = total_rating / l
                action_rating = avg_rating * 20
                action_l = l
            if genre_movie_list_action == []:
                action_rating = None
                action_l = None

            if utm.movie.movie_genre_list.filter(genre=2):
                total_rating = 0
                genre_movie_list_roco.append(utm)
                l = len(genre_movie_list_roco)
                for genre_movie in genre_movie_list_roco:
                    total_rating += genre_movie.rating
                avg_rating = total_rating / l
                roco_rating = avg_rating * 20
                roco_l = l
            if genre_movie_list_roco == []:
                roco_rating = None
                roco_l = None

            if utm.movie.movie_genre_list.filter(genre=3):
                total_rating = 0
                genre_movie_list_mistery.append(utm)
                l = len(genre_movie_list_mistery)
                for genre_movie in genre_movie_list_mistery:
                    total_rating += genre_movie.rating
                avg_rating = total_rating / l
                mistery_rating = avg_rating * 20
                mistery_l = l
            if genre_movie_list_mistery == []:
                mistery_rating = None
                mistery_l = None

            if utm.movie.movie_genre_list.filter(genre=4):
                total_rating = 0
                genre_movie_list_crime.append(utm)
                l = len(genre_movie_list_crime)
                for genre_movie in genre_movie_list_crime:
                    total_rating += genre_movie.rating
                avg_rating = total_rating / l
                crime_rating = avg_rating * 20
                crime_l = l
            if genre_movie_list_crime == []:
                crime_rating = None
                crime_l = None

            if utm.movie.movie_genre_list.filter(genre=5):
                total_rating = 0
                genre_movie_list_thriller.append(utm)
                l = len(genre_movie_list_thriller)
                for genre_movie in genre_movie_list_thriller:
                    total_rating += genre_movie.rating
                avg_rating = total_rating / l
                thriller_rating = avg_rating * 20
                thriller_l = l
            if genre_movie_list_thriller == []:
                thriller_rating = None
                thriller_l = None

            if utm.movie.movie_genre_list.filter(genre=6):
                total_rating = 0
                genre_movie_list_drama.append(utm)
                l = len(genre_movie_list_drama)
                for genre_movie in genre_movie_list_drama:
                    total_rating += genre_movie.rating
                avg_rating = total_rating / l
                drama_rating = avg_rating * 20
                drama_l = l
            if genre_movie_list_drama == []:
                drama_rating = None
                drama_l = None

            if utm.movie.movie_genre_list.filter(genre=7):
                total_rating = 0
                genre_movie_list_family.append(utm)
                l = len(genre_movie_list_family)
                for genre_movie in genre_movie_list_family:
                    total_rating += genre_movie.rating
                avg_rating = total_rating / l
                family_rating = avg_rating * 20
                family_l = l
            if genre_movie_list_family == []:
                family_rating = None
                family_l = None

            if utm.movie.movie_genre_list.filter(genre=8):
                total_rating = 0
                genre_movie_list_animation.append(utm)
                l = len(genre_movie_list_animation)
                for genre_movie in genre_movie_list_animation:
                    total_rating += genre_movie.rating
                avg_rating = total_rating / l
                animation_rating = avg_rating * 20
                animation_l = l
            if genre_movie_list_animation == []:
                animation_rating = None
                animation_l = None

            if utm.movie.movie_genre_list.filter(genre=9):
                total_rating = 0
                genre_movie_list_romance.append(utm)
                l = len(genre_movie_list_romance)
                for genre_movie in genre_movie_list_romance:
                    total_rating += genre_movie.rating
                avg_rating = total_rating / l
                romance_rating = avg_rating * 20
                romance_l = l
            if genre_movie_list_romance == []:
                romance_rating = None
                romance_l = None

            if utm.movie.movie_genre_list.filter(genre=10):
                total_rating = 0
                genre_movie_list_fantasy.append(utm)
                l = len(genre_movie_list_fantasy)
                for genre_movie in genre_movie_list_fantasy:
                    total_rating += genre_movie.rating
                avg_rating = total_rating / l
                fantasy_rating = avg_rating * 20
                fantasy_l = l
            if genre_movie_list_fantasy == []:
                fantasy_rating = None
                fantasy_l = None

            if utm.movie.movie_genre_list.filter(genre=11):
                total_rating = 0
                genre_movie_list_comedy.append(utm)
                l = len(genre_movie_list_comedy)
                for genre_movie in genre_movie_list_comedy:
                    total_rating += genre_movie.rating
                avg_rating = total_rating / l
                comedy_rating = avg_rating * 20
                comedy_l = l
            if genre_movie_list_comedy == []:
                comedy_rating = None
                comedy_l = None

            if utm.movie.movie_genre_list.filter(genre=12):
                total_rating = 0
                genre_movie_list_documentary.append(utm)
                l = len(genre_movie_list_documentary)
                for genre_movie in genre_movie_list_documentary:
                    total_rating += genre_movie.rating
                avg_rating = total_rating / l
                documentary_rating = avg_rating * 20
                documentary_l = l
            if genre_movie_list_documentary == []:
                documentary_rating = None
                documentary_l = None

            if utm.movie.movie_genre_list.filter(genre=13):
                total_rating = 0
                genre_movie_list_adventure.append(utm)
                l = len(genre_movie_list_adventure)
                for genre_movie in genre_movie_list_adventure:
                    total_rating += genre_movie.rating
                avg_rating = total_rating / l
                adventure_rating = avg_rating * 20
                adventure_l = l
            if genre_movie_list_adventure == []:
                adventure_rating = None
                adventure_l = None

            if utm.movie.movie_genre_list.filter(genre=14):
                total_rating = 0
                genre_movie_list_suspense.append(utm)
                l = len(genre_movie_list_suspense)
                for genre_movie in genre_movie_list_suspense:
                    total_rating += genre_movie.rating
                avg_rating = total_rating / l
                suspense_rating = avg_rating * 20
                suspense_l = l
            if genre_movie_list_suspense == []:
                suspense_rating = None
                suspense_l = None

            if utm.movie.movie_genre_list.filter(genre=15):
                total_rating = 0
                genre_movie_list_horror.append(utm)
                l = len(genre_movie_list_horror)
                for genre_movie in genre_movie_list_horror:
                    total_rating += genre_movie.rating
                avg_rating = total_rating / l
                horror_rating = avg_rating * 20
                horror_l = l
            if genre_movie_list_horror == []:
                horror_rating = None
                horror_l = None

            if utm.movie.movie_genre_list.filter(genre=16):
                total_rating = 0
                genre_movie_list_blackcomedy.append(utm)
                l = len(genre_movie_list_blackcomedy)
                for genre_movie in genre_movie_list_blackcomedy:
                    total_rating += genre_movie.rating
                avg_rating = total_rating / l
                blackcomedy_rating = avg_rating * 20
                blackcomedy_l = l
            if genre_movie_list_blackcomedy == []:
                blackcomedy_rating = None
                blackcomedy_l = None

            if utm.movie.movie_genre_list.filter(genre=17):
                total_rating = 0
                genre_movie_list_sf.append(utm)
                l = len(genre_movie_list_sf)
                for genre_movie in genre_movie_list_sf:
                    total_rating += genre_movie.rating
                avg_rating = total_rating / l
                sf_rating = avg_rating * 20
                sf_l = l
            if genre_movie_list_sf == []:
                sf_rating = None
                sf_l = None

            if utm.movie.movie_genre_list.filter(genre=18):
                total_rating = 0
                genre_movie_list_war.append(utm)
                l = len(genre_movie_list_war)
                for genre_movie in genre_movie_list_war:
                    total_rating += genre_movie.rating
                avg_rating = total_rating / l
                war_rating = avg_rating * 20
                war_l = l
            if genre_movie_list_war == []:
                war_rating = None
                war_l = None

            if utm.movie.movie_genre_list.filter(genre=19):
                total_rating = 0
                genre_movie_list_musical.append(utm)
                l = len(genre_movie_list_musical)
                for genre_movie in genre_movie_list_musical:
                    total_rating += genre_movie.rating
                avg_rating = total_rating / l
                musical_rating = avg_rating * 20
                musical_l = l
            if genre_movie_list_musical == []:
                musical_rating = None
                musical_l = None

            if utm.movie.movie_genre_list.filter(genre=20):
                total_rating = 0
                genre_movie_list_noir.append(utm)
                l = len(genre_movie_list_noir)
                for genre_movie in genre_movie_list_noir:
                    total_rating += genre_movie.rating
                avg_rating = total_rating / l
                noir_rating = avg_rating * 20
                noir_l = l
            if genre_movie_list_noir == []:
                noir_rating = None
                noir_l = None

            if utm.movie.movie_genre_list.filter(genre=21):
                total_rating = 0
                genre_movie_list_narrative.append(utm)
                l = len(genre_movie_list_narrative)
                for genre_movie in genre_movie_list_narrative:
                    total_rating += genre_movie.rating
                avg_rating = total_rating / l
                narrative_rating = avg_rating * 20
                narrative_l = l
            if genre_movie_list_narrative == []:
                narrative_rating = None
                narrative_l = None

            if utm.movie.movie_genre_list.filter(genre=22):
                total_rating = 0
                genre_movie_list_martial_arts.append(utm)
                l = len(genre_movie_list_martial_arts)
                for genre_movie in genre_movie_list_martial_arts:
                    total_rating += genre_movie.rating
                avg_rating = total_rating / l
                martial_arts_rating = avg_rating * 20
                martial_arts_l = l
            if genre_movie_list_martial_arts == []:
                martial_arts_rating = None
                martial_arts_l = None
        genre_eval = {
            'action': {
                'action_rating': action_rating,
                'action_count': action_l
            },
            'roco': {
                'roco_rating': roco_rating,
                'roco_count': roco_l
            },
            'mistery': {
                'mistery_rating': mistery_rating,
                'mistery_count': mistery_l
            },
            'crime': {
                'crime_rating': crime_rating,
                'crime_count': crime_l
            },
            'thriller': {
                'thriller_rating': thriller_rating,
                'thriller_count': thriller_l
            },
            'drama': {
                'drama_rating': drama_rating,
                'drama_count': drama_l
            },
            'family': {
                'family_rating': family_rating,
                'family_count': family_l
            },
            'animation': {
                'animation_rating': animation_rating,
                'animation_count': animation_l
            },
            'romance': {
                'romance_rating': romance_rating,
                'romance_count': romance_l
            },
            'fantasy': {
                'fantasy_rating': fantasy_rating,
                'fantasy_count': fantasy_l
            },
            'comedy': {
                'comedy_rating': comedy_rating,
                'comedy_count': comedy_l
            },
            'documentary': {
                'documentary_rating': documentary_rating,
                'documentary_count': documentary_l
            },
            'adventure': {
                'adventure_rating': adventure_rating,
                'adventure_count': adventure_l
            },
            'suspense': {
                'suspense_rating': suspense_rating,
                'suspense_count': suspense_l
            },
            'horror': {
                'horror_rating': horror_rating,
                'horror_count': horror_l
            },
            'blackcomedy': {
                'blackcomedy_rating': blackcomedy_rating,
                'blackcomedy_count': blackcomedy_l
            },
            'sf': {
                'sf_rating': sf_rating,
                'sf_count': sf_l
            },
            'war': {
                'war_rating': war_rating,
                'war_count': war_l
            },
            'musical': {
                'musical_rating': musical_rating,
                'musical_count': musical_l
            },
            'noir': {
                'noir_rating': noir_rating,
                'noir_count': noir_l
            },
            'narrative': {
                'narrative_rating': narrative_rating,
                'narrative_count': narrative_l
            },
            'martial_arts': {
                'martial_arts_rating': martial_arts_rating,
                'martial_arts_count': martial_arts_l
            },
        }
        return genre_eval

    def get_nation_statistics(self, obj):
        user_to_movies = UserToMovie.objects.filter(user=self.context['user'], user_watched_movie=True)
        nation_movie_list_kr = []
        nation_movie_list_us = []
        nation_movie_list_gb = []
        nation_movie_list_jp = []
        nation_movie_list_ch = []
        nation_movie_list_hk = []
        nation_movie_list_fr = []
        nation_movie_list_gm = []
        nation_movie_list_it = []
        nation_movie_list_th = []

        l = 1
        for utm in user_to_movies:
            total_rating = 0

            if utm.movie.nation == 'KR':
                nation_movie_list_kr.append(utm)
                l = len(nation_movie_list_kr)
                for nation_movie in nation_movie_list_kr:
                    total_rating += nation_movie.rating
                avg_rating = total_rating / l
                kr_rating = avg_rating * 20
                kr_l = l
            if nation_movie_list_kr == []:
                kr_rating = None
                kr_l = None

            if utm.movie.nation == 'US':
                nation_movie_list_us.append(utm)
                l = len(nation_movie_list_us)
                for nation_movie in nation_movie_list_us:
                    total_rating += nation_movie.rating
                avg_rating = total_rating / l
                us_rating = avg_rating * 20
                us_l = l
            if nation_movie_list_us == []:
                us_rating = None
                us_l = None

            if utm.movie.nation == 'GB':
                nation_movie_list_gb.append(utm)
                l = len(nation_movie_list_gb)
                for nation_movie in nation_movie_list_gb:
                    total_rating += nation_movie.rating
                avg_rating = total_rating / l
                gb_rating = avg_rating * 20
                gb_l = l
            if nation_movie_list_gb == []:
                gb_rating = None
                gb_l = None

            if utm.movie.nation == 'JP':
                nation_movie_list_jp.append(utm)
                l = len(nation_movie_list_jp)
                for nation_movie in nation_movie_list_jp:
                    total_rating += nation_movie.rating
                avg_rating = total_rating / l
                jp_rating = avg_rating * 20
                jp_l = l
            if nation_movie_list_jp == []:
                jp_rating = None
                jp_l = None

            if utm.movie.nation == 'CH':
                nation_movie_list_ch.append(utm)
                l = len(nation_movie_list_ch)
                for nation_movie in nation_movie_list_ch:
                    total_rating += nation_movie.rating
                avg_rating = total_rating / l
                ch_rating = avg_rating * 20
                ch_l = l
            if nation_movie_list_ch == []:
                ch_rating = None
                ch_l = None

            if utm.movie.nation == 'HK':
                nation_movie_list_hk.append(utm)
                l = len(nation_movie_list_hk)
                for nation_movie in nation_movie_list_hk:
                    total_rating += nation_movie.rating
                avg_rating = total_rating / l
                hk_rating = avg_rating * 20
                hk_l = l
            if nation_movie_list_hk == []:
                hk_rating = None
                hk_l = None

            if utm.movie.nation == 'FR':
                nation_movie_list_fr.append(utm)
                l = len(nation_movie_list_fr)
                for nation_movie in nation_movie_list_fr:
                    total_rating += nation_movie.rating
                avg_rating = total_rating / l
                fr_rating = avg_rating * 20
                fr_l = l
            if nation_movie_list_fr == []:
                fr_rating = None
                fr_l = None

            if utm.movie.nation == 'GM':
                nation_movie_list_gm.append(utm)
                l = len(nation_movie_list_gm)
                for nation_movie in nation_movie_list_gm:
                    total_rating += nation_movie.rating
                avg_rating = total_rating / l
                gm_rating = avg_rating * 20
                gm_l = l
            if nation_movie_list_gm == []:
                gm_rating = None
                gm_l = None

            if utm.movie.nation == 'IT':
                nation_movie_list_it.append(utm)
                l = len(nation_movie_list_it)
                for nation_movie in nation_movie_list_it:
                    total_rating += nation_movie.rating
                avg_rating = total_rating / l
                it_rating = avg_rating * 20
                it_l = l
            if nation_movie_list_it == []:
                it_rating = None
                it_l = None

            if utm.movie.nation == 'TH':
                nation_movie_list_th.append(utm)
                l = len(nation_movie_list_th)
                for nation_movie in nation_movie_list_th:
                    total_rating += nation_movie.rating
                avg_rating = total_rating / l
                th_rating = avg_rating * 20
                th_l = l
            if nation_movie_list_th == []:
                th_rating = None
                th_l = None

        nation_eval = {
            'KR': {
                "kr_rating": kr_rating,
                "kr_count": kr_l,
            },
            'US': {
                "us_rating": us_rating,
                "us_count": us_l,
            },
            'GB': {
                "gb_rating": gb_rating,
                "gb_count": gb_l,
            },
            'JP': {
                "jp_rating": jp_rating,
                "jp_count": jp_l,
            },
            'CH': {
                "ch_rating": ch_rating,
                "ch_count": ch_l,
            },
            'HK': {
                "hk_rating": hk_rating,
                "hk_count": hk_l,
            },
            'FR': {
                "fr_rating": fr_rating,
                "fr_count": fr_l,
            },
            'GM': {
                "gm_rating": gm_rating,
                "gm_count": gm_l,
            },
            'IT': {
                "it_rating": it_rating,
                "it_count": it_l,
            },
            'TH': {
                'th_rating': th_rating,
                'th_count': th_l,
            },
        }
        return nation_eval

    def get_rating_eval(self, obj):
        total_rating = 0
        user_avg_rating = None
        rating_count = 0
        user_to_movies = UserToMovie.objects.filter(user=self.context['user'], user_watched_movie=True)
        if not user_to_movies == '':
            for utm in user_to_movies:
                total_rating += utm.rating
                l = len(user_to_movies)
            user_avg_ratings = total_rating / l
            user_avg_rating = round(user_avg_ratings, 2)

        user_to_movie_5_0 = UserToMovie.objects.filter(user=self.context['user'], user_watched_movie=True, rating=5.0)
        if not user_to_movie_5_0 == '':
            user_to_movie_5_0 = len(user_to_movie_5_0)
        else:
            user_to_movie_5_0 = rating_count
        user_to_movie_4_5 = UserToMovie.objects.filter(user=self.context['user'], user_watched_movie=True, rating=4.5)
        if not user_to_movie_4_5 == '':
            user_to_movie_4_5 = len(user_to_movie_4_5)
        else:
            user_to_movie_4_5 = rating_count
        user_to_movie_4_0 = UserToMovie.objects.filter(user=self.context['user'], user_watched_movie=True, rating=4.0)
        if not user_to_movie_4_0 == '':
            user_to_movie_4_0 = len(user_to_movie_4_0)
        else:
            user_to_movie_4_0 = rating_count
        user_to_movie_3_5 = UserToMovie.objects.filter(user=self.context['user'], user_watched_movie=True, rating=3.5)
        if not user_to_movie_3_5 == '':
            user_to_movie_3_5 = len(user_to_movie_3_5)
        else:
            user_to_movie_3_5 = rating_count
        user_to_movie_3_0 = UserToMovie.objects.filter(user=self.context['user'], user_watched_movie=True, rating=3.0)
        if not user_to_movie_3_0 == '':
            user_to_movie_3_0 = len(user_to_movie_3_0)
        else:
            user_to_movie_3_0 = rating_count
        user_to_movie_2_5 = UserToMovie.objects.filter(user=self.context['user'], user_watched_movie=True, rating=2.5)
        if not user_to_movie_2_5 == '':
            user_to_movie_2_5 = len(user_to_movie_2_5)
        else:
            user_to_movie_2_5 = rating_count
        user_to_movie_2_0 = UserToMovie.objects.filter(user=self.context['user'], user_watched_movie=True, rating=2.0)
        if not user_to_movie_2_0 == '':
            user_to_movie_2_0 = len(user_to_movie_2_0)
        else:
            user_to_movie_2_0 = rating_count
        user_to_movie_1_5 = UserToMovie.objects.filter(user=self.context['user'], user_watched_movie=True, rating=1.5)
        if not user_to_movie_1_5 == '':
            user_to_movie_1_5 = len(user_to_movie_1_5)
        else:
            user_to_movie_1_5 = rating_count
        user_to_movie_1_0 = UserToMovie.objects.filter(user=self.context['user'], user_watched_movie=True, rating=1.0)
        if not user_to_movie_1_0 == '':
            user_to_movie_1_0 = len(user_to_movie_1_0)
        else:
            user_to_movie_1_0 = rating_count
        user_to_movie_0_5 = UserToMovie.objects.filter(user=self.context['user'], user_watched_movie=True, rating=0.5)
        if not user_to_movie_0_5 == '':
            user_to_movie_0_5 = len(user_to_movie_0_5)
        else:
            user_to_movie_0_5 = rating_count

        rating_eval = {
            'total_rating_count': l,
            'total_rating': total_rating,
            'user_avg_rating': user_avg_rating,
            'rating_5_0': user_to_movie_5_0,
            'rating_4_5': user_to_movie_4_5,
            'rating_4_0': user_to_movie_4_0,
            'rating_3_5': user_to_movie_3_5,
            'rating_3_0': user_to_movie_3_0,
            'rating_2_5': user_to_movie_2_5,
            'rating_2_0': user_to_movie_2_0,
            'rating_1_5': user_to_movie_1_5,
            'rating_1_0': user_to_movie_1_0,
            'rating_0_5': user_to_movie_0_5,
        }
        return rating_eval

    # def get_kr(self, obj):
    #     user_to_movies = UserToMovie.objects.filter(user=self.context['user'], user_watched_movie=True)
    #     nation_movie_list = []
    #     l = 1
    #     for utm in user_to_movies:
    #         total_rating = 0
    #         if utm.movie.nation == 'KR':
    #             nation_movie_list.append(utm)
    #             l = len(nation_movie_list)
    #         for nation_movie in nation_movie_list:
    #             total_rating += nation_movie.rating
    #         avg_rating = total_rating / l
    #         nation_rating = avg_rating * 20
    #     if nation_rating == 0:
    #         return None
    #     return nation_rating
    #
    # def get_kr_count(self, obj):
    #     user_to_movies = UserToMovie.objects.filter(user=self.context['user'], user_watched_movie=True)
    #     nation_movie_list = []
    #     l = None
    #     for utm in user_to_movies:
    #         total_rating = 0
    #         if utm.movie.nation == 'KR':
    #             nation_movie_list.append(utm)
    #             l = len(nation_movie_list)
    #     return l

    # def get_total_rating(self, obj):
    #     total_rating = 0
    #     user_to_movies = UserToMovie.objects.filter(user=self.context['user'], user_watched_movie=True)
    #     if not user_to_movies == '':
    #         for utm in user_to_movies:
    #             total_rating += utm.rating
    #     return total_rating
    #
    # def get_user_avg_rating(self, obj):
    #     total_rating = 0
    #     user_avg_rating = None
    #     user_to_movies = UserToMovie.objects.filter(user=self.context['user'], user_watched_movie=True)
    #     if not user_to_movies == '':
    #         for utm in user_to_movies:
    #             total_rating += utm.rating
    #             l = len(user_to_movies)
    #         user_avg_rating = total_rating / l
    #     return user_avg_rating
    #
    # def get_five(self, obj):
    #     rating_count = 0
    #     user_to_movie = UserToMovie.objects.filter(user=self.context['user'], user_watched_movie=True, rating=5.0)
    #     rating_count += len(user_to_movie)
    #     return rating_count
