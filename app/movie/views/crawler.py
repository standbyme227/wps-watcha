import re

import os

from PIL import Image
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
    # chrome_option = webdriver.ChromeOptions()
    # chrome_option.add_argument("--headless")
    # chrome_option.add_argument("--disable-gpu")
    #
    # driver = webdriver.Chrome('/Users/shsf/Projects/chromedriver', chrome_options=chrome_option)
    # driver = webdriver.Chrome('/Users/shsf/Projects/chromedriver')
    driver = webdriver.Chrome('chromedriver')
    # driver = webdriver.Chrome('/srv/project/')
    # 웹드라이버로 뭘 지정할건지 설정 및 option 부가

    driver.implicitly_wait(3)
    # 드라이버의 웹 자원 로드를 위해 3초까지 기다려준다.

    # driver.get('https://movie.naver.com/')
    # driver.find_element_by_id('movieChartAllView').click()
    # # html의 id 값으로 해당 태그를 가져와서 클릭한다.

    driver.get('https://movie.naver.com/movie/running/current.nhn?order=open')

    # source = response.text
    # soup = BeautifulSoup(source, 'lxml')

    # if driver.switch_to.alert:
    #     driver.switch_to.alert.accept()

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

            naver_movie_id_a = info_area.find('h3', class_='h_movie').find('a').get('href')
            naver_movie_id_pattern = re.compile(r'.*?(\d+).*?', re.DOTALL)
            naver_movie_id = re.search(naver_movie_id_pattern, naver_movie_id_a).group(1)

            title = info_area.find('h3', class_='h_movie').find('a').text
            raw_title_detail_text = info_area.find('strong', class_='h_movie2').text
            title_detail_text = re.sub(r'\s', '', raw_title_detail_text)

            created_date_pattern = re.compile(r'.*?(\d+).*?', re.DOTALL)
            movie_created_date = re.search(created_date_pattern, raw_title_detail_text).group(1)

            info_spec_area_1 = info_area.find('p', class_='info_spec')

            nation = info_spec_area_1.select_one("span:nth-of-type(2) a:nth-of-type(1)").text

            span = info_spec_area_1.find_all('span')

            if len(span) > 3:
                running_time_text = info_spec_area_1.select_one("span:nth-of-type(3)").get_text(strip=True)

                d_day_year = info_spec_area_1.select_one("span:nth-of-type(4) a:nth-of-type(1)").text
                d_day_date = info_spec_area_1.select_one("span:nth-of-type(4) a:nth-of-type(2)").text

            else:
                running_time_text = None
                d_day_year = info_spec_area_1.select_one("span:nth-of-type(3) a:nth-of-type(1)").text
                d_day_date = info_spec_area_1.select_one("span:nth-of-type(3) a:nth-of-type(2)").text

            film_rate = ''
            film_rate_area1 = driver.find_elements_by_xpath("//*[contains(text(), '관람가')]")
            if film_rate_area1:
                film_rate = film_rate_area1[1].text
            film_rate_area2 = driver.find_elements_by_xpath("//*[contains(text(), '관람불가')]")
            if film_rate_area2:
                film_rate = film_rate_area2[1].text

            for short, full in Movie.CHOICES_FILE_RATE_TYPE:
                if film_rate == '':
                    film_rate = Movie.ETC
                elif film_rate.strip() == full:
                    film_rate = short
                    break
            else:
                film_rate = Movie.LIMIT

            d_day = d_day_year + d_day_date
            if running_time_text:
                running_time_pattern = re.compile(r'.*?(\d+).*?', re.DOTALL)
                running_time = re.search(running_time_pattern, running_time_text).group(1)
            else:
                running_time = None

            if info_spec_area_1.select_one('span.count'):
                audience_area = info_spec_area_1.find_all("span")[-1].get_text()
                audience_pattern = re.compile(r'(.*?\,*\d+)명.*?', re.DOTALL)
                audience_text = re.search(audience_pattern, audience_area).group(1)
                audience = audience_text.replace(',', '')

            else:
                audience = 0

            info_spec_area_2 = info_area.find('div', class_='info_spec2')

            people = info_spec_area_2.find_all('a', class_=None)

            people_list = []
            for name_data in people:
                name = name_data.text
                people_list.append(name)

            # director = people_list[0]
            # actor = people_list[1:]

            if soup.find('div', class_='story_area').find('p', class_='h_tx_story'):
                story1 = soup.find('div', class_='story_area').find('p', class_='h_tx_story').text
                story2 = soup.find('div', class_='story_area').find('p', class_='con_tx').text
                story = story1 + story2
            else:
                story = soup.find('div', class_='story_area').find('p', class_='con_tx').text

            poster_area = soup.find('div', class_='poster').find('img').get('src')
            poster_pattern = re.compile(r'(.*?)\?type=m77_110_2', re.DOTALL)
            poster_url = re.search(poster_pattern, poster_area).group(1)

            if driver.find_elements_by_xpath("//*[contains(text(), '예매율')]"):
                rate_area = info_spec_area_1.select_one('span:nth-of-type(6)').text
                rate_rank_pattern = re.compile(r'.*?(\d+).*?', re.DOTALL)
                rate_rank = re.search(rate_rank_pattern, rate_area).group(1)

                driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd/div/p[@class="rate"]/a').click()

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
                rank_share = None

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
                    'movie_created_date': int(movie_created_date),
                    'nation': nation,
                    'running_time': running_time,
                    'film_rate': film_rate,
                    'ticketing_rate': rank_share,
                    'audience': audience,
                    'intro': story,
                    'd_day': datetime.strptime(d_day, '%Y.%m.%d') if d_day else None,
                }
            )

            genre_list = []
            genre_text = info_spec_area_1.select("span:nth-of-type(1) a")
            for genre_data in genre_text:
                genre = genre_data.text
                genre_list.append(genre)

            from ..models.genre import Genre

            for genre in genre_list:
                genre, genre_created = Genre.objects.get_or_create(genre=genre)
                movie.movie_genre_list.update_or_create(genre=genre, movie=movie)

            temp_file = download(poster_url)

            ext = get_buffer_ext(temp_file)
            im = Image.open(temp_file)
            large = im.resize((460, 650))
            temp_file = BytesIO()
            large.save(temp_file, ext)

            file_name = '{movie_id}_large.{ext}'.format(
                movie_id=naver_movie_id,
                ext=ext,
            )

            if not movie.poster_image:
                movie.poster_image.save(file_name, File(temp_file))

            driver.find_element_by_xpath('//*[@id="movieEndTabMenu"]/li[2]/a').click()
            if driver.find_elements_by_xpath('//*/button[@id="actorMore"]'):
                driver.find_element_by_xpath('//*[@id="actorMore"]').click()
            from actor_director.models import Member
            from movie.models import MovieToMember
            html = driver.page_source
            soup = BeautifulSoup(html, 'lxml')

            director_part = soup.find('h4', class_='h_director').find('strong', class_='blind').text
            div_list = soup.find_all('div', class_='dir_obj')
            for div in div_list:
                img_tag = div.find('p', class_='thumb_dir').find('img')
                if img_tag:
                    img_profile_url = img_tag.get('src')
                else:
                    img_profile_url = ''

                id_area = div.find('a', class_='k_name').get('href')
                id_pattern = re.compile(r'.*?(\d+).*?', re.DOTALL)
                actor_director_id = re.search(id_pattern, id_area).group(1)

                name = div.find('a', class_='k_name').text
                real_name = div.find('em', class_='e_name').text

                part = director_part

                for short, full in MovieToMember.CHOICES_MEMBER_TYPE:
                    if part == None:
                        part = MovieToMember.D
                    elif part.strip() == full:
                        part = short
                        break
                else:
                    part = MovieToMember.D

                member, member_created = Member.objects.update_or_create(
                    actor_director_id=actor_director_id,
                    defaults={
                        'name': name,
                        'real_name': real_name,
                    }
                )
                if not img_profile_url == '':
                    temp_file = download(img_profile_url)
                    file_name = '{actor_director_id}.{ext}'.format(
                        actor_director_id=actor_director_id,
                        ext=get_buffer_ext(temp_file),
                    )

                    if not member.img_profile:
                        member.img_profile.save(file_name, File(temp_file))

                movie.movie_member_list.update_or_create(
                    member=member,
                    movie=movie,
                    defaults={
                        'type': part,
                    }
                )

            # ul = soup.find('ul', class_='lst_people')
            li_list = soup.select('ul.lst_people > li')
            for li in li_list:
                img_tag = li.find('img')
                if img_tag:
                    img_profile_url = img_tag.get('src')
                else:
                    img_profile_url = ''

                id_area = li.find('a', class_='k_name').get('href')
                id_pattern = re.compile(r'.*?(\d+).*?', re.DOTALL)
                actor_director_id = re.search(id_pattern, id_area).group(1)

                name = li.find('a', class_='k_name').text
                real_name = li.find('em', class_='e_name').text
                part = li.find('em', class_='p_part').text

                if li.select_one('p.pe_cmt'):
                    character = li.select_one('p.pe_cmt').get_text(strip=True)
                else:
                    character = ''

                for short, full in MovieToMember.CHOICES_MEMBER_TYPE:
                    if part == None:
                        part = MovieToMember.D
                    elif part.strip() == full:
                        part = short
                        break
                else:
                    part = MovieToMember.D

                member, member_created = Member.objects.update_or_create(
                    actor_director_id=actor_director_id,
                    defaults={
                        'name': name,
                        'real_name': real_name,
                    }
                )
                if not img_profile_url == '':
                    temp_file = download(img_profile_url)
                    file_name = '{actor_director_id}.{ext}'.format(
                        actor_director_id=actor_director_id,
                        ext=get_buffer_ext(temp_file),
                    )

                    if not member.img_profile:
                        member.img_profile.save(file_name, File(temp_file))

                movie.movie_member_list.update_or_create(
                    member=member,
                    movie=movie,
                    defaults={
                        'role_name': character,
                        'type': part,
                    }
                )
            driver.find_element_by_xpath('//*[@id="movieEndTabMenu"]/li[3]/a').click()
            html = driver.page_source
            soup = BeautifulSoup(html, 'lxml')
            img_area = soup.select('li._list a img')
            if img_area:
                just_three = img_area[0:3]
                num = 1
                for i in just_three:
                    stillcut_url = i.get('src')
                    stillcut_pattern = re.compile(r'(.*?)\?type=.*?', re.DOTALL)
                    if len(stillcut_url) > 85:
                        stillcut = re.search(stillcut_pattern, stillcut_url).group(1)
                    else:
                        stillcut = stillcut_url
                    temp_file = download(stillcut)

                    ext = get_buffer_ext(temp_file)
                    im = Image.open(temp_file)
                    # if im.width >= im.height:
                    x = im.width / 128 * 72
                    img = im.crop((0, 0, im.width, x))

                    # img = im.crop((0, 0, 200, 100))

                    still = img.resize((1280, 720))
                    # 넓이, 높이
                    temp_file = BytesIO()
                    still.save(temp_file, ext)
                    file_name = '{movie_id}_stillcut_{num}.{ext}'.format(
                        movie_id=naver_movie_id,
                        ext=ext,
                        num=num,
                    )
                    test_file_name = 'still_cut/' + file_name

                    from movie.models import StillCut
                    if not StillCut.objects.filter(still_img=test_file_name):
                        stillcut = StillCut.objects.create(movie=movie)
                        stillcut.still_img.save(file_name, File(temp_file))

                    num += 1


            driver.get('https://movie.naver.com/movie/running/current.nhn?order=open')
