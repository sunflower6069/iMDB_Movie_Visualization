from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /movies/
    url(r'^$', views.index, name='index'),
    # ex: /movies/latest_n_movies/300/
    url(r'^latest_n_movies/(?P<count>[0-9]+)/$', views.latest_n_movies, name='latest_n_movies'),
    # ex: /movies/movie_genres/300/
    url(r'^movie_genres/(?P<count>[0-9]+)/$', views.movie_genres, name='movie_genres'),
    # ex: /movies/movie_genres/300/json/
    url(r'^movie_genres/(?P<count>[0-9]+)/json/$',views.movie_genres_json, name='movie_genres_json'),
    url(r'^date_range_movies/$', views.date_range_main, name='date_range_main'),
    url(r'^movie_genres/$', views.genre_main, name='genre_main'),
    # ex: /movies/date_range_movies/2013-01-01&2013-04-01/
    url(r'^date_range_movies/(?P<start_date>[1-2][0-9][0-9][0-9]\-[0-1][0-9]\-[0-3][0-9])&(?P<end_date>[1-2][0-9][0-9][0-9]\-[0-1][0-9]\-[0-3][0-9])/$', views.date_range_movies, name='date_range_movies'),
    url(r'^date_range_movies/(?P<start_date>[1-2][0-9][0-9][0-9]\-[0-1][0-9]\-[0-3][0-9])&(?P<end_date>[1-2][0-9][0-9][0-9]\-[0-1][0-9]\-[0-3][0-9])/json/$', views.date_range_json, name='date_range_movies_json'),
    url(r'^calendar', views.calendar, name='calendar'),
    url(r'^genre', views.genre, name='genre'),
    url(r'^top250', views.top250, name='top250'),
    url(r'^tv_ratings', views.tv_ratings, name='tv_ratings'),
    url(r'^comments', views.comments, name='comments'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^index', views.index, name='index2'),
    url(r'^features', views.features, name='features'),
    # ex: /movies/actor_genres/
    url(r'^actor_genres/$', views.actor_genre_main, name='actor_genre_main'),
    url(r'^actor_genres/(?P<actor_name>[^\/]+)/$', views.actor_genre, name='actor_genre'),
    url(r'^actor_genres/(?P<actor_name>[^\/]+)/json/$', views.actor_genre_json, name='actor_genre_json'),
]
