from src.utils.config import load_config
from src.utils.console import log_step


class Example:
    def __init__(self):
        self.value = 10

    def get_result(self):
        config = load_config()
        final_result = self.value + config['to_add']
        print("Final result - ", final_result)
        return final_result


@log_step
def main():
    instance = Example()
    instance.get_result()


if __name__ == '__main__':
    main()
