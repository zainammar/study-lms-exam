from django.contrib import admin
from .models import Quiz, Question, Option, UserAnswer, Result


class OptionInline(admin.TabularInline):
    model = Option
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]


admin.site.register(Quiz)
admin.site.register(Question, QuestionAdmin)
admin.site.register(UserAnswer)


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'quiz', 'score', 'total', 'submitted_at')
    list_filter = ('quiz', 'submitted_at')
    search_fields = ('user__username',)
