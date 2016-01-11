from django.db import models

class dates(models.Model):
    movie_id = models.IntegerField(default=0)
    date = models.CharField(db_index=True, max_length=50)
    def __str__(self):
        return str(self.movie_id) + ': ' + self.date

class ratings(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    rating = models.FloatField(db_index=True, default=0)
    def __str__(self):
        return str(self.movie_id) + ': ' + self.title + ' with Rating: ' + self.rating

    @property
    def genre_list(self):
        return [i.genre for i in genres.objects.filter(movie_id=self.movie_id)]

class genres(models.Model):
    movie_id = models.IntegerField(db_index=True, default=0)
    genre = models.CharField(max_length=50)
    def __str__(self):
        return str(self.movie_id) + ': ' + self.genre

class person(models.Model):
    person_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    def __str__(self):
        return str(self.person_id) + ': ' + self.name

    @property
    def genre_list(self):
        return [i.genre_list for i in cast.objects.filter(person_id=self.person_id)]    

class cast(models.Model):
    movie_id = models.IntegerField(default=0)
    person_id = models.IntegerField(db_index=True, default=0)
    def __str__(self):
        return str(self.person_id) + str(self.movie_id)
    
    @property
    def genre_list(self):
        return [i.genre for i in genres.objects.filter(movie_id=self.movie_id)]

##class Movie(models.Model):
##    title = models.CharField(max_length=100)
##    description = models.CharField(max_length=200)
##    pub_date = models.DateTimeField('date published')
##    
##    def __unicode__(self):
##       return 'Movie: ' + self.title
##
##class Person(models.Model):
##    name = models.CharField(max_length=100)
##    gender = models.CharField(max_length=10)
##    
##    def __unicode__(self):
##       return 'Person: ' + self.name
##
##class Actor(models.Model):
##    movie = models.ForeignKey(Movie)
##    person = models.ForeignKey(Person)
##    
##    def __unicode__(self):
##       return 'Actor: ' + self.movie.title + ', ' + self.person.name
##
##class Director(models.Model):
##    movie = models.ForeignKey(Movie)
##    person = models.ForeignKey(Person)
##    
##    def __unicode__(self):
##       return 'Actor: ' + self.movie.title + ', ' + self.person.name
##
##class Rating(models.Model):
##    movie = models.ForeignKey(Movie)
##    rating = models.DecimalField(max_digits=4, decimal_places=2)
##    comment = models.CharField(max_length=400)
##    
##    def __unicode__(self):
##       return 'Actor: ' + self.movie.title + ', ' + str(self.rating) + ': ' + self.comment
