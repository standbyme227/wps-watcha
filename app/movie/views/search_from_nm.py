import re

from bs4 import BeautifulSoup
from django.http import HttpResponse
from django.shortcuts import render, redirect
from pip._vendor import requests


from ..models import Movie


def movie_search_from_naver(request):
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
        # ul = soup.find('div', id='old_content').find('ul', class_='search_list_1')

        movie_info_list = []

        for li in soup.select('div#old_content ul.search_list_1 li'):
            if li.find('dt'):
                movie_url = li.find('dt').find('a')['href']
                match_id = re.search(r'.*?(\d+).*?', movie_url)
                movie_id = match_id.group(1)
                url_img_cover = li.select_one('p.result_thumb img').get('src')

                title = li.find('dt').find('a').text
                rating = li.find('dd').find('em', class_='num').text
                genre = li.find('dd', class_='etc').find('a').text
                if li.find('dd', class_='etc').find('em'):
                    nation = li.find('dd', class_='etc').find('em').find('a').text
                else:
                    nation=None

                people = li.find_all('dd')[2].text

                movie_info_list.append({
                    'title': title,
                    'naver_movie_id': movie_id,
                    'url_img_cover': url_img_cover,
                    'rating': rating,
                    'genre': genre,
                    'nation': nation,
                    'people': people,
                    'is_exist': Movie.objects.filter(naver_movie_id=movie_id).exists(),
                })

        context['movie_info_list'] = movie_info_list
    return render(request, 'movie/movie_search_from_naver.html', context)

        #
        #
        #
        #     result.append([
        #         movie_id, title, rating, genre, people
        #     ])
        # return result