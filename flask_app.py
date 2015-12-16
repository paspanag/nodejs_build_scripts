import node_build
import os
from flask import Flask, Response
app = Flask(__name__)

@app.route("/app/<github_user>/<github_project>")
def get_app(github_user, github_project):
        git_url = "https://github.com/{0}/{1}".format(github_user, github_project)
        if not node_build.check_project(node_build.PROJECT_PATH):
                node_build.clone_project(git_url, node_build.PROJECT_PATH)
        node_build.init_project(node_build.PROJECT_PATH)
        app_name = "app.iso"
        app_tup = "exp_demo"
        node_build.package_project(node_build.PROJECT_PATH, app_name, node_build.BUILDS_DIR)
        file_name = node_build.package_with_binary(app_tup, node_build.BUILDS_DIR, app_name, node_build.NODE_BIN)
        # return app.send_file(file_name, attachment_filename=file_name, mimetype='application/octet-stream')
        def generate():
                with open(file_name, 'rb') as app_file:
                        while True:
                                chunk = app_file.read(512)
                                if chunk:
                                        yield chunk
                                else:
                                        break
        return Response(generate(),
                mimetype='application/zip',
                headers={'Content-Disposition':'attachment;filename=app.zip'})

if __name__ == "__main__":
    # get_app('paspanag', 'expressdemo')
    app.run()
