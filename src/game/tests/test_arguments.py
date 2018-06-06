import unittest
from ..game import Game


class TestArgumentsMethods(unittest.TestCase):

    def test_state_parameter_create_error_with_invalid_json_string(self):
        arg = ["""--state={"grid" : {"A2": 10,"C1":3,"D1":12},"turn" :{"player" : 1,"selected" : 7}"""]
        parameter, error_message = Game().parse_state_from_args(arg)
        self.assertNotEqual(len(error_message), 0)

    def test_state_parameter_dont_create_error_with_valid_json_string(self):
        arg = ["""--state={"grid" : {"A2": 10,"C1":3,"D1":12},"turn" :{"player" : 1,"selected" : 7}}"""]
        parameter, error_message = Game().parse_state_from_args(arg)
        self.assertEqual(len(error_message), 0)

    def test_state_parameter_create_dictionary_with_valid_json_string(self):
        arg = ["""--state={"grid" : {"A2": 10,"C1":3,"D1":12},"turn" :{"player" : 1,"selected" : 7}}"""]
        parameter, error_message = Game().parse_state_from_args(arg)
        self.assertEqual(isinstance(parameter, dict), True)


if __name__ == '__main__':
    unittest.main()
