from django.contrib import admin
from django.utils import timezone
from .models import Question, Choice

# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'datepublished')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    list_per_page = 10

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)