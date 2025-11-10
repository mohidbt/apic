"""CRUD operations package."""
from .specs import (
    create_spec,
    get_spec,
    get_spec_by_name_version,
    list_specs,
    search_specs,
    filter_by_tag,
    get_versions,
    delete_spec,
    get_or_create_tag,
    add_tags_to_spec,
    list_tags,
)

__all__ = [
    "create_spec",
    "get_spec",
    "get_spec_by_name_version",
    "list_specs",
    "search_specs",
    "filter_by_tag",
    "get_versions",
    "delete_spec",
    "get_or_create_tag",
    "add_tags_to_spec",
    "list_tags",
]

