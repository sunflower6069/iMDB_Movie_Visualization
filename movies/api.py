from .models import dates, ratings, genres, person
from collections import defaultdict
import time

class MovieManager(object):
	
	def latest_n_movies(self, count):
		today = time.strftime("%Y-%m-%d")
		if(count == -1):
			d = dates.objects.order_by('-date').filter(date__lte = today)
		else:
			d = dates.objects.order_by('-date').filter(date__lte = today)[:count]
		date_count = defaultdict(int);
		for movie in d:
			date_count[movie.date] += 1		
		
		return date_count;
	
	def date_range_movies(self, start_date, end_date):
		d = dates.objects.filter(date__gte = start_date).filter(date__lte = end_date)
		date_count = defaultdict(int);
		for movie in d:
			date_count[movie.date] += 1		
		
		return date_count;

	def movie_genres(self, count = 30):
		rs = ratings.objects.order_by('-rating')[:count]
		title_genres = {}
		for movie in rs:
			title_genres[movie.title] = movie.genre_list

		return title_genres;

	def person_genres(self, actor_name='Atu'):
                last = actor_name.split(',')[1]
                first = actor_name.split(',')[0]
##		persons = person.objects.filter(name__contains=actor_name)
                persons = person.objects.filter(name__contains='%s, %s'%(last, first))
		if not persons:
			return {}
		aperson = persons[0]
		gs = aperson.genre_list
		name_genres = defaultdict(int)
		for genres in gs:
			for genre in genres:
				name_genres[genre] += 1
		person_data = {}
		person_data[aperson.name] = name_genres
		return person_data
