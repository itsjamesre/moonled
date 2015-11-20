from django.contrib import admin

from moon_led.models import Problem

class ProblemAdmin(admin.ModelAdmin):
    search_fields = ['grade']

admin.site.register(Problem, ProblemAdmin)