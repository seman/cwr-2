import os

from argparse import Namespace
from unittest import TestCase

from cloudweatherreport import cloud_weather_report


class TestRunner(TestCase):

    def test_parse_args_defaults(self):
        args = cloud_weather_report.parse_args(['aws', 'test_plan'])
        expected = Namespace(
            bundle=None, controller=['aws'], deployment=None, dryrun=False,
            exclude=None, failfast=True, log_level='INFO',
            no_destroy=False, reporter='spec', result_output=None,
            skip_implicit=False, test_pattern=None, test_plan='test_plan',
            testdir=os.getcwd(), tests_yaml=None, verbose=False)

        self.assertEqual(args, expected)

    def test_parse_args_set_all_options(self):
        args = cloud_weather_report.parse_args(
            ['aws', 'gce', 'test_plan', '--result-output', 'result', '--testdir',
             '/test/dir', '--bundle', 'foo-bundle', '--deployment', 'depl',
             '--no-destroy', '--log-level', 'debug', '--dry-run', '--reporter',
             'json', '--verbose', '--allow-failure', '--skip-implicit',
             '--exclude', 'skip_test', '--tests-yaml', 'test_yaml_file',
             '--test-pattern', 'tp'])
        expected = Namespace(
            bundle='foo-bundle', controller=['aws', 'gce'], deployment='depl',
            dryrun=True, exclude=['skip_test'], failfast=False,
            log_level='debug', no_destroy=True, reporter='json',
            result_output='result', skip_implicit=True, test_pattern='tp',
            test_plan='test_plan', testdir='/test/dir',
            tests_yaml='test_yaml_file', verbose=True)
        self.assertEqual(args, expected)
