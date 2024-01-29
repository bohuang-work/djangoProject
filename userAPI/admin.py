from django.contrib import admin
from django.utils.html import format_html

from userAPI.models import UserDB


class ArticleAdmin(admin.ModelAdmin):
    # 定制哪些字段需要展示
    list_display = ("id", "name", "age", "title", "join_date", "active")

    # list_display_links = ('title', ) # 默认
    # sortable_by # 排序

    """定义哪个字段可以编辑"""
    list_editable = ("active",)

    """分页每页10条"""
    list_per_page = 5

    """最大条目"""
    list_max_show_all = 200  # default

    """搜索框 ^, =, @, None=icontains"""
    search_fields = ["title"]

    """按日期分组"""
    date_hierarchy = "join_date"

    """默认空值"""
    empty_value_display = "NA"

    """过滤选项"""
    list_filter = (
        "active",
        "age",
    )


admin.site.register(UserDB, ArticleAdmin)
