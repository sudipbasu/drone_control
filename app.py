from flask import Flask, render_template, request, jsonify
import paho.mqtt.client as mqtt

app = Flask(__name__)

BROKER = "broker.hivemq.com"
TOPIC = "drone/commands"

mqtt_client = mqtt.Client("WebController")
mqtt_client.connect(BROKER, 1883, 60)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/command", methods=["POST"])
def send_command():
    command = request.json.get("command")
    mqtt_client.publish(TOPIC, command)
    print(f"[Web -> Drone] Command sent: {command}")
    return jsonify({"status": "Command sent", "command": command})

if __name__ == "__main__":
    app.run(debug=True)
