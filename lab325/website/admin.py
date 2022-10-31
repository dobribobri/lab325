from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *


# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


admin.site.register(UserProfile)

admin.site.register(NewsBlock, PostAdmin)
admin.site.register(AnnouncementConferenceBlock, PostAdmin)
admin.site.register(AnnouncementSeminarBlock, PostAdmin)
admin.site.register(SeminarBlock, PostAdmin)

admin.site.register(GrantsBlock, PostAdmin)
admin.site.register(AchievementsBlock, PostAdmin)

admin.site.register(LaboratoryMemberBlock)

admin.site.register(CRFBlock, PostAdmin)
admin.site.register(UrlBlock, PostAdmin)

admin.site.register(Publication)
