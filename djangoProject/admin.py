from dataclasses import dataclass

from django.conf import settings
from django.contrib import admin


@dataclass(frozen=True)
class ServiceThemeConfig:
    """Service theme config.

    Attributes:
    """

    tab_title: str
    navbar_title: str
    landing_page_service_url: str = ""

    # index page
    has_items_list: bool = True
    index_items_list_title: str = "Cached Items Management"
    has_admin: bool = True
    has_api_swagger: bool = True
    has_service_documentation: bool = False
    service_documentation_url: str = ""
    has_checkmk_link: bool = True

    # checkmk
    checkmk_url: str = ""

    # list view
    frontend_item_create: str = "Create Item"
    frontend_item_delete: str = "Delete Item"
    frontend_item_list: str = "List Items"
    frontend_item_has_create: bool = False
    frontend_item_search_exception_filters: bool = True
    frontend_item_search_exception_filters_per_line: int = 4
    frontend_item_search_exception_excludes: bool = True
    frontend_item_search_exception_excludes_per_line: int = 4
    frontend_item_search_filters: bool = True
    frontend_item_search_filters_per_line: int = 4
    frontend_item_search_querysets: bool = True
    frontend_item_search_querysets_per_line: int = 4


theme_settings: ServiceThemeConfig = settings.SERVICE_THEME_CONFIG
service_name = theme_settings.get("navbar_title")

admin.site.site_header = service_name
admin.site.site_title = service_name
admin.site.index_title = f"{service_name} Administration"
