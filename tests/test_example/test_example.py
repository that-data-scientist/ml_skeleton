from src.example.run_example import Example


class TestExample:
    def test_example_result(self):
        example = Example()
        assert example.get_result() == 30
