# coding:utf-8

import urllib2
from bs4 import BeautifulSoup
from com.fourier.moviespy.Dao.DBHelper import DBHelper
from com.fourier.moviespy.Entity.MovieInfo import MovieInfo


html_doc = urllib2.urlopen(
    "http://www.meituan.com/dianying/zuixindianying").read()
soup = BeautifulSoup(html_doc, "lxml")

base_url = "http://www.meituan.com"
dbHelper = DBHelper()
i = 0

for movies_cell in soup.find_all(attrs={"class": "movie-cell"}):
    poster = movies_cell.find("img").get("src")
    movie_name = movies_cell.find(
        attrs={"class": "movie-cell__cover"}).get("title")

    movies_detail_soup = BeautifulSoup(urllib2.urlopen(
        base_url + movies_cell.find(attrs={"class": "btn-normal btn-mini buy-ticket"}).get("href")).read(), "lxml")
    i = i + 1
    print i
    print movie_name
    dbHelper.insertMovieInfo(MovieInfo(movie_name.encode('utf-8'), poster))

    try:
 
        for date in movies_detail_soup.find(attrs={"class": "inline-block-list"}).children:
            date_soup = BeautifulSoup(urllib2.urlopen(
                date.a.get("href")).read(), "lxml")
 
 
            for cinema_item in date_soup.find_all(attrs={"class": "J-cinema-item cinema-item cf"}):
                try:
                    cinema_name = cinema_item.find(
                        attrs={"class": "cinema-item__block cinema-item__block--detail"}).h4.a.get_text()
                    cinema_addr = cinema_item.find(
                        attrs={"class": "cinema-info-row cinema-info-row--addr cf"}).dd.get_text().strip()
                    price = cinema_item.find(
                        attrs={"class": "btn-block btn-block--seat cf"}).p.em.get_text()
 
                except AttributeError, e:
                    continue
 
    except AttributeError, e:
        continue
