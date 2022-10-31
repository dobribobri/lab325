from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UserProfile)

admin.site.register(NewsBlock)
admin.site.register(AnnouncementConferenceBlock)
admin.site.register(AnnouncementSeminarBlock)
admin.site.register(SeminarBlock)

admin.site.register(GrantsBlock)
admin.site.register(AchievementsBlock)

admin.site.register(LaboratoryMemberBlock)

admin.site.register(CRFBlock)
admin.site.register(UrlBlock)

admin.site.register(Publication)
