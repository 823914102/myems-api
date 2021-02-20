# MyEMS API Service

## Introduction
Providing REST API service for [MyEMS](https://github.com/MyEMS/myems) components and third parties.

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/dc671ff43f374b4a8c72f14a4462660c)](https://app.codacy.com/gh/myems/myems-api?utm_source=github.com&utm_medium=referral&utm_content=myems/myems-api&utm_campaign=Badge_Grade)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/myems/myems-api/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/myems/myems-api/?branch=master)
[![Maintainability](https://api.codeclimate.com/v1/badges/db3f8cbee8920476f3c4/maintainability)](https://codeclimate.com/github/myems/myems-api/maintainability)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/myems/myems-api.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/myems/myems-api/alerts/)


## Prerequisites

anytree

simplejson

mysql.connector

falcon

falcon_cors

gunicorn

openpyxl


## Installation

In this step, you will install myems-api on Ubuntu for production or development.

For macOS developers, please refer to [Installation on macOS (Chinese)](./installation_macos_zh.md)

* Install anytree
```
$ cd ~/tools
$ git clone https://github.com/c0fec0de/anytree.git
$ cd anytree
$ sudo python3 setup.py install 
```

* Install simplejson
```
$ cd ~/tools
$ git clone https://github.com/simplejson/simplejson.git
$ cd simplejson
$ sudo python3 setup.py install 
```

* Install MySQL Connector
```
  $ cd ~/tools
  $ wget https://dev.mysql.com/get/Downloads/Connector-Python/mysql-connector-python-8.0.20.tar.gz
  $ tar xzf mysql-connector-python-8.0.20.tar.gz
  $ cd ~/tools/mysql-connector-python-8.0.20
  $ sudo python3 setup.py install
```

* Install Falcon,

  if you are behind proxy, use --proxy parameter

  Refer to 
  
  https://falconframework.org/

  https://github.com/lwcolton/falcon-cors

  https://github.com/yohanboniface/falcon-multipart
```
  $ mkdir ~/tools/falcon && cd ~/tools/falcon
  $ pip3 download cython falcon falcon-cors falcon-multipart
  $ export LC_ALL="en_US.UTF-8"
  $ export LC_CTYPE="en_US.UTF-8"
  $ sudo dpkg-reconfigure locales
  $ sudo pip3 install --upgrade --no-index --find-links ~/tools/falcon cython falcon falcon-cors falcon-multipart
```

* Install gunicorn, refer to http://gunicorn.org
```
  $ mkdir ~/tools/gunicorn && cd ~/tools/gunicorn
  $ pip3 download gunicorn
  $ sudo pip3 install --no-index --find-links ~/tools/gunicorn gunicorn
```

* Install openpyxl, refer to https://foss.heptapod.net/openpyxl/openpyxl

Get the latest version of et_xmlfile from https://foss.heptapod.net/openpyxl/et_xmlfile

Get the latest version of jdcal from https://github.com/phn/jdcal

Get the latest version of openpyxl from https://foss.heptapod.net/openpyxl/openpyxl

```
  $ cd ~/tools  
  $ wget https://foss.heptapod.net/openpyxl/et_xmlfile/-/archive/branch/default/et_xmlfile-branch-default.tar.gz
  $ tar xzf et_xmlfile-branch-default.tar.gz
  $ cd ~/tools/et_xmlfile-branch-default
  $ sudo python3 setup.py install
  $ cd ~/tools
  $ git clone https://github.com/phn/jdcal.git
  $ cd ~/tools/jdcal
  $ sudo python3 setup.py install
  $ mkdir ~/tools/pillow && cd ~/tools/pillow 
  $ pip3 download Pillow
  $ sudo pip3 install --no-index --find-links ~/tools/pillow Pillow
  $ cd ~/tools
  $ wget https://foss.heptapod.net/openpyxl/openpyxl/-/archive/branch/3.0/openpyxl-branch-3.0.tar.gz
  $ tar xzf openpyxl-branch-3.0.tar.gz
  $ cd openpyxl-branch-3.0
  $ sudo python3 setup.py install
```

* Install gunicorn service for myems-api:
```
  $ cd ~/myems-api
  $ sudo cp -R ~/myems-api /myems-api
```
  Check and change the config file if necessary:
```
  $ sudo nano /myems-api/config.py
```
   Change the listening port (default is 8000) in gunicorn.socket:
```
   $ sudo nano /myems-api/gunicorn.socket
ListenStream=0.0.0.0:8000
    $ sudo ufw allow 8000
```
   Setup systemd configure files:
```
   $ sudo cp /myems-api/gunicorn.service /lib/systemd/system/
   $ sudo cp /myems-api/gunicorn.socket /lib/systemd/system/
   $ sudo cp /myems-api/gunicorn.conf /usr/lib/tmpfiles.d/
```
   Next enable the services so they autostart at boot:
```
   $ sudo systemctl enable gunicorn.socket
   $ sudo systemctl enable gunicorn.service
```
   Start the services :
```
   $ sudo systemctl start gunicorn.socket
   $ sudo systemctl start gunicorn.service
```

## Run for debugging and testing
```
$ cd myems-api
$ sudo gunicorn -b 127.0.0.1:8000 app:api
```

## API List

View in Postman: import the file MyEMS.postman_collection.json with Postman


[Energy Category](#Energy-Category) | [Energy Item](#Energy-Item)

[Data Source](#Data-Source) | [Point](#Point)

[Tariff](#Tariff) | [Cost Center](#Cost-Center)

[Meter](#Meter) | [Virtual Meter](#Virtual-Meter) | [Offline Meter](#Offline-Meter) | [Offline Meter File](#Offline-Meter-File) 

[Space](#Space) | [Tenant](#Tenant) | [Tenant Type](#Tenant-Type) | [Store](#Store) | [Store Type](#Store-Type) | [Shopfloor](#Shopfloor) 

[Equipment](#Equipment) | [Combined Equipment](#Combined-Equipment)

[Energy Flow Diagram](#Energy-Flow-Diagram)

[Distribution System](#Distribution-System) | [Distribution Circuit](#Distribution-Circuit)

[Rule](#Rule) | [Email Message](#Email Message) | [Text Message](#Text Message) | [Web Message](#Web Message) | [Wechat Message](#Wechat Message)

[Email Server](#Email Server) | [GSM Modem](#GSM Modem)

[User](#User) | [Privilege](#Privilege) | [Contact](#Contact)  | [Notification](#Notification)

[Timezone](#Timezone)

[Knowledge File](#Knowledge-File)

[Reports](#Reports)


### Contact
* GET Contact by ID
```bash
$ curl -i -X GET {{base_url}}/contacts/{id}
```
* GET All Contacts
```bash
$ curl -i -X GET {{base_url}}/contacts
```
* DELETE Contact by ID
```bash
$ curl -i -X DELETE {{base_url}}/contacts/{id}
```
* POST Create a New Contact
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"name":"albert", "email":"albert@myems.io", "phone":"+8613888888888", "description":"contact description"}}' {{base_url}}/contacts
```
* PUT Update a Contact
```bash
$ curl -i -H "Content-Type: application/json" -X PUT -d '{"data":{"name":"albert", "email":"albert@myems.io", "phone":"+8613888888899", "description":"contact description"}}' {{base_url}}/contacts/{id}
```

### Cost Center
* GET Cost Center by ID

```bash
$ curl -i -X GET {{base_url}}/costcenters/{id}
```
Result in JSON

| Name          | Data Type | Description                               |
|---------------|-----------|-------------------------------------------|
| id            | integer   | Cost Center ID                            |
| name          | string    | Cost Center name                          |
| uuid          | string    | Cost Center UUID                          |
| external_id   | string    | Cost Center External ID ( For example, ID in SAP, ERP...) |

* GET all Cost Centers
```bash
$ curl -i -X GET {{base_url}}/costcenters
```
* DELETE Cost Center by ID
```bash
$ curl -i -X DELETE {{base_url}}/costcenters/{id}
```
* POST Create New Cost Center
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"name":"动力中心", "external_id":"21829198980001"}}' {{base_url}}/costcenters
```
* PUT Update a Cost Center
```bash
$ curl -i -H "Content-Type: application/json" -X PUT -d '{"data":{"name":"动力中心2", "external_id":"21829198980002"}}' {{base_url}}/costcenters/{id}
```
* GET All Tariffs associated with Cost Center ID
```bash
$ curl -i -X GET {{base_url}}/costcenters/{id}/tariffs
```
* POST Create a Cost Center and Tariff Relation
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"tariff_id":"3"}}' {{base_url}}/costcenters/{id}/tariffs
```
* DELETE a Cost Center and Tariff Relation by tid
```bash
$ curl -i -X DELETE {{base_url}}/costcenters/{id}/tariffs/{tid}
```

### Data Source
* GET Data Source by ID

```bash
$ curl -i -X GET {{base_url}}/datasources/{id}
```
Result in JSON

| Name          | Data Type | Description                               |
|---------------|-----------|-------------------------------------------|
| id            | integer   | Data Source ID                            |
| name          | string    | Data Source name                          |
| gateway       | object    | Gateway                                   |
| uuid          | string    | Data Source UUID                          |
| protocol      | string    | Protocol Type Supported: 'modbus-tcp', 'modbus-rtu', 'bacnet-ip', 's7', 'profibus', 'profinet', 'opc-ua', 'lora', 'simulation', 'controllogix', 'weather' |
| connection    | json      | Connection data in JSON. BACnet/IP example: {"host":"10.1.2.88"}, Modbus TCP example: {"host":"10.1.2.88", "port":502}, S7 example: {"host":"10.1.2.202", "port":102, "rack": 0, "slot": 2}, ControlLogix example: {"host":"10.1.2.88","port":44818,"processorslot":3} OPC UA example: {"url":"opc.tcp://10.1.2.5:49320/OPCUA/SimulationServer/"} |
| last_seen_datetime| float | Indicates the last time when the data source was seen in a number of milliseconds since January 1, 1970, 00:00:00, universal time |
| status        | string    | 'online' or 'offline' determined by last seen datetime|

* GET all Data Sources
```bash
$ curl -i -X GET {{base_url}}/datasources
```
* DELETE Data Source by ID
```bash
$ curl -i -X DELETE {{base_url}}/datasources/{id}
```
* POST Data Source
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"name":"Modbus1", "gateway_id":1, "protocol":"modbus-tcp", "connection":"{\"host\":\"10.1.2.88\", \"port\":502}"}}' {{base_url}}/datasources
```
* PUT Data Source
```bash
$ curl -i -H "Content-Type: application/json" -X PUT -d '{"data":{"name":"Modbus1", "gateway_id":1, "protocol":"modbus-tcp", "connection":"{\"host\":\"10.1.2.99\", \"port\":502}"}}' {{base_url}}/datasources/{id}
```
* GET all points of the Data Source by ID
```bash
$ curl -i -X GET {{base_url}}/datasources/{id}/points
```

### Distribution Circuit
* GET Distribution Circuit by ID

```bash
$ curl -i -X GET {{base_url}}/distributioncircuits/{id}
```
Result in JSON

| Name          | Data Type | Description                               |
|---------------|-----------|-------------------------------------------|
| id            | integer   | Distribution Circuit ID                   |
| name          | string    | Distribution Circuit name                 |
| uuid          | string    | Distribution Circuit UUID                 |
| distribution_system| object | Distribution System Object              |
| distribution_room| string | Distribution Room                         |
| switchgear    | string    | Switchgear                                |
| peak_load     | decimal(18,3)| Peak Load (KW)                         |
| peak_current  | decimal(18,3)| Peak Current (A)                       |
| customers     | string    | Customers or users                        |
| meters        | string    | Meters (output or next level)             |

* GET all Distribution Circuits
```bash
$ curl -i -X GET {{base_url}}/distributioncircuits
```
* DELETE a Distribution Circuit by ID
```bash
$ curl -i -X DELETE {{base_url}}/distributioncircuits/{id}
```
* POST Create new Distribution Circuit
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"name":"51W91", "distribution_system_id":1, "distribution_room":"EW1", "switchgear":"51AL9", "peak_load": 30, "peak_current": 53.6, "customers": "地下室应急照明", "meters": "ALE-1102, ALE-1082"}}' {{base_url}}/distributioncircuits
```
* PUT Update a Distribution Circuit
```bash
$ curl -i -H "Content-Type: application/json" -X PUT -d '{"data":{"name":"51W92", "distribution_system_id":1, "distribution_room":"EW1", "switchgear":"51AL9", "peak_load": 30, "peak_current": 53.6, "customers": "地下室应急照明", "meters": "ALE-1102, ALE-1082"}}' {{base_url}}/distributioncircuits/{id}
```
* GET All Points associated with Distribution Circuit ID
```bash
$ curl -i -X GET {{base_url}}/distributioncircuits/{id}/points
```
* POST Bind Point to Distribution Circuit
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"point_id":"3"}}' {{base_url}}/distributioncircuits/{id}/points
```
* DELETE Unbind Point from Distribution Circuit
```bash
$ curl -i -X DELETE {{base_url}}/distributioncircuits/{id}/points/{pid}
```

### Distribution System
* GET Distribution System by ID

```bash
$ curl -i -X GET {{base_url}}/distributionsystems/{id}
```
Result in JSON

| Name          | Data Type | Description                               |
|---------------|-----------|-------------------------------------------|
| id            | integer   | Distribution System ID                    |
| name          | string    | Distribution System name                  |
| uuid          | string    | Distribution System UUID                  |
| svg           | string    | SVG file in plain text                    |
| description   | string    | Description (allow None)                  |

* GET all Distribution Systems
```bash
$ curl -i -X GET {{base_url}}/distributionsystems
```
* DELETE a Distribution System by ID
```bash
$ curl -i -X DELETE {{base_url}}/distributionsystems/{id}
```
* POST Create new Distribution System
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"name":"示例配电系统", "svg":"<?xml version=\"1.0\" encoding=\"UTF-8\"?><svg width=\"5cm\" height=\"4cm\" version=\"1.1\" xmlns=\"http://www.w3.org/2000/svg\"><desc>Four separate rectangles</desc><rect x=\".5cm\" y=\".5cm\" width=\"2cm\" height=\"1cm\"/></svg>", "description":"demo description"}}' {{base_url}}/distributionsystems
```
* PUT Update a Distribution System
```bash
$ curl -i -H "Content-Type: application/json" -X PUT -d '{"data":{"name":"示例配电系统", "svg":"<?xml version=\"1.0\" encoding=\"UTF-8\"?><svg width=\"5cm\" height=\"4cm\" version=\"1.1\" xmlns=\"http://www.w3.org/2000/svg\"><desc>Four separate rectangles</desc><rect x=\".5cm\" y=\".5cm\" width=\"2cm\" height=\"1cm\"/></svg>", "description":"demo description"}}' {{base_url}}/distributionsystems/{id}
```
* GET All Distribution Circuits associated with Distribution Circuit
```bash
$ curl -i -X GET {{base_url}}/distributionsystems/{id}/distributioncircuits
```

### Email Message
* GET an Email Message by ID

Result in JSON

| Name          | Data Type | Description                               |
|---------------|-----------|-------------------------------------------|
| id            | integer   | Email Message ID                          |
| recipient_name| string    | Recipient Name                            |
| recipient_email| string   | Recipient Email                           |
| subject       | string    | Email Message Subject                     |
| message       | string    | Email Message Body                        |
| attachment_file_name| string| Email Attachment File Name              |
| create_datetime| float    | Email Message Created Datetime (POSIX timestamp * 1000)|
| scheduled_datetime| float | Email Message Scheduled Datetime (POSIX timestamp * 1000)|
| status        | string    | Status ('new', 'sent', 'timeout'          |

```bash
$ curl -i -X GET {{base_url}}/emailmessages/{id}
```
* GET Email Messages from Startdate to Enddate
```bash
$ curl -i -X GET {{base_url}}/emailmessages/from/{startdate}/to/{enddate}
```
* DELETE an Email Message by ID
```bash
$ curl -i -X DELETE {{base_url}}/emailmessages/{id}
```


### Email Server
* GET an Email Server by ID

```bash
$ curl -i -X GET {{base_url}}/emailservers/{id}
```
Result in JSON

| Name          | Data Type | Description                           |
|---------------|-----------|---------------------------------------|
| id            | integer   | Email Server ID                       |
| host          | string    | Email Server host                     |
| port          | integer   | Email Server port                     |
| requires_authentication   | boolean | Indicates if the server requires authentication |
| user_name     | string    | Email Server user name                |
| password      | string    | Email Server password                 |
| from_addr     | string    | Indicates from which email address to send emails |

* GET All Email Servers
```bash
$ curl -i -X GET {{base_url}}/emailservers
```
* DELETE an Email Server by ID
```bash
$ curl -i -X DELETE {{base_url}}/emailservers/{id}
```
* POST Create New Email Server
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"host":"smtp.163.com","port":25, "requires_authentication":true, "user_name":"myems" , "password":"!MyEMS1" , "from_addr":"myems@163.com"}}' {{base_url}}/emailservers
```
* PUT Update an Email Server
```bash
$ curl -i -H "Content-Type: application/json" -X PUT -d '{"data":{"host":"smtp.myems.io","port":25, "requires_authentication":true, "user_name":"myems" , "password":"!MyEMS1" , "from_addr":"myems@myems.io"}}' {{base_url}}/emailservers/{id}
```


### Energy Category
* GET an Energy Category by ID

```bash
$ curl -i -X GET {{base_url}}/energycategories/{id}
```
Result in JSON

| Name          | Data Type | Description                               |
|---------------|-----------|-------------------------------------------|
| id            | integer   | Energy Category ID                        |
| name          | string    | Energy Category name                      |
| uuid          | string    | Energy Category UUID                      |
| unit_of_measure   | string| Unit of measure                           |
| kgce          | string    | KG coal equivalent                        |
| kgco2e        | string    | KG Carbon dioxide equivalent              |


* GET All Energy Categories
```bash
$ curl -i -X GET {{base_url}}/energycategories
```
* DELETE an Energy Category by ID
```bash
$ curl -i -X DELETE {{base_url}}/energycategories/{id}
```
* POST Create an Energy Category
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"name":"电","unit_of_measure":"kWh", "kgce":0.1229 , "kgco2e":0.8825}}' {{base_url}}/energycategories
```
* PUT Update an Energy Category
```bash
$ curl -i -H "Content-Type: application/json" -X PUT -d '{"data":{"name":"电","unit_of_measure":"kWh", "kgce":0.1329 , "kgco2e":0.9825}}' {{base_url}}/energycategories/{id}
```


### Energy Flow Diagram
* GET an Energy Flow Diagram by ID
```bash
$ curl -i -X GET {{base_url}}/energyflowdiagrams/{id}
```
Result

| Name          | Data Type | Description                               |
|---------------|-----------|-------------------------------------------|
| id            | integer   | Equipment ID                              |
| name          | string    | Equipment name                            |
| uuid          | string    | Equipment UUID                            |

* GET All Energy Flow Diagrams
```bash
$ curl -i -X GET {{base_url}}/energyflowdiagrams
```
* DELETE an Energy Flow Diagram by ID
```bash
$ curl -i -X DELETE {{base_url}}/energyflowdiagrams/{id}
```
* POST Create an Energy Flow Diagram
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"name":"MyEMS Energy Flow"}}' {{base_url}}/energyflowdiagrams
```
* PUT Update an Energy Flow Diagram
```bash
$ curl -i -H "Content-Type: application/json" -X PUT -d '{"data":{"name":"MyEMS Energy Flow Diagram"}}' {{base_url}}/energyflowdiagrams/{id}
```
* GET All Nodes of an Energy Flow Diagram by ID
```bash
$ curl -i -X GET {{base_url}}/energyflowdiagrams/{id}/nodes
```
* POST Create a Node of an Energy Flow Diagram
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"name":"10KV#1"}}' {{base_url}}/energyflowdiagrams/{id}/nodes
```
* PUT Update a Node of an Energy Flow Diagram
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"name":"10KV#2"}}' {{base_url}}/energyflowdiagrams/{id}/nodes/{nid}
```
* DELETE a Node of an Energy Flow Diagram
```bash
$ curl -i -X DELETE {{base_url}}/energyflowdiagrams/{id}/nodes/{nid}
```
* GET All Links of an Energy Flow Diagram by ID
```bash
$ curl -i -X GET {{base_url}}/energyflowdiagrams/{id}/links
```
* POST Create a Link of an Energy Flow Diagram
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"source_node_id":1, "target_node_id":3, "meter_uuid":"d806a78d-a31e-4833-b5c8-81261cfeb1f2"}}' {{base_url}}/energyflowdiagrams/{id}/links
```
* PUT Update a Link of an Energy Flow Diagram
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"source_node_id":1, "target_node_id":4, "meter_uuid":"d806a78d-a31e-4833-b5c8-81261cfeb1f2"}}' {{base_url}}/energyflowdiagrams/{id}/links/{lid}
```
* DELETE a Link of an Energy Flow Diagram
```bash
$ curl -i -X DELETE {{base_url}}/energyflowdiagrams/{id}/links/{lid}
```


### Energy Item
* GET an Energy Item by ID

```bash
$ curl -i -X GET {{base_url}}/energyitems/{id}
```
Result in JSON

| Name          | Data Type | Description                           |
|---------------|-----------|---------------------------------------|
| id            | integer   | Energy Item ID                        |
| name          | string    | Energy Item name                      |
| uuid          | string    | Energy Item UUID                      |
| Energy Category| object | Energy Category Object                  |


* GET All Energy Items
```bash
$ curl -i -X GET {{base_url}}/energyitems
```
* DELETE an Energy Item by ID
```bash
$ curl -i -X DELETE {{base_url}}/energyitems/{id}
```
* POST Create an Energy Item
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"name":"空调用电","energy_category_id":1}}' {{base_url}}/energyitems
```
* PUT Update an Energy Item
```bash
$ curl -i -H "Content-Type: application/json" -X PUT -d '{"data":{"name":"动力用电","energy_category_id":1}}' {{base_url}}/energyitems/{id}
```


### Equipment
* GET Equipment by ID
```bash
$ curl -i -X GET {{base_url}}/equipments/{id}
```
Result

| Name          | Data Type | Description                               |
|---------------|-----------|-------------------------------------------|
| id            | integer   | Equipment ID                              |
| name          | string    | Equipment name                            |
| uuid          | string    | Equipment UUID                            |
| is_input_counted | boolean | Indicates if the Equipment's energy input is counted for aggregating|                        |
| is_output_counted | boolean | Indicates if the Equipment's energy output is counted for aggregating|                        |
| cost_center   | Object    | Cost Center Object                        |
| description   | string    | Equipment description                     |

* GET All Equipments
```bash
$ curl -i -X GET {{base_url}}/equipments
```
* DELETE an Equipment by ID
```bash
$ curl -i -X DELETE {{base_url}}/equipments/{id}
```
* POST Create an Equipment
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"name":"MyEMS Chiller", "is_input_counted":true, "is_output_counted":false, "cost_center_id":1, "description":"equipment description"}}' {{base_url}}/equipments
```
* PUT Update an Equipment
```bash
$ curl -i -H "Content-Type: application/json" -X PUT -d '{"data":{"name":"MyEMS Chiller", "is_input_counted":true, "is_output_counted":true, "cost_center_id":1, "description":"equipment description"}}' {{base_url}}/equipments/{id}
```
* POST Clone an Equipment
```bash
$ curl -i -H "Content-Type: application/json" -X PUT -d '{"data":{}}' {{base_url}}/equipments/{id}
```
* GET All Meters of an Equipment by ID
```bash
$ curl -i -X GET {{base_url}}/equipments/{id}/meters
```
* POST Bind a Meter to an Equipment
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"meter_id":1}}' {{base_url}}/equipments/{id}/meters
```
* DELETE a Meter from an Equipment
```bash
$ curl -i -X DELETE {{base_url}}/equipments/{id}/meters/{mid}
```
* GET All Parameters of an Equipment by ID
```bash
$ curl -i -X GET {{base_url}}/equipments/{id}/parameters
```
* GET a Parameter of an Equipment by ID
```bash
$ curl -i -X GET {{base_url}}/equipments/{id}/parameters/{pid}
```
Result

| Name          | Data Type | Description                               |
|---------------|-----------|-------------------------------------------|
| id            | integer   | Parameter ID                              |
| name          | string    | Parameter name                            |
| parameter_type | string   | Parameter Type: constant, point, meter    |
| is_input_counted  | boolean | Indicates if the equipment's energy input is counted for aggregating|                        |
| is_output_counted | boolean | Indicates if the equipment's energy output is counted for aggregating|                        |
| constant            | string    | Parameter constant value            |
| point               | object    | Parameter point object              |
| numerator_meter     | object    | Parameter numerator meter object    |
| denominator_meter   | object    | Parameter numerator meter object    |

* POST Create a constant Parameter for an Equipment
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"name":"test parameter", "parameter_type":"constant", "constant":"test constant", "point_id":null, "numerator_meter_uuid":null, "denominator_meter_uuid":null}}' {{base_url}}/equipments/{id}/parameters
```
* POST Create a point Parameter for an Equipment
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"name":"test parameter", "parameter_type":"point", "constant":null, "point_id":1, "numerator_meter_uuid":null, "denominator_meter_uuid":null}}' {{base_url}}/equipments/{id}/parameters
```
* POST Create a meter Parameter for an Equipment
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"name":"test parameter", "parameter_type":"fraction", "constant":null, "point_id":null, "numerator_meter_uuid":"89ff5118-d0c2-4dd8-8098-a8698189b2ea", "denominator_meter_uuid":"5ca62d2a-908e-40c5-a6b5-a8e436d60db4"}}' {{base_url}}/equipments/{id}/parameters
```
* DELETE a Parameter from an Equipment
```bash
$ curl -i -X DELETE {{base_url}}/equipments/{id}/parameters/{pid}
```
* GET All Offline Meters of an Equipment by ID
```bash
$ curl -i -X GET {{base_url}}/equipments/{id}/offlinemeters
```
* POST Bind an Offline Meter to an Equipment
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"offline_meter_id":1}}' {{base_url}}/equipments/{id}/offlinemeters
```
* DELETE an Offline Meter from an Equipment
```bash
$ curl -i -X DELETE {{base_url}}/equipments/{id}/offlinemeters/{mid}
```
* GET All Virtual Meters of an Equipment by ID
```bash
$ curl -i -X GET {{base_url}}/equipments/{id}/virtualmeters
```
* POST Bind an Virtual Meter to an Equipment
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"virtual_meter_id":1}}' {{base_url}}/equipments/{id}/virtualmeters
```
* DELETE an Virtual Meter from an Equipment
```bash
$ curl -i -X DELETE {{base_url}}/equipments/{id}/virtualmeters/{mid}
```

### Combined Equipment
* GET a Combined Equipment by ID
```bash
$ curl -i -X GET {{base_url}}/combinedequipments/{id}
```
Result

| Name          | Data Type | Description                               |
|---------------|-----------|-------------------------------------------|
| id            | integer   | Combined Equipment ID                     |
| name          | string    | Combined Equipment name                   |
| uuid          | string    | Combined Equipment UUID                   |
| is_input_counted | boolean | Indicates if the combined equipment's energy input is counted for aggregating|                        |
| is_output_counted | boolean | Indicates if the combined equipment's energy output is counted for aggregating|                        |
| cost_center   | Object    | Cost Center Object                        |
| description   | string    | Combined Equipment description            |

* GET All Equipments
```bash
$ curl -i -X GET {{base_url}}/combinedequipments
```
* DELETE a Combined Equipment by ID
```bash
$ curl -i -X DELETE {{base_url}}/combinedequipments/{id}
```
* POST Create a Combined Equipment
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"name":"MyEMS Chiller Plant", "is_input_counted":true, "is_output_counted":false, "cost_center_id":1, "description":"equipment description"}}' {{base_url}}/combinedequipments
```
* PUT Update a Combined Equipment
```bash
$ curl -i -H "Content-Type: application/json" -X PUT -d '{"data":{"name":"MyEMS Chiller Plant", "is_input_counted":true, "is_output_counted":true, "cost_center_id":1, "description":"equipment description"}}' {{base_url}}/combinedequipments/{id}
```
* POST Clone a Combined Equipment
```bash
$ curl -i -H "Content-Type: application/json" -X PUT -d '{"data":{}}' {{base_url}}/combinedequipments/{id}
```
* GET All Equipments of a Combined Equipment by ID
```bash
$ curl -i -X GET {{base_url}}/combinedequipments/{id}/equipments
```
* POST Bind an Equipment to a Combined Equipment
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"equipment_id":1}}' {{base_url}}/combinedequipments/{id}/equipments
```
* DELETE an Equipment from a Combined Equipment
```bash
$ curl -i -X DELETE {{base_url}}/combinedequipments/{id}/equipments/{eid}
```
* GET All Meters of a Combined Equipment by ID
```bash
$ curl -i -X GET {{base_url}}/combinedequipments/{id}/meters
```
* POST Bind a Meter to a Combined Equipment
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"meter_id":1}}' {{base_url}}/combinedequipments/{id}/meters
```
* DELETE a Meter from a Combined Equipment
```bash
$ curl -i -X DELETE {{base_url}}/combinedequipments/{id}/meters/{mid}
```
* GET All Parameters of a Combined Equipment by ID
```bash
$ curl -i -X GET {{base_url}}/combinedequipments/{id}/parameters
```
* GET a Parameter of a Combined Equipment by ID
```bash
$ curl -i -X GET {{base_url}}/combinedequipments/{id}/parameters/{pid}
```
Result

| Name          | Data Type | Description                               |
|---------------|-----------|-------------------------------------------|
| id            | integer   | Parameter ID                              |
| name          | string    | Parameter name                            |
| parameter_type | string   | Parameter Type: constant, point, meter    |
| is_input_counted  | boolean | Indicates if the Combined Equipment's energy input is counted for aggregating|                        |
| is_output_counted | boolean | Indicates if the Combined Equipment's energy output is counted for aggregating|                        |
| constant            | string    | Parameter constant value            |
| point               | object    | Parameter point object              |
| numerator_meter     | object    | Parameter numerator meter object    |
| denominator_meter   | object    | Parameter numerator meter object    |

* POST Create a constant Parameter for a Combined Equipment
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"name":"test parameter", "parameter_type":"constant", "constant":"test constant", "point_id":null, "numerator_meter_uuid":null, "denominator_meter_uuid":null}}' {{base_url}}/combinedequipments/{id}/parameters
```
* POST Create a point Parameter for a Combined Equipment
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"name":"test parameter", "parameter_type":"point", "constant":null, "point_id":1, "numerator_meter_uuid":null, "denominator_meter_uuid":null}}' {{base_url}}/combinedequipments/{id}/parameters
```
* POST Create a meter Parameter for a Combined Equipment
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"name":"test parameter", "parameter_type":"fraction", "constant":null, "point_id":null, "numerator_meter_uuid":"89ff5118-d0c2-4dd8-8098-a8698189b2ea", "denominator_meter_uuid":"5ca62d2a-908e-40c5-a6b5-a8e436d60db4"}}' {{base_url}}/combinedequipments/{id}/parameters
```
* DELETE a Parameter from a Combined Equipment
```bash
$ curl -i -X DELETE {{base_url}}/combinedequipments/{id}/parameters/{pid}
```
* GET All Offline Meters of a Combined Equipment by ID
```bash
$ curl -i -X GET {{base_url}}/combinedequipments/{id}/offlinemeters
```
* POST Bind an Offline Meter to a Combined Equipment
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"offline_meter_id":1}}' {{base_url}}/combinedequipments/{id}/offlinemeters
```
* DELETE an Offline Meter from a Combined Equipment
```bash
$ curl -i -X DELETE {{base_url}}/combinedequipments/{id}/offlinemeters/{mid}
```
* GET All Virtual Meters of a Combined Equipment by ID
```bash
$ curl -i -X GET {{base_url}}/combinedequipments/{id}/virtualmeters
```
* POST Bind an Virtual Meter to a Combined Equipment
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"virtual_meter_id":1}}' {{base_url}}/combinedequipments/{id}/virtualmeters
```
* DELETE an Virtual Meter from a Combined Equipment
```bash
$ curl -i -X DELETE {{base_url}}/combinedequipments/{id}/virtualmeters/{mid}
```


### Gateway
* GET Gateway by ID

```bash
$ curl -i -X GET {{base_url}}/gateways/{id}
```
Result in JSON

| Name          | Data Type | Description                               |
|---------------|-----------|-------------------------------------------|
| id            | integer   | Gateway ID                                |
| name          | string    | Gateway name                              |
| uuid          | string    | Data Source UUID                          |
| token         | string    | Data Source Token                         |
| last_seen_datetime| float | Indicates the last time when the gateway was seen in a number of milliseconds since January 1, 1970, 00:00:00, universal time |
| status        | string    | 'online' or 'offline' determined by last seen datetime|

* GET all Gateways
```bash
$ curl -i -X GET {{base_url}}/gateways
```
* DELETE Gateway by ID
```bash
$ curl -i -X DELETE {{base_url}}/gateways/{id}
```
* POST Gateway
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"name":"MyEMS Gateway 1"}}' {{base_url}}/gateways
```
* PUT Gateway
```bash
$ curl -i -H "Content-Type: application/json" -X PUT -d '{"data":{"name":"MyEMS Gateway #1"}}' {{base_url}}/gateways/{id}
```
* GET all data sources of the Gateway by ID
```bash
$ curl -i -X GET {{base_url}}/gateways/{id}/datasources
```

### GSM Modem
* GET a GSM Modem by ID

```bash
$ curl -i -X GET {{base_url}}/gsmmodems/{id}
```
Result in JSON

| Name          | Data Type | Description                           |
|---------------|-----------|---------------------------------------|
| id            | integer   | GSM Modem ID                          |
| serial_port   | string    | GSM Modem serial port                 |
| baud_rate     | integer   | GSM Modem baud rate                   |

* GET All GSM Modems
```bash
$ curl -i -X GET {{base_url}}/gsmmodems
```
* DELETE a GSM Modem by ID
```bash
$ curl -i -X DELETE {{base_url}}/gsmmodems/{id}
```
* POST Create New GSM Modem
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"serial_port":"/dev/ttyS0","baud_rate":115200}}' {{base_url}}/gsmmodems
```
* PUT Update a GSM Modem
```bash
$ curl -i -H "Content-Type: application/json" -X PUT -d '{"data":{"serial_port":"/dev/ttyS0","baud_rate":115200}}' {{base_url}}/gsmmodems/{id}
```


### Knowledge File
* GET Knowledge File by ID

```bash
$ curl -i -X GET {{base_url}}/knowledgefiles/{id}
```
Result

| Name          | Data Type | Description                               |
|---------------|-----------|-------------------------------------------|
| id            | integer   | Knowledge File ID                         |
| file_name     | string    | Knowledge File name                       |
| uuid          | string    | Knowledge File UUID                       |
| upload_datetime | float | the number of milliseconds since January 1, 1970, 00:00:00, universal time |
| user_display_name | string| Upload user's display name                |
| file_object   | BLOB      | Knowledge File Object                     |

* GET All Knowledge Files
```bash
$ curl -i -X GET {{base_url}}/knowledgefiles
```
* DELETE a Knowledge File by id
```bash
$ curl -i -X DELETE {{base_url}}/knowledgefiles/{id}
```
* POST Upload a Knowledge File
 (user must login first to get cookie)
```bash
$ curl -i -H "Content-Type: application/TBD" -X POST -d 'file: (binary)' {{base_url}}/knowledgefiles
```
* GET Restore a Knowledge File by id from database to disk
```bash
$ curl -i -X GET {{base_url}}/knowledgefiles/{id}/restore
```

### Meter
* GET Meter by ID

```bash
$ curl -i -X GET {{base_url}}/meters/{id}
```
Result

| Name          | Data Type | Description                               |
|---------------|-----------|-------------------------------------------|
| id            | integer   | Meter ID                                  |
| name          | string    | Meter name                                |
| uuid          | string    | Meter UUID                                |
| energy_category| Object   | Energy Category Object                    |
| is_counted    | boolean   | Meter is counted in associated unit       |
| hourly_low_limit  | decimal(18,3)   | Inclusive. Default is 0. If the meter has accuracy problems, set the value to a small positive value, such as 0.100|
| hourly_high_limit | decimal(18,3)   | Inclusive. Maximum energy consumption per hour, Rated total active Power, Rated Flow, etc.|
| cost_center   | Object    | Cost Center Object                        |
| energy_item   | Object    | Energy Item Object                        |
| master_meter  | Object    | Master Meter Object                       |
| description   | string    | Meter description                         |

* GET All Meters
```bash
$ curl -i -X GET {{base_url}}/meters
```
* DELETE Meter by ID
```bash
$ curl -i -X DELETE {{base_url}}/meters/{id}
```
* POST Create a Meter
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"name":"PM20", "energy_category_id":1, "hourly_low_limit":0.000, "hourly_high_limit":999.999, "is_counted":true, "cost_center_id":1, "energy_item_id":1, "master_meter_id":1, "description":"空调用电"}}' {{base_url}}/meters
```
* PUT Update a Meter
```bash
$ curl -i -H "Content-Type: application/json" -X PUT -d '{"data":{"name":"PM20", "energy_category_id":1, "hourly_low_limit":0.000, "hourly_high_limit":999.999, "is_counted":true, "cost_center_id":1, "energy_item_id":1, "master_meter_id":1, "description":"空调用电"}}' {{base_url}}/meters/{id}
```
* GET All Submeters of Meter by ID
```bash
$ curl -i -X GET {{base_url}}/meters/{id}/submeters
```
* GET All Points associated with Meter ID
```bash
$ curl -i -X GET {{base_url}}/meters/{id}/points
```
* POST Meter Point Relation
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"point_id":"3"}}' {{base_url}}/meters/{id}/points
```
* DELETE Meter Point Relation
```bash
$ curl -i -X DELETE {{base_url}}/meters/{id}/points/{pid}
```


### Notification
NOTE: Login before call these APIs, and then update User-UUID and Token in Headers

* GET a Notification by ID

```bash
$ curl -i -X GET {{base_url}}/notifications/{id}
```
Result

| Name          | Data Type | Description                               |
|---------------|-----------|-------------------------------------------|
| id            | integer   | Notification ID                           |
| created_datetime| string  | Created Datetime                          |
| status        | string    | Notification Status (unread, read, archived)| 
| subject       | string    | Notification Subject                      | 
| message       | string    | Notification Message                      |
| url           | string    | Notification URL                          |

* GET All Notifications
```bash
$ curl -i -H "User-UUID: dcdb67d1-6116-4987-916f-6fc6cf2bc0e4" -H "Token: 02f93023a39c98e1d1bc9f5197a83dfc5ddc0d48" -X GET {{base_url}}/notifications?startdatetime={startdatetime}&enddatetime={enddatetime}&status={status}
```
* DELETE Notification by ID
```bash
$ curl -i -H "User-UUID: dcdb67d1-6116-4987-916f-6fc6cf2bc0e4" -H "Token: 02f93023a39c98e1d1bc9f5197a83dfc5ddc0d48" -X DELETE {{base_url}}/notifications/{id}
```
* PUT Update a Notification
```bash
$ curl -i -H "User-UUID: dcdb67d1-6116-4987-916f-6fc6cf2bc0e4" -H "Token: 02f93023a39c98e1d1bc9f5197a83dfc5ddc0d48" -H "Content-Type: application/json" -X PUT -d '{"data":{"status":"read"}}' {{base_url}}/notifications/{id}
```
* DELETE Notification
```bash
$ curl -i -H "User-UUID: dcdb67d1-6116-4987-916f-6fc6cf2bc0e4" -H "Token: 02f93023a39c98e1d1bc9f5197a83dfc5ddc0d48" -X DELETE {{base_url}}/notifications/{id}
```

### Offline Meter
* GET Offline Meter by ID

```bash
$ curl -i -X GET {{base_url}}/offlinemeters/{id}
```
Result

| Name          | Data Type | Description                               |
|---------------|-----------|-------------------------------------------|
| id            | integer   | Offline Meter ID                          |
| name          | string    | Offline Meter name                        |
| uuid          | string    | Offline Meter UUID                        |
| energy_category| Object   | Energy Category Object                    |
| is_counted    | boolean   | Offline Meter is counted in associated unit   |
| hourly_low_limit  | decimal(18,3)   | Inclusive. Default is 0. If the meter has accuracy problems, set the value to a small positive value, such as 0.100|
| hourly_high_limit | decimal(18,3)   | Inclusive. Maximum energy consumption per hour, Rated total active Power, Rated Flow, etc.|
| cost_center   | Object    | Cost Center Object                        |
| energy_item   | Object    | Energy Item Object                        |
| description   | string    | Offline Meter description                 |

* GET All Offline Meters
```bash
$ curl -i -X GET {{base_url}}/offlinemeters
```
* DELETE Offline Meter by ID
```bash
$ curl -i -X DELETE {{base_url}}/offlinemeters/{id}
```
* POST Create a Offline Meter
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"name":"OfflinePM20", "energy_category_id":1, "is_counted":true, "hourly_low_limit":0.000, "hourly_high_limit":999.999, "cost_center_id":1, "energy_item_id":1, "description":"空调用电"}}' {{base_url}}/offlinemeters
```
* PUT Update a Offline Meter
```bash
$ curl -i -H "Content-Type: application/json" -X PUT -d '{"data":{"name":"OfflinePM20", "energy_category_id":1, "is_counted":true, "hourly_low_limit":0.000, "hourly_high_limit":999.999, "cost_center_id":1, "energy_item_id":1, "description":"空调用电"}}' {{base_url}}/offlinemeters/{id}
```

### Offline Meter File
* GET an Offline Meter File by ID

```bash
$ curl -i -X GET {{base_url}}/offlinemeterfiles/{id}
```
Result

| Name          | Data Type | Description                               |
|---------------|-----------|-------------------------------------------|
| id            | integer   | Offline Meter File ID                     |
| file_name     | string    | Offline Meter File name                   |
| uuid          | string    | Offline Meter File UUID                   |
| upload_datetime | float | the number of milliseconds since January 1, 1970, 00:00:00, universal time |
| status        | string    | Offline Meter File processing status (new, done, error)   |
| file_object   | BLOB       | Offline Meter File Object                 |

* GET All Offline Meter Files
```bash
$ curl -i -X GET {{base_url}}/offlinemeterfiles
```
* DELETE an Offline Meter File by ID
```bash
$ curl -i -X DELETE {{base_url}}/offlinemeterfiles/{id}
```
* POST Upload an Offline Meter File
 (user must login first to get cookie)
```bash
$ curl -i -H "Content-Type: application/TBD" -X POST -d 'file: (binary)' {{base_url}}/offlinemeters
```

### Point

* GET Point by ID

```bash
$ curl -i -X GET {{base_url}}/points/{id}
```
Result in JSON

| Name          | Data Type | Description                               |
|---------------|-----------|-------------------------------------------|
| id            | integer   | Point ID                                  |
| name          | string    | Point name                                |
| data_source   | object    | Data Source Object                        |
| object_type   | string    | Object Type ('ENERGY_VALUE', 'ANALOG_VALUE, 'BINARY_VALUE')   |
| units         | string    | Units of Measure                          |
| high_limit    | float     | High Limit of the Point Value             |
| low_limit     | float     | Low Limit of the Point Value              |
| ratio         | float     | Raw value will be multiplied by ratio value|                            |
| is_trend      | boolean   | The Point Value is Recorded as Trend      |
| address       | json      | Address structure varied by protocol      |
|               |           | Modbus TCP Structure                      |
| ├slave_id     | integer   | Slave ID                                  |
| ├function_code| integer   | Modbus functions:READ_COILS = 1, READ_DISCRETE_INPUTS = 2, READ_HOLDING_REGISTERS = 3, READ_INPUT_REGISTERS = 4    |
| ├offset       | integer   | Offset                                    |
| ├number_of_registers  | integer   | Number of Registers               |
| └format       | string    | Data Format. see below introductions      |
|               |           | BACnet/IP Structure                       |
| ├object_type  | string    | BACnet Object Type ('analogValue', 'analogInput', 'analogOutput', 'binaryValue', 'binaryInput', 'binaryOutput')|
| ├object_id    | integer   | BACnet Object Instance Number             |
| ├property_name| string    | BACnet Property Name ('presentValue')     |
| └property_array_index| integer/null    | BACnet Property Array Index or None of Object Type is not Array   |
| description   | string    | Point description, allow null             |

* GET all Points
```bash
$ curl -i -X GET {{base_url}}/points
```
* DELETE Point by ID
```bash
$ curl -i -X DELETE {{base_url}}/points/{id}
```
* POST Point
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"name":"ModbusPoint1", "data_source_id":1, "object_type": "ENERGY_VALUE", "units":"kWh", "low_limit":0, "high_limit":999999999, "is_trend":true, "address":"{\"slave_id\":1, \"function_code\":3, \"offset\":1, \"number_of_registers\":2, \"data_format\":\"float\"}", "description":null}}' {{base_url}}/points
```
* PUT Point
```bash
$ curl -i -H "Content-Type: application/json" -X PUT -d '{"data":{"name":"ModbusPoint1", "data_source_id":1, "object_type": "ENERGY_VALUE", "units":"kWh", "low_limit":0, "high_limit":999999999, "is_trend":true, "address":"{\"slave_id\":1, \"function_code\":3, \"offset\":1, \"number_of_registers\":2, \"data_format\":\"float\"}", "description":null}}' {{base_url}}/points/{id}
```


### Privilege
* GET Privilege by ID
```bash
$ curl -i -X GET {{base_url}}/privileges/{id}
```
* GET All Privileges
```bash
$ curl -i -X GET {{base_url}}/privileges
```
* DELETE Privilege by ID
```bash
$ curl -i -X DELETE {{base_url}}/privileges/{id}
```
* POST New Privilege
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"name":"superusers","data":"{\"spaces\":[1,2,3,5]}"}}' {{base_url}}/privileges
```
* PUT Privilege
```bash
$ curl -i -H "Content-Type: application/json" -X PUT -d '{"data":{"name":"superusers", "data":"{\"spaces\":[1, 3]}"}}' {{base_url}}/privileges/{id}
```


### Rule
* GET Rule by ID

Result in JSON

| Name          | Data Type | Description                               |
|---------------|-----------|-------------------------------------------|
| id            | integer   | Rule ID                                   |
| name          | string    | Rule Name                                 |
| uuid          | string    | Rule UUID                                 |
| fdd_code      | string    | SYSTEM01, SYSTEM02, ... SPACE01, SPACE02, ... METER01, METER02, ... |
| category      | string    | SYSTEM, SPACE, METER, TENANT, STORE, SHOPFLOOR, EQUIPMENT, COMBINEDEQUIPMENT |
| priority      | string    | CRITICAL, HIGH, MEDIUM, LOW               |
| channel       | string    | WEB, EMAIL, SMS, WECHAT, CALL             |
| expression    | string    | JSON string of diagnosed objects, points, values, and recipients |
| message_template | string | Plain text template that supports $-substitutions |
| is_enabled    | boolean   | Indicates if this rule is enabled         |

```bash
$ curl -i -X GET {{base_url}}/rules/{id}
```
* GET All Rules
```bash
$ curl -i -X GET {{base_url}}/rules
```
* DELETE a Rule by ID
```bash
$ curl -i -X DELETE {{base_url}}/rules/{id}
```
* POST Create New Rule
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"name":"Space Energy Consumption Over Limit", "fdd_code":"SPACE01", "category":"SPACE", "priority":"HIGH", "channel":"WEB", "expression":"{\"space_id\":1, \"high_limit\":1000.000}", "message_template":"%s截止到目前电耗%s，超标%s。", "is_enabled":true}}' {{base_url}}/rules
```
* PUT Update a Rule
```bash
$ curl -i -H "Content-Type: application/json" -X PUT -d '{"data":{"name":"Space Energy Consumption Over Limit", "fdd_code":"SPACE01", "category":"SPACE", "priority":"HIGH", "channel":"WEB", "expression":"{\"space_id\":1, \"high_limit\":1000.000}", "message_template":"%s截止到目前电耗%s，超标%s。", "is_enabled":true}}' {{base_url}}/rules/{id}
```


### Sensor
* GET a Sensor by ID

```bash
$ curl -i -X GET {{base_url}}/sensors/{id}
```
Result

| Name          | Data Type | Description                               |
|---------------|-----------|-------------------------------------------|
| id            | integer   | Sensor ID                                 |
| name          | string    | Sensor name                               |
| uuid          | string    | Sensor UUID                               |
| description   | string    | Sensor description                        |

* GET All Sensors
```bash
$ curl -i -X GET {{base_url}}/sensors
```
* DELETE a Sensor by ID
```bash
$ curl -i -X DELETE {{base_url}}/sensors/{id}
```
* POST Create New Sensor
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"name":"Sensor10", "description":"sensor description"}}' {{base_url}}/sensors
```
* PUT Update a Sensor
```bash
$ curl -i -H "Content-Type: application/json" -X PUT -d '{"data":{"name":"Sensor10", "description":"sensor description"}}' {{base_url}}/sensors/{id}
```
* GET All Points associated with Sensor ID
```bash
$ curl -i -X GET {{base_url}}/sensors/{id}/points
```
* POST Sensor Point Relation
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"point_id":"3"}}' {{base_url}}/sensors/{id}/points
```
* DELETE Sensor Point Relation
```bash
$ curl -i -X DELETE {{base_url}}/sensors/{id}/points/{pid}
```

### Shopfloor
* GET Shopfloor by ID
```bash
$ curl -i -X GET {{base_url}}/shopfloors/{id}
```
Result

| Name          | Data Type | Description                               |
|---------------|-----------|-------------------------------------------|
| id            | integer   | Shopfloor ID                              |
| name          | string    | Shopfloor name                            |
| uuid          | string    | Shopfloor UUID                            |
| area          | decimal(18, 3) | Area                                 |
| is_input_counted | boolean | Indicates if the Shopfloor's energy input is counted for aggregating|                        |
| contact       | Object    | Contact Object                            |
| cost_center   | Object    | Cost Center Object                        |
| description   | string    | Shopfloor description                     |

* GET All Shopfloors
```bash
$ curl -i -X GET {{base_url}}/shopfloors
```
* DELETE a Shopfloor by ID
```bash
$ curl -i -X DELETE {{base_url}}/shopfloors/{id}
```
* POST Create a Shopfloor
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"name":"MyEMS Shopfloor", "area":999.99, "is_input_counted":true, "contact_id":1, "cost_center_id":1, "description":"Shopfloor description"}}' {{base_url}}/shopfloors
```
* PUT Update a Shopfloor
```bash
$ curl -i -H "Content-Type: application/json" -X PUT -d '{"data":{"name":"MyEMS Shopfloor", "area":999.99, "is_input_counted":true, "contact_id":1, "cost_center_id":1, "description":"Shopfloor description"}}' {{base_url}}/shopfloors/{id}
```
* GET All Equipments of Shopfloor by ID
```bash
$ curl -i -X GET {{base_url}}/shopfloors/{id}/equipments
```
* POST Bind an Equipment to a Shopfloor
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"equipment_id":1}}' {{base_url}}/shopfloors/{id}/equipments
```
* DELETE an Equipment from Shopfloor
```bash
$ curl -i -X DELETE {{base_url}}/shopfloors/{id}/equipments/{eid}
```
* GET All Meters of Shopfloor by ID
```bash
$ curl -i -X GET {{base_url}}/shopfloors/{id}/meters
```
* POST Bind a Meter to a Shopfloor
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"meter_id":1}}' {{base_url}}/shopfloors/{id}/meters
```
* DELETE a Meter from Shopfloor
```bash
$ curl -i -X DELETE {{base_url}}/shopfloors/{id}/meters/{mid}
```
* GET All Offline Meters of Shopfloor by ID
```bash
$ curl -i -X GET {{base_url}}/shopfloors/{id}/offlinemeters
```
* POST Bind an Offline Meter to a Shopfloor
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"offline_meter_id":1}}' {{base_url}}/shopfloors/{id}/offlinemeters
```
* DELETE an Offline Meter from Shopfloor
```bash
$ curl -i -X DELETE {{base_url}}/shopfloors/{id}/offlinemeters/{mid}
```
* GET All Points of Shopfloor by ID
```bash
$ curl -i -X GET {{base_url}}/shopfloors/{id}/points
```
* POST Bind a Point to a Shopfloor
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"point_id":1}}' {{base_url}}/shopfloors/{id}/points
```
* DELETE a Point from Shopfloor
```bash
$ curl -i -X DELETE {{base_url}}/shopfloors/{id}/points/{pid}
```
* GET All Sensors of Shopfloor by ID
```bash
$ curl -i -X GET {{base_url}}/shopfloors/{id}/sensors
```
* POST Bind a Sensor to a Shopfloor
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"sensor_id":1}}' {{base_url}}/shopfloors/{id}/sensors
```
* DELETE a Sensor from Shopfloor
```bash
$ curl -i -X DELETE {{base_url}}/shopfloors/{id}/sensors/{sid}
```
* GET All Virtual Meters of Shopfloor by ID
```bash
$ curl -i -X GET {{base_url}}/shopfloors/{id}/virtualmeters
```
* POST Bind an Virtual Meter to a Shopfloor
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"virtual_meter_id":1}}' {{base_url}}/shopfloors/{id}/virtualmeters
```
* DELETE an Virtual Meter from Shopfloor
```bash
$ curl -i -X DELETE {{base_url}}/shopfloors/{id}/virtualmeters/{mid}
```

### Space
* GET Space by ID
```bash
$ curl -i -X GET {{base_url}}/spaces/{id}
```
Result

| Name          | Data Type | Description                               |
|---------------|-----------|-------------------------------------------|
| id            | integer   | Space ID                                  |
| name          | string    | Space name                                |
| uuid          | string    | Space UUID                                |
| parent_space_id| integer  | Parent Space ID                           |
| area          | decimal(18, 3) | Area                                 |
| timezone      | Object    | Timezone Object                           |
| is_input_counted | boolean | Indicates if the space's energy input is counted for aggregating|                        |
| is_output_counted | boolean | Indicates if the space's energy output is counted for aggregating|                        |
| contact       | Object    | Contact Object                            |
| cost_center   | Object    | Cost Center Object                        |
| description   | string    | Space description                         |

* GET All Spaces
```bash
$ curl -i -X GET {{base_url}}/spaces
```
* DELETE Space by ID
```bash
$ curl -i -X DELETE {{base_url}}/spaces/{id}
```
* POST Create a Space
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"name":"MyEMSSpace", "parent_space_id":1, "area":999.99, "timezone_id":56, "is_input_counted":true, "is_output_counted":false, "contact_id":1, "cost_center_id":1, "description":"Space description"}}' {{base_url}}/spaces
```
* PUT Update a Space
```bash
$ curl -i -H "Content-Type: application/json" -X PUT -d '{"data":{"name":"MyEMSSpace", "parent_space_id":2, "area":999.99, "timezone_id":56, "is_input_counted":true, "is_output_counted":true, "contact_id":1, "cost_center_id":1, "description":"Space description"}}' {{base_url}}/spaces/{id}
```
* GET All Children of Space by ID
```bash
$ curl -i -X GET {{base_url}}/spaces/{id}/children
```
* GET All Combined Equipments of Space by ID
```bash
$ curl -i -X GET {{base_url}}/spaces/{id}/combinedequipments
```
* POST Bind a Combined Equipment to a Space
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"combined_equipment_id":1}}' {{base_url}}/spaces/{id}/equipments
```
* DELETE a Combined Equipment from Space
```bash
$ curl -i -X DELETE {{base_url}}/spaces/{id}/combinedequipments/{eid}
```
* GET All Equipments of Space by ID
```bash
$ curl -i -X GET {{base_url}}/spaces/{id}/equipments
```
* POST Bind an Equipment to a Space
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"equipment_id":1}}' {{base_url}}/spaces/{id}/equipments
```
* DELETE an Equipment from Space
```bash
$ curl -i -X DELETE {{base_url}}/spaces/{id}/equipments/{eid}
```
* GET All Meters of Space by ID
```bash
$ curl -i -X GET {{base_url}}/spaces/{id}/meters
```
* POST Bind a Meter to a Space
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"meter_id":1}}' {{base_url}}/spaces/{id}/meters
```
* DELETE a Meter from Space
```bash
$ curl -i -X DELETE {{base_url}}/spaces/{id}/meters/{mid}
```
* GET All Offline Meters of Space by ID
```bash
$ curl -i -X GET {{base_url}}/spaces/{id}/offlinemeters
```
* POST Bind an Offline Meter to a Space
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"offline_meter_id":1}}' {{base_url}}/spaces/{id}/offlinemeters
```
* DELETE an Offline Meter from Space
```bash
$ curl -i -X DELETE {{base_url}}/spaces/{id}/offlinemeters/{mid}
```
* GET All Points of Space by ID
```bash
$ curl -i -X GET {{base_url}}/spaces/{id}/points
```
* POST Bind a Point to a Space
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"point_id":1}}' {{base_url}}/spaces/{id}/points
```
* DELETE a Point from Space
```bash
$ curl -i -X DELETE {{base_url}}/spaces/{id}/points/{pid}
```
* GET All Sensors of Space by ID
```bash
$ curl -i -X GET {{base_url}}/spaces/{id}/sensors
```
* POST Bind a Sensor to a Space
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"sensor_id":1}}' {{base_url}}/spaces/{id}/sensors
```
* DELETE a Sensor from Space
```bash
$ curl -i -X DELETE {{base_url}}/spaces/{id}/sensors/{sid}
```
* GET All Stores of Space by ID
```bash
$ curl -i -X GET {{base_url}}/spaces/{id}/stores
```
* POST Bind a Store to a Space
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"store_id":1}}' {{base_url}}/spaces/{id}/stores
```
* DELETE a Store from Space
```bash
$ curl -i -X DELETE {{base_url}}/spaces/{id}/stores/{tid}
```
* GET All Tenants of Space by ID
```bash
$ curl -i -X GET {{base_url}}/spaces/{id}/tenants
```
* POST Bind a Tenant to a Space
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"tenant_id":1}}' {{base_url}}/spaces/{id}/tenants
```
* DELETE a Tenant from Space
```bash
$ curl -i -X DELETE {{base_url}}/spaces/{id}/tenants/{tid}
```
* GET All Virtual Meters of Space by ID
```bash
$ curl -i -X GET {{base_url}}/spaces/{id}/virtualmeters
```
* POST Bind an Virtual Meter to a Space
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"virtual_meter_id":1}}' {{base_url}}/spaces/{id}/virtualmeters
```
* DELETE an Virtual Meter from Space
```bash
$ curl -i -X DELETE {{base_url}}/spaces/{id}/virtualmeters/{mid}
```
* GET Space Tree of User
```bash
$ curl -i -H "User-UUID: 793f1bb4-6e25-4242-8cdc-2f662b25484f" -H "Token: a6e52af82e5b4168ae03b1c5fd8fa31b2ab3a338" -X GET {{base_url}}/spaces/tree
```


### Store
* GET Store by ID
```bash
$ curl -i -X GET {{base_url}}/stores/{id}
```
Result

| Name          | Data Type | Description                               |
|---------------|-----------|-------------------------------------------|
| id            | integer   | Store ID                                  |
| name          | string    | Store name                                |
| uuid          | string    | Store UUID                                |
| address       | string    | Address                                   |
| latitude      | decimal(9, 6) | Latitude                              |
| longitude     | decimal(9, 6) | Longitude                             |
| area          | decimal(18, 3) | Area                                 |
| store_type   | Object    | Store Type object                          |
| is_input_counted| boolean | Indicates if this store's input energy is counted into parent space|
| contact       | Object    | Contact Object                            |
| cost_center   | Object    | Cost Center Object                        |
| description   | string    | Store description                         |

* GET All Stores
```bash
$ curl -i -X GET {{base_url}}/stores
```
* POST Create New Store
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"name":"麦当劳(新王府井店)", "address":"北京市东城区王府井大街200号工美大厦1层010-65120499", "latitude":39.909429, "longitude":116.416993, "area":418.8, "store_type_id":9, "is_input_counted": true, "contact_id":1, "cost_center_id":1, "description":"my description"}}' {{base_url}}/stores
```
* PUT Update a Store
```bash
$ curl -i -H "Content-Type: application/json" -X PUT -d '{"data":{"name":"麦当劳(新王府井店)", "address":"北京市东城区王府井大街200号工美大厦1层010-65120499", "latitude":39.909429, "longitude":116.416993, "area":818.8, "store_type_id":9, "is_input_counted": true, "contact_id":1, "cost_center_id":1, "description":"my description"}}' {{base_url}}/stores/{id}
```
* DELETE Store by ID
```bash
$ curl -i -X DELETE {{base_url}}/stores/{id}
```
* GET All Meters of Store by ID
```bash
$ curl -i -X GET {{base_url}}/stores/{id}/meters
```
* POST Bind a Meter to a Store
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"meter_id":1}}' {{base_url}}/stores/{id}/meters
```
* DELETE a Meter from Store
```bash
$ curl -i -X DELETE {{base_url}}/stores/{id}/meters/{mid}
```
* GET All Offline Meters of Store by ID
```bash
$ curl -i -X GET {{base_url}}/stores/{id}/offlinemeters
```
* POST Bind an Offline Meter to a Store
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"offline_meter_id":1}}' {{base_url}}/stores/{id}/offlinemeters
```
* DELETE an Offline Meter from Store
```bash
$ curl -i -X DELETE {{base_url}}/stores/{id}/offlinemeters/{mid}
```
* GET All Points of Store by ID
```bash
$ curl -i -X GET {{base_url}}/stores/{id}/points
```
* POST Bind a Point to a Store
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"point_id":1}}' {{base_url}}/stores/{id}/points
```
* DELETE a Point from Store
```bash
$ curl -i -X DELETE {{base_url}}/stores/{id}/points/{pid}
```
* GET All Sensors of Store by ID
```bash
$ curl -i -X GET {{base_url}}/stores/{id}/sensors
```
* POST Bind a Sensor to a Store
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"sensor_id":1}}' {{base_url}}/stores/{id}/sensors
```
* DELETE a Sensor from Store
```bash
$ curl -i -X DELETE {{base_url}}/stores/{id}/sensors/{sid}
```
* GET All Virtual Meters of Store by ID
```bash
$ curl -i -X GET {{base_url}}/stores/{id}/virtualmeters
```
* POST Bind an Virtual Meter to a Store
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"virtual_meter_id":1}}' {{base_url}}/stores/{id}/virtualmeters
```
* DELETE an Virtual Meter from Store
```bash
$ curl -i -X DELETE {{base_url}}/stores/{id}/virtualmeters/{mid}
```


### Store Type
* GET a Store Type by ID

```bash
$ curl -i -X GET {{base_url}}/storetypes/{id}
```
Result

| Name          | Data Type | Description                               |
|---------------|-----------|-------------------------------------------|
| id            | integer   | Store Type ID                            |
| name          | string    | Store Type name                          |
| uuid          | string    | Store Type UUID                          |
| description   | string    | Store Type description                   |
| simplified_code | string  | Store Type simplified code               |

* GET All Store Types
```bash
$ curl -i -X GET {{base_url}}/storetypes
```
* POST Create New Store Types
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"name": "Office", "description":"办公", "simplified_code":"OF"}}' {{base_url}}/storetypes
```
* PUT Update a Store Types
```bash
$ curl -i -H "Content-Type: application/json" -X PUT -d '{"data":{"name": "Office1", "description":"办公", "simplified_code":"OF1"}}' {{base_url}}/storetypes/{id}
```
* DELETE a Store Types by ID
```bash
$ curl -i -X DELETE {{base_url}}/storetypes/{id}
```


### Tariff
* GET Tariff by id

```bash
$ curl -i -X GET {{base_url}}/tariffs/{id}
```
Result in JSON

| Name          | Data Type | Description                               |
|---------------|-----------|-------------------------------------------|
| id            | integer   | Tariff ID                                 |
| name          | string    | Tariff name                               |
| uuid          | string    | Tariff UUID                               |
| unit_of_price | string    | Unit of Price                             |
| valid_from    | float     | Valid From (POSIX timestamp * 1000)       |
| valid_through | float     | Valid Through (POSIX timestamp * 1000)    |
| tariff_type   | string    | Tariff type (timeofuse or block)          |
| timeofuse[]   | json array| Time Of Use items                         |
| ├             | integer   | array index                               |
|  ├ start_time_of_day  | string    | Start time of day                 |
|  ├ end_time_of_day    | string    | End time of day                   |
|  ├ peak_type  | string    | Peak type: toppeak,onpeak,midpeak,offpeak |
|  └ price      | decimal   | Price                                     |
| block[]       | json array| Block items                               |
| ├             | integer   | array index                               |
|  ├ start_amount | decimal | Start amount                              |
|  ├ end_amount | decimal   | End amount                                |
|  └ price      | decimal   | Price                                     |

* GET All Tariffs
```bash
$ curl -i -X GET {{base_url}}/tariffs
```
* DELETE Tariff by ID
```bash
$ curl -i -X DELETE {{base_url}}/tariffs/{id}
```
* POST Create a Tariff
To POST a block tariff:
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"name":"阶梯电价","energy_category_id":1, "tariff_type":"block", "unit_of_price":"元/千瓦时", "valid_from":"2020-01-01T00:00:00", "valid_through":"2021-01-01T00:00:00", "block":[{"start_amount":"0", "end_amount":"10000", "price":"0.567"}, {"start_amount":"10000", "end_amount":"30000", "price":"0.678"}, {"start_amount":"30000", "end_amount":"100000", "price":"0.789"}]}}' {{base_url}}/tariffs
```
To POST a time of use tariff:
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"name":"2020分时电价1-6","energy_category_id":1, "tariff_type":"timeofuse", "unit_of_price":"元/千瓦时", "valid_from":"2020-01-01T00:00:00", "valid_through":"2020-07-01T00:00:00", "timeofuse":[{"start_time_of_day":"00:00:00", "end_time_of_day":"05:59:59", "peak_type":"offpeak", "price":0.345}, {"start_time_of_day":"06:00:00", "end_time_of_day":"07:59:59", "peak_type":"midpeak", "price":0.708}, {"start_time_of_day":"08:00:00", "end_time_of_day":"10:59:59", "peak_type":"onpeak", "price":1.159}, {"start_time_of_day":"11:00:00", "end_time_of_day":"17:59:59", "peak_type":"midpeak", "price":0.708}, {"start_time_of_day":"18:00:00", "end_time_of_day":"20:59:59", "peak_type":"onpeak", "price":1.159}, {"start_time_of_day":"21:00:00", "end_time_of_day":"21:59:59", "peak_type":"midpeak", "price":0.708}, {"start_time_of_day":"22:00:00", "end_time_of_day":"23:59:59", "peak_type":"offpeak", "price":0.345}]}}' {{base_url}}/tariffs
```

* PUT Update a Tariff
To update a block tariff:
```bash
$ curl -i -H "Content-Type: application/json" -X PUT -d '{"data":{"name":"阶梯电价","energy_category_id":1, "tariff_type":"block", "unit_of_price":"元/千瓦时", "valid_from":"2020-01-01T00:00:00", "valid_through":"2021-01-01T00:00:00", "block":[{"start_amount":"0", "end_amount":"20000", "price":"0.567"}, {"start_amount":"20000", "end_amount":"30000", "price":"0.678"}, {"start_amount":"30000", "end_amount":"100000", "price":"0.789"}]}}' {{base_url}}/tariffs/{id}
```
To update a time of use tariff:
```bash
$ curl -i -H "Content-Type: application/json" -X PUT -d '{"data":{"name":"2020分时电价1-6","energy_category_id":1, "tariff_type":"timeofuse", "unit_of_price":"元/千瓦时", "valid_from":"2020-01-01T00:00:00", "valid_through":"2020-07-01T00:00:00", "timeofuse":[{"start_time_of_day":"00:00:00", "end_time_of_day":"05:59:59", "peak_type":"offpeak", "price":0.456}, {"start_time_of_day":"06:00:00", "end_time_of_day":"07:59:59", "peak_type":"midpeak", "price":0.708}, {"start_time_of_day":"08:00:00", "end_time_of_day":"10:59:59", "peak_type":"onpeak", "price":1.159}, {"start_time_of_day":"11:00:00", "end_time_of_day":"17:59:59", "peak_type":"midpeak", "price":0.708}, {"start_time_of_day":"18:00:00", "end_time_of_day":"20:59:59", "peak_type":"onpeak", "price":1.159}, {"start_time_of_day":"21:00:00", "end_time_of_day":"21:59:59", "peak_type":"midpeak", "price":0.708}, {"start_time_of_day":"22:00:00", "end_time_of_day":"23:59:59", "peak_type":"offpeak", "price":0.345}]}}' {{base_url}}/tariffs/{id}
```


### Tenant
* GET Tenant by ID
```bash
$ curl -i -X GET {{base_url}}/tenants/{id}
```
Result

| Name          | Data Type | Description                               |
|---------------|-----------|-------------------------------------------|
| id            | integer   | Tenant ID                                 |
| name          | string    | Tenant name                               |
| uuid          | string    | Tenant UUID                               |
| buildings     | string    | Buildings (one or many)                   |
| floors        | string    | Floors (one or many)                      |
| rooms         | string    | Rooms (one or many)                       |
| area          | decimal(18, 3) | Area                                 |
| tenant_type   | Object    | Tenant Type object                        |
| is_input_counted| boolean | Indicates if this tenant's input energy is counted into parent space|
| is_key_tenant | boolean   | Indicates if this is a key tenant         |
| lease_number  | string    | Tenant lease number                       |
| lease_start_datetime_utc | float   | Lease start datetime in utc timezone (POSIX timestamp * 1000)  |
| lease_end_datetime_utc   | float   | Lease end datetime in utc timezone (POSIX timestamp * 1000)    |
| is_in_lease   | boolean   | Indicates if this tenant is in lease      |
| contact       | Object    | Contact Object                            |
| cost_center   | Object    | Cost Center Object                        |
| description   | string    | Tenant description                        |

* GET All Tenants
```bash
$ curl -i -X GET {{base_url}}/tenants
```
* POST Create New Tenant
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"name":"Starbucks", "buildings":"Building #1", "floors":"L1 L2 L3", "rooms":"1201b+2247+3F", "area":418.8, "tenant_type_id":9, "is_input_counted": true, "is_key_tenant":true, "lease_number":"6b0da806",  "lease_start_datetime_utc":"2019-12-31T16:00:00", "lease_end_datetime_utc":"2022-12-31T16:00:00", "is_in_lease":true, "contact_id":1, "cost_center_id":1, "description":"my description"}}' {{base_url}}/tenants
```
* PUT Update a Tenant
```bash
$ curl -i -H "Content-Type: application/json" -X PUT -d '{"data":{"name":"Hermes 爱马仕", "buildings":"Building #1", "floors":"L1 L2 L3 L4 L5", "rooms":"1201b+2247+3F", "area":818.8, "tenant_type_id":9, "is_input_counted": true, "is_key_tenant":true, "lease_number":"6b0da806",  "lease_start_datetime_utc":"2019-12-31T16:00:00", "lease_end_datetime_utc":"2022-12-31T16:00:00", "is_in_lease":true, "contact_id":1, "cost_center_id":1, "description":"my description"}}' {{base_url}}/tenants/{id}
```
* DELETE Tenant by ID
```bash
$ curl -i -X DELETE {{base_url}}/tenants/{id}
```
* GET All Meters of Tenant by ID
```bash
$ curl -i -X GET {{base_url}}/tenants/{id}/meters
```
* POST Bind a Meter to a Tenant
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"meter_id":1}}' {{base_url}}/tenants/{id}/meters
```
* DELETE a Meter from Tenant
```bash
$ curl -i -X DELETE {{base_url}}/tenants/{id}/meters/{mid}
```
* GET All Offline Meters of Tenant by ID
```bash
$ curl -i -X GET {{base_url}}/tenants/{id}/offlinemeters
```
* POST Bind an Offline Meter to a Tenant
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"offline_meter_id":1}}' {{base_url}}/tenants/{id}/offlinemeters
```
* DELETE an Offline Meter from Tenant
```bash
$ curl -i -X DELETE {{base_url}}/tenants/{id}/offlinemeters/{mid}
```
* GET All Points of Tenant by ID
```bash
$ curl -i -X GET {{base_url}}/tenants/{id}/points
```
* POST Bind a Point to a Tenant
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"point_id":1}}' {{base_url}}/tenants/{id}/points
```
* DELETE a Point from Tenant
```bash
$ curl -i -X DELETE {{base_url}}/tenants/{id}/points/{pid}
```
* GET All Sensors of Tenant by ID
```bash
$ curl -i -X GET {{base_url}}/tenants/{id}/sensors
```
* POST Bind a Sensor to a Tenant
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"sensor_id":1}}' {{base_url}}/tenants/{id}/sensors
```
* DELETE a Sensor from Tenant
```bash
$ curl -i -X DELETE {{base_url}}/tenants/{id}/sensors/{sid}
```
* GET All Virtual Meters of Tenant by ID
```bash
$ curl -i -X GET {{base_url}}/tenants/{id}/virtualmeters
```
* POST Bind an Virtual Meter to a Tenant
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"virtual_meter_id":1}}' {{base_url}}/tenants/{id}/virtualmeters
```
* DELETE an Virtual Meter from Tenant
```bash
$ curl -i -X DELETE {{base_url}}/tenants/{id}/virtualmeters/{mid}
```


### Tenant Type
* GET a Tenant Type by ID

```bash
$ curl -i -X GET {{base_url}}/tenanttypes/{id}
```
Result

| Name          | Data Type | Description                               |
|---------------|-----------|-------------------------------------------|
| id            | integer   | Tenant Type ID                            |
| name          | string    | Tenant Type name                          |
| uuid          | string    | Tenant Type UUID                          |
| description   | string    | Tenant Type description                   |
| simplified_code | string  | Tenant Type simplified code               |

* GET All Tenant Types
```bash
$ curl -i -X GET {{base_url}}/tenanttypes
```
* POST Create New Tenant Types
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"name": "Office", "description":"办公", "simplified_code":"OF"}}' {{base_url}}/tenanttypes
```
* PUT Update a Tenant Types
```bash
$ curl -i -H "Content-Type: application/json" -X PUT -d '{"data":{"name": "Office1", "description":"办公", "simplified_code":"OF1"}}' {{base_url}}/tenanttypes/{id}
```
* DELETE a Tenant Types by ID
```bash
$ curl -i -X DELETE {{base_url}}/tenanttypes/{id}
```

### Text Message
* GET an Text Message by ID

Result in JSON

| Name          | Data Type | Description                               |
|---------------|-----------|-------------------------------------------|
| id            | integer   | Text Message ID                           |
| recipient_name| string    | Recipient Name                            |
| recipient_mobile| string  | Recipient Mobile Number                   |
| message       | string    | Email Message Body                        |
| attachment_file_name| string| Email Attachment File Name              |
| create_datetime| float    | Email Message Created Datetime (POSIX timestamp * 1000)|
| scheduled_datetime| float | Email Message Scheduled Datetime (POSIX timestamp * 1000)|
| acknowledge_code| string  | Recipient reply with Acknowledge code to acknowledge |
| status        | string    | Status ('new', 'sent', 'acknowledged', 'timeout'| 
```bash
$ curl -i -X GET {{base_url}}/textmessages/{id}
```
* GET Text Messages from Startdate to Enddate
```bash
$ curl -i -X GET {{base_url}}/textmessages/from/{startdate}/to/{enddate}
```
* DELETE an Text Message by ID
```bash
$ curl -i -X DELETE {{base_url}}/textmessages/{id}
```


### Timezone
* GET a Timezone by ID
```bash
$ curl -i -X GET {{base_url}}/timezones/{id}
```
* GET all Timezones
```bash
$ curl -i -X GET {{base_url}}/timezones
```
* PUT Update a Timezone by ID
```bash
$ curl -i -H "Content-Type: application/json" -X PUT -d '{"data":{"name":"Hawaiian Standard Time","description":"(GMT-10:00) Hawaii", "utc_offset":"-10:00"}}' {{base_url}}/timezones/{id}
```

### User
* GET User by ID
```bash
$ curl -i -X GET {{base_url}}/users/{id}
```
* GET All Users
```bash
$ curl -i -X GET {{base_url}}/users
```
* DELETE User by id
```bash
$ curl -i -X DELETE {{base_url}}/users/{id}
```
* POST New User
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"name":"albert", "display_name":"Mr. Albert", "email":"albert@myems.io", "is_admin":false, "password":"!MyEMS1"}}' {{base_url}}/users
```
* PUT User Profile
```bash
$ curl -i -H "Content-Type: application/json" -X PUT -d '{"data":{"name":"albert", "display_name":"Mr. Albert", "email":"albert@myems.io", "is_admin":false, "privilege_id":1, "password":"!MyEMS1"}}' {{base_url}}/users/{id}
```
* PUT User Login by Username
```bash
$ curl -i -H "Content-Type: application/json" -X PUT -d '{"data":{"name":"johnson", "password":"!Password1"}}' {{base_url}}/users/login
```
* PUT User Login by Email
```bash
$ curl -i -H "Content-Type: application/json" -X PUT -d '{"data":{"email":"johnson@myems.io", "password":"!Password1"}}' {{base_url}}/users/login
```
* PUT User Logout
```bash
$ curl -i -H "Content-Type: application/json" -H "User-UUID: 793f1bb4-6e25-4242-8cdc-2f662b25484f" -H "Token: a6e52af82e5b4168ae03b1c5fd8fa31b2ab3a338" -X PUT  {{base_url}}/users/logout
```
* PUT User change password
```bash
$ curl -i -H "Content-Type: application/json" -H "User-UUID: 793f1bb4-6e25-4242-8cdc-2f662b25484f" -H "Token: a6e52af82e5b4168ae03b1c5fd8fa31b2ab3a338" -X PUT -d '{"data":{"old_password":"Password1", "new_password":"Password2"}}' {{base_url}}/users/changepassword
```
* PUT User reset other user's password by administrator
```bash
$ curl -i -H "Content-Type: application/json" -H "User-UUID: 793f1bb4-6e25-4242-8cdc-2f662b25484f" -H "Token: a6e52af82e5b4168ae03b1c5fd8fa31b2ab3a338" -X PUT -d '{"data":{"name":"johnson","password":"NewPassword1"}}'  {{base_url}}/users/resetpassword
```


### Virtual Meter
* GET a Virtual Meter by ID

```bash
$ curl -i -X GET {{base_url}}/virtualmeters/{id}
```
Result

| Name          | Data Type | Description                               |
|---------------|-----------|-------------------------------------------|
| id            | integer   | Virtual Meter ID                          |
| name          | string    | Virtual Meter name                        |
| uuid          | string    | Virtual Meter UUID                        |
| energy_category| Object   | Energy Category Object                    |
| is_counted    | boolean   | the Virtual Meter is counted in           |
| cost_center   | Object    | Cost Center Object                        |
| energy_item   | Object    | Energy Item Object                        |
| description   | string    | Offline Meter description                 |
| expression    | json      | Expression                                |
|  ├ id         | integer   | Expression ID                             |
|  ├ uuid       | string    | Expression UUID                           |
|  ├ equation   | string    | Expression Equation                       |
|  └ variables[]| json array| Expression Variables                      |
|  ├            | integer   | array index                               |
|   ├ id        | integer   | Variable ID                               |
|   ├ name      | string    | Variable Name                             |
|   ├ meter_type| string    | Meter Type ('meter', 'offline_meter', 'virtual_meter' |
|   ├ meter_name| string    | Meter Name                                |

* GET All Virtual Meters
```bash
$ curl -i -X GET {{base_url}}/virtualmeters
```
* DELETE a Virtual Meter by ID
```bash
$ curl -i -X DELETE {{base_url}}/virtualmeters/{id}
```
* POST Create New Virtual Meter
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"name":"VM21", "energy_category_id":1, "is_counted": true, "cost_center_id":1, "energy_item_id":1, "description":"virtual description", "expression": {"equation":"x1-x2-x3", "variables":[{"name":"x1", "meter_type":"meter", "meter_id":3},{"name":"x2", "meter_type":"meter", "meter_id":4},{"name":"x3", "meter_type":"meter", "meter_id":5}] } }}' {{base_url}}/virtualmeters
```
* PUT Update a Virtual Meter by ID
```bash
$ curl -i -H "Content-Type: application/json" -X PUT -d '{"data":{"name":"VM21", "energy_category_id":1, "is_counted": true, "cost_center_id":1, "energy_item_id":1, "description":"virtual description", "expression": {"equation":"x1-x2-x3", "variables":[{"name":"x1", "meter_type":"meter", "meter_id":3},{"name":"x2", "meter_type":"meter", "meter_id":4},{"name":"x3", "meter_type":"meter", "meter_id":5}] } }}' {{base_url}}/virtualmeters/{id}
```

### Web Message
* GET a Web Message by ID

Result in JSON

| Name          | Data Type | Description                               |
|---------------|-----------|-------------------------------------------|
| id            | integer   | Web Message ID                            |
| user_id       | integer   | Web Message User ID                       |
| user_display_name| string | User Display Name                         |
| subject       | string    | Web Message Subject                       |
| message       | string    | Web Message Body                          |
| created_datetime| float   | Web Message Created Datetime (POSIX timestamp * 1000)|
| status        | string    | Status ('new', 'acknowledged', 'timeout') | 
| reply         | string    | User's Reply text, allow null             |
```bash
$ curl -i -X GET {{base_url}}/webmessages/{id}
```
* GET Web Messages from Startdate to Enddate
```bash
$ curl -i -X GET {{base_url}}/webmessages/from/{startdate}/to/{enddate}
```
* GET New Web Messages
```bash
$ curl -i -X GET {{base_url}}/webmessagesnew
```
* DELETE a Web Message by ID
```bash
$ curl -i -X DELETE {{base_url}}/webmessages/{id}
```

### Wechat Message
* GET an Wechat Message by ID

Result in JSON

| Name          | Data Type | Description                               |
|---------------|-----------|-------------------------------------------|
| id            | integer   | Message ID                            |
| recipient_name| string    | Recipient Name                            |
| recipient_openid| string  | Recipient OpenID                          |
| message_template_id|string| Message Template ID                       |
| message_data  | json      | Message Data in JSON                      |
| created_datetime| float   | Message Created Datetime (POSIX timestamp * 1000)|
| scheduled_datetime| float | Message Scheduled Datetime (POSIX timestamp * 1000)|
| acknowledge_code| string  | Recipient reply with Acknowledge code to acknowledge |
| status        | string    | Status ('new', 'sent', 'acknowledged', 'timeout'| 
```bash
$ curl -i -X GET {{base_url}}/wechatmessages/{id}
```
* GET a Wechat Messages from Startdate to Enddate
```bash
$ curl -i -X GET {{base_url}}/wechatmessages/from/{startdate}/to/{enddate}
```
* DELETE a Wechat Message by ID
```bash
$ curl -i -X DELETE {{base_url}}/wechatmessages/{id}
```

### Reports
* GET AdvancedReports
```
$ curl -i -X GET {{base_url}}/reports/advancedreports?reportingperiodstartdatetime={reportingperiodstartdatetime}&reportingperiodenddatetime={reportingperiodenddatetime}
```
* GET AdvancedReport by ID
```
$ curl -i -X GET {{base_url}}/reports/advancedreports/{id}
```
* DELETE AdvancedReport by ID
```
$ curl -i -X GET {{base_url}}/reports/advancedreports/{id}
```
* GET Dashboard
```
$ curl -i -X GET {{base_url}}/reports/dashboard?useruuid={useruuid}&periodtype={periodtype}&baseperiodstartdatetime={baseperiodstartdatetime}&baseperiodenddatetime={baseperiodenddatetime}&reportingperiodstartdatetime={reportingperiodstartdatetime}&reportingperiodenddatetime={reportingperiodenddatetime}
```
* GET Distribution System Report
```
$ curl -i -X GET {{base_url}}/reports/distributionsystem?distributionsystemid=1
```
* GET Energy Flow Diagram Report
```
$ curl -i -X GET {{base_url}}/reports/energyflowdiagram?energyflowdiagramid=1&reportingperiodstartdatetime={reportingperiodstartdatetime}&reportingperiodenddatetime={reportingperiodenddatetime}
```
* GET Equipment Efficiency Report
```
$ curl -i -X GET {{base_url}}/reports/equipmentefficiency?equipmentid=1&periodtype=daily&baseperiodstartdatetime=2020-08-01T00:00:00&baseperiodenddatetime=2020-09-01T00:00:00&reportingperiodstartdatetime=2020-09-01T00:00:00&reportingperiodenddatetime=2020-10-01T00:00:00
```
* GET Equipment Energy Category Report
```
$ curl -i -X GET {{base_url}}/reports/equipmentenergycategory?equipmentid=1&periodtype=daily&baseperiodstartdatetime=2020-08-01T00:00:00&baseperiodenddatetime=2020-09-01T00:00:00&reportingperiodstartdatetime=2020-09-01T00:00:00&reportingperiodenddatetime=2020-10-01T00:00:00
```
* GET Equipment Energy Item Report
```
$ curl -i -X GET {{base_url}}/reports/equipmentenergyitem?equipmentid=1&periodtype=daily&baseperiodstartdatetime=2020-08-01T00:00:00&baseperiodenddatetime=2020-09-01T00:00:00&reportingperiodstartdatetime=2020-09-01T00:00:00&reportingperiodenddatetime=2020-10-01T00:00:00
```
* GET Equipment Income Report
```
$ curl -i -X GET {{base_url}}/reports/equipmentincome?equipmentid=1&periodtype=daily&baseperiodstartdatetime=2020-08-01T00:00:00&baseperiodenddatetime=2020-09-01T00:00:00&reportingperiodstartdatetime=2020-09-01T00:00:00&reportingperiodenddatetime=2020-10-01T00:00:00
```
* GET Equipment Load Report
```
$ curl -i -X GET {{base_url}}/reports/equipmentload?equipmentid=1&periodtype=daily&baseperiodstartdatetime=2020-08-01T00:00:00&baseperiodenddatetime=2020-09-01T00:00:00&reportingperiodstartdatetime=2020-09-01T00:00:00&reportingperiodenddatetime=2020-10-01T00:00:00
```
* GET Equipment Output Report
```
$ curl -i -X GET {{base_url}}/reports/equipmentoutput?equipmentid=1&periodtype=daily&baseperiodstartdatetime=2020-08-01T00:00:00&baseperiodenddatetime=2020-09-01T00:00:00&reportingperiodstartdatetime=2020-09-01T00:00:00&reportingperiodenddatetime=2020-10-01T00:00:00
```
* GET Equipment Saving Report
```
$ curl -i -X GET {{base_url}}/reports/equipmentsaving?equipmentid=1&periodtype=daily&baseperiodstartdatetime=2020-08-01T00:00:00&baseperiodenddatetime=2020-09-01T00:00:00&reportingperiodstartdatetime=2020-09-01T00:00:00&reportingperiodenddatetime=2020-10-01T00:00:00
```
* GET Equipment Statistics Report
```
$ curl -i -X GET {{base_url}}/reports/equipmentstatistics?equipmentid=1&periodtype=daily&baseperiodstartdatetime=2020-08-01T00:00:00&baseperiodenddatetime=2020-09-01T00:00:00&reportingperiodstartdatetime=2020-09-01T00:00:00&reportingperiodenddatetime=2020-10-01T00:00:00
```
* GET Meter Energy Report
```
$ curl -i -X GET {{base_url}}/reports/meterenergy?meterid=6&periodtype=daily&baseperiodstartdatetime=2020-08-01T00:00:00&baseperiodenddatetime=2020-09-01T00:00:00&reportingperiodstartdatetime=2020-09-01T00:00:00&reportingperiodenddatetime=2020-10-01T00:00:00
```
* GET Meter Cost Report
```
$ curl -i -X GET {{base_url}}/reports/metercost?meterid=6&periodtype=daily&baseperiodstartdatetime=2020-08-01T00:00:00&baseperiodenddatetime=2020-09-01T00:00:00&reportingperiodstartdatetime=2020-09-01T00:00:00&reportingperiodenddatetime=2020-10-01T00:00:00
```
* GET Meter Realtime Report
```
$ curl -i -X GET {{base_url}}/reports/meterrealtime?meterid=1
```
* GET Meter Submeters Balance Report
```
$ curl -i -X GET {{base_url}}/reports/metersubmetersbalance?meterid=1&periodtype=daily&reportingperiodstartdatetime=2020-09-01T00:00:00&reportingperiodenddatetime=2020-10-01T00:00:00
```
* GET Meter Trend Report
```
$ curl -i -X GET {{base_url}}/reports/metertrend?meterid=6&reportingperiodstartdatetime=2020-09-10T00:00:00&reportingperiodenddatetime=2020-09-11T00:00:00
```
* GET Meter Tracking Report
```
$ curl -i -X GET {{base_url}}/reports/metertracking?spaceid=1
```
* GET Offline Meter Energy Report
```
$ curl -i -X GET {{base_url}}/reports/offlinemeterenergy?offlinemeterid=1&periodtype=daily&baseperiodstartdatetime=2020-08-01T00:00:00&baseperiodenddatetime=2020-09-01T00:00:00&reportingperiodstartdatetime=2020-09-01T00:00:00&reportingperiodenddatetime=2020-10-01T00:00:00
```
* GET Offline Meter Cost Report
```
$ curl -i -X GET {{base_url}}/reports/offlinemetercost?offlinemeterid=1&periodtype=daily&baseperiodstartdatetime=2020-08-01T00:00:00&baseperiodenddatetime=2020-09-01T00:00:00&reportingperiodstartdatetime=2020-09-01T00:00:00&reportingperiodenddatetime=2020-10-01T00:00:00
```
* GET Space Cost Report
```
$ curl -i -X GET {{base_url}}/reports/spacecost?spaceid=1&periodtype=daily&baseperiodstartdatetime=2020-08-01T00:00:00&baseperiodenddatetime=2020-09-01T00:00:00&reportingperiodstartdatetime=2020-09-01T00:00:00&reportingperiodenddatetime=2020-10-01T00:00:00
```
* GET Space Efficiency Report
```
$ curl -i -X GET {{base_url}}/reports/spaceefficiency?spaceid=1&periodtype=daily&baseperiodstartdatetime=2020-08-01T00:00:00&baseperiodenddatetime=2020-09-01T00:00:00&reportingperiodstartdatetime=2020-09-01T00:00:00&reportingperiodenddatetime=2020-10-01T00:00:00
```
* GET Space Energy Category Report
```
$ curl -i -X GET {{base_url}}/reports/spaceenergycategory?spaceid=1&periodtype=daily&baseperiodstartdatetime=2020-08-01T00:00:00&baseperiodenddatetime=2020-09-01T00:00:00&reportingperiodstartdatetime=2020-09-01T00:00:00&reportingperiodenddatetime=2020-10-01T00:00:00
```
* GET Space Energy Item Report
```
$ curl -i -X GET {{base_url}}/reports/spaceenergyitem?spaceid=1&periodtype=daily&baseperiodstartdatetime=2020-08-01T00:00:00&baseperiodenddatetime=2020-09-01T00:00:00&reportingperiodstartdatetime=2020-09-01T00:00:00&reportingperiodenddatetime=2020-10-01T00:00:00
```
* GET Space Income Report
```
$ curl -i -X GET {{base_url}}/reports/spaceincome?spaceid=1&periodtype=daily&baseperiodstartdatetime=2020-08-01T00:00:00&baseperiodenddatetime=2020-09-01T00:00:00&reportingperiodstartdatetime=2020-09-01T00:00:00&reportingperiodenddatetime=2020-10-01T00:00:00
```
* GET Space Load Report
```
$ curl -i -X GET {{base_url}}/reports/spaceload?spaceid=1&periodtype=daily&baseperiodstartdatetime=2020-08-01T00:00:00&baseperiodenddatetime=2020-09-01T00:00:00&reportingperiodstartdatetime=2020-09-01T00:00:00&reportingperiodenddatetime=2020-10-01T00:00:00
```
* GET Space Output Report
```
$ curl -i -X GET {{base_url}}/reports/spaceoutput?spaceid=1&periodtype=daily&baseperiodstartdatetime=2020-08-01T00:00:00&baseperiodenddatetime=2020-09-01T00:00:00&reportingperiodstartdatetime=2020-09-01T00:00:00&reportingperiodenddatetime=2020-10-01T00:00:00
```
* GET Space Saving Report
```
$ curl -i -X GET {{base_url}}/reports/spacesaving?spaceid=1&periodtype=daily&baseperiodstartdatetime=2020-08-01T00:00:00&baseperiodenddatetime=2020-09-01T00:00:00&reportingperiodstartdatetime=2020-09-01T00:00:00&reportingperiodenddatetime=2020-10-01T00:00:00
```
* GET Space Statistics Report
```
$ curl -i -X GET {{base_url}}/reports/spacestatistics?spaceid=1&periodtype=daily&baseperiodstartdatetime=2020-08-01T00:00:00&baseperiodenddatetime=2020-09-01T00:00:00&reportingperiodstartdatetime=2020-09-01T00:00:00&reportingperiodenddatetime=2020-10-01T00:00:00
```
* GET Tenant Bill Report
```
$ curl -i -X GET {{base_url}}/reports/tenantbill?tenantid=1&reportingperiodstartdatetime=2020-10-01T00:00:00&reportingperiodenddatetime=2020-11-01T00:00:00
```
* GET Tenant Cost Report
```
$ curl -i -X GET {{base_url}}/reports/tenantcost?tenantid=1&periodtype=daily&baseperiodstartdatetime=2020-08-01T00:00:00&baseperiodenddatetime=2020-09-01T00:00:00&reportingperiodstartdatetime=2020-09-01T00:00:00&reportingperiodenddatetime=2020-10-01T00:00:00
```
* GET Tenant Energy Category Report
```
$ curl -i -X GET {{base_url}}/reports/tenantenergycategory?tenantid=1&periodtype=daily&baseperiodstartdatetime=2020-08-01T00:00:00&baseperiodenddatetime=2020-09-01T00:00:00&reportingperiodstartdatetime=2020-09-01T00:00:00&reportingperiodenddatetime=2020-10-01T00:00:00
```
* GET Tenant Energy Item Report
```
$ curl -i -X GET {{base_url}}/reports/tenantenergyitem?tenantid=1&periodtype=daily&baseperiodstartdatetime=2020-08-01T00:00:00&baseperiodenddatetime=2020-09-01T00:00:00&reportingperiodstartdatetime=2020-09-01T00:00:00&reportingperiodenddatetime=2020-10-01T00:00:00
```
* GET Tenant Load Report
```
$ curl -i -X GET {{base_url}}/reports/tenantload?tenantid=1&periodtype=daily&baseperiodstartdatetime=2020-08-01T00:00:00&baseperiodenddatetime=2020-09-01T00:00:00&reportingperiodstartdatetime=2020-09-01T00:00:00&reportingperiodenddatetime=2020-10-01T00:00:00
```
* GET Tenant Saving Report
```
$ curl -i -X GET {{base_url}}/reports/tenantsaving?tenantid=1&periodtype=daily&baseperiodstartdatetime=2020-08-01T00:00:00&baseperiodenddatetime=2020-09-01T00:00:00&reportingperiodstartdatetime=2020-09-01T00:00:00&reportingperiodenddatetime=2020-10-01T00:00:00
```
* GET Tenant Statistics Report
```
$ curl -i -X GET {{base_url}}/reports/tenantstatistics?tenantid=1&periodtype=daily&baseperiodstartdatetime=2020-08-01T00:00:00&baseperiodenddatetime=2020-09-01T00:00:00&reportingperiodstartdatetime=2020-09-01T00:00:00&reportingperiodenddatetime=2020-10-01T00:00:00
```
* GET Virtual Meter Energy Report
```
$ curl -i -X GET {{base_url}}/reports/virtualmeterenergy?virtualmeterid=1&periodtype=daily&baseperiodstartdatetime=2020-08-01T00:00:00&baseperiodenddatetime=2020-09-01T00:00:00&reportingperiodstartdatetime=2020-09-01T00:00:00&reportingperiodenddatetime=2020-10-01T00:00:00
```
* GET Virtual Meter Cost Report
```
$ curl -i -X GET {{base_url}}/reports/virtualmetercost?virtualmeterid=1&periodtype=daily&baseperiodstartdatetime=2020-08-01T00:00:00&baseperiodenddatetime=2020-09-01T00:00:00&reportingperiodstartdatetime=2020-09-01T00:00:00&reportingperiodenddatetime=2020-10-01T00:00:00
```
