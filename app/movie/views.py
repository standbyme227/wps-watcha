import re

from bs4 import BeautifulSoup
from django.http import HttpResponse
from django.shortcuts import render, redirect
from pip._vendor import requests
from django.contrib.auth import authenticate

from .models import Movie


def movie_search_from_nm(request):
    context = {
        'movie_info_list': [],
    }
    ie = 'utf8'
    keyword = request.GET.get('keyword')
    if keyword:
        url = 'http://movie.naver.com/movie/search/result.nhn'

        params = {
            'query': keyword,
            'ie': ie,
        }

        response = requests.get(url, params)
        source = response.text
        soup = BeautifulSoup(source, 'lxml')
        ul = soup.find('div', id='old_content').find('ul', class_='search_list_1')

        result = []
        for li in ul.find_all('li'):
            movie_url = li.find('a')['href']
            match_id = re.search(r'.*?(\d+).*?', movie_url)
            movie_id = match_id.group(1)

            title = li.find('dt').find('a').text
            rating = li.find('dd').find('em', class_='num').text
            genre = li.find('dd', class_='etc').find('a').text
            people = li.find_all('dd')[2].text
            result.append([
                movie_id, title, rating, genre, people
            ])
        return result


def get_movie_detail(movie_id, refresh_html=False):
    url = f'http://movie.naver.com/movie/bi/mi/basic.nhn' #?code=153651

    params = {
        'code':movie_id
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

    info_spec_area = info_area.find('p', class_='info_spec')
    info_spec_area_a = info_spec_area.find_all('a')
    genre = info_spec_area_a.


    dl2 = info_area.find('div', class_='info_spec2')
    # for dl in info_area.find_all('p', class_='info_spec'):
    #     if dl[-1]:



    # summary = "".join(line.strip() for line in dl.split("\n"))

    # result.append(summary)
    # summary = dl.find_all('dd')[0]
    # summary = summary_list.find('span').text
    print(result)