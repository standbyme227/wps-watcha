import requests
from django.conf import settings
from django.core.management import BaseCommand, CommandError

from ...models import Movie, TrailerYouTube


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        movie_cnt = 3
        trailer_cnt = 2

        movie_list = Movie.objects.filter(id__lte=movie_cnt)
        if movie_list.count() == 0:
            raise CommandError('Movie does not exist')

        for movie in movie_list:
            keyword = movie.title_ko + ' 예고편'
            url = 'https://www.googleapis.com/youtube/v3/search'
            params = {
                'key': settings.YOUTUBE_API_KEY,
                'part': 'snippet',
                'type': 'video',
                'maxResults': trailer_cnt,
                'q': keyword,
            }
            response = requests.get(url, params)
            response_dic = response.json()
            for item in response_dic['items']:
                youtube_id = item['id']['videoId']
                title = item['snippet']['title']
                url_thumbnail = item['snippet']['thumbnails']['medium']['url']

                trailer, _ = TrailerYouTube.objects.get_or_create(
                    movie=movie,
                    youtube_id=youtube_id,
                    title=title,
                    url_thumbnail=url_thumbnail,
                )
