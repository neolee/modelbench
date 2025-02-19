from rich import print
from runner import Runner


class GetModelsRunner(Runner):
    def run(self):
        print(self.client.models.list())


if __name__ == "__main__":
    r = GetModelsRunner()
    r.run()
