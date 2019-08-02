import logging
import os
import shlex
import subprocess

logger = logging.getLogger(__name__)

SUBMODULE_DIRECTORY = 'external'
# List of desired submodules, as (name, URL, commit) tuples.
SUBMODULE_SPECIFICATIONS = [
    ('Catch2', 'https://github.com/catchorg/Catch2.git', 'tags/v2.9.1'),
    ('sanitizers-cmake', 'https://github.com/arsenm/sanitizers-cmake.git', 'master'),
]

def run(*args, cwd=None):
    command_str = ' '.join(shlex.quote(arg) for arg in args)
    cwd_str = ' \t[cwd: {}]'.format(cwd) if cwd else ''
    logger.info('Running command:  %s%s', command_str, cwd_str)
    subprocess.run(args, check=True, cwd=cwd, capture_output=True)

def init():
    run('git', 'init')

def clone_submodules():
    for name, url, commit in SUBMODULE_SPECIFICATIONS:
        path = os.path.join(SUBMODULE_DIRECTORY, name)
        run('git', 'submodule', 'add', url, path)
        run('git', 'checkout', commit, cwd=path)
        run('git', 'add', path)
        run('git', 'commit', '-m', 'Add {} submodule at {}'.format(name, commit))

if __name__ == '__main__':
    log_level = getattr(logging, os.getenv('COOKIECUTTER_LOG_LEVEL', 'WARNING'))
    # The cookiecutter framework copies the hook before running it, so that %(filename)s
    # has a value like 'tmpf9qrjfmo.py'.  To provide an informative message, the actual
    # script name is hardcoded.
    logging.basicConfig(format='%(levelname)s (post_gen_project.py:%(lineno)d): %(message)s', level=log_level)
    init()
    clone_submodules()