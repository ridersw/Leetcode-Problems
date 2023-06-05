from awscrt import io, mqtt, auth, http
from awsiot import mqtt_connection_builder

# Define ENDPOINT, CLIENT_ID, PATH_TO_CERTIFICATE, PATH_TO_PRIVATE_KEY, PATH_TO_AMAZON_ROOT_CA_1, MESSAGE, TOPIC, and RANGE
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
mqtt_connection = mqtt_connection_builder.mtls_from_path(
            endpoint=ENDPOINT,
            cert_filepath=PATH_TO_CERTIFICATE,
            pri_key_filepath=PATH_TO_PRIVATE_KEY,
            client_bootstrap=client_bootstrap,
            ca_filepath=PATH_TO_AMAZON_ROOT_CA_1,
            client_id=CLIENT_ID,
            clean_session=False,
            keep_alive_secs=6
            )
print("Connecting to {} with client ID '{}'...".format(
        ENDPOINT, CLIENT_ID))
# Make the connect() call
connect_future = mqtt_connection.connect()
# Future.result() waits until a result is available
connect_future.result()
print("Connected!",connect_future)
# Publish message to server desired number of times.
print('Begin Publish')
try:
    mqtt_connection.publish(topic=TOPIC, payload=MESSAGE, qos=mqtt.QoS.AT_LEAST_ONCE)
    print(f'Published Successfully')
except:
    print('Publish Failed')
print("Published: '" + MESSAGE + "' to the topic: " + "'test/testing'")
print('Publish End')
disconnect_future = mqtt_connection.disconnect()
disconnect_future.result()

