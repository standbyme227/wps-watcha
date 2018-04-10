import re
from datetime import datetime
from bs4 import BeautifulSoup
from django.core.files import File
from django.db import models

from utils.file import *

__all__ = (
    'MovieManager',
)


class MovieManager(models.Manager):

    def update_or_create_from_naver(self, naver_movie_id):

        from .movie import Movie

        url = f'http://movie.naver.com/movie/bi/mi/basic.nhn'  # ?code=153651

        params = {
            'code': naver_movie_id
        }
        response = requests.get(url, params)
        source = response.text
        soup = BeautifulSoup(source, 'lxml')

        info_area = soup.find('div', class_='mv_info')

        result = []
        title = info_area.find('h3', class_='h_movie').find('a').text
        raw_title_detail_text = info_area.find('strong', class_='h_movie2').text
        title_detail_text = re.sub(r'\s', '', raw_title_detail_text)

        # audience_score = info_area.find('span', class_='st_on').text
        # critic_score = info_area.find('a', class_='spc').find('span', class_='st_off').text
        # netizen = info_area.find('div', class_='score').find('a', class_='ntz_score').find('span', class_='st_on').text

        info_spec_area_1 = info_area.find('p', class_='info_spec')

        genre_list = []
        genre_text = info_spec_area_1.select("span:nth-of-type(1) a")
        for genre_data in genre_text:
            genre = genre_data.text
            genre_list.append(genre)

        # info_spec_area_a = info_spec_area_1.find_all('a')
        nation = info_spec_area_1.select_one("span:nth-of-type(2) a:nth-of-type(1)").text

        d_day_year = info_spec_area_1.select_one("span:nth-of-type(4) a:nth-of-type(1)").text
        d_day_date = info_spec_area_1.select_one("span:nth-of-type(4) a:nth-of-type(2)").text
        d_day = d_day_year + d_day_date

        film_rate = info_spec_area_1.select_one("span:nth-of-type(5) a").text
        # film_rate = None
        rank_share = ''

        running_time_text = info_spec_area_1.select_one("span:nth-of-type(3)").get_text(strip=True)
        running_time_pattern = re.compile(r'.*?(\d+).*?', re.DOTALL)
        running_time = re.search(running_time_pattern, running_time_text).group(1)

        if info_spec_area_1.select_one('span.count'):
            audience_text = info_spec_area_1.find_all("span")[-1].get_text()
            audience_pattern = re.compile(r'.*?(\d+).*?', re.DOTALL)
            audience = re.search(audience_pattern, audience_text).group(1)
        else:
            audience = 0

        info_spec_area_2 = info_area.find('div', class_='info_spec2')
        director = info_spec_area_2.select_one('a:nth-of-type(1)').text

        people = info_spec_area_2.find_all('a', class_=None)

        people_list = []
        for name_data in people:
            name = name_data.text
            people_list.append(name)

        director = people_list[0]
        actor = people_list[1:]

        people_id_list = []
        for a in info_spec_area_2.find_all('a', class_=None):
            people_id_link = a.get('href')
            people_id_pattern = re.compile(r'.*?(\d+).*?', re.DOTALL)
            people_id = re.search(people_id_pattern, people_id_link).group(1)
            people_id_list.append(people_id)

        if soup.find('div', class_='story_area').find('p', class_='h_tx_story'):
            story1 = soup.find('div', class_='story_area').find('p', class_='h_tx_story').text
            story2 = soup.find('div', class_='story_area').find('p', class_='con_tx').text
            story = story1 + story2
        else:
            story = soup.find('div', class_='story_area').find('p', class_='con_tx').text

        poster_url = soup.find('div', class_='poster').find('img').get('src')

        for short, full in Movie.CHOICES_NATION_CODE:
            if nation == None:
                nation = Movie.ETC
            elif nation.strip() == full:
                nation = short
                break
        else:
            nation = Movie.ETC


        movie, movie_created = self.update_or_create(
            naver_movie_id=naver_movie_id,
            defaults={
                'title_ko': title,
                'title_detail': title_detail_text,
                'nation': nation,
                'running_time': running_time,
                'film_rate': film_rate,
                'rank_share': rank_share,
                'audience': audience,
                'story': story,
                'd_day': datetime.strptime(d_day, '%Y.%m.%d') if d_day else None,
            }
        )



        temp_file = download(poster_url)
        file_name = '{movie_id}.{ext}'.format(
            movie_id=naver_movie_id,
            ext=get_buffer_ext(temp_file),
        )

        if not movie.poster_image:
            movie.poster_image.save(file_name, File(temp_file))
        return movie, movie_created
