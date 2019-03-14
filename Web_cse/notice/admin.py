from django.contrib import admin
from .models import Notices
from .models import Slide
from .models import Logo
from .models import Event

admin.site.register(Notices)
admin.site.register(Slide)
admin.site.register(Logo)
admin.site.register(Event)
