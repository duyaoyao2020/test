import io
import unittest
from contextlib import redirect_stdout

from hello_world import main


class HelloWorldTest(unittest.TestCase):
    def test_main_prints_hello_world(self):
        output = io.StringIO()

        with redirect_stdout(output):
            main()

        self.assertEqual(output.getvalue(), "Hello, world!\n")


if __name__ == "__main__":
    unittest.main()
