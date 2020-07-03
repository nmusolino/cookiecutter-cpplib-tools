""" This hook adds the following to the generated project:
 * the requested license
 * the unit test framework as git submodule
"""


import logging
import os
import shlex
import subprocess
import pathlib
import shutil


__copyright__ = "Copyright 2020, Contributors to the cookiecutter-cpplib-tools project"
__license__ = "GPL V3"


logger = logging.getLogger(__name__)

SUBMODULE_DIRECTORY = 'external'

def run(command, cwd=None, redirect_output=False):
    cmd_list = shlex.split(command)
    cwd_str = f' \t[cwd: {cwd}]' if cwd else ''
    logger.info(f'Running command:  {command}{cwd_str}')
    process = subprocess.Popen(cmd_list, cwd=cwd, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    
    while True:
        # This loop is needed even if the output shall not be redirected to stdout for the following reason:
        # Popen spawns a background process and continues execution here.
        # That means, without the while loop, we would e.g. execute "git checkout master" right after the download has started, which would crash cookiecutter.
        output = process.stdout.readline().strip()
        return_code = process.poll()
        if output and redirect_output:
            print(output)
        if return_code is not None:
            break


def git_init():
    run(f"git init")


def git_first_commit():
    run(f"git add .")
    run(f"git commit -m 'Create project'")


def git_clone_submodule(name, url, commit):
    path = os.path.join(SUBMODULE_DIRECTORY, name)
    run(f"git submodule add {url} {path}", redirect_output=True)
    run(f"git checkout {commit}", cwd=path)
    run(f"git add {path}")
    run(f"git commit -m 'Add {name} at {commit}'")


def remove_files(list_of_files):
    for file_name in list_of_files:
        os.remove(file_name)


def get_available_licenses():
    """Looks for all files named LICENSE.XXX and creates list of available licenses
    """
    folder_content = pathlib.Path().glob("*")
    lics_vendor = [file.name for file in folder_content if file.name.startswith("LICENSE")]
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


def git_add_Catch2():
    git_clone_submodule('Catch2', 'https://github.com/catchorg/Catch2.git', 'tags/v2.9.1')


def git_add_sanitizers_cmake():
    git_clone_submodule('sanitizers-cmake', 'https://github.com/arsenm/sanitizers-cmake.git', 'master')


def run_git_commands():
    git_init()
    if "{{cookiecutter.unit_test_framework}}" == "Catch2":
        git_add_Catch2()
    git_add_sanitizers_cmake()
    git_first_commit()


if __name__ == '__main__':
    log_level = getattr(logging, os.getenv('COOKIECUTTER_LOG_LEVEL', 'WARNING'))
    # The cookiecutter framework copies the hook before running it, so that %(filename)s
    # has a value like 'tmpf9qrjfmo.py'.  To provide an informative message, the actual
    # script name is hardcoded.
    logging.basicConfig(format='%(levelname)s (post_gen_project.py:%(lineno)d): %(message)s', level=log_level)
    set_license()
    if "{{cookiecutter.unit_test_framework}}" == "None":
        shutil.rmtree("tests")
    run_git_commands()
