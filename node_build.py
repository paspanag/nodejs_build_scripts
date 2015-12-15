import subprocess
import sys
import os

PROJECT_PATH="project"
RR_NODEJS="rumprun-packages/nodejs"

#rm -rf $FLNAME
#git clone $REPO $FLNAME

#cd $FLNAME

#npm install

#cd ..

#genisoimage -l -r -o app.iso $FLNAME

class cd(object):
        def __init__(self, path):
                self._og_dir = os.getcwd()
                self._other_dir = path
        def __enter__(self):
                os.chdir(self._other_dir)

        def __exit__(self, exc_type, exc_value, traceback):
                os.chdir(self._og_dir)

def clone_project(git_url, project_dir):
        return subprocess.call(["git", "clone", git_url, project_dir])

def checkout(project_dir, branch):
        with cd(project_dir):
                subprocess.call(["git", "checkout", branch])

def check_rr():
        return os.path.isdir(RR_NODEJS)

def check_project(project_dir):
        return os.path.isdir(project_dir)

def init_project(project_dir):
        with cd(project_dir):
                subprocess.call(["npm", "install"])

def package_project(project_dir, app_name):
        subprocess.call(["genisoimage", "-l" ,"-r" ,"-o" ,app_name , project_dir])

def hash_project(project_dir):
        with cd(project_dir):
                return subprocess.check_output(["nix-hash", "."])

if __name__ == "__main__":
        if not check_project(PROJECT_PATH):
                clone_project(sys.argv[1], PROJECT_PATH)
        init_project(PROJECT_PATH)
        package_project(PROJECT_PATH, "app.iso")
