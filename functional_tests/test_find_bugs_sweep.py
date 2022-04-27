import unittest
import subprocess
from functional_tests import constants


class FindBugsSweepTestCase(unittest.TestCase):
    def test_sweep_bugs(self):
        out = subprocess.check_output(
            constants.ELLIOTT_CMD
            + [
                "--group=openshift-4.3", "find-bugs:sweep",
            ]
        )
        self.assertRegex(self, out.decode("utf-8"), "Found \\d+ bugs")


if __name__ == '__main__':
    unittest.main()