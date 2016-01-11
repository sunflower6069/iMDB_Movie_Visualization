from movies.models import dates
from django.db import transaction
import time

start_time = time.clock()

all_date = dates.objects.all()
print len(all_date)
n = 0

with transaction.atomic():
    for dateinfo in all_date:
        print dateinfo.id
        date_tmp = dateinfo.date.replace(': ',':')
        date_tmp = date_tmp.split(':')[1]
        if len(date_tmp.split(' ')) < 3:
            dateinfo.delete()
            n += 1
        else:
            date_tmp = time.strptime(date_tmp, '%d %B %Y')
            date_new = str(date_tmp.tm_year) + '-' + str(date_tmp.tm_mon).zfill(2) + '-' + str(date_tmp.tm_mday).zfill(2)
            dateinfo.date = date_new
            dateinfo.save()

elapsed_time = time.clock() - start_time

print "Time elapsed: {} seconds".format(elapsed_time)
print 'Deleting', n, 'queries.'
