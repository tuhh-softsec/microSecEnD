---
title: jferrater/Tap-And-Eat-MicroServices
keywords: model
tags: [docker, docker_compose, eureka, hystrix, maven, spring_config]
sidebar: datasetdoc_sidebar
permalink: jferrater_tap-and-eat-microservices.html
toc: false
---

## General Information

The repository for this application ([open on GitHub](https://github.com/jferrater/Tap-And-Eat-MicroServices)) has 6 stars and was forked 4 times. The codebase consists of 1484 lines of code and makes use of the following technologies:

<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_docker.html">Docker</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_docker_compose.html">Docker Compose</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_eureka.html">Eureka</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_hystrix.html">Hystrix</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_maven.html">Maven</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_spring_config.html">Spring Config</a>

## Data Flow Diagram

![Dataflow Diagram](./jferrater_tap-and-eat-microservices.png)

Download the following model file [here](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/jferrater_tap-and-eat-microservices/jferrater_tap-and-eat-microservices.json).
Other formats are provided below.

```json
{
    "services": [
        {
            "name": "discovery_service",
            "stereotypes": [
                "service_discovery",
                "infrastructural"
            ],
            "tagged_values": {
                "Service Discovery": "Eureka",
                "Port": 8888
            }
        },
        {
            "name": "config_service",
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
            "name": "account_service",
            "stereotypes": [
                "internal"
            ],
            "tagged_values": {
                "Port": 8000,
                "Endpoints": [
                    "/accounts"
                ]
            }
        },
        {
            "name": "customer_service",
            "stereotypes": [
                "internal"
            ],
            "tagged_values": {
                "Port": 8002,
                "Endpoints": [
                    "/customers"
                ]
            }
        },
        {
            "name": "store_service",
            "stereotypes": [
                "internal"
            ],
            "tagged_values": {
                "Port": 8003,
                "Endpoints": [
                    "/stores"
                ]
            }
        },
        {
            "name": "item_service",
            "stereotypes": [
                "internal"
            ],
            "tagged_values": {
                "Port": 8004,
                "Endpoints": [
                    "/items"
                ]
            }
        },
        {
            "name": "price_service",
            "stereotypes": [
                "internal"
            ],
            "tagged_values": {
                "Port": 8001,
                "Endpoints": [
                    "/prices"
                ]
            }
        },
        {
            "name": "foodtray_service",
            "stereotypes": [
                "infrastructural",
                "monitoring_dashboard",
                "circuit_breaker"
            ],
            "tagged_values": {
                "Monitoring Dashboard": "Hystrix",
                "Circuit Breaker": "Hystrix",
                "Port": 8005,
                "Endpoints": [
                    "/foodtrays",
                    "/foodtrays/{itemCode}",
                    "/foodtrays/price/{itemCode}",
                    "/foodtrays/item/{itemCode}"
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
                "URL": "https://github.com/jferrater/ConfigData"
            }
        }
    ],
    "information_flows": [
        {
            "sender": "github_repository",
            "receiver": "config_service",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "config_service",
            "receiver": "discovery_service",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "config_service",
            "receiver": "account_service",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "account_service",
            "receiver": "discovery_service",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "config_service",
            "receiver": "customer_service",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "customer_service",
            "receiver": "discovery_service",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "config_service",
            "receiver": "store_service",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "store_service",
            "receiver": "discovery_service",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "config_service",
            "receiver": "item_service",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "item_service",
            "receiver": "discovery_service",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "config_service",
            "receiver": "price_service",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "price_service",
            "receiver": "discovery_service",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "config_service",
            "receiver": "foodtray_service",
            "stereotypes": [
                "restful_http",
                "circuit_breaker_link"
            ],
            "tagged_values": {
                "'Circuit Breaker'": "\"Hystrix\""
            }
        },
        {
            "sender": "foodtray_service",
            "receiver": "discovery_service",
            "stereotypes": [
                "restful_http",
                "circuit_breaker_link"
            ],
            "tagged_values": {
                "'Circuit Breaker'": "\"Hystrix\""
            }
        },
        {
            "sender": "foodtray_service",
            "receiver": "item_service",
            "stereotypes": [
                "restful_http",
                "feign_connection",
                "load_balanced_link",
                "circuit_breaker_link"
            ],
            "tagged_values": {
                "'Load Balancer'": "\"Ribbon\"",
                " 'Circuit Breaker'": "\"Hystrix\""
            }
        },
        {
            "sender": "foodtray_service",
            "receiver": "price_service",
            "stereotypes": [
                "restful_http",
                "feign_connection",
                "load_balanced_link",
                "circuit_breaker_link"
            ],
            "tagged_values": {
                "'Load Balancer'": "\"Ribbon\"",
                " 'Circuit Breaker'": "\"Hystrix\""
            }
        }
    ]
}
```

### Model Items

The Application consists of a total of 88 elements:

Element | Count
-- | --
Services | 8
External Entities | 1
Information Flows | 16
Annotations | 63
Total Items | 88

### Model Representations {#representations}

Open the model in the following formats:

- [JSON model](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/jferrater_tap-and-eat-microservices/jferrater_tap-and-eat-microservices.json)
- [PlantUML description](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/jferrater_tap-and-eat-microservices/jferrater_tap-and-eat-microservices.txt)
- [PNG graph](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/jferrater_tap-and-eat-microservices/jferrater_tap-and-eat-microservices.png)
- [CodeableModels](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/jferrater_tap-and-eat-microservices/jferrater_tap-and-eat-microservices.py)

### Traceability

Open the traceability information for all model items:

- [Traceability](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/jferrater_tap-and-eat-microservices/jferrater_tap-and-eat-microservices_traceability.json)

## Security Rules

The following table shows the application's adherence to the 17 architectural security rules. The last column provides model variants that adhere to the rule for each rule that is initially violated.

Rule ID &nbsp;&nbsp;| Verdict &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| Evidence &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| Model Variant &nbsp;&nbsp;&nbsp;|
-- | -- | -- | -- |
**R1** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule01">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/jferrater_tap-and-eat-microservices/model_variants/1.txt) |
**R2** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule02">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/jferrater_tap-and-eat-microservices/model_variants/2.txt) |
**R3** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule03">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/jferrater_tap-and-eat-microservices/model_variants/3.txt) |
**R4** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule04">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/jferrater_tap-and-eat-microservices/model_variants/4.txt) |
**R5** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule05">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/jferrater_tap-and-eat-microservices/model_variants/5.txt) |
**R6** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule06">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/jferrater_tap-and-eat-microservices/model_variants/6.txt) |
**R7** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule07">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/jferrater_tap-and-eat-microservices/model_variants/7.txt) |
**R8** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule08">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/jferrater_tap-and-eat-microservices/model_variants/8.txt) |
**R9** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule09">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/jferrater_tap-and-eat-microservices/model_variants/9.txt) |
**R10** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule10">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/jferrater_tap-and-eat-microservices/model_variants/10.txt) |
**R11** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule11">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/jferrater_tap-and-eat-microservices/model_variants/11.txt) |
**R12** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule12">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/jferrater_tap-and-eat-microservices/model_variants/12.txt) |
**R13** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule13">Evidence |  |
**R14** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule14">Evidence |  |
**R16** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule16">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/jferrater_tap-and-eat-microservices/model_variants/16.txt) |
**R17** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule17">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/jferrater_tap-and-eat-microservices/model_variants/17.txt) |
**R18** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule18">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/jferrater_tap-and-eat-microservices/model_variants/18.txt) |



### Evidence and explanations for rule decisions

#### R1 {#rule01}

Rule is violated: The user communicates with the foodtray service, however the internal services do not restrict access from external entities.

Artifacts:
- FoodTrayServiceApplication.java: Line: [21](https://github.com/jferrater/Tap-And-Eat-MicroServices/blob/master/FoodTrayService/src/main/java/com/github/joffryferrater/foodtrayservice/FoodTrayServiceApplication.java#L21)
- bootstrap.yml: Line: [11](https://github.com/jferrater/Tap-And-Eat-MicroServices/blob/master/ItemService/src/main/resources/bootstrap.yml#L11)
- bootstrap.yml: Line: [8](https://github.com/jferrater/Tap-And-Eat-MicroServices/blob/master/PriceService/src/main/resources/bootstrap.yml#L8)

#### R2  {#rule02}

Rule is violated: Services communicate internally over plain HTTP using Feign connections (See example artifacts). The connection is thus not authenticated.

Artifacts:
- FoodTrayServiceApplication.java: Line: [21](https://github.com/jferrater/Tap-And-Eat-MicroServices/blob/master/FoodTrayService/src/main/java/com/github/joffryferrater/foodtrayservice/FoodTrayServiceApplication.java#L21)
- bootstrap.yml: Line: [11](https://github.com/jferrater/Tap-And-Eat-MicroServices/blob/master/ItemService/src/main/resources/bootstrap.yml#L11)
- bootstrap.yml: Line: [8](https://github.com/jferrater/Tap-And-Eat-MicroServices/blob/master/PriceService/src/main/resources/bootstrap.yml#L8)

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
- bootstrap.yml: Line: [19](https://github.com/jferrater/Tap-And-Eat-MicroServices/blob/master/FoodTrayService/src/main/resources/bootstrap.yml#L19)

#### R8 {#rule08}

Rule is violated: All internal services communicate over insecure HTTP connections.

Artifacts:
- FoodTrayServiceApplication.java: Line: [21](https://github.com/jferrater/Tap-And-Eat-MicroServices/blob/master/FoodTrayService/src/main/java/com/github/joffryferrater/foodtrayservice/FoodTrayServiceApplication.java#L21)
- bootstrap.yml: Line: [11](https://github.com/jferrater/Tap-And-Eat-MicroServices/blob/master/ItemService/src/main/resources/bootstrap.yml#L11)
- bootstrap.yml: Line: [8](https://github.com/jferrater/Tap-And-Eat-MicroServices/blob/master/PriceService/src/main/resources/bootstrap.yml#L8)



#### R9 {#rule09}

Rule is violated: No central logging system is deployed.

#### R10 {#rule10}

Rule is violated: No central logging system is deployed.

#### R11 {#rule11}

Rule is violated: No logs are generated by the application.

#### R12 {#rule12}

Rule is violated: No message broker is deployed and no logging is performed.



#### R13 {#rule13}

Rule is adhered to: Hystrix is deployed as a [circuit breaker](https://cloud.spring.io/spring-cloud-static/Greenwich.RC1/multi/multi_spring-cloud-consul-hystrix.html) on the gateway server.

Artifacts:
- FoodTrayServiceApplication.java: Line: [19](https://github.com/jferrater/Tap-And-Eat-MicroServices/blob/master/FoodTrayService/src/main/java/com/github/joffryferrater/foodtrayservice/FoodTrayServiceApplication.java#L19)

#### R14 {#rule14}

Rule is adhered to: The gateway server uses load balancing via [Ribbon](https://cloud.spring.io/spring-cloud-netflix/multi/multi_spring-cloud-feign.html#netflix-feign-starter) to access dependent services.

Artifacts:
- bootstrap.yml: Line: [11](https://github.com/jferrater/Tap-And-Eat-MicroServices/blob/master/ItemService/src/main/resources/bootstrap.yml#L11)
- bootstrap.yml: Line: [8](https://github.com/jferrater/Tap-And-Eat-MicroServices/blob/master/PriceService/src/main/resources/bootstrap.yml#L8)

#### R15 {#rule15}

This rule is not applicable: Not a service mesh deployment.



#### R16 {#rule16}

Rule is violated:
1. Registry Service (Eureka Server) with [@EnableEurekaServer](https://docs.spring.io/spring-cloud-netflix/docs/4.0.1-SNAPSHOT/reference/html/#spring-cloud-eureka-server) present.
1. The discovery service is missing from the docker compose file.

Artifacts:
- DiscoveryServiceApplication.java: Line: [13](https://github.com/jferrater/Tap-And-Eat-MicroServices/blob/master/DiscoveryService/src/main/java/com/github/joffry/ferrater/discoveryservice/DiscoveryServiceApplication.java#L13)
- docker-compose.yml: [File](https://github.com/jferrater/Tap-And-Eat-MicroServices/blob/master/Docker/docker-compose.yml)

#### R17 {#rule17}

Rule is violated: No [HTTP basic password](https://cloud.spring.io/spring-cloud-netflix/reference/html/#authenticating-with-the-eureka-server) listed in any YML-Configuration of format username:password@here-location-of-eureka-server at "eureka.client.serviceUrl.defaultZone".

Artifacts:
- DiscoveryServiceApplication.java: Line: [13](https://github.com/jferrater/Tap-And-Eat-MicroServices/blob/master/DiscoveryService/src/main/java/com/github/joffry/ferrater/discoveryservice/DiscoveryServiceApplication.java#L13)
- application.yml: Line: [5](https://github.com/jferrater/Tap-And-Eat-MicroServices/blob/master/ConfigService/src/main/resources/application.yml#L5)



#### R18 {#rule18}

Rule is violated: No secret manager is deployed. The deployed git configuration server is not a secrets manager.

Artifacts:
- application.yml: Line: [12](https://github.com/jferrater/Tap-And-Eat-MicroServices/blob/master/ConfigService/src/main/resources/application.yml#L12)
