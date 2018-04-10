import re

import os
from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import datetime
from django.core.files import File
from movie.models import Movie
from utils.file import *


PATH_MODULE = os.path.abspath(__name__)  # __name__ 모듈이라는 파일이 있는 위치를 뽑아내기위한 abspath
ROOT_DIR = os.path.dirname(PATH_MODULE)
PATH_DATA_DIR = os.path.join(ROOT_DIR, 'data')
os.makedirs(PATH_DATA_DIR, exist_ok=True)



def update_or_create_from_crawler(request):

    driver = webdriver.Chrome('/Users/shsf/Projects/chromedriver')

    # driver = webdriver.PhantomJS('/Users/shsf/Projects/phantomjs-2.1.1-macosx/bin/phantomjs')
    # 웹드라이버로 뭘 지정할건지 설정
    driver.implicitly_wait(3)
    # 드라이버의 웹 자원 로드를 위해 3초까지 기다려준다.

    # driver.get('https://movie.naver.com/')
    # driver.find_element_by_id('movieChartAllView').click()
    # # html의 id 값으로 해당 태그를 가져와서 클릭한다.

    driver.get('https://movie.naver.com/movie/running/current.nhn?order=point')
    # 위의 2과정의 목적이가 이곳이기에 그냥 이걸 불러온다.

    # driver.find_elements_by_class_name('lst_detail_t1')
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    ul = soup.select('ul.lst_detail_t1')

    for li in ul:
        a_list = li.select('dt.tit a')
        num = len(a_list)
        for a in range(0, num):
            a += 1
            driver.find_element_by_xpath(f'//*[@id="content"]/div[1]/div[1]/div[3]/ul/li[{a}]/div/a/img').click()
            html = driver.page_source
            soup = BeautifulSoup(html, 'lxml')

            info_area = soup.find('div', class_='mv_info')

            result = []

            naver_movie_id_a = info_area.find('h3', class_='h_movie').find('a').get('href')
            naver_movie_id_pattern = re.compile(r'.*?(\d+).*?', re.DOTALL)
            naver_movie_id = re.search(naver_movie_id_pattern, naver_movie_id_a).group(1)

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

            # rate_rank =

            info_spec_area_2 = info_area.find('div', class_='info_spec2')
            # director = info_spec_area_2.select_one('a:nth-of-type(1)').text

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
            driver.get('https://movie.naver.com/movie/running/current.nhn?order=point')



