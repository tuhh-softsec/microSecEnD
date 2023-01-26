---
title: yidongnan/spring-cloud-netflix-example
keywords: model
tags: [docker, docker_compose, eureka, gradle, hystrix, rabbitmq, ribbon, spring_admin, spring_config, turbine, zipkin, zuul]
sidebar: datasetdoc_sidebar
permalink: yidongnan_spring-cloud-netflix-example.html
toc: false
---

## General Information

The repository for this application ([open on GitHub](https://github.com/yidongnan/spring-cloud-netflix-example)) has 782 stars and was forked 370 times. The codebase consists of 1182 lines of code and makes use of the following technologies:

<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_docker.html">Docker</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_docker_compose.html">Docker Compose</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_eureka.html">Eureka</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_gradle.html">Gradle</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_hystrix.html">Hystrix</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_rabbitmq.html">RabbitMQ</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_ribbon.html">Ribbon</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_spring_admin.html">Spring Admin</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_spring_config.html">Spring Config</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_turbine.html">Turbine</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_zipkin.html">Zipkin</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_zuul.html">Zuul</a>

## Data Flow Diagram

![Dataflow Diagram](./yidongnan_spring-cloud-netflix-example.png)

Download the following model file [here](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/yidongnan_spring-cloud-netflix-example/yidongnan_spring-cloud-netflix-example.json).
Other formats are provided below.

```json
{
    "services": [
        {
            "name": "admin_dashboard",
            "stereotypes": [
                "administration_server",
                "infrastructural",
                "csrf_disabled"
            ],
            "tagged_values": {
                "Administration Server": "Spring Boot Admin",
                "Port": 8040
            }
        },
        {
            "name": "eureka_server",
            "stereotypes": [
                "service_discovery",
                "infrastructural",
                "csrf_disabled"
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
                "Port": 4369
            }
        },
        {
            "name": "config_server",
            "stereotypes": [
                "configuration_server",
                "infrastructural",
                "csrf_disabled"
            ],
            "tagged_values": {
                "Configuration Server": "Spring Cloud Config",
                "Port": 8100
            }
        },
        {
            "name": "hystrix_dashboard",
            "stereotypes": [
                "monitoring_dashboard",
                "monitoring_server",
                "infrastructural",
                "csrf_disabled"
            ],
            "tagged_values": {
                "Monitoring Dashboard": "Hystrix",
                "Monitoring Server": "Turbine",
                "Port": 8050
            }
        },
        {
            "name": "service_a",
            "stereotypes": [
                "internal",
                "circuit_breaker",
                "csrf_disabled"
            ],
            "tagged_values": {
                "Port": 8080,
                "Endpoints": [
                    "/"
                ],
                "Circuit Breaker": "Hystrix"
            }
        },
        {
            "name": "service_b",
            "stereotypes": [
                "internal",
                "csrf_disabled"
            ],
            "tagged_values": {
                "Port": 8070,
                "Endpoints": [
                    "/"
                ]
            }
        },
        {
            "name": "zuul",
            "stereotypes": [
                "gateway",
                "infrastructural",
                "load_balancer",
                "csrf_disabled"
            ],
            "tagged_values": {
                "Gateway": "Zuul",
                "Port": 8060,
                "Load Balancer": "Ribbon"
            }
        },
        {
            "name": "zipkin",
            "stereotypes": [
                "tracing_server",
                "infrastructural"
            ],
            "tagged_values": {
                "Tracing Server": "Zipkin",
                "Port": 9411
            }
        }
    ],
    "information_flows": [
        {
            "sender": "admin_dashboard",
            "receiver": "config_server",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "config_server",
            "receiver": "eureka_server",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "config_server",
            "receiver": "rabbitmq",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "admin_dashboard",
            "receiver": "eureka_server",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "admin_dashboard",
            "receiver": "hystrix_dashboard",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "hystrix_dashboard",
            "receiver": "eureka_server",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "admin_dashboard",
            "receiver": "service_a",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "service_a",
            "receiver": "rabbitmq",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "config_server",
            "receiver": "service_a",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "service_a",
            "receiver": "eureka_server",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "service_a",
            "receiver": "hystrix_dashboard",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "admin_dashboard",
            "receiver": "service_b",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "service_b",
            "receiver": "rabbitmq",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "config_server",
            "receiver": "service_b",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "service_b",
            "receiver": "eureka_server",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "service_a",
            "receiver": "service_b",
            "stereotypes": [
                "restful_http",
                "feign_connection"
            ],
            "tagged_values": {}
        },
        {
            "sender": "zuul",
            "receiver": "user",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "user",
            "receiver": "zuul",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "zuul",
            "receiver": "service_a",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "eureka_server",
            "receiver": "zuul",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "rabbitmq",
            "receiver": "zipkin",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "service_b",
            "receiver": "zipkin",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "service_b",
            "receiver": "hystrix_dashboard",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "service_a",
            "receiver": "zipkin",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "admin_dashboard",
            "receiver": "rabbitmq",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "admin_dashboard",
            "receiver": "zuul",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "zuul",
            "receiver": "rabbitmq",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "zuul",
            "receiver": "zipkin",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "zuul",
            "receiver": "config_server",
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

The Application consists of a total of 121 elements:

Element | Count
-- | --
Services | 9
External Entities | 1
Information Flows | 30
Annotations | 81
Total Items | 121

### Model Representations {#representations}

Open the model in the following formats:

- [JSON model](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/yidongnan_spring-cloud-netflix-example/yidongnan_spring-cloud-netflix-example.json)
- [PlantUML description](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/yidongnan_spring-cloud-netflix-example/yidongnan_spring-cloud-netflix-example.txt)
- [PNG graph](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/yidongnan_spring-cloud-netflix-example/yidongnan_spring-cloud-netflix-example.png)
- [CodeableModels](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/yidongnan_spring-cloud-netflix-example/yidongnan_spring-cloud-netflix-example.py)

### Traceability

Open the traceability information for all model items:

- [Traceability](..)

## Security Rules

The following table shows the application's adherence to the 17 architectural security rules. The last column provides model variants that adhere to the rule for each rule that is initially violated.

Rule ID &nbsp;&nbsp;| Verdict &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| Evidence &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| Model Variant &nbsp;&nbsp;&nbsp;|
-- | -- | -- | -- |
**R1** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule01">Evidence |  |
**R2** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule02">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/yidongnan_spring-cloud-netflix-example/model_variants/2.txt) |
**R3** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule03">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/yidongnan_spring-cloud-netflix-example/model_variants/3.txt) |
**R4** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule04">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/yidongnan_spring-cloud-netflix-example/model_variants/4.txt) |
**R5** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule05">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/yidongnan_spring-cloud-netflix-example/model_variants/5.txt) |
**R6** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule06">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/yidongnan_spring-cloud-netflix-example/model_variants/6.txt) |
**R7** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule07">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/yidongnan_spring-cloud-netflix-example/model_variants/7.txt) |
**R8** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule08">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/yidongnan_spring-cloud-netflix-example/model_variants/8.txt) |
**R9** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule09">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/yidongnan_spring-cloud-netflix-example/model_variants/9.txt) |
**R10** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule10">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/yidongnan_spring-cloud-netflix-example/model_variants/10.txt) |
**R11** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule11">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/yidongnan_spring-cloud-netflix-example/model_variants/11.txt) |
**R12** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule12">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/yidongnan_spring-cloud-netflix-example/model_variants/12.txt) |
**R13** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule13">Evidence |  |
**R14** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule14">Evidence |  |
**R16** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule16">Evidence |  |
**R17** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule17">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/yidongnan_spring-cloud-netflix-example/model_variants/17.txt) |
**R18** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule18">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/yidongnan_spring-cloud-netflix-example/model_variants/18.txt) |



### Evidence and explanations for rule decisions

#### R1 {#rule01}

Rule is adhered to: User only communicates with the Zuul gateway service.

Artifacts:
- ZuulApplication.java: Line: [17](https://github.com/yidongnan/spring-cloud-netflix-example/blob/master/zuul/src/main/java/net/devh/ZuulApplication.java#L17)
- bootstrap.yml: Line: [2](https://github.com/yidongnan/spring-cloud-netflix-example/blob/master/zuul/src/main/resources/bootstrap.yml#L2)

#### R2  {#rule02}

Rule is violated: The services do not authenticate requests mutually. Internal requests are sent via plain HTTP.

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
- bootstrap.yml: Line: [2](https://github.com/yidongnan/spring-cloud-netflix-example/blob/master/zuul/src/main/resources/bootstrap.yml#L2)

#### R8 {#rule08}

Rule is violated: All internal services communicate over insecure HTTP connections.

Artifacts:
- bootstrap.yml: Line: [2](https://github.com/yidongnan/spring-cloud-netflix-example/blob/master/service-a/src/main/resources/bootstrap.yml#L2)



#### R9 {#rule09}

Rule is violated: No central logging system is deployed.

#### R10 {#rule10}

Rule is violated: No central logging system is deployed.

#### R11 {#rule11}

Rule is violated: Logs are not explicitly sanitized.

#### R12 {#rule12}

Rule is violated: No explicit logging mechanism is deployed.



#### R13 {#rule13}

Rule is adhered to: The internal service with indirect connection to the user (via Zuul) is protected using the Hystrix circuit breaker. Note however, that the circuit breaker is not deployed at the proxy node, but at the internal service.

Artifacts:
- A1ServiceApplication.java: Line: [30](https://github.com/yidongnan/spring-cloud-netflix-example/blob/master/service-a/src/main/java/net/devh/A1ServiceApplication.java#L30)

#### R14 {#rule14}

Rule is adhered to: The Zuul API gateway performs load balancing using Ribbon by default.

Artifacts:
- ZuulApplication.java: Line: [17](https://github.com/yidongnan/spring-cloud-netflix-example/blob/master/zuul/src/main/java/net/devh/ZuulApplication.java#L17)

#### R15 {#rule15}

This rule is not applicable: Not a service mesh deployment.



#### R16 {#rule16}

Rule is adhered to:
1. Registry Service (Eureka Server) with @EnableEurekaServer present.
1. Started in Docker Container through Compose, thus deployable on dedicated server

Artifacts:
- EurekaServeApplication.java: Line: [10](https://github.com/yidongnan/spring-cloud-netflix-example/blob/master/eureka-server/src/main/java/net/devh/EurekaServeApplication.java#L10)
- docker-compose.yml: Line: [15](https://github.com/yidongnan/spring-cloud-netflix-example/blob/master/docker-compose.yml#L15)

#### R17 {#rule17}

Rule is violated: No HTTP basic password listed in any YML-Configuration of format username:password@here-location-of-eureka-server at "eureka.client.serviceUrl.defaultZone".

Artifacts:
- EurekaServeApplication.java: Line: [10](https://github.com/yidongnan/spring-cloud-netflix-example/blob/master/eureka-server/src/main/java/net/devh/EurekaServeApplication.java#L10)
- bootstrap.yml: Lines: [39](https://github.com/yidongnan/spring-cloud-netflix-example/blob/master/eureka-server/src/main/resources/bootstrap.yml#L39), [49](https://github.com/yidongnan/spring-cloud-netflix-example/blob/master/eureka-server/src/main/resources/bootstrap.yml#L49)



#### R18 {#rule18}

Rule is violated: No secret manager is deployed.
