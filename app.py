from flask import Flask
from flask import render_template
import ldclient
from ldclient.config import Config
import configparser

app = Flask(__name__)
config = configparser.ConfigParser()
config.read('app.ini')
sdk_key = config['App']['SDKKey']
flag_fedex = ""
flag_usps = ""
flag_ups = ""

def show_message(s):
    print("*** %s" % s)
    print()

def get_flags():
    global flag_fedex
    global flag_usps
    global flag_ups

    ldclient.set_config(Config(sdk_key))

    if ldclient.get().is_initialized():
        show_message("SDK successfully initialized!")
    else:
        show_message("SDK failed to initialize")
        exit()

    user = {
        "key": "example-user-key",
        "name": "Kevin Cochran"
    }

    flag_fedex = ldclient.get().variation("shipQuoteFedex", user, False)
    flag_usps = ldclient.get().variation("shipQuoteUSPS", user, False)
    flag_ups = ldclient.get().variation("shipQuoteUPS", user, False)

    ldclient.get().close()


@app.route("/")
def get_feature():  
    get_flags()
    return render_template("index.html",
        flag_fedex=flag_fedex,
        flag_usps=flag_usps,
        flag_ups=flag_ups)
        
if __name__ == '__main__':
    app.run(debug=True)
