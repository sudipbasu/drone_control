import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
TOPIC = "drone/commands"

def on_connect(client, userdata, flags, rc):
    print("[Drone] Connected to broker.")
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    command = msg.payload.decode()
    print(f"[Drone] Received command: {command}")
    if command == "takeoff":
        print("🛫 Drone is taking off...")
    elif command == "land":
        print("🛬 Drone is landing...")
    else:
        print(f"🚁 Executing command: {command}")

client = mqtt.Client(client_id="DroneSimulator")
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER, 1883, 60)
client.loop_forever()
