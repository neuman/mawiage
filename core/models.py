from django.db import models

# Create your models here.

MONTH_CHOICES = (
    ('1', 'Jan'),
    ('2', 'Feb'),
    ('3', 'Mar'),
    ('4', 'Apr'),
    ('5', 'May'),
    ('6', 'Jun'),
    ('7', 'Jul'),
    ('8', 'Aug'),
    ('9', 'Sep'),
    ('10', 'Oct'),
    ('11', 'Nov'),
    ('12', 'Dec'),
)

class Guest(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    plus = models.IntegerField()
    
    
    def __unicode__(self):
        return self.first_name + self.last_name

    '''
    def get_absolute_url(self):
        return reverse(viewname='location_detail', args=[self.id], current_app=APPNAME)
    '''

class Invite(models.Model):
    token = models.TextField()
    guests = models.ManyToManyField(Guest, null=True, blank=True)