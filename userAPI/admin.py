from django.contrib import admin

from userAPI.models.computer import ComputerDB
from userAPI.models.job import JobDB
from userAPI.models.office import OfficeDB
from userAPI.models.user import UserDB


class UserDBModelAdmin(admin.ModelAdmin):
    # User API
    ordering = ["join_date"]
    list_display = (
        "name",
        "title",
        "join_date",
        "active",
    )  # Fields to display in the admin list view
    search_fields = (
        "name",
        "active",
    )  # Enable searching by name in the admin


admin.site.register(UserDB, UserDBModelAdmin)


class JobDBModelAdmin(admin.ModelAdmin):
    # Job API
    ordering = ["id"]
    list_display = (
        "name",
        "user",
        "active",
    )  # Fields to display in the admin list view
    search_fields = (
        "name",
        "active",
    )  # Enable searching by name in the admin


admin.site.register(JobDB, JobDBModelAdmin)


class ComputerDBModelAdmin(admin.ModelAdmin):
    # Computer API
    ordering = ["id"]
    list_display = ["brand"]  # Fields to display in the admin list view
    search_fields = ("brand",)  # Enable searching by name in the admin


admin.site.register(ComputerDB, ComputerDBModelAdmin)


class OfficeDBModelAdmin(admin.ModelAdmin):
    # Computer API
    ordering = ["id"]
    list_display = ["name"]  # Fields to display in the admin list view
    search_fields = ("name",)  # Enable searching by name in the admin


admin.site.register(OfficeDB, OfficeDBModelAdmin)
