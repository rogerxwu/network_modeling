# Network Modeling

# Terminology
OpenConfig(https://www.openconfig.net/docs/) is a collaborative effort in the networking industry to move toward a more dynamic, programmable method for configuring and managing multivendor networks. OpenConfig supports the use of vendor-neutral data models to configure and manage the network. These data models define the configuration and operational state of network devices for common network protocols or services. The data models are written in YANG, a standards-based, data modeling language that is modular, easy to read, and supports remote procedure calls (RPCs). Using industry standard models greatly benefits an operator with devices in a network from multiple vendors. The goal of OpenConfig is for operators to be able to use a single set of data models to configure and manage all the network devices that support the OpenConfig initiative.

YANG Data Modeling Language: Yet Another Next Generation

gRPC: google remote procedure call is a framework that brings performance benefits and modern features to client-server applications
streaming RPCs
gNMI: gRPC Network Management Interface is a Google Protocol RPC (gRPC) based protocol to manage network devices.
gNOI: gRPC Network Operations Interface (gNOI) defines a set of gRPC-based microservices for executing operational commands on network devices.
Protocol Buffers(https://protobuf.dev/): Protocol Buffers are a language-neutral, platform-neutral extensible mechanism for serializing structured data

Juniper YANG Model: https://github.com/Juniper/yang
Arista YANG Model: https://github.com/aristanetworks/yang
Cisco YANG Model: https://github.com/YangModels/yang


# Requirement
1. grpc_client: ubuntu (https://github.com/openconfig/gnmic)
2. grpc_server: vSRX instance




Openconfig YANG Model:
- use openconfig YANG model the network device configuration
- generate network device configuration based on openconfig YANG
- Design intent model
- Get live model


config ? store in json database?
state
    - telemetry -> store in TSDB(time series data base) like influxDB
    - operation


To-do:
1. setup a grpc_client node
2. enable grpc on vsrx
3. dev .yang to get config
3. get config related info
4. where to store the data?