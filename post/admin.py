from django.contrib import admin
from .models import Post, Review
# Register your models here.
admin.site.register(Post)

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('comment', 'date_posted')
    list_filter = ['date_posted']
    search_fields = ['comment']

admin.site.register(Review, ReviewAdmin)
