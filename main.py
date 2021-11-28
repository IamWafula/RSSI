from flask import Flask, render_template

app = Flask(__name__, template_folder='static')

'''@app.route("/")
def hello_world():
    return render_template("main.html")
'''

def distance(rssi):
    dist = []
    rssi = abs(int(rssi))

    if rssi>=100:
        left = "80%"
        top = str(980/rssi)
        top = top+"%"
    elif rssi >= 90:
        left = "65%"
        top = str(980/rssi)
        top = top+"%"
    elif rssi>= 80:
        left = "40%"
        top = str(980/rssi)
        top = top+"%"
    elif rssi >=70:
        left = "35%"
        top = str(980/rssi)
        top = top+"%"
    elif rssi >=60:
        left = "30%"
        top = str(980/rssi)
        top = top+"%"
    else:
        left = "25%"
        top = str(980/rssi)
        top = top+"%"
    
    dist.append(left)
    dist.append(top)

    return dist




@app.route("/<rssi>")
def rssi(rssi):
    dist = distance(rssi)

    left = dist[0]
    top = dist[1]

    return render_template("main.html", left=left, top = top)


app.run()