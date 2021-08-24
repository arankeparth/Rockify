from django.contrib import admin
from .models import images
from .models import Videos
admin.site.register(images)
admin.site.register(Videos)
from .models import Lesson
admin.site.register(Lesson)
from .models import Posters
admin.site.register(Posters)
# Register your models here.
