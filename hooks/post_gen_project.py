#!/usr/bin/env python

import logging
import os
import shutil
import subprocess

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("post_gen_project")

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
ALL_TEMP_FOLDERS = ["licenses"]



def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_temp_folders(temp_folders):
    for folder in temp_folders:
        logger.debug("Remove temporary folder: %s", folder)
        shutil.rmtree(folder, ignore_errors=True)


if __name__ == "__main__":
    remove_temp_folders(ALL_TEMP_FOLDERS)
    msg = ''
    # try to run git init
    try:
        subprocess.run(["git", "init", "-q"])
        subprocess.run(["git", "checkout", "-b", "main"])
    except Exception:
        pass

{% if cookiecutter.install_precommit == 'y' %}
    # closedPylancetry to install and update pre-commit
    try:
        print("install pre-commit ...")
        subprocess.run(["pip", "install", "pre-commit"], stdout=subprocess.DEVNULL)
        print("updating pre-commit...")
        subprocess.run(["pre-commit", "autoupdate"], stdout=subprocess.DEVNULL)
        subprocess.run(["git", "add", "."])
        subprocess.run(["pre-commit", "run", "black", "-a"], capture_output=True)
    except Exception:
        pass
{% endif %}
    try:
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-q", "-m", "initial commit"])
    except Exception:
        msg += """
Your package template is ready!  Next steps:

1. `cd` into your new directory and initialize a git repo
   (this is also important for version control!)
     cd {{ cookiecutter.plugin_name }}
     git init -b main
     git add .
     git commit -m 'initial commit'
     # you probably want to install your new package into your environment
     pip install -e ."""
    else:
        msg +="""
Your plugin template is ready!  Next steps:
1. `cd` into your new directory
     cd {{ cookiecutter.plugin_name }}
     # you probably want to install your new package into your env
     pip install -e ."""

{% if cookiecutter.install_precommit == 'y' %}
    # try to install and update pre-commit
    # installing after commit to avoid problem with comments in setup.cfg.
    try:
        print("install pre-commit hook...")
        subprocess.run(["pre-commit", "install"])
    except Exception:
        pass
{% endif %}

{% if cookiecutter.github_repository_url != 'provide later' %}
    msg += """
2. Create a github repository with the name '{{ cookiecutter.plugin_name }}':
   https://github.com/{{ cookiecutter.github_username_or_organization }}/{{ cookiecutter.plugin_name }}.git
3. Add your newly created github repo as a remote and push:
     git remote add origin https://github.com/{{ cookiecutter.github_username_or_organization }}/{{ cookiecutter.plugin_name }}.git
     git push -u origin main
4. The following default URLs have been added to `setup.cfg`:
    Bug Tracker = https://github.com/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.plugin_name}}/issues
    Documentation = https://github.com/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.plugin_name}}#README.md
    Source Code = https://github.com/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.plugin_name}}
    User Support = https://github.com/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.plugin_name}}/issues
    These URLs will be displayed on your plugin's napari hub page.
    You may wish to change these before publishing your plugin!"""

{% else %}
    msg += """
2. Create a github repository for your plugin:
   https://github.com/new
3. Add your newly created github repo as a remote and push:
     git remote add origin https://github.com/your-repo-username/your-repo-name.git
     git push -u origin main
   Don't forget to add this url to setup.cfg!
     [metadata]
     url = https://github.com/your-repo-username/your-repo-name.git
4. Consider adding additional links for documentation and user support to setup.cfg
   using the project_urls key e.g.
    [metadata]
    project_urls =
        Bug Tracker = https://github.com/your-repo-username/your-repo-name/issues
        Documentation = https://github.com/your-repo-username/your-repo-name#README.md
        Source Code = https://github.com/your-repo-username/your-repo-name
        User Support = https://github.com/your-repo-username/your-repo-name/issues"""
{% endif %}
    msg += """
5. Read the README for more info: https://github.com/Kapoorlabs-CAPED/cookiecutter-template

"""

    print(msg)