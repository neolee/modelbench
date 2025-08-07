from typing import Iterable, Tuple
from simple_term_menu import TerminalMenu


# show menu of a collection, whose element should have a `description` attribute
def show_menu_of(collection: Iterable, title: str) -> int | Tuple[int, ...] | None:
    items = [f"[{idx:02d}] {obj.name}" for idx, obj in enumerate(collection)]
    terminal_menu = TerminalMenu(items, title=title)
    return terminal_menu.show()
