from flask import Flask
from github import Github
import base64
import sys
app = Flask(__name__)

@app.route("/v1/<filename>")
def readconfig(filename):
    URL= sys.argv[1]
    print "URL", URL
    repo_name= URL.rsplit("/",1)
    user_name=URL.rsplit("/",2)
    name=user_name[1]
    print "user_name",name
    repon=repo_name[1]
    print " repo_argumnent", repo_name[1]
    g = Github()
    try:
     repo=g.get_user(name).get_repo(repon)
     file_contents=repo.get_file_contents(filename)
     file_data = base64.b64decode(file_contents.content)
     return file_data
    except:
        return 'Cannot open repository=> %s' % repon 

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
   