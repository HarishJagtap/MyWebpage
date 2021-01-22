from django.contrib import admin

from main.models import Detail
from main.models import Item
from main.models import Post
from main.models import Resume
from main.models import PriorityTag

admin.site.register(Detail)
admin.site.register(Item)
admin.site.register(Post)
admin.site.register(Resume)
admin.site.register(PriorityTag)
