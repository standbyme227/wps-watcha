import re
from datetime import datetime
from bs4 import BeautifulSoup
from django.db import models
from utils.file import *

__all__ = (
    'MovieManager',
)


class MovieManager(models.Manager):

    def update_or_create_from_naver(self, movie_id):
        url = f'http://movie.naver.com/movie/bi/mi/basic.nhn'  # ?code=153651

        params = {
            'code': movie_id
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
        genre_text = info_spec_area_1.select_one("a:nth-of-type(1)").text
        # info_spec_area_a = info_spec_area_1.find_all('a')
        nation = info_spec_area_1.select_one("a:nth-of-type(2)").text

        d_day_year = info_spec_area_1.select_one("a:nth-of-type(3)").text
        d_day_date = info_spec_area_1.select_one("a:nth-of-type(4)").text
        d_day = d_day_year + d_day_date

        film_rate = info_spec_area_1.select_one("a:nth-of-type(5)").text
        running_time = info_spec_area_1.select_one("span:nth-of-type(3)").get_text(strip=True)
        # int로 바꾼다.

        audience = info_spec_area_1.find_all("span")[-1].get_text()

        info_spec_area_2 = info_area.find('div', class_='info_spec2')
        director = info_spec_area_2.select_one('a:nth-of-type(1)').text

        people = info_spec_area_2.find_all('a', class_=None)

        people_list = []
        for name_data in people:
            name = name_data.text
            people_list.append(name)

        director = people_list[0]
        actor = people_list[1:]

        # movie, movie_created = self.update_or_create(
        #     movie_id=movie_id,
        #     defaults={
        #         'title' :
        #     }
        # )


    # artist, artist_created = self.update_or_create(
    #     melon_id=artist_id,
    #     defaults={
    #         'name': name,
    #         'real_name': real_name if real_name else '',
    #         'nationality': nationality,
    #         'birth_date': datetime.strptime(
    #             birth_date_str, '%Y.%m.%d') if birth_date_str else None,
    #         'constellation': constellation,
    #         'blood_type': blood_type,
    #     }
    # )
    #
    # temp_file = download(url_img_cover)
    # file_name = '{artist_id}.{ext}'.format(
    #     artist_id=artist_id,
    #     ext=get_buffer_ext(temp_file),
    # )
    #
    # # if artist.image:
    # #     artist.image.delete()
    # # 아티스트 이미지가 있다면 지운다.
    # if not artist.image:
    #     artist.image.save(file_name, File(temp_file))
    # # 아티스트 이미지가 없다면 만든다.
    # return artist, artist_created
