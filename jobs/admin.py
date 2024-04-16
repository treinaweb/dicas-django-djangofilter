from django.contrib import admin

from .models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "company",
        "location",
        "job_type",
        "job_level",
        "salary",
        "is_active",
    )
    list_filter = ("job_type", "job_level", "is_active", "skills")
    search_fields = ("title", "company", "location")
    actions = ("deactivate_jobs", "activate_jobs")

    def deactivate_jobs(self, request, queryset):
        queryset.update(is_active=False)

    def activate_jobs(self, request, queryset):
        queryset.update(is_active=True)

    deactivate_jobs.short_description = "Desativar as vagas selecionadas"
    activate_jobs.short_description = "Ativar as vagas selecionadas"
