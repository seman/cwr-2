import argparse
import os

from bundle import BundleTest
from bundletester import tester
from bundletester import reporter


def bundle_tester_args(parser):
    #parser.add_argument('-e', '--environment')
    parser.add_argument('-t', '--testdir', default=os.getcwd())
    parser.add_argument('-b', '-c', '--bundle',
                        type=str,
                        help=("""
                        Specify a bundle ala
                        {path/to/bundle.yaml}. Relative paths will be
                        mapped within the bundle itself for remote
                        bundles. Explicit local paths to bundles
                        currently not supported.
                        """))
    parser.add_argument('-d', '--deployment')

    parser.add_argument('--no-destroy', action="store_true")

    parser.add_argument('-l', '--log-level', dest="log_level",
                        default='INFO')
    #parser.add_argument('-o', '--output', dest="output",
    #                    type=argparse.FileType('w'))
    parser.add_argument('-n', '--dry-run', action="store_true",
                        dest="dryrun")
    parser.add_argument('-r', '--reporter', default="spec",
                        choices=reporter.FACTORY.keys())
    parser.add_argument('-v', '--verbose', action="store_true")

    parser.add_argument('-F', '--allow-failure', dest="failfast",
                        action="store_false")
    parser.add_argument('-s', '--skip-implicit', action="store_true",
                        help="Don't include automatically generated tests")
    parser.add_argument('-x', '--exclude', dest="exclude", action="append")
    parser.add_argument('-y', '--tests-yaml', dest="tests_yaml",
                        help="Path to a tests.yaml file which will "
                        "override the one in the charm or bundle "
                        "being tested.")
    parser.add_argument('--test-pattern', dest="test_pattern")
    #parser.add_argument('tests', nargs="*")
    return parser

def parse_args(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('controller', nargs='+', help="Controller list.")
    parser.add_argument('test_plan', help="Test plan YAML file.")
    parser.add_argument('--result-output', help="Test result output file.")
    bundle_tester_args(parser)
    args = parser.parse_args(argv)

    return args

def run_bundle_test():
    bundle_test = BundleTest()


if __name__ == '__main__':
    args = parse_args()