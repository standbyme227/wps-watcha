import re
from datetime import datetime
from bs4 import BeautifulSoup
from django.core.files import File
from django.db import models
from selenium import webdriver
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
        # source = response.text
        # soup = BeautifulSoup(source, 'lxml')

        driver = webdriver.Chrome('/Users/shsf/Projects/chromedriver')
        driver.implicitly_wait(3)

        # options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        # options.add_argument('window-size=1920x1080')
        # options.add_argument("disable-gpu")
        # options.add_argument(
        #     "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) "
        #     "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

        driver.get(response.url)
        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')

        info_area = soup.find('div', class_='mv_info')

        title = info_area.find('h3', class_='h_movie').find('a').text
        raw_title_detail_text = info_area.find('strong', class_='h_movie2').text
        title_detail_text = re.sub(r'\s', '', raw_title_detail_text)

        info_spec_area_1 = info_area.find('p', class_='info_spec')

        genre_list = []
        genre_text = info_spec_area_1.select("span:nth-of-type(1) a")
        for genre_data in genre_text:
            genre = genre_data.text
            genre_list.append(genre)

        nation = info_spec_area_1.select_one("span:nth-of-type(2) a:nth-of-type(1)").text

        span = info_spec_area_1.find_all('span')

        if len(span) > 3:
            running_time_text = info_spec_area_1.select_one("span:nth-of-type(3)").get_text(strip=True)

            d_day_year = info_spec_area_1.select_one("span:nth-of-type(4) a:nth-of-type(1)").text
            d_day_date = info_spec_area_1.select_one("span:nth-of-type(4) a:nth-of-type(2)").text
            if len(span) > 4:
                film_rate = info_spec_area_1.select_one("span:nth-of-type(5) a").text
            else:
                film_rate = ''

        else:
            running_time_text = None
            d_day_year = info_spec_area_1.select_one("span:nth-of-type(3) a:nth-of-type(1)").text
            d_day_date = info_spec_area_1.select_one("span:nth-of-type(3) a:nth-of-type(2)").text
            if len(span) > 3:
                film_rate = info_spec_area_1.select_one("span:nth-of-type(4) a").text
            else:
                film_rate = ''

        d_day = d_day_year + d_day_date
        if running_time_text:
            running_time_pattern = re.compile(r'.*?(\d+).*?', re.DOTALL)
            running_time = re.search(running_time_pattern, running_time_text).group(1)
        else:
            running_time = None

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

        if driver.find_elements_by_xpath("//*[contains(text(), '예매율')]"):
            rate_area = info_spec_area_1.select_one('span:nth-of-type(6)').text
            rate_rank_pattern = re.compile(r'.*?(\d+).*?', re.DOTALL)
            rate_rank = re.search(rate_rank_pattern, rate_area).group(1)

            driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[5]/div/p[1]/a').click()
            html = driver.page_source
            soup = BeautifulSoup(html, 'lxml')
            num_list = []
            for num_data in soup.select('div.b_star span.num'):
                num = num_data.get_text()
                num_list.append(num)
            r = int(rate_rank) - 1
            rank_share = num_list[int(f'{r}')]
            driver.back()

        else:
            rank_share = ''

        for short, full in Movie.CHOICES_NATION_CODE:
            if nation == None:
                nation = Movie.ETC
            elif nation.strip() == full:
                nation = short
                break
        else:
            nation = Movie.ETC

        movie, movie_created = Movie.objects.update_or_create(
            naver_movie_id=naver_movie_id,
            defaults={
                'title_ko': title,
                'title_en': title_detail_text,
                'nation': nation,
                'running_time': running_time,
                'film_rate': film_rate,
                'ticketing_rate': rank_share,
                'audience': audience,
                'intro': story,
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