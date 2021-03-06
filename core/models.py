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

ALIGNMENT_CHOICES = (
    ('L', 'Left'),
    ('R', 'Right'),
)

CONTENT_CHOICES = (
    ('C', 'HTML Content'),
    ('P', 'Pure HTML'),
)

import os
import uuid

def upload_to_location(instance, filename):
    blocks = filename.split('.')
    ext = blocks[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    instance.title = blocks[0]
    return os.path.join('uploads/', filename)

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


from ordered_model.models import OrderedModel

class Story(models.Model):
    title = models.TextField()

class Chapter(OrderedModel):
    story = models.ForeignKey(Story)
    alignment = models.CharField(choices=ALIGNMENT_CHOICES, max_length=400, null=True, blank=True)
    title = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    menu_item = models.TextField(null=True, blank=True)
    image_file = models.ImageField(upload_to=upload_to_location, max_length=400, null=True, blank=True)
    content_style = models.CharField(choices=CONTENT_CHOICES, max_length=10, null=True, blank=True)

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        try:
            return self.title
        except Exception as e:
            return "error"

    def get_story_title(self):
        return self.story.title

    def get_anchor_string(self):
        return self.menu_item.replace(" ","")

    def is_menu_item(self):
        return (self.menu_item != "") and (self.menu_item != None)

    def is_pure_html(self):
        return self.content_style == "P"

    def is_content_html(self):
        return self.content_style == "C"

    def is_left_aligned(self):
        return self.alignment == "L"

    def is_right_aligned(self):
        return self.alignment == "R"