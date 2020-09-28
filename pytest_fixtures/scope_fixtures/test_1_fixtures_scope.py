def test_one(function_fixture, class_fixture, module_fixture, session_fixture):
    print("test_one executed")


def test_two(function_fixture, class_fixture, module_fixture, session_fixture):
    print("test_two executed")


class TestClass:

    def test_one_in_class(self, function_fixture, class_fixture, module_fixture, session_fixture):
        print("test_one_in_class executed")

    def test_two_in_class(self, function_fixture, class_fixture, module_fixture, session_fixture):
        print("test_two_in_class executed")