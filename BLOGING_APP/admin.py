from django.contrib import admin

from BLOGING_APP.models import BlogPost, Login, Blogger

# Register your models here.
admin.site.register(Login)
admin.site.register(Blogger)
admin.site.register(BlogPost)
