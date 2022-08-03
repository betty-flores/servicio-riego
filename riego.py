from flask import Flask
import py_eureka_client.eureka_client as eureka_client

app = Flask(__name__)

rest_port = 8000
host = "riego-service1.herokuapp.com"
eureka_client.init(eureka_server="http://52.73.98.2:8099/eureka/",
                   app_name="riego",
                   instance_port=rest_port, instance_host=host)

@app.route('/riego/<humedad>', methods=['POST'])
def enceder_riego(humedad):
    print(humedad)
    if int(humedad) < 30:
        return "Encendido"
    else:
        return "Apagado"

if __name__ == "__main__":
    app.run(port=8000)