from rich import print
from runner import Runner


class GetModelsRunner(Runner):
    name = "Get Model List"

    def run(self):
        print(self.get_models())


if __name__ == "__main__":
    r = GetModelsRunner()
    r.run()
