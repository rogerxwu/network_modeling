from ncclient import manager
#from pyang import FileRepository
#from pyang.util import yanglint

# Define the YANG models for different vendor devices
yang_model = './juniper/openconfig-config.yang'

# Validate the YANG models
""" repo = FileRepository(yang_model)
yanglint(['--strict', '-p', repo.get_root()], yang_model) """

network_devices = [
    {
        'ip': '192.168.223.2',
        'port': '22',
        'username': 'admin',
        'password': '1qaz2wsx'
    }
]
# Connect to each network device and retrieve the configuration
for device in network_devices:
    try:
        # Connect to the device using NETCONF
        device_connection = manager.connect(
            host=device['ip'],
            port=device['port'],
            username=device['username'],
            password=device['password'],
            hostkey_verify=False,
        )

        # Retrieve the device configuration using NETCONF get-config operation
        config = device_connection.get_config(source='running').data_xml

        # Process the configuration as needed
        print(config)

        # Close the NETCONF session
        device_connection.close_session()

    except Exception as e:
        print(f"Failed to retrieve configuration for {device['ip']}: {str(e)}")