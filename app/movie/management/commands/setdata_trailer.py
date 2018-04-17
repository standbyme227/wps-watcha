import requests
from django.conf import settings
from django.core.management import BaseCommand, CommandError

from ...models import Movie, TrailerYouTube


class Command(BaseCommand):
    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument('--movie_cnt', dest='movie_cnt', type=int)
        parser.add_argument('--trailer_cnt', dest='trailer_cnt', type=int)
        parser.add_argument('--all', dest='all')

    def handle(self, *args, **options):
        movie_cnt = 1 if not options['movie_cnt'] else options['movie_cnt']
        trailer_cnt = 2 if not options['trailer_cnt'] else options['trailer_cnt']

        if options['all']:
            movie_list = Movie.objects.all()
        else:
            movie_list = Movie.objects.all()[:movie_cnt]

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
        self.stdout.write(self.style.SUCCESS('Success: setdata_trailer command'))
