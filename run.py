from rich import print
from menu import show_menu_of
from provider import Provider, providers
from runner import Runner
from runners import runners


def show_menu_of_providers() -> Provider | None:
    idx = show_menu_of(providers, "Choose a model provider")
    if not isinstance(idx, int): return None
    return providers[idx]

def show_menu_of_runners() -> Runner | None:
    idx = show_menu_of(runners, "Choose feature runner")
    if not isinstance(idx, int): return None
    return runners[idx]


def main():
    while True:
        provider = show_menu_of_providers()
        if not provider: break
        while True:
            runner_class = show_menu_of_runners()
            if not runner_class: break
            runner = runner_class(provider) # type: ignore
            runner.run()
            print()


if __name__ == "__main__":
    main()
