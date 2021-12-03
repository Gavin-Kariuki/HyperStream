from django.contrib import admin
from .models import Post,Profile,Comment
'''
    >>>filter_horizontal property allows ordering of many to many fields<<<
    class HyperAdmin(admin.ModelAdmin):
        filter_horizontal = ('',) 
'''

# Register your models here.
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Comment)
