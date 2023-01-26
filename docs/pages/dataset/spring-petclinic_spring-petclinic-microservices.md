---
title: spring-petclinic/spring-petclinic-microservices
keywords: model
tags: [docker, docker_compose, eureka, grafana, hystrix, maven, prometheus, ribbon, spring_admin, spring_config, spring_gateway, zipkin]
sidebar: datasetdoc_sidebar
permalink: spring-petclinic_spring-petclinic-microservices.html
toc: false
---

## General Information

The repository for this application ([open on GitHub](https://github.com/spring-petclinic/spring-petclinic-microservices)) has 1288 stars and was forked 1676 times. The codebase consists of 3990 lines of code and makes use of the following technologies:

<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_docker.html">Docker</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_docker_compose.html">Docker Compose</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_eureka.html">Eureka</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_grafana.html">Grafana</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_hystrix.html">Hystrix</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_maven.html">Maven</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_prometheus.html">Prometheus</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_ribbon.html">Ribbon</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_spring_admin.html">Spring Admin</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_spring_config.html">Spring Config</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_spring_gateway.html">Spring Gateway</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_zipkin.html">Zipkin</a>

## Data Flow Diagram

![Dataflow Diagram](./spring-petclinic_spring-petclinic-microservices.png)

Download the following model file [here](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/spring-petclinic_spring-petclinic-microservices/spring-petclinic_spring-petclinic-microservices.json).
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
                "Port": 8888
            }
        },
        {
            "name": "discovery_server",
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
            "name": "tracing_server",
            "stereotypes": [
                "tracing_server",
                "infrastructural"
            ],
            "tagged_values": {
                "Tracing Server": "Zipkin",
                "Port": 9411
            }
        },
        {
            "name": "admin_server",
            "stereotypes": [
                "administration_server",
                "infrastructural"
            ],
            "tagged_values": {
                "Administration Server": "Spring Boot Admin",
                "Port": 9090
            }
        },
        {
            "name": "prometheus_server",
            "stereotypes": [
                "metrics_server",
                "infrastructural"
            ],
            "tagged_values": {
                "Metrics Server": "Prometheus",
                "Port": 9090
            }
        },
        {
            "name": "grafana_server",
            "stereotypes": [
                "monitoring_dashboard",
                "infrastructural"
            ],
            "tagged_values": {
                "Monitoring Dashboard": "Grafana",
                "Port": 3000
            }
        },
        {
            "name": "customers_service",
            "stereotypes": [
                "in_memory_data_store",
                "local_logging",
                "internal"
            ],
            "tagged_values": {
                "Port": 8081,
                "In-Memory Data Store": "HSQLDB",
                "Logging Technology": "Lombok",
                "Endpoints": [
                    "/owners",
                    "/owners/{ownerId}"
                ]
            }
        },
        {
            "name": "vets_service",
            "stereotypes": [
                "in_memory_data_store",
                "internal"
            ],
            "tagged_values": {
                "Port": 8083,
                "In-Memory Data Store": "HSQLDB",
                "Endpoints": [
                    "/vets"
                ]
            }
        },
        {
            "name": "visits_service",
            "stereotypes": [
                "in_memory_data_store",
                "local_logging",
                "internal"
            ],
            "tagged_values": {
                "Port": 8082,
                "In-Memory Data Store": "HSQLDB",
                "Logging Technology": "Lombok"
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
                "Gateway": "Spring Cloud Gateway",
                "Port": 8080,
                "Load Balancer": "Spring Cloud",
                "Endpoints": [
                    "/api/gatewayowners/{ownerId}",
                    "/api/gateway"
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
                "URL": "https://github.com/spring-petclinic/spring-petclinic-microservices-config"
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
            "receiver": "discovery_server",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "tracing_server",
            "receiver": "discovery_server",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "config_server",
            "receiver": "tracing_server",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "admin_server",
            "receiver": "discovery_server",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "config_server",
            "receiver": "admin_server",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "prometheus_server",
            "receiver": "grafana_server",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "customers_service",
            "receiver": "discovery_server",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "config_server",
            "receiver": "customers_service",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "customers_service",
            "receiver": "tracing_server",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "customers_service",
            "receiver": "prometheus_server",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "vets_service",
            "receiver": "discovery_server",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "config_server",
            "receiver": "vets_service",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "vets_service",
            "receiver": "tracing_server",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "vets_service",
            "receiver": "prometheus_server",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "visits_service",
            "receiver": "discovery_server",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "config_server",
            "receiver": "visits_service",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "visits_service",
            "receiver": "tracing_server",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "visits_service",
            "receiver": "prometheus_server",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "discovery_server",
            "receiver": "api_gateway",
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
            "sender": "api_gateway",
            "receiver": "user",
            "stereotypes": [
                "restful_http",
                "load_balanced_link"
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
            "receiver": "prometheus_server",
            "stereotypes": [
                "restful_http",
                "load_balanced_link"
            ],
            "tagged_values": {}
        },
        {
            "sender": "api_gateway",
            "receiver": "vets_service",
            "stereotypes": [
                "restful_http",
                "load_balanced_link"
            ],
            "tagged_values": {}
        },
        {
            "sender": "api_gateway",
            "receiver": "visits_service",
            "stereotypes": [
                "restful_http",
                "load_balanced_link"
            ],
            "tagged_values": {}
        },
        {
            "sender": "api_gateway",
            "receiver": "customers_service",
            "stereotypes": [
                "restful_http",
                "load_balanced_link",
                "circuit_breaker_link"
            ],
            "tagged_values": {}
        },
        {
            "sender": "api_gateway",
            "receiver": "tracing_server",
            "stereotypes": [
                "restful_http",
                "load_balanced_link"
            ],
            "tagged_values": {}
        }
    ]
}
```

### Model Items

The Application consists of a total of 129 elements:

Element | Count
-- | --
Services | 10
External Entities | 2
Information Flows | 28
Annotations | 89
Total Items | 129

### Model Representations {#representations}

Open the model in the following formats:

- [JSON model](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/spring-petclinic_spring-petclinic-microservices/spring-petclinic_spring-petclinic-microservices.json)
- [PlantUML description](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/spring-petclinic_spring-petclinic-microservices/spring-petclinic_spring-petclinic-microservices.txt)
- [PNG graph](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/spring-petclinic_spring-petclinic-microservices/spring-petclinic_spring-petclinic-microservices.png)
- [CodeableModels](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/spring-petclinic_spring-petclinic-microservices/spring-petclinic_spring-petclinic-microservices.py)

### Traceability

Open the traceability information for all model items:

- [Traceability](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/spring-petclinic_spring-petclinic-microservices/spring-petclinic_spring-petclinic-microservices_traceability.json)

## Security Rules

The following table shows the application's adherence to the 17 architectural security rules. The last column provides model variants that adhere to the rule for each rule that is initially violated.

Rule ID &nbsp;&nbsp;| Verdict &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| Evidence &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| Model Variant &nbsp;&nbsp;&nbsp;|
-- | -- | -- | -- |
**R1** | <i class="fa fa-warning" style="color: #bfc600;"> | <a href="#rule01">Evidence |  |
**R2** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule02">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/spring-petclinic_spring-petclinic-microservices/model_variants/2.txt) |
**R3** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule03">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/spring-petclinic_spring-petclinic-microservices/model_variants/3.txt) |
**R4** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule04">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/spring-petclinic_spring-petclinic-microservices/model_variants/4.txt) |
**R5** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule05">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/spring-petclinic_spring-petclinic-microservices/model_variants/5.txt) |
**R6** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule06">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/spring-petclinic_spring-petclinic-microservices/model_variants/6.txt) |
**R7** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule07">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/spring-petclinic_spring-petclinic-microservices/model_variants/7.txt) |
**R8** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule08">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/spring-petclinic_spring-petclinic-microservices/model_variants/8.txt) |
**R9** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule09">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/spring-petclinic_spring-petclinic-microservices/model_variants/9.txt) |
**R10** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule10">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/spring-petclinic_spring-petclinic-microservices/model_variants/10.txt) |
**R11** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule11">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/spring-petclinic_spring-petclinic-microservices/model_variants/11.txt) |
**R12** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule12">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/spring-petclinic_spring-petclinic-microservices/model_variants/12.txt) |
**R13** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule13">Evidence |  |
**R14** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule14">Evidence |  |
**R16** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule16">Evidence |  |
**R17** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule17">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/spring-petclinic_spring-petclinic-microservices/model_variants/17.txt) |
**R18** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule18">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/spring-petclinic_spring-petclinic-microservices/model_variants/18.txt) |



### Evidence and explanations for rule decisions

#### R1 {#rule01}

This rule is unknown:
1. Spring Cloud Gateway Routes defined in the YML-Configuration
1. No authorization server present in this application, thus no authentication and authorization mechanism present,
1. Also no @EnableResourceServer annotation is present.

Artifacts:
- ApiGatewayApplication.java: [File](https://github.com/spring-petclinic/spring-petclinic-microservices/blob/master/spring-petclinic-api-gateway/src/main/java/org/springframework/samples/petclinic/api/ApiGatewayApplication.java)
- application.yml: [File](https://github.com/spring-petclinic/spring-petclinic-microservices/blob/master/spring-petclinic-api-gateway/src/main/resources/application.yml)

#### R2  {#rule02}

Rule is violated: No authorization/authentication mechanism is deployed.

#### R3 {#rule03}

Rule is violated: No authorization/authentication mechanism is deployed.

#### R4 {#rule04}

Rule is violated: No authorization/authentication mechanism is deployed.

#### R5 {#rule05}

Rule is violated: No validation of tokens as no tokens are issued.

#### R6 {#rule06}

Rule is violated: As there is no authorization/authentications mechanisms, there are no login attempts possible.



#### R7 {#rule07}

Rule is violated: No mention of SSL, TLS, key-store or trust store in the entire repository.

#### R8 {#rule08}

Rule is violated: See Rule 7 arguments.



#### R9 {#rule09}

Rule is violated: No central logging system is deployed.

#### R10 {#rule10}

Rule is violated: No central logging system is deployed.

#### R11 {#rule11}

Rule is violated: No central logging system is deployed.

#### R12 {#rule12}

Rule is violated: No message broker is deployed and no logs are collected.



#### R13 {#rule13}

Rule is adhered to:
1. Circuit breaker bean defined
1. Circuit breaker instantiated and started for specific route

Artifacts:
- ApiGatewayApplication.java: Line: [84](https://github.com/spring-petclinic/spring-petclinic-microservices/blob/master/spring-petclinic-api-gateway/src/main/java/org/springframework/samples/petclinic/api/ApiGatewayApplication.java#L84)
- ApiGatewayController.java: Lines: [54](https://github.com/spring-petclinic/spring-petclinic-microservices/blob/master/spring-petclinic-api-gateway/src/main/java/org/springframework/samples/petclinic/api/boundary/web/ApiGatewayController.java#L54), [55](https://github.com/spring-petclinic/spring-petclinic-microservices/blob/master/spring-petclinic-api-gateway/src/main/java/org/springframework/samples/petclinic/api/boundary/web/ApiGatewayController.java#L55)

#### R14 {#rule14}

Rule is adhered to: Route URI given with "lb://" for Spring Cloud LoadBalancer to resolve from discovery service to.

Artifacts:
- application.yml: Lines: [10](https://github.com/spring-petclinic/spring-petclinic-microservices/blob/master/spring-petclinic-api-gateway/src/main/resources/application.yml#L10), [16](https://github.com/spring-petclinic/spring-petclinic-microservices/blob/master/spring-petclinic-api-gateway/src/main/resources/application.yml#L16), [22](https://github.com/spring-petclinic/spring-petclinic-microservices/blob/master/spring-petclinic-api-gateway/src/main/resources/application.yml#L22)

#### R15 {#rule15}

This rule is not applicable: Not a service mesh deployment.



#### R16 {#rule16}

Rule is adhered to:
1. Registry Service (Eureka) present with @EnableEurekaServer annotation,
1. Started through Docker-Compose, should also be able to be deployed on dedicated server.

Artifacts:
- DiscoveryServerApplication.java: Line: [26](https://github.com/spring-petclinic/spring-petclinic-microservices/blob/master/spring-petclinic-discovery-server/src/main/java/org/springframework/samples/petclinic/discovery/DiscoveryServerApplication.java#L26)
- docker-compose.yml: Line: [11](https://github.com/spring-petclinic/spring-petclinic-microservices/blob/master/docker-compose.yml#L11)

#### R17 {#rule17}

Rule is violated: No HTTP basic password listed in any YML-Configuration of format username:password@here-location-of-eureka-server at "eureka.client.serviceUrl.defaultZone".

Artifacts:
- DiscoveryServerApplication.java: Line: [26](https://github.com/spring-petclinic/spring-petclinic-microservices/blob/master/spring-petclinic-discovery-server/src/main/java/org/springframework/samples/petclinic/discovery/DiscoveryServerApplication.java#L26)



#### R18 {#rule18}

Rule is violated: No secret manager is deployed.
