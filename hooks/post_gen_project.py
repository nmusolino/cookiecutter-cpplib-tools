import logging
import os
import shlex
import subprocess
import pathlib

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

def git_init():
    run('git', 'init')

def git_first_commit():
    run('git', 'add', '.')
    run('git', 'commit', '-m', 'Create project')

def git_clone_submodules():
    for name, url, commit in SUBMODULE_SPECIFICATIONS:
        path = os.path.join(SUBMODULE_DIRECTORY, name)
        run('git', 'submodule', 'add', url, path)
        run('git', 'checkout', commit, cwd=path)
        run('git', 'add', path)
        run('git', 'commit', '-m', 'Add {} submodule at {}'.format(name, commit))

def remove_files(list_of_files):
    for file_name in list_of_files:
        os.remove(file_name)


def get_available_licenses():
    """Looks for all files named LICENSE.XXX and creates list of available licenses
    """
    content = pathlib.Path().glob("*")
    lics_vendor = [x.name for x in content if "LICENSE" in x.name]
    lics = [lic.lstrip('LICENSE.') for lic in lics_vendor]
    return lics

def remove_open_source_files():
    lics = get_available_licenses()
    license_files = [f"LICENSE.{lic}" for lic in lics]
    remove_files(license_files)
    remove_gplv3_files()


def remove_gplv3_files():
    gpl_files = ["CONTRIBUTORS.txt", "COPYING"]
    remove_files(gpl_files)

def remove_all_licenses_except(requested_lic):
    unneeded_lics = get_available_licenses()
    unneeded_lics.remove(requested_lic)
    unneeded_license_files = [f"LICENSE.{lic}" for lic in unneeded_lics]
    remove_files(unneeded_license_files)
            
    if "GNU General Public License v3" in unneeded_lics:
        remove_gplv3_files()
    
    os.rename(f"LICENSE.{requested_lic}", "LICENSE")

def set_license():
    requested_lic = "{{cookiecutter.license}}"
    is_open_source = requested_lic != "Not open source"
    
    if is_open_source:
        remove_all_licenses_except(requested_lic)
    else:
        remove_open_source_files()

def run_git_commands():
    git_init()
    git_clone_submodules()
    git_first_commit()

if __name__ == '__main__':
    log_level = getattr(logging, os.getenv('COOKIECUTTER_LOG_LEVEL', 'WARNING'))
    # The cookiecutter framework copies the hook before running it, so that %(filename)s
    # has a value like 'tmpf9qrjfmo.py'.  To provide an informative message, the actual
    # script name is hardcoded.
    logging.basicConfig(format='%(levelname)s (post_gen_project.py:%(lineno)d): %(message)s', level=log_level)
    set_license()
    run_git_commands()