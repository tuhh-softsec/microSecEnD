---
title: shabbirdwd53/Springboot-Microservice
keywords: model
tags: [eureka, hystrix, maven, spring_config, spring_gateway, zipkin]
sidebar: datasetdoc_sidebar
permalink: shabbirdwd53_springboot-microservice.html
toc: false
---

## General Information

The repository for this application ([open on GitHub](https://github.com/shabbirdwd53/Springboot-Microservice)) has 272 stars and was forked 570 times. The codebase consists of 879 lines of code and makes use of the following technologies:

<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_eureka.html">Eureka</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_hystrix.html">Hystrix</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_maven.html">Maven</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_spring_config.html">Spring Config</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_spring_gateway.html">Spring Gateway</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_zipkin.html">Zipkin</a>

## Data Flow Diagram

![Dataflow Diagram](./shabbirdwd53_springboot-microservice.png)

Download the following model file [here](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/shabbirdwd53_springboot-microservice/shabbirdwd53_springboot-microservice.json).
Other formats are provided below.

```json
{
    "services": [
        {
            "name": "service_registry",
            "stereotypes": [
                "infrastructural",
                "service_discovery"
            ],
            "tagged_values": {
                "Port": 8761,
                "Service Discovery": "Eureka"
            }
        },
        {
            "name": "config_server",
            "stereotypes": [
                "infrastructural",
                "configuration_server"
            ],
            "tagged_values": {
                "Port": 9296,
                "Configuration Server": "Spring Cloud Config"
            }
        },
        {
            "name": "zipkin_server",
            "stereotypes": [
                "infrastructural",
                "tracing_server"
            ],
            "tagged_values": {
                "Port": 9411,
                "Tracing Server": "Zipkin"
            }
        },
        {
            "name": "department_service",
            "stereotypes": [
                "internal",
                "local_logging"
            ],
            "tagged_values": {
                "Port": 9001,
                "Endpoints": [
                    "/departments",
                    "/departments/{id}"
                ],
                "Logging Technology": "Lombok"
            }
        },
        {
            "name": "user_service",
            "stereotypes": [
                "internal",
                "local_logging",
                "load_balancer"
            ],
            "tagged_values": {
                "Port": 9002,
                "Endpoints": [
                    "/users",
                    "/users/{id}"
                ],
                "Load Balancer": "Spring Cloud",
                "Logging Technology": "Lombok"
            }
        },
        {
            "name": "hystrix_dashboard",
            "stereotypes": [
                "infrastructural",
                "monitoring_dashboard",
                "local_logging"
            ],
            "tagged_values": {
                "Port": 9295,
                "Monitoring Dashboard": "Hystrix"
            }
        },
        {
            "name": "api_gateway",
            "stereotypes": [
                "infrastructural",
                "gateway",
                "circuit_breaker",
                "load_balancer"
            ],
            "tagged_values": {
                "Port": 9191,
                "Gateway": "Spring Cloud Gateway",
                "Circuit Breaker": "Hystrix",
                "Endpoints": [
                    "/userServiceFallBack",
                    "/departmentServiceFallBack"
                ]
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
                "URL": "https://github.com/shabbirdwd53/config-server"
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
            "receiver": "service_registry",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "department_service",
            "receiver": "zipkin_server",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "config_server",
            "receiver": "department_service",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "department_service",
            "receiver": "service_registry",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "user_service",
            "receiver": "zipkin_server",
            "stereotypes": [
                "restful_http",
                "load_balanced_link"
            ],
            "tagged_values": {}
        },
        {
            "sender": "config_server",
            "receiver": "user_service",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "user_service",
            "receiver": "service_registry",
            "stereotypes": [
                "restful_http",
                "load_balanced_link"
            ],
            "tagged_values": {}
        },
        {
            "sender": "user_service",
            "receiver": "department_service",
            "stereotypes": [
                "restful_http",
                "load_balanced_link"
            ],
            "tagged_values": {}
        },
        {
            "sender": "config_server",
            "receiver": "hystrix_dashboard",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "hystrix_dashboard",
            "receiver": "service_registry",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "api_gateway",
            "receiver": "user",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "user",
            "receiver": "api_gateway",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "service_registry",
            "receiver": "api_gateway",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "config_server",
            "receiver": "api_gateway",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "api_gateway",
            "receiver": "user_service",
            "stereotypes": [
                "restful_http",
                "circuit_breaker_link",
                "load_balanced_link"
            ],
            "tagged_values": {}
        },
        {
            "sender": "api_gateway",
            "receiver": "department_service",
            "stereotypes": [
                "restful_http",
                "circuit_breaker_link",
                "load_balanced_link"
            ],
            "tagged_values": {}
        },
        {
            "sender": "zipkin_server",
            "receiver": "hystrix_dashboard",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        }
    ]
}
```

### Model Items

The Application consists of a total of 92 elements:

Element | Count
-- | --
Services | 7
External Entities | 2
Information Flows | 18
Annotations | 65
Total Items | 92

### Model Representations {#representations}

Open the model in the following formats:

- [JSON model](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/shabbirdwd53_springboot-microservice/shabbirdwd53_springboot-microservice.json)
- [PlantUML description](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/shabbirdwd53_springboot-microservice/shabbirdwd53_springboot-microservice.txt)
- [PNG graph](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/shabbirdwd53_springboot-microservice/shabbirdwd53_springboot-microservice.png)
- [CodeableModels](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/shabbirdwd53_springboot-microservice/shabbirdwd53_springboot-microservice.py)

### Traceability

Open the traceability information for all model items:

- [Traceability](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/shabbirdwd53_springboot-microservice/shabbirdwd53_springboot-microservice_traceability.json)

## Security Rules

The following table shows the application's adherence to the 17 architectural security rules. The last column provides model variants that adhere to the rule for each rule that is initially violated.

Rule ID &nbsp;&nbsp;| Verdict &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| Evidence &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| Model Variant &nbsp;&nbsp;&nbsp;|
-- | -- | -- | -- |
**R1** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule01">Evidence |  |
**R2** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule02">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/shabbirdwd53_springboot-microservice/model_variants/2.txt) |
**R3** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule03">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/shabbirdwd53_springboot-microservice/model_variants/3.txt) |
**R4** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule04">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/shabbirdwd53_springboot-microservice/model_variants/4.txt) |
**R5** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule05">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/shabbirdwd53_springboot-microservice/model_variants/5.txt) |
**R6** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule06">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/shabbirdwd53_springboot-microservice/model_variants/6.txt) |
**R7** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule07">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/shabbirdwd53_springboot-microservice/model_variants/7.txt) |
**R8** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule08">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/shabbirdwd53_springboot-microservice/model_variants/8.txt) |
**R9** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule09">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/shabbirdwd53_springboot-microservice/model_variants/9.txt) |
**R10** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule10">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/shabbirdwd53_springboot-microservice/model_variants/10.txt) |
**R11** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule11">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/shabbirdwd53_springboot-microservice/model_variants/11.txt) |
**R12** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule12">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/shabbirdwd53_springboot-microservice/model_variants/12.txt) |
**R13** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule13">Evidence |  |
**R14** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule14">Evidence |  |
**R16** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule16">Evidence |  |
**R17** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule17">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/shabbirdwd53_springboot-microservice/model_variants/17.txt) |
**R18** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule18">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/shabbirdwd53_springboot-microservice/model_variants/18.txt) |



### Evidence and explanations for rule decisions

#### R1 {#rule01}

Rule is adhered to: User only communicates with the Spring Cloud gateway server.

Artifacts:
- application.yml: Line: [2](https://github.com/shabbirdwd53/Springboot-Microservice/blob/master/cloud-gateway/src/main/resources/application.yml#L2)

#### R2  {#rule02}

Rule is violated: Services communicate internally over plain HTTP. The communication is not authenticated.

Artifacts:
- application.yml: Line: [2](https://github.com/shabbirdwd53/Springboot-Microservice/blob/master/department-service/src/main/resources/application.yml#L2)
- application.yml: Line: [2](https://github.com/shabbirdwd53/Springboot-Microservice/blob/master/user-service/src/main/resources/application.yml#L2)

#### R3 {#rule03}

Rule is violated: No authentication mechanism is deployed.

#### R4 {#rule04}

Rule is violated: Users are represented by IDs in the user registry. However, these user representations are not used to authenticate incoming connections.

#### R5 {#rule05}

Rule is violated: No authentication tokens are used.

#### R6 {#rule06}

Rule is violated: No rate limiting of any means is deployed.



#### R7 {#rule07}

Rule is violated: User external entities can call the gateway service using an unencrypted HTTP connection.

Artifacts:
- application.yml: Line: [2](https://github.com/shabbirdwd53/Springboot-Microservice/blob/master/cloud-gateway/src/main/resources/application.yml#L2)

#### R8 {#rule08}

Rule is violated: All internal services communicate over insecure HTTP connections.

Artifacts:
- application.yml: Lines: [11](https://github.com/shabbirdwd53/Springboot-Microservice/blob/master/cloud-gateway/src/main/resources/application.yml#L11), [20](https://github.com/shabbirdwd53/Springboot-Microservice/blob/master/cloud-gateway/src/main/resources/application.yml#L20)



#### R9 {#rule09}

Rule is violated: No central logging system is deployed. This application uses the Hystrix monitoring dashboard to traces reported by the Zipkin tracing server.

#### R10 {#rule10}

Rule is violated: No central logging system is deployed. All internal services do perform local logging using Lombok, however none of the logs are consumed and accessed through monitoring software.

Artifacts:
- UserController.java: Lines: [21](https://github.com/shabbirdwd53/Springboot-Microservice/blob/master/user-service/src/main/java/com/dailycodebuffer/user/controller/UserController.java#L21), [27](https://github.com/shabbirdwd53/Springboot-Microservice/blob/master/user-service/src/main/java/com/dailycodebuffer/user/controller/UserController.java#L27)
- UserService.java: Lines: [23](https://github.com/shabbirdwd53/Springboot-Microservice/blob/master/user-service/src/main/java/com/dailycodebuffer/user/service/UserService.java#L23), [28](https://github.com/shabbirdwd53/Springboot-Microservice/blob/master/user-service/src/main/java/com/dailycodebuffer/user/service/UserService.java#L28)
- DepartmentController.java: Lines: [19](https://github.com/shabbirdwd53/Springboot-Microservice/blob/master/department-service/src/main/java/com/dailycodebuffer/department/controller/DepartmentController.java#L19), [25](https://github.com/shabbirdwd53/Springboot-Microservice/blob/master/department-service/src/main/java/com/dailycodebuffer/department/controller/DepartmentController.java#L25)
- DepartmentService.java: Lines: [17](https://github.com/shabbirdwd53/Springboot-Microservice/blob/master/department-service/src/main/java/com/dailycodebuffer/department/service/DepartmentService.java#L17), [22](https://github.com/shabbirdwd53/Springboot-Microservice/blob/master/department-service/src/main/java/com/dailycodebuffer/department/service/DepartmentService.java#L22)

#### R11 {#rule11}

Rule is violated: Logs are not explicitly sanitized. All services write constant log messages without structured logging or template parameters. No PII or secrets will be leaked by the logging messages (see example artifact).

Artifacts:
- InvoiceService.java: Line: [25](https://github.com/shabbirdwd53/Springboot-Microservice/blob/master/microservice-kafka/microservice-kafka-invoicing/src/main/java/com/ewolff/microservice/invoicing/InvoiceService.java#L25)

#### R12 {#rule12}

Rule is violated: No logs are collected and no message broker is deployed.



#### R13 {#rule13}

Rule is adhered to: Hystrix is deployed as a circuit breaker on the gateway server.

Artifacts:
- application.yml: Lines: [30](https://github.com/shabbirdwd53/Springboot-Microservice/blob/master/cloud-gateway/src/main/resources/application.yml#L30), [15](https://github.com/shabbirdwd53/Springboot-Microservice/blob/master/cloud-gateway/src/main/resources/application.yml#L15), [24](https://github.com/shabbirdwd53/Springboot-Microservice/blob/master/cloud-gateway/src/main/resources/application.yml#L24)

#### R14 {#rule14}

Rule is violated: The gateway server uses load balancing to access dependent services.

Artifacts:
- application.yml: Lines: [11](https://github.com/shabbirdwd53/Springboot-Microservice/blob/master/cloud-gateway/src/main/resources/application.yml#L11), [20](https://github.com/shabbirdwd53/Springboot-Microservice/blob/master/cloud-gateway/src/main/resources/application.yml#L20)

#### R15 {#rule15}

This rule is not applicable: Not a service mesh deployment.



#### R16 {#rule16}

Rule is adhered to:
1. Registry Service (Eureka Server) with @EnableEurekaServer present.
1. Eureka is started on Port 8761 and can be deployed on a dedicated server.

Artifacts:
- ServiceRegistryApplication.java: Line: [8](https://github.com/shabbirdwd53/Springboot-Microservice/blob/master/service-registry/src/main/java/com/dailycodebuffer/service/registry/ServiceRegistryApplication.java#L8)
- application.yml: Line: [2](https://github.com/shabbirdwd53/Springboot-Microservice/blob/master/service-registry/src/main/resources/application.yml#L2)

#### R17 {#rule17}

Rule is violated: No HTTP basic password listed in any YML-Configuration of format username:password@here-location-of-eureka-server at "eureka.client.serviceUrl.defaultZone".

Artifacts:
- ServiceRegistryApplication.java: Line: [8](https://github.com/shabbirdwd53/Springboot-Microservice/blob/master/service-registry/src/main/java/com/dailycodebuffer/service/registry/ServiceRegistryApplication.java#L8)
- application.yml: Line: [1](https://github.com/shabbirdwd53/config-server/blob/main/application.yml#L1)



#### R18 {#rule18}

Rule is violated: No secret manager is deployed.
