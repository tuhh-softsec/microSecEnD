---
title: fernandoabcampos/spring-netflix-oss-microservices
keywords: model
tags: [docker, eureka, hystrix, maven, rabbitmq, spring_config, turbine, zuul]
sidebar: datasetdoc_sidebar
permalink: fernandoabcampos_spring-netflix-oss-microservices.html
toc: false
---

## General Information

The repository for this application ([open on GitHub](https://github.com/fernandoabcampos/spring-netflix-oss-microservices)) has 10 stars and was forked 12 times. The codebase consists of 1644 lines of code and makes use of the following technologies:

<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_docker.html">Docker</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_eureka.html">Eureka</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_hystrix.html">Hystrix</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_maven.html">Maven</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_rabbitmq.html">RabbitMQ</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_spring_config.html">Spring Config</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_turbine.html">Turbine</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_zuul.html">Zuul</a>

## Data Flow Diagram

![Dataflow Diagram](./fernandoabcampos_spring-netflix-oss-microservices.png)

Download the following model file [here](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/fernandoabcampos_spring-netflix-oss-microservices/fernandoabcampos_spring-netflix-oss-microservices.json).
Other formats are provided below.

```json
{
    "services": [
        {
            "name": "config_server",
            "stereotypes": [
                "configuration_server",
                "infrastructural"
            ],
            "tagged_values": {
                "Configuration Server": "Spring Cloud Config",
                "Port": 9090
            }
        },
        {
            "name": "discovery_service",
            "stereotypes": [
                "service_discovery",
                "infrastructural"
            ],
            "tagged_values": {
                "Service Discovery": "Eureka",
                "Port": 8761
            }
        },
        {
            "name": "rabbitmq",
            "stereotypes": [
                "message_broker",
                "infrastructural"
            ],
            "tagged_values": {
                "Message Broker": "RabbitMQ",
                "Port": 5672
            }
        },
        {
            "name": "monitor_dashboard",
            "stereotypes": [
                "monitoring_dashboard",
                "infrastructural"
            ],
            "tagged_values": {
                "Monitoring Dashboard": "Hystrix",
                "Port": 8179
            }
        },
        {
            "name": "turbine",
            "stereotypes": [
                "monitoring_server",
                "infrastructural"
            ],
            "tagged_values": {
                "Monitoring Server": "Turbine",
                "Port": 8989
            }
        },
        {
            "name": "statement_service",
            "stereotypes": [
                "internal"
            ],
            "tagged_values": {
                "Port": 8080
            }
        },
        {
            "name": "card_service",
            "stereotypes": [
                "internal"
            ],
            "tagged_values": {
                "Port": 8080
            }
        },
        {
            "name": "card_statement_composite",
            "stereotypes": [
                "internal",
                "circuit_breaker"
            ],
            "tagged_values": {
                "Port": 8080,
                "Circuit Breaker": "Hystrix"
            }
        },
        {
            "name": "edge_server",
            "stereotypes": [
                "gateway",
                "infrastructural",
                "load_balancer"
            ],
            "tagged_values": {
                "Gateway": "Zuul",
                "Port": 8765,
                "Load Balancer": "Ribbon"
            }
        }
    ],
    "external_entities": [
        {
            "name": "github_repository",
            "stereotypes": [
                "github_repository",
                "entrypoint"
            ],
            "tagged_values": {
                "URL": "https://github.com/fernandoabcampos/microservices-config.git"
            }
        },
        {
            "name": "user",
            "stereotypes": [
                "user_stereotype",
                "entrypoint",
                "exitpoint"
            ],
            "tagged_values": {}
        }
    ],
    "information_flows": [
        {
            "sender": "github_repository",
            "receiver": "config_server",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "config_server",
            "receiver": "discovery_service",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "monitor_dashboard",
            "receiver": "discovery_service",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "config_server",
            "receiver": "monitor_dashboard",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "turbine",
            "receiver": "discovery_service",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "rabbitmq",
            "receiver": "turbine",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "config_server",
            "receiver": "turbine",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "turbine",
            "receiver": "monitor_dashboard",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "statement_service",
            "receiver": "discovery_service",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "config_server",
            "receiver": "statement_service",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "card_service",
            "receiver": "discovery_service",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "config_server",
            "receiver": "card_service",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "card_statement_composite",
            "receiver": "discovery_service",
            "stereotypes": [
                "restful_http",
                "circuit_breaker_link"
            ],
            "tagged_values": {}
        },
        {
            "sender": "card_statement_composite",
            "receiver": "card_service",
            "stereotypes": [
                "restful_http",
                "circuit_breaker_link",
                "feign_connection",
                "load_balanced_link"
            ],
            "tagged_values": {
                "'Circuit Breaker'": "\"Hystrix\"",
                " 'Load Balancer'": "\"Ribbon\""
            }
        },
        {
            "sender": "card_statement_composite",
            "receiver": "statement_service",
            "stereotypes": [
                "restful_http",
                "circuit_breaker_link",
                "feign_connection",
                "load_balanced_link"
            ],
            "tagged_values": {
                "'Circuit Breaker'": "\"Hystrix\"",
                " 'Load Balancer'": "\"Ribbon\""
            }
        },
        {
            "sender": "config_server",
            "receiver": "card_statement_composite",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "card_statement_composite",
            "receiver": "rabbitmq",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "discovery_service",
            "receiver": "edge_server",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "user",
            "receiver": "edge_server",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "edge_server",
            "receiver": "user",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "config_server",
            "receiver": "edge_server",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "edge_server",
            "receiver": "card_service",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "edge_server",
            "receiver": "statement_service",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "edge_server",
            "receiver": "card_statement_composite",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        }
    ]
}
```

### Model Items

The Application consists of a total of 110 elements:

Element | Count
-- | --
Services | 9
External Entities | 2
Information Flows | 24
Annotations | 75
Total Items | 110

### Model Representations {#representations}

Open the model in the following formats:

- [JSON model](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/fernandoabcampos_spring-netflix-oss-microservices/fernandoabcampos_spring-netflix-oss-microservices.json)
- [PlantUML description](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/fernandoabcampos_spring-netflix-oss-microservices/fernandoabcampos_spring-netflix-oss-microservices.txt)
- [PNG graph](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/fernandoabcampos_spring-netflix-oss-microservices/fernandoabcampos_spring-netflix-oss-microservices.png)
- [CodeableModels](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/fernandoabcampos_spring-netflix-oss-microservices/fernandoabcampos_spring-netflix-oss-microservices.py)

### Traceability

Open the traceability information for all model items:

- [Traceability](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/fernandoabcampos_spring-netflix-oss-microservices/fernandoabcampos_spring-netflix-oss-microservices_traceability.json)

## Security Rules

The following table shows the application's adherence to the 17 architectural security rules. The last column provides model variants that adhere to the rule for each rule that is initially violated.

Rule ID &nbsp;&nbsp;| Verdict &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| Evidence &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| Model Variant &nbsp;&nbsp;&nbsp;|
-- | -- | -- | -- |
**R1** | <i class="fa fa-warning" style="color: #bfc600;"> | <a href="#rule01">Evidence |  |
**R2** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule02">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/fernandoabcampos_spring-netflix-oss-microservices/model_variants/2.txt) |
**R3** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule03">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/fernandoabcampos_spring-netflix-oss-microservices/model_variants/3.txt) |
**R4** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule04">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/fernandoabcampos_spring-netflix-oss-microservices/model_variants/4.txt) |
**R5** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule05">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/fernandoabcampos_spring-netflix-oss-microservices/model_variants/5.txt) |
**R6** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule06">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/fernandoabcampos_spring-netflix-oss-microservices/model_variants/6.txt) |
**R7** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule07">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/fernandoabcampos_spring-netflix-oss-microservices/model_variants/7.txt) |
**R8** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule08">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/fernandoabcampos_spring-netflix-oss-microservices/model_variants/8.txt) |
**R9** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule09">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/fernandoabcampos_spring-netflix-oss-microservices/model_variants/9.txt) |
**R10** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule10">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/fernandoabcampos_spring-netflix-oss-microservices/model_variants/10.txt) |
**R11** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule11">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/fernandoabcampos_spring-netflix-oss-microservices/model_variants/11.txt) |
**R12** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule12">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/fernandoabcampos_spring-netflix-oss-microservices/model_variants/12.txt) |
**R13** | <i class="fa fa-check-square-o" style="color: #6be16d;"> | <a href="#rule13">Evidence | 
**R14** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule14">Evidence |  |
**R16** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule16">Evidence |  |
**R17** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule17">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/fernandoabcampos_spring-netflix-oss-microservices/model_variants/17.txt) |
**R18** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule18">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/fernandoabcampos_spring-netflix-oss-microservices/model_variants/18.txt) |



### Evidence and explanations for rule decisions

#### R1 {#rule01}

Rule is partially adhered to: The application uses Spring Cloud Zuul as a single entry-point. There is no indication in the repository, that the API gateway does perform authentication/authorization for incoming requests.

Artifacts:

- EdgeServerApplication.java: Line: [10](https://github.com/fernandoabcampos/spring-netflix-oss-microservices/blob/master/edge-server/src/main/java/com/spring/netflix/oss/microservices/EdgeServerApplication.java#L10)

- edge-server.yml: Line: [9](https://github.com/fernandoabcampos/microservices-config/blob/master/MASTER/edge-server.yml#L9)

#### R2  {#rule02}

Rule is violated: Services communicate internally over plain HTTP (See example artifacts). The communication is not authenticated.

Artifacts:
- docker-compose.yml: Lines: [7](https://github.com/fernandoabcampos/spring-netflix-oss-microservices/blob/master/docker-compose.yml#L7), [16](https://github.com/fernandoabcampos/spring-netflix-oss-microservices/blob/master/docker-compose.yml#L16), [30](https://github.com/fernandoabcampos/spring-netflix-oss-microservices/blob/master/docker-compose.yml#L30), [44](https://github.com/fernandoabcampos/spring-netflix-oss-microservices/blob/master/docker-compose.yml#L44), [82](https://github.com/fernandoabcampos/spring-netflix-oss-microservices/blob/master/docker-compose.yml#L82), [93](https://github.com/fernandoabcampos/spring-netflix-oss-microservices/blob/master/docker-compose.yml#L93)

#### R3 {#rule03}

Rule is violated: No authentication mechanism is deployed.

#### R4 {#rule04}

Rule is violated: External entities are not represented in the application. Users behave transparent to the server. Note, that the server has a user-service, that is not used for authentication purposes.

#### R5 {#rule05}

Rule is violated: No authentication tokens are used.

#### R6 {#rule06}

Rule is violated: No rate limiting of any means is deployed.



#### R7 {#rule07}

Rule is violated: User external entities can call the gateway service using an unencrypted HTTP connection.

Artifacts:
- docker-compose.yml: Lines: [7](https://github.com/fernandoabcampos/spring-netflix-oss-microservices/blob/master/docker-compose.yml#L7), [16](https://github.com/fernandoabcampos/spring-netflix-oss-microservices/blob/master/docker-compose.yml#L16), [30](https://github.com/fernandoabcampos/spring-netflix-oss-microservices/blob/master/docker-compose.yml#L30), [44](https://github.com/fernandoabcampos/spring-netflix-oss-microservices/blob/master/docker-compose.yml#L44), [82](https://github.com/fernandoabcampos/spring-netflix-oss-microservices/blob/master/docker-compose.yml#L82), [93](https://github.com/fernandoabcampos/spring-netflix-oss-microservices/blob/master/docker-compose.yml#L93)

#### R8 {#rule08}

Rule is violated: All internal services communicate over insecure HTTP connections.

Artifacts:
- docker-compose.yml: Lines: [7](https://github.com/fernandoabcampos/spring-netflix-oss-microservices/blob/master/docker-compose.yml#L7), [16](https://github.com/fernandoabcampos/spring-netflix-oss-microservices/blob/master/docker-compose.yml#L16), [30](https://github.com/fernandoabcampos/spring-netflix-oss-microservices/blob/master/docker-compose.yml#L30), [44](https://github.com/fernandoabcampos/spring-netflix-oss-microservices/blob/master/docker-compose.yml#L44), [82](https://github.com/fernandoabcampos/spring-netflix-oss-microservices/blob/master/docker-compose.yml#L82), [93](https://github.com/fernandoabcampos/spring-netflix-oss-microservices/blob/master/docker-compose.yml#L93)



#### R9 {#rule09}

Rule is violated: No central logging system is deployed.

#### R10 {#rule10}

Rule is violated: No central logging system is deployed.

#### R11 {#rule11}

Rule is violated: No logs are generated by the application.

#### R12 {#rule12}

Rule is violated: RabbitMQ is deployed as a message broker between the circuit breaker and the monitoring server. It does not handle logging nor is the traffic encrypted and authenticated.



#### R13 {#rule13}

Rule is adhered to: Hystrix is deployed as a [circuit breaker](https://cloud.spring.io/spring-cloud-netflix/multi/multi__router_and_filter_zuul.html#netflix-zuul-reverse-proxy) in the service application and the gateway (see artifacts).

Artifacts:
- EdgeServerApplication.java: Line: [10](https://github.com/fernandoabcampos/spring-netflix-oss-microservices/blob/master/edge-server/src/main/java/com/spring/netflix/oss/microservices/EdgeServerApplication.java#L10)
- CardServiceApplication.java: Line: [8](https://github.com/fernandoabcampos/spring-netflix-oss-microservices/blob/master/card-service/src/main/java/com/spring/netflix/oss/microservices/CardServiceApplication.java#L8)
- StatementServiceApplication.java: Line: [8](https://github.com/fernandoabcampos/spring-netflix-oss-microservices/blob/master/statement-service/src/main/java/com/spring/netflix/oss/microservices/StatementServiceApplication.java#L8)

#### R14 {#rule14}

Rule is adhered to: The gateway server uses load balancing via [Ribbon](https://cloud.spring.io/spring-cloud-netflix/multi/multi__router_and_filter_zuul.html#netflix-zuul-reverse-proxy) to access dependent services.

Artifacts:
- EdgeServerApplication.java: Line: [10](https://github.com/fernandoabcampos/spring-netflix-oss-microservices/blob/master/edge-server/src/main/java/com/spring/netflix/oss/microservices/EdgeServerApplication.java#L10)

#### R15 {#rule15}

This rule is not applicable: Not a service mesh deployment.



#### R16 {#rule16}

Rule is adhered to:
1. Registry Service (Eureka Server) with [@EnableEurekaServer](https://docs.spring.io/spring-cloud-netflix/docs/4.0.1-SNAPSHOT/reference/html/#spring-cloud-eureka-server) present.
1. Started in Docker Container through Compose, thus deployable on dedicated server

Artifacts:
- DiscoveryServiceApplication.java: Line: [8](https://github.com/fernandoabcampos/spring-netflix-oss-microservices/blob/master/discovery-service/src/main/java/com/spring/netflix/oss/microservices/DiscoveryServiceApplication.java#L8)
- docker-compose.yml: Line: [12](https://github.com/fernandoabcampos/spring-netflix-oss-microservices/blob/master/docker-compose.yml#L12)

#### R17 {#rule17}

Rule is violated: No [HTTP basic password](https://cloud.spring.io/spring-cloud-netflix/reference/html/#authenticating-with-the-eureka-server)  listed in any YML-Configuration of format username:password@here-location-of-eureka-server at "eureka.client.serviceUrl.defaultZone".

Artifacts:
- DiscoveryServiceApplication.java: Line: [8](https://github.com/fernandoabcampos/spring-netflix-oss-microservices/blob/master/discovery-service/src/main/java/com/spring/netflix/oss/microservices/DiscoveryServiceApplication.java#L8)
- card-service.yml: Line: [8](https://github.com/fernandoabcampos/microservices-config/blob/master/MASTER/card-service.yml#L8)



#### R18 {#rule18}

Rule is violated: No secret manager is deployed. The deployed git configuration server is not a secrets manager.

Artifacts:
- ConfigServerApplication.java: Line: [8](https://github.com/fernandoabcampos/spring-netflix-oss-microservices/blob/master/config-server/src/main/java/com/spring/netflix/oss/microservices/ConfigServerApplication.java#L8)
