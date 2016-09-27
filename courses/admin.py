from django.contrib import admin
from courses.models import Course,Answers,Question,Assignment
# Register your models here.

admin.site.register(Course)


class QuestionStepInline(admin.StackedInline):
    model = Question

class AnswerStepInline(admin.StackedInline):
    model = Answers
    
class AssignmentAdmin(admin.ModelAdmin):
    inlines = [QuestionStepInline,]

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerStepInline,]

admin.site.register(Assignment,AssignmentAdmin)
admin.site.register(Question,QuestionAdmin)
admin.site.register(Answers)
