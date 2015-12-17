##
##   display environment variables in mod_wsgi - shows if wsgi, flask etc is working
##

from flask import Flask, request, make_response
import sys
application = Flask(__name__)

def showEnv(environ):

    version = sys.version

    o = "<table>"
    o += "<tr>"
    o += "<td>Python version</td>"
    o += "<td>"+str(version)+"</td>"
    for key in environ:
       o += "<tr>"
       o += "<td>"+str(key)+"</td>"
       o += "<td>"+str(environ[key])+"</td>"
       o += "</tr>\n"
    o += "</table>"
    return o

def WSerrorTextHTML(txt):
    err = "<p>ERROR!</p>"
    err += "<pre>"+ txt + "</pre>"
    return err

@application.route('/', methods=['POST', 'GET'])
def indexApp():

    try:
        env = request.environ
        output = 'Hello World!<hr>'

        if not env['mod_wsgi.process_group']:
            output += 'EMBEDDED MODE<hr>'
        else:
            output += 'DAEMON MODE<hr>'

        output += showEnv(env) + "<hr>"
        output += str(request.method) + "<hr>"
        output += str(__name__)
        return output
    except:
        import traceback
        response = make_response(WSerrorTextHTML(traceback.format_exc()))
        response.headers['Content-Type'] = 'text/html'
        return response

    return "<p>something wrong!</p>"

if __name__ == "__main__":
    application.run()
