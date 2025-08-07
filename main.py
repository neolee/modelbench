from rich import print
from rich.console import Console

from mal.adapter.openai import Model

from models import models

from menu import show_menu_of
from runner import Runner
from runners import runners


def show_menu_of_models() -> Model | None:
    idx = show_menu_of(models, "Choose a model provider")
    if not isinstance(idx, int): return None
    return models[idx]

def show_menu_of_runners() -> Runner | None:
    idx = show_menu_of(runners, "Choose feature runner")
    if not isinstance(idx, int): return None
    return runners[idx]


console = Console()

def main():
    while True:
        model = show_menu_of_models()
        if not model: break
        while True:
            runner_class = show_menu_of_runners()
            if not runner_class: break
            runner = runner_class(model) # type: ignore
            console.rule(f"[bold red]Running {runner_class.name}")
            try:
                runner.run()
            except Exception as e:
                print(f"'{runner_class.name}' test failed on '{model.name}' (detail below).\n")
                print(e)
            console.rule(f"[bold red]End of {runner_class.name}")
            print()


if __name__ == "__main__":
    main()
