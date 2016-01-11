from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.http import JsonResponse
from .api import MovieManager
import json
from django.utils.safestring import mark_safe
from django.core import serializers
from .forms import CalendarForm1, CalendarForm2, SchForm, CmtForm, GForm, FirstnameForm, LastnameForm
import random

#def index(request):
#	return HttpResponse('Welcome to IMDb database analysis page!\nDesign By Tianyi Cai, Mengting Gu, Huamin Li, Di Wu, Xin Yan, Jun Zhao')

def latest_n_movies(request, count=300):
	movie_manager = MovieManager()
	return JsonResponse(movie_manager.latest_n_movies(count))

def index(request):
    context = {'SearchForm':SchForm(), 'CommentForm':CmtForm()}
    if request.method == 'POST':
        SearchForm = SchForm(request.POST)
        CommentForm = CmtForm(request.POST)
        if SearchForm.is_valid():
            schtxt = SearchForm.cleaned_data['search']
            url = 'http://www.google.com/?gws_rd=ssl#q='+schtxt
            return HttpResponseRedirect(url)
        elif CommentForm.is_valid():
          cmttxt = CommentForm.cleaned_data['comment']
          context.update({'comment':cmttxt})
          return render(request, 'movies/index.html', context)
    return render(request, 'movies/index.html', context)

def calendar(request):
    if request.method == 'POST':
        StartdateForm = CalendarForm1(request.POST)
        EnddateForm = CalendarForm2(request.POST)
        if StartdateForm.is_valid() and EnddateForm.is_valid():
            sd = StartdateForm.cleaned_data['date1']
            ed = EnddateForm.cleaned_data['date2']
            url = '../../movies/date_range_movies/'+sd+'&'+ed
            return HttpResponseRedirect(url) 
    else:
        StartdateForm = CalendarForm1()
        EnddateForm = CalendarForm2()
        context = {'StartdateForm':StartdateForm, 'EnddateForm':EnddateForm}
    return render(request, 'movies/calendar.html', context)

def genre(request):
    if request.method == 'POST':
        GenreForm = GForm(request.POST)
        if GenreForm.is_valid():
            num = GenreForm.cleaned_data['number']
            url = '../../movies/movie_genres/'+num
            return HttpResponseRedirect(url)
    else:
        GenreForm = GForm()
    return render(request, 'movies/genre.html', {'GenreForm':GenreForm})

def tv_ratings(request):
    template = loader.get_template('movies/tv_ratings.html')
    return HttpResponse(template.render())

def actor_genre_main(request):
    if request.method == 'POST':
        FnameForm = FirstnameForm(request.POST)
        LnameForm = LastnameForm(request.POST)
        if FnameForm.is_valid() and LnameForm.is_valid():
            fname = FnameForm.cleaned_data['first']
            lname = LnameForm.cleaned_data['last']
            url = '../../movies/actor_genres/'+fname+','+lname
            return HttpResponseRedirect(url)
    else:
        FnameForm = FirstnameForm()
        LnameForm = LastnameForm()
        context = {'FnameForm':FnameForm, 'LnameForm':LnameForm}
    return render(request, 'movies/top250_main.html', context)

def top250(request):
    if request.method == 'POST':
        FnameForm = FirstnameForm(request.POST)
        LnameForm = LastnameForm(request.POST)
        if FnameForm.is_valid() and LnameForm.is_valid():
            fname = FnameForm.cleaned_data['first']
            lname = LnameForm.cleaned_data['last']
            url = '../../movies/actor_genres/'+fname+','+lname
            return HttpResponseRedirect(url)
    else:
        FnameForm = FirstnameForm()
        LnameForm = LastnameForm()
        context = {'FnameForm':FnameForm, 'LnameForm':LnameForm}
    return render(request, 'movies/top250.html', context)

def comments(request):
    template = loader.get_template('movies/comments.html')
    return HttpResponse(template.render())

def contact(request):
    template = loader.get_template('movies/contact.html')
    return HttpResponse(template.render())

def features(request):
    template = loader.get_template('movies/features.html')
    return HttpResponse(template.render())

def date_range_main(request):
    if request.method == 'POST':
        StartdateForm = CalendarForm1(request.POST)
        EnddateForm = CalendarForm2(request.POST)
        if StartdateForm.is_valid() and EnddateForm.is_valid():
            sd = StartdateForm.cleaned_data['date1']
            ed = EnddateForm.cleaned_data['date2']
            url = '../../movies/date_range_movies/'+sd+'&'+ed
            return HttpResponseRedirect(url) 
    else:
        StartdateForm = CalendarForm1()
        EnddateForm = CalendarForm2()
        context = {'StartdateForm':StartdateForm, 'EnddateForm':EnddateForm}
    return render(request, 'movies/calendar_main.html', context)
    #    return render(request, 'movies/calendar_main.html')

def date_range_movies(request, start_date="2013-01-01", end_date="2013-04-01"):
        start_year = start_date.split("-")[0]
        end_year = str(int(end_date.split("-")[0])+1)
        context = {"start_year":start_year, "end_year": end_year}
        return render(request, 'movies/calendar.html', context)

def date_range_json(request, start_date="2013-01-01", end_date="2013-04-01"):
        movie_manager = MovieManager()
        movie_range = movie_manager.date_range_movies(start_date, end_date)
        range_list = []
        for k in movie_range.keys():
                tmp = {}
                tmp["Date"] = k
                tmp["Count"] = str(movie_range[k])
                range_list.append(tmp)
        return JsonResponse(range_list, safe=False)

def movie_genres(request, count=1000):
        context = {"count": count}
        return render(request, 'movies/genre.html', context)

def movie_genres_json(request, count=1000):
        genre_list = ['Documentary','Reality-TV','Horror','Drama','Comedy','Musical','Talk-Show','Mystery','News','Sport','Sci-Fi','Romance','Family','Short','Biography','Music','Game-Show','Adventure','Crime','War','Fantasy','Thriller','Animation','Action','History','Adult','Western','Lifestyle','Film-Noir','Experimental','Commercial','Erotica']
        genre_num = {}
        genre_ind = 0
        for genre_type in genre_list:
                genre_num[genre_type] = genre_ind
                genre_ind += 1
        movie_manager = MovieManager()
        genres = movie_manager.movie_genres(count)
        res = {}
        res["nodes"] = []
        res["links"] = []
        name_num = {}
        ind_num = 0
        for title in genres:
                name_num[ind_num] = title
                ind_num += 1
                name_tmp = {}
                name_tmp["name"] = title
                if len(genres[title])>0:
                        name_tmp["group"] = genre_num[genres[title][0]]
                else:
                        name_tmp["group"] = random.sample(range(len(genre_list)),1)[0]
                        genres[title] = genre_list[name_tmp["group"]]
                res["nodes"].append(name_tmp)
        for i in xrange(len(name_num)):
                for j in xrange(i,len(name_num)):
                        link_tmp = {}
                        link_tmp["source"] = i
                        link_tmp["target"] = j
                        genre_s = genres[name_num[i]]
                        genre_t = genres[name_num[j]]
                        value = len(set(genre_s) & set(genre_t))
                        link_tmp["value"] = value
                        res["links"].append(link_tmp)
        return JsonResponse(res)

def genre_main(request):
    if request.method == 'POST':
        GenreForm = GForm(request.POST)
        if GenreForm.is_valid():
            num = GenreForm.cleaned_data['number']
            url = '../../movies/movie_genres/'+num
            return HttpResponseRedirect(url)
    else:
        GenreForm = GForm()
    return render(request, 'movies/genre_main.html', {'GenreForm':GenreForm})

def actor_genre(request,actor_name='Atu'):
    context = {"actor_name": actor_name}
    return render(request, 'movies/top250.html', context)

def actor_genre_json(request,actor_name='Atu'):
        movie_manager = MovieManager()
        genre_list = movie_manager.person_genres(actor_name).values()[0]
        res = []
        for key in genre_list:
                tmp = {}
                tmp["text"] = key
                tmp["size"] = genre_list[key]
                res.append(tmp)
        return JsonResponse(res, safe=False)

#def actor_genre_main(request):
#        ## please add a main page here
#        return render(request, 'movies/top250_main.html')


##def viewdate(request,date_id):
##        try:
##                date_tmp = dates.object.get(pk=date_id)
##        except dates.DoesNotExist:
##                raise Http404('Date id does not exist.')
##        return render(request, 'movies/viewdate.html', {'Date': date_tmp})
##
####def index(request):
##	latest_movie_list = Movie.objects.order_by('title')
##	template = loader.get_template('movies/index.html')
##	context = RequestContext(request, {
##		'latest_movie_list': latest_movie_list,
##	})
##	return HttpResponse(template.render(context))
