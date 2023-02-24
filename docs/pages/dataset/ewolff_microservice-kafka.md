---
title: ewolff/microservice-kafka
keywords: model
tags: [apache_httpd, docker, docker_compose, kafka, zookeeper]
sidebar: datasetdoc_sidebar
permalink: ewolff_microservice-kafka.html
toc: false
---

## General Information

The repository for this application ([open on GitHub](https://github.com/ewolff/microservice-kafka)) has 535 stars and was forked 282 times. The codebase consists of 2797 lines of code and makes use of the following technologies:

<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_apache_httpd.html">Apache httpd</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_docker.html">Docker</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_docker_compose.html">Docker Compose</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_kafka.html">Kafka</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_zookeeper.html">ZooKeeper</a>

## Data Flow Diagram

![Dataflow Diagram](./ewolff_microservice-kafka.png)

Download the following model file [here](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/ewolff_microservice-kafka/ewolff_microservice-kafka.json).
Other formats are provided below.

```json
{
    "services": [
        {
            "name": "zookeeper",
            "stereotypes": [
                "configuration_server",
                "infrastructural"
            ],
            "tagged_values": {
                "Configuration Server": "ZooKeeper"
            }
        },
        {
            "name": "kafka",
            "stereotypes": [
                "message_broker",
                "infrastructural"
            ],
            "tagged_values": {
                "Message Broker": "Kafka",
                "Port": 9092
            }
        },
        {
            "name": "order",
            "stereotypes": [
                "internal"
            ],
            "tagged_values": {
                "Port": 8080,
                "Endpoints": [
                    "/order"
                ]
            }
        },
        {
            "name": "invoicing",
            "stereotypes": [
                "internal",
                "local_logging"
            ],
            "tagged_values": {
                "Port": 8080
            }
        },
        {
            "name": "shipping",
            "stereotypes": [
                "internal",
                "local_logging"
            ],
            "tagged_values": {
                "Port": 8080
            }
        },
        {
            "name": "apache",
            "stereotypes": [
                "web_server",
                "infrastructural"
            ],
            "tagged_values": {
                "Web Server": "Apache httpd",
                "Port": 80
            }
        },
        {
            "name": "postgres",
            "stereotypes": [
                "database",
                "plaintext_credentials",
                "exitpoint"
            ],
            "tagged_values": {
                "Database": "PostgreSQL",
                "Username": "dbuser",
                "Password": "dbpass"
            }
        }
    ],
    "information_flows": [
        {
            "sender": "zookeeper",
            "receiver": "kafka",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "order",
            "receiver": "kafka",
            "stereotypes": [
                "restful_http",
                "message_producer_kafka"
            ],
            "tagged_values": {
                "'Producer Topic'": "\"order\""
            }
        },
        {
            "sender": "kafka",
            "receiver": "invoicing",
            "stereotypes": [
                "restful_http",
                "message_consumer_kafka"
            ],
            "tagged_values": {
                "'Consumer Topic'": "\"order\""
            }
        },
        {
            "sender": "kafka",
            "receiver": "shipping",
            "stereotypes": [
                "restful_http",
                "message_consumer_kafka"
            ],
            "tagged_values": {
                "'Consumer Topic'": "\"order\""
            }
        },
        {
            "sender": "apache",
            "receiver": "order",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "apache",
            "receiver": "shipping",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "apache",
            "receiver": "invoicing",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "user",
            "receiver": "apache",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "apache",
            "receiver": "user",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "postgres",
            "receiver": "order",
            "stereotypes": [
                "jdbc",
                "plaintext_credentials_link"
            ],
            "tagged_values": {
                "'Username'": "\"dbuser\"",
                " 'Password'": "\"dbpass\""
            }
        },
        {
            "sender": "postgres",
            "receiver": "shipping",
            "stereotypes": [
                "jdbc",
                "plaintext_credentials_link"
            ],
            "tagged_values": {
                "'Username'": "\"dbuser\"",
                " 'Password'": "\"dbpass\""
            }
        },
        {
            "sender": "postgres",
            "receiver": "invoicing",
            "stereotypes": [
                "jdbc",
                "plaintext_credentials_link"
            ],
            "tagged_values": {
                "'Username'": "\"dbuser\"",
                " 'Password'": "\"dbpass\""
            }
        }
    ],
    "external_entities": [
        {
            "name": "user",
            "stereotypes": [
                "user_stereotype",
                "entrypoint",
                "exitpoint"
            ],
            "tagged_values": {}
        }
    ]
}
```

### Model Items

The Application consists of a total of 76 elements:

Element | Count
-- | --
Services | 7
External Entities | 1
Information Flows | 12
Annotations | 56
Total Items | 76

### Model Representations {#representations}

Open the model in the following formats:

- [JSON model](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/ewolff_microservice-kafka/ewolff_microservice-kafka.json)
- [PlantUML description](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/ewolff_microservice-kafka/ewolff_microservice-kafka.txt)
- [PNG graph](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/ewolff_microservice-kafka/ewolff_microservice-kafka.png)
- [CodeableModels](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/ewolff_microservice-kafka/ewolff_microservice-kafka.py)

### Traceability

Open the traceability information for all model items:

- [Traceability](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/ewolff_microservice-kafka/ewolff_microservice-kafka_traceability.json)

## Security Rules

The following table shows the application's adherence to the 17 architectural security rules. The last column provides model variants that adhere to the rule for each rule that is initially violated.

Rule ID &nbsp;&nbsp;| Verdict &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| Evidence &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| Model Variant &nbsp;&nbsp;&nbsp;|
-- | -- | -- | -- |
**R1** | <i class="fa fa-warning" style="color: #bfc600;"> | <a href="#rule01">Evidence |  |
**R2** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule02">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/ewolff_microservice-kafka/model_variants/3.txt) |
**R3** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule03">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/ewolff_microservice-kafka/model_variants/3.txt) |
**R4** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule04">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/ewolff_microservice-kafka/model_variants/4.txt) |
**R5** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule05">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/ewolff_microservice-kafka/model_variants/5.txt) |
**R6** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule06">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/ewolff_microservice-kafka/model_variants/6.txt) |
**R7** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule07">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/ewolff_microservice-kafka/model_variants/7.txt) |
**R8** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule08">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/ewolff_microservice-kafka/model_variants/8.txt) |
**R9** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule09">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/ewolff_microservice-kafka/model_variants/9.txt) |
**R10** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule10">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/ewolff_microservice-kafka/model_variants/10.txt) |
**R11** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule11">Evidence |  |
**R12** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule12">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/ewolff_microservice-kafka/model_variants/12.txt) |
**R13** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule12">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/ewolff_microservice-kafka/model_variants/13.txt) |
**R14** |  <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule12">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/ewolff_microservice-kafka/model_variants/14.txt) |
**R16** |  <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule12">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/ewolff_microservice-kafka/model_variants/16.txt) |
**R17** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule17">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/ewolff_microservice-kafka/model_variants/17.txt) |
**R18** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule18">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/ewolff_microservice-kafka/model_variants/18.txt) |



### Evidence and explanations for rule decisions
#### R1 {#rule01}

Rule is partially adhered to: User only communicates with the Apache httpd web server. There is no indication or configuration that the Apache httpd webserver is authenticating/authorizing the requests.

Artifacts:
- 000-default.conf: Line: [1](https://github.com/ewolff/microservice-kafka/blob/master/docker/apache/000-default.conf#L1)
- Dockerfile: Line: [17](https://github.com/ewolff/microservice-kafka/blob/master/docker/apache/Dockerfile#L17)

#### R2  {#rule02}

Rule is violated: Internal services do not mutually authenticate nor authorize. Only the database accesses are authorized using plaintext credentials.

Artifacts:
- application.properties: Line: [11](https://github.com/ewolff/microservice-kafka/blob/master/microservice-kafka/microservice-kafka-order/src/main/resources/application.properties#L11)
- application.properties: Line: [13](https://github.com/ewolff/microservice-kafka/blob/master/microservice-kafka/microservice-kafka-shipping/src/main/resources/application.properties#L13)
- application.properties: Line: [13](https://github.com/ewolff/microservice-kafka/blob/master/microservice-kafka/microservice-kafka-invoicing/src/main/resources/application.properties#L13)

#### R3 {#rule03}

Rule is violated: No authentication mechanism is deployed.

#### R4 {#rule04}

Rule is violated: External entities are not represented in the application. Users behave transparent to the server.

#### R5 {#rule05}

Rule is violated: No authentication tokens are used.

#### R6 {#rule06}

Rule is violated: No rate limiting of any means is deployed.



#### R7 {#rule07}

Rule is violated: User external entities can call the gateway service using an unencrypted HTTP connection.

Artifacts:
- 000-default.conf: Line: [1](https://github.com/ewolff/microservice-kafka/blob/master/docker/apache/000-default.conf#L1)
- Dockerfile: Line: [17](https://github.com/ewolff/microservice-kafka/blob/master/docker/apache/Dockerfile#L17)

#### R8 {#rule08}

Rule is violated: All internal services communicate over insecure HTTP connections.

Artifacts:
- 000-default.conf: Lines: [15](https://github.com/ewolff/microservice-kafka/blob/master/docker/apache/000-default.conf#L15), [18](https://github.com/ewolff/microservice-kafka/blob/master/docker/apache/000-default.conf#L18), [21](https://github.com/ewolff/microservice-kafka/blob/master/docker/apache/000-default.conf#L21)



#### R9 {#rule09}

Rule is violated: No central logging system is deployed.

#### R10 {#rule10}

Rule is violated: No central logging system is deployed. All internal services do perform local logging, however none of the logs are consumed and accessed through monitoring software.

Artifacts:
- InvoiceService.java: Line: [25](https://github.com/ewolff/microservice-kafka/blob/master/microservice-kafka/microservice-kafka-invoicing/src/main/java/com/ewolff/microservice/invoicing/InvoiceService.java#L25)
- OrderKafkaTest.java: Line: [70](https://github.com/ewolff/microservice-kafka/blob/master/microservice-kafka/microservice-kafka-order/src/test/java/com/ewolff/microservice/order/kafka/OrderKafkaTest.java#L70)
- ShipmentService.java: Line: [25](https://github.com/ewolff/microservice-kafka/blob/master/microservice-kafka/microservice-kafka-shipping/src/main/java/com/ewolff/microservice/shipping/ShipmentService.java#L25)

#### R11 {#rule11}

Rule is adhered to: All internal services perform structured logging and only entity IDs and events are logged. No PII or secrets will be leaked by the logging messages (see example artifact).

Artifacts:
- InvoiceService.java: Line: [25](https://github.com/ewolff/microservice-kafka/blob/master/microservice-kafka/microservice-kafka-invoicing/src/main/java/com/ewolff/microservice/invoicing/InvoiceService.java#L25)

#### R12 {#rule12}

Rule is violated: The deployed Kafka message broker does not handle logging. No logs are collected.



#### R13 {#rule13}

Rule is violated: No explicit circuit breaker is deployed.

#### R14 {#rule14}

Rule is violated: No load balancing is deployed.

#### R15 {#rule15}

This rule is not applicable: Not a service mesh deployment.



#### R16 {#rule16}

Rule is violated: No service registration is deployed. Services are statically linked.

Artifacts:
- 000-default.conf: Lines: [15](https://github.com/ewolff/microservice-kafka/blob/master/docker/apache/000-default.conf#L15), [18](https://github.com/ewolff/microservice-kafka/blob/master/docker/apache/000-default.conf#L18), [21](https://github.com/ewolff/microservice-kafka/blob/master/docker/apache/000-default.conf#L21)

#### R17 {#rule17}

Rule is violated: No service registration is deployed. Services are statically linked.

Artifacts:
- 000-default.conf: Lines: [15](https://github.com/ewolff/microservice-kafka/blob/master/docker/apache/000-default.conf#L15), [18](https://github.com/ewolff/microservice-kafka/blob/master/docker/apache/000-default.conf#L18), [21](https://github.com/ewolff/microservice-kafka/blob/master/docker/apache/000-default.conf#L21)



#### R18 {#rule18}

Rule is violated: No secret manager is deployed.
