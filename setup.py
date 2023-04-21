import sys
import subprocess
import conda.cli.python_api as Conda # if conda is not used comment this line

# This is a script to install all needed packages to run the main.py script

# Note:     install conda first (if conda is neede for installation)

# add conda-forge
subprocess.check_call([sys.executable, '-m', 'conda', 'config', '--add', 'channels', 'conda-forge'])
subprocess.check_call([sys.executable, '-m', 'conda', 'config', '--set', 'channel_priority', 'strict'])

def install_package(package_name):
    try:
        # implement pip as a subprocess:
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package_name])
        except:
            subprocess.check_call(['pip', 'install', package_name])
    except:
        # implement conda as subprocess
        try:
            subprocess.check_call([sys.executable, '-m', 'conda', 'install', package_name])
        except:
            subprocess.check_call(['conda', 'install', package_name])

    # process output with an API in the subprocess module:
    reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
    installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
    print(installed_packages)


packages = ["selenium", 
            "bs4", ] # BeautifulSoup

# packages used that are native to python:
# time
# urllib

for package in packages:
    install_package(package)