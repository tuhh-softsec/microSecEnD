---
title: mudigal-technologies/microservices-sample
keywords: model
tags: [consul, docker, docker_compose, elasticsearch, kibana, logstash, nginx, rabbitmq, weave_scope, zuul]
sidebar: datasetdoc_sidebar
permalink: mudigal-technologies_microservices-sample.html
toc: false
---

## General Information

The repository for this application ([open on GitHub](https://github.com/mudigal-technologies/microservices-sample)) has 310 stars and was forked 317 times. The codebase consists of 14527 lines of code and makes use of the following technologies:

<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_consul.html">Consul</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_docker.html">Docker</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_docker_compose.html">Docker Compose</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_elasticsearch.html">Elasticsearch</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_kibana.html">Kibana</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_logstash.html">Logstash</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_nginx.html">Nginx</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_rabbitmq.html">RabbitMQ</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_weave_scope.html">Weave Scope</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_zuul.html">Zuul</a>

## Data Flow Diagram

![Dataflow Diagram](./mudigal-technologies_microservices-sample.png)

Download the following model file [here](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/mudigal-technologies_microservices-sample/mudigal-technologies_microservices-sample.json).
Other formats are provided below.

```json
{
    "services": [
        {
            "name": "consul",
            "stereotypes": [
                "service_discovery",
                "infrastructural"
            ],
            "tagged_values": {
                "Service Discovery": "Consul",
                "Port": 8500
            }
        },
        {
            "name": "consul2",
            "stereotypes": [
                "service_discovery",
                "infrastructural"
            ],
            "tagged_values": {
                "Service Discovery": "Consul",
                "Port": 8500
            }
        },
        {
            "name": "consul3",
            "stereotypes": [
                "service_discovery",
                "infrastructural"
            ],
            "tagged_values": {
                "Service Discovery": "Consul",
                "Port": 8500
            }
        },
        {
            "name": "elasticsearch",
            "stereotypes": [
                "search_engine",
                "infrastructural"
            ],
            "tagged_values": {
                "Search Engine": "Elasticsearch",
                "Port": 9200
            }
        },
        {
            "name": "logstash",
            "stereotypes": [
                "logging_server",
                "infrastructural"
            ],
            "tagged_values": {
                "Logging Server": "Logstash",
                "Port": 5000
            }
        },
        {
            "name": "kibana",
            "stereotypes": [
                "monitoring_dashboard",
                "infrastructural"
            ],
            "tagged_values": {
                "Monitoring Dashboard": "Kibana",
                "Port": 5601
            }
        },
        {
            "name": "rabbit",
            "stereotypes": [
                "message_broker",
                "plaintext_credentials",
                "infrastructural"
            ],
            "tagged_values": {
                "Message Broker": "RabbitMQ",
                "Port": 15672,
                "Username": "mudigal",
                "Password": "mudigal"
            }
        },
        {
            "name": "service_one",
            "stereotypes": [
                "internal",
                "local_logging"
            ],
            "tagged_values": {
                "Port": 8082
            }
        },
        {
            "name": "service_two",
            "stereotypes": [
                "internal",
                "local_logging"
            ],
            "tagged_values": {
                "Port": 8084
            }
        },
        {
            "name": "service_one_db",
            "stereotypes": [
                "database",
                "plaintext_credentials"
            ],
            "tagged_values": {
                "Database": "MongoDB",
                "Username": "service-one",
                "Password": "service-one",
                "Port": 27017
            }
        },
        {
            "name": "service_two_db",
            "stereotypes": [
                "database",
                "plaintext_credentials"
            ],
            "tagged_values": {
                "Database": "MySQL",
                "Username": "service-two",
                "Password": "service-two",
                "Port": 3310
            }
        },
        {
            "name": "api_gateway",
            "stereotypes": [
                "gateway",
                "infrastructural",
                "load_balancer"
            ],
            "tagged_values": {
                "Gateway": "Zuul",
                "Load Balancer": "Ribbon",
                "Port": 8080
            }
        },
        {
            "name": "web_application",
            "stereotypes": [
                "web_application",
                "infrastructural"
            ],
            "tagged_values": {
                "Web Application": "Nginx",
                "Port": 4200
            }
        },
        {
            "name": "scope",
            "stereotypes": [
                "monitoring_dashboard",
                "infrastructural"
            ],
            "tagged_values": {
                "Monitoring Dashboard": "Weave Scope",
                "Port": 4040
            }
        }
    ],
    "information_flows": [
        {
            "sender": "consul2",
            "receiver": "consul",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "consul3",
            "receiver": "consul",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "consul3",
            "receiver": "consul2",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "logstash",
            "receiver": "elasticsearch",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "elasticsearch",
            "receiver": "kibana",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "consul",
            "receiver": "service_one",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "service_one",
            "receiver": "logstash",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "service_one",
            "receiver": "rabbit",
            "stereotypes": [
                "message_producer_rabbitmq",
                "plaintext_credentials_link",
                "restful_http"
            ],
            "tagged_values": {
                "'Producer Exchange'": "\"com.mudigal.microservices-sample.services-exchange\"",
                " 'Routing Key'": "\"com.mudigal.microservices-sample.service-*\""
            }
        },
        {
            "sender": "rabbit",
            "receiver": "service_one",
            "stereotypes": [
                "message_consumer_rabbitmq",
                "restful_http"
            ],
            "tagged_values": {
                "'Queue'": "\"com.mudigal.microservices-sample.service-one\""
            }
        },
        {
            "sender": "consul",
            "receiver": "service_two",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "service_two",
            "receiver": "logstash",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "service_two",
            "receiver": "rabbit",
            "stereotypes": [
                "message_producer_rabbitmq",
                "restful_http",
                "plaintext_credentials_link"
            ],
            "tagged_values": {
                "'Producer Exchange'": "\"com.mudigal.microservices-sample.services-exchange\"",
                " 'Routing Key'": "\"com.mudigal.microservices-sample.service-*\""
            }
        },
        {
            "sender": "rabbit",
            "receiver": "service_two",
            "stereotypes": [
                "message_consumer_rabbitmq",
                "restful_http"
            ],
            "tagged_values": {
                "'Queue'": "\"com.mudigal.microservices-sample.service-two\""
            }
        },
        {
            "sender": "service_one_db",
            "receiver": "service_one",
            "stereotypes": [
                "jdbc"
            ],
            "tagged_values": {}
        },
        {
            "sender": "service_two_db",
            "receiver": "service_two",
            "stereotypes": [
                "jdbc",
                "plaintext_credentials_link"
            ],
            "tagged_values": {
                "'Username'": "\"service-two\"",
                " 'Password'": "\"service-two\""
            }
        },
        {
            "sender": "api_gateway",
            "receiver": "service_one",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "api_gateway",
            "receiver": "service_two",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "consul",
            "receiver": "api_gateway",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "user",
            "receiver": "web_application",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "web_application",
            "receiver": "user",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "web_application",
            "receiver": "api_gateway",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "api_gateway",
            "receiver": "scope",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "service_one",
            "receiver": "scope",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "service_one_db",
            "receiver": "scope",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "service_two",
            "receiver": "scope",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "service_two_db",
            "receiver": "scope",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "web_application",
            "receiver": "scope",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "rabbit",
            "receiver": "scope",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "consul",
            "receiver": "scope",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "consul2",
            "receiver": "scope",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "consul3",
            "receiver": "scope",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "kibana",
            "receiver": "scope",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "elasticsearch",
            "receiver": "scope",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "logstash",
            "receiver": "scope",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
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

The Application consists of a total of 164 elements:

Element | Count
-- | --
Services | 14
External Entities | 1
Information Flows | 34
Annotations | 115
Total Items | 164

### Model Representations {#representations}

Open the model in the following formats:

- [JSON model](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/mudigal-technologies_microservices-sample/mudigal-technologies_microservices-sample.json)
- [PlantUML description](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/mudigal-technologies_microservices-sample/mudigal-technologies_microservices-sample.txt)
- [PNG graph](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/mudigal-technologies_microservices-sample/mudigal-technologies_microservices-sample.png)
- [CodeableModels](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/mudigal-technologies_microservices-sample/mudigal-technologies_microservices-sample.py)

### Traceability

Open the traceability information for all model items:

- [Traceability](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/mudigal-technologies_microservices-sample/mudigal-technologies_microservices-sample_traceability.json)

## Security Rules

The following table shows the application's adherence to the 17 architectural security rules. The last column provides model variants that adhere to the rule for each rule that is initially violated.

Rule ID &nbsp;&nbsp;| Verdict &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| Evidence &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| Model Variant &nbsp;&nbsp;&nbsp;|
-- | -- | -- | -- |
**R1** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule01">Evidence |  |
**R2** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule02">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/mudigal-technologies_microservices-sample/model_variants/2.txt) |
**R3** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule03">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/mudigal-technologies_microservices-sample/model_variants/3.txt) |
**R4** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule04">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/mudigal-technologies_microservices-sample/model_variants/4.txt) |
**R5** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule05">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/mudigal-technologies_microservices-sample/model_variants/5.txt) |
**R6** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule06">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/mudigal-technologies_microservices-sample/model_variants/6.txt) |
**R7** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule07">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/mudigal-technologies_microservices-sample/model_variants/7.txt) |
**R8** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule08">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/mudigal-technologies_microservices-sample/model_variants/8.txt) |
**R9** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule09">Evidence |  |
**R10** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule10">Evidence |  |
**R11** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule11">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/mudigal-technologies_microservices-sample/model_variants/11.txt) |
**R12** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule12">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/mudigal-technologies_microservices-sample/model_variants/12.txt) |
**R13** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule13">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/mudigal-technologies_microservices-sample/model_variants/13.txt) |
**R14** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule14">Evidence |  |
**R16** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule16">Evidence |  |
**R17** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule17">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/mudigal-technologies_microservices-sample/model_variants/17.txt) |
**R18** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule18">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/mudigal-technologies_microservices-sample/model_variants/18.txt) |



### Evidence and explanations for rule decisions

#### R1 {#rule01}

Rule is adhered to: User only communicates with the Nginx proxy, that acts proxies all requests.

Artifacts:
- Dockerfile: Line: [23](https://github.com/mudigal-technologies/microservices-sample/blob/master/web-application/docker/Dockerfile#L23)

#### R2  {#rule02}

Rule is violated: The services do not authenticate requests mutually. No client authentication is configured and no authentication header is used.

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

#### R8 {#rule08}

Rule is violated: All internal services communicate over insecure HTTP connections.

Artifacts:
- gateway.service.ts: Line: [13](https://github.com/mudigal-technologies/microservices-sample/blob/master/web-application/src/app/service/gateway/gateway.service.ts#L13)



#### R9 {#rule09}

Rule is adhered to: This microservice application deploys the ELK stack (Elasticsearch, Logstash, Kibana) as a logging mechanism. Logstash is deployed as a central logging subsystem. Logstash then sends the formatted data to an Elasticsearch indexing server. Additionally Kibana is deployed as a monitoring dashboard on top of the indexing server.

Artifacts:
- docker-compose.yml: Lines: [214](https://github.com/mudigal-technologies/microservices-sample/blob/master/build/docker/docker-compose.yml#L214), [233](https://github.com/mudigal-technologies/microservices-sample/blob/master/build/docker/docker-compose.yml#L233), [261](https://github.com/mudigal-technologies/microservices-sample/blob/master/build/docker/docker-compose.yml#L261)

#### R10 {#rule10}

Rule is adhered to: Both service containers and the API gateway deploy local logging agents. The services use logback as a local logging agent to send the collected log files from the spring servers to the central logstash server.

Artifacts:
- logback.xml: Line: [23](https://github.com/mudigal-technologies/microservices-sample/blob/master/api-gateway/src/main/resources/logback.xml#L23)
- logback-spring.xml: Line: [20](https://github.com/mudigal-technologies/microservices-sample/blob/master/service-one/src/main/resources/logback-spring.xml#L20)
- logback-spring.xml: Line: [20](https://github.com/mudigal-technologies/microservices-sample/blob/master/service-two/src/main/resources/logback-spring.xml#L20)

#### R11 {#rule11}

Rule is violated: No explicit log sanitization is deployed. Even though no API keys or PII are written to any log in this application, this rule is still considered disregarded because the string data sent via RabbitMQ is directly logged without local checking (see exemplary artifacts).

Artifacts:
- ServiceOneRabbitMessageConsumer.java: Line: [40](https://github.com/mudigal-technologies/microservices-sample/blob/master/service-one/src/main/java/com/mudigal/one/service/impl/ServiceOneRabbitMessageConsumer.java#L40)
- ServiceTwoRabbitMessageConsumer.java: Line: [38](https://github.com/mudigal-technologies/microservices-sample/blob/master/service-two/src/main/java/com/mudigal/two/service/impl/ServiceTwoRabbitMessageConsumer.java#L38)

#### R12 {#rule12}

Rule is violated: The communication between logging agents is not brokered by any message broker. The deployed RabbitMQ broker only handles service queues, not logging calls. The logs are not encrypted during transmission and not mutually authenticated, nor is any availability ensured apart from container startup dependencies.

Artifacts:
- logback.xml: Line: [23](https://github.com/mudigal-technologies/microservices-sample/blob/master/api-gateway/src/main/resources/logback.xml#L23)



#### R13 {#rule13}

Rule is violated: No explicit circuit breaker is deployed.

#### R14 {#rule14}

Rule is adhered to: The Zuul API gateway performs load balancing using Ribbon by default.

Artifacts:
- ApiGatewayApplication.java: Line: [17](https://github.com/mudigal-technologies/microservices-sample/blob/master/api-gateway/src/main/java/com/mudigal/ApiGatewayApplication.java#L17)

#### R15 {#rule15}

This rule is not applicable: Not a service mesh deployment.



#### R16 {#rule16}

Rule is adhered to: Consul is deployed as a service registry.

Artifacts:
- RegistryApplication.java: Line: [19](https://github.com/mudigal-technologies/microservices-sample/blob/master/webservice-registry/src/main/java/com/anilallewar/microservices/registry/RegistryApplication.java#L19)

#### R17 {#rule17}

Rule is violated: Registration with the Consul server is not secured using access tokens or access control lists.

Artifacts:
- docker-compose.yml: Lines: [156](https://github.com/mudigal-technologies/microservices-sample/blob/master/build/docker/docker-compose.yml#L156), [166](https://github.com/mudigal-technologies/microservices-sample/blob/master/build/docker/docker-compose.yml#L166), [179](https://github.com/mudigal-technologies/microservices-sample/blob/master/build/docker/docker-compose.yml#L179)
- application.yml: Line: [50](https://github.com/mudigal-technologies/microservices-sample/blob/master/service-one/src/main/resources/application.yml#L50)



#### R18 {#rule18}

Rule is violated: No secret manager is deployed. Passwords are either deployed in plaintext in the Docker Compose configuration or in the Spring Boot configuration.

Artifacts:
- docker-compose.yml: Lines: [52](https://github.com/mudigal-technologies/microservices-sample/blob/master/build/docker/docker-compose.yml#L52), [94](https://github.com/mudigal-technologies/microservices-sample/blob/master/build/docker/docker-compose.yml#L94), [97](https://github.com/mudigal-technologies/microservices-sample/blob/master/build/docker/docker-compose.yml#L97), [141](https://github.com/mudigal-technologies/microservices-sample/blob/master/build/docker/docker-compose.yml#L141)
- application.yml: Line: [64](https://github.com/mudigal-technologies/microservices-sample/blob/master/service-one/src/main/resources/application.yml#L64)
- application.yml: Lines: [46](https://github.com/mudigal-technologies/microservices-sample/blob/master/service-two/src/main/resources/application.yml#L46), [74](https://github.com/mudigal-technologies/microservices-sample/blob/master/service-two/src/main/resources/application.yml#L74), [85](https://github.com/mudigal-technologies/microservices-sample/blob/master/service-two/src/main/resources/application.yml#L85)
