from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin
import core.models as cm

class ChapterAdmin(OrderedModelAdmin):
    list_display = ('get_story_title', 'title', 'move_up_down_links')

admin.site.register(cm.Story)
admin.site.register(cm.Chapter, ChapterAdmin)