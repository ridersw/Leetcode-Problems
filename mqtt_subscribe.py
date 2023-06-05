from awscrt import io, mqtt, auth, http
from awsiot import mqtt_connection_builder

# Set up the MQTT connection parameters
ENDPOINT = "a2qx0h90p3xwh8-ats.iot.us-west-2.amazonaws.com"
CLIENT_ID = "iotconsole-5f70febf-4209-43d7-ac4c-4534c1c80d41"
PATH_TO_CERTIFICATE = "/Users/wshashiraj/Downloads/7e19fe6111d58bb36e800c36ff4b8b28736f0cc5313e4c05e499e803b63cd60a-certificate.pem.crt"
PATH_TO_PRIVATE_KEY = "/Users/wshashiraj/Downloads/7e19fe6111d58bb36e800c36ff4b8b28736f0cc5313e4c05e499e803b63cd60a-private.pem.key"
PATH_TO_AMAZON_ROOT_CA_1 = "/Users/wshashiraj/Downloads/AmazonRootCA1.pem"
MESSAGE = '{"pumpStatus": "ON"}'
TOPIC = "arn:aws:iot:us-west-2:068820307922:thing/CapstoneProjectThing"
RANGE = 20

# Spin up resources
event_loop_group = io.EventLoopGroup(1)
host_resolver = io.DefaultHostResolver(event_loop_group)
client_bootstrap = io.ClientBootstrap(event_loop_group, host_resolver)
client = mqtt_connection_builder.mtls_from_path(
            endpoint=ENDPOINT,
            cert_filepath=PATH_TO_CERTIFICATE,
            pri_key_filepath=PATH_TO_PRIVATE_KEY,
            client_bootstrap=client_bootstrap,
            ca_filepath=PATH_TO_AMAZON_ROOT_CA_1,
            client_id=CLIENT_ID,
            clean_session=False,
            keep_alive_secs=6
            )

# # Start the connection
# print("Connecting to MQTT broker...")
# connect_future = client.connect()
# connect_future.result()
# print("Connected!")

# # Subscribe to the topic
# print(f"Subscribing to topic '{TOPIC}'...")
# subscribe_future, _ = client.subscribe(topic=TOPIC, qos=mqtt.QoS.AT_LEAST_ONCE)
# subscribe_future.result()
# print(f"Subscribed to topic '{TOPIC}'.")

# # Wait for messages
# while True:
#     message = client.receive()
#     print(f"Received message: {message.payload.decode()}")

# Define the message callback function
def on_message_received(topic, payload, **kwargs):
    print(f"Received message: {payload.decode()}")

# Set up the subscription
print(f"Subscribing to topic '{TOPIC}'...")
subscribe_future, packet_id = client.subscribe(topic=TOPIC, qos=mqtt.QoS.AT_LEAST_ONCE, callback=on_message_received)
subscribe_result = subscribe_future.result()
print(f"Subscribed to topic '{TOPIC}' with result {subscribe_result['qos']}")

# Start the connection
print("Connecting to MQTT broker...")
connect_future = client.connect()
connect_future.result()
print("Connected!")

# Keep the connection alive
while True:
    pass
