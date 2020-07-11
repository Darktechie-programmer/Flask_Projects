from flask import Flask,render_template,request
import requests 
app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html",error=None)
    else : 
        city_name = request.form.get("city")
        key = "1a4c4f306c55a790989a33c6b9d37973"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}"
        data = requests.get(url)
        if data.status_code == 200 : 
            d = data.json()
            code = d['weather'][0]['icon']
            icon_url = f"http://openweathermap.org/img/wn/{code}@2x.png"
            temp = round(d['main']['temp']-273.15,2)
            humidity = d['main']['humidity']
            #visibility = d['visibility']
            wind_speed  = d['wind']['speed']
            name = d['name']
            data = { 

                "Tempreature" : temp,
                "Humidity" : humidity,
                #	"Visibility" : visibility,
                "Wind Speed" : wind_speed,
                "City" : name,
                }
            return render_template('index.html',data=data,icon=icon_url)
        else :
            error = f"No Weather Data Found for city {city_name}" 
            return render_template("index.html",error=error)
if __name__ == "__main__" : 
    app.run("localhost",5050,debug=True)