"""
This module provides functions for handling entry, mood, tag, and entry_tag requests.
"""
from .entry_requests import (
    get_all_entries,
    get_single_entry,
    create_entry,
    delete_entry,
    update_entry
)

from .mood_requests import (
    get_all_moods,
    get_single_mood,
    create_mood,
    delete_mood,
    update_mood
)

# from .tag_requests import (
#     get_all_tags,
#     get_single_tag,
#     create_tag,
#     delete_tag,
#     update_tag
# )

# from .entry_tag_requests import (
#     get_all_entry_tags,
#     get_single_entry_tag,
#     create_entry_tag,
#     delete_entry_tag,
#     update_entry_tag
# )