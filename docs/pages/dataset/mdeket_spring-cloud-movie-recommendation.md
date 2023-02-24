---
title: mdeket/spring-cloud-movie-recommendation
keywords: model
tags: [eureka, hystrix, maven, ribbon, spring_config, zipkin, zuul]
sidebar: datasetdoc_sidebar
permalink: mdeket_spring-cloud-movie-recommendation.html
toc: false
---

## General Information

The repository for this application ([open on GitHub](https://github.com/mdeket/spring-cloud-movie-recommendation)) has 13 stars and was forked 11 times. The codebase consists of 1800 lines of code and makes use of the following technologies:

<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_eureka.html">Eureka</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_hystrix.html">Hystrix</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_maven.html">Maven</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_ribbon.html">Ribbon</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_spring_config.html">Spring Config</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_zipkin.html">Zipkin</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_zuul.html">Zuul</a>

## Data Flow Diagram

![Dataflow Diagram](./mdeket_spring-cloud-movie-recommendation.png)

Download the following model file [here](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/mdeket_spring-cloud-movie-recommendation/mdeket_spring-cloud-movie-recommendation.json).
Other formats are provided below.

```json
{
    "services": [
        {
            "name": "config_service",
            "stereotypes": [
                "configuration_server",
                "infrastructural"
            ],
            "tagged_values": {
                "Port": 8888,
                "Configuration Server": "Spring Cloud Config"
            }
        },
        {
            "name": "eureka_service",
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
            "name": "movie_service",
            "stereotypes": [
                "internal"
            ],
            "tagged_values": {
                "Port": 8002,
                "Endpoints": [
                    "/movie/dummyData",
                    "/movie/list",
                    "/movie/{movieId}",
                    "/movie"
                ]
            }
        },
        {
            "name": "user_service",
            "stereotypes": [
                "internal"
            ],
            "tagged_values": {
                "Port": 8001,
                "Endpoints": [
                    "/user",
                    "/user/{userId}"
                ]
            }
        },
        {
            "name": "recommendation_service",
            "stereotypes": [
                "internal"
            ],
            "tagged_values": {
                "Port": 8003,
                "Endpoints": [
                    "/recommendation",
                    "/recommendation/recommend/user/{userId}",
                    "/recommendation/user",
                    "/recommendation/movie/{movieId}",
                    "/recommendation/user/{userId}",
                    "/recommendation/dummyData",
                    "/recommendation/movie"
                ]
            }
        },
        {
            "name": "recommendation_client",
            "stereotypes": [
                "gateway",
                "monitoring_dashboard",
                "local_logging",
                "infrastructural",
                "circuit_breaker",
                "load_balancer"
            ],
            "tagged_values": {
                "Port": 9000,
                "Gateway": "Zuul",
                "Monitoring Dashboard": "Hystrix",
                "Circuit Breaker": "Hystrix",
                "Load Balancer": "Ribbon",
                "Endpoints": [
                    "/user/{userId}",
                    "/api/userDetails/{userId}",
                    "/user",
                    "/api",
                    "/recommendation/dummyData",
                    "/movie/dummyData",
                    "/newuser",
                    "/api/recommendation/user/{userId}",
                    "/movie"
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
                "URL": "https://github.com/mdeket/spring-cloud-example-config-repo.git"
            }
        },
        {
            "name": "database_movie_service",
            "stereotypes": [
                "entrypoint",
                "exitpoint",
                "external_database"
            ],
            "tagged_values": {}
        },
        {
            "name": "database_user_service",
            "stereotypes": [
                "entrypoint",
                "exitpoint",
                "external_database",
                "plaintext_credentials"
            ],
            "tagged_values": {
                "Port": 3306,
                "Database": "MySQL",
                "Username": "root",
                "Password": "root"
            }
        },
        {
            "name": "database_recommendation_service",
            "stereotypes": [
                "exitpoint",
                "entrypoint",
                "external_database",
                "plaintext_credentials"
            ],
            "tagged_values": {
                "Database": "Neo4j",
                "Port": 7474,
                "Username": "neo4j",
                "Password": "root"
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
            "receiver": "config_service",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "config_service",
            "receiver": "eureka_service",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "movie_service",
            "receiver": "eureka_service",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "config_service",
            "receiver": "movie_service",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "database_movie_service",
            "receiver": "movie_service",
            "stereotypes": [
                "jdbc"
            ],
            "tagged_values": {}
        },
        {
            "sender": "user_service",
            "receiver": "eureka_service",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "config_service",
            "receiver": "user_service",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "database_user_service",
            "receiver": "user_service",
            "stereotypes": [
                "jdbc",
                "plaintext_credentials_link"
            ],
            "tagged_values": {
                "'Username'": "\"root\"",
                " 'Password'": "\"root\""
            }
        },
        {
            "sender": "recommendation_service",
            "receiver": "eureka_service",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "config_service",
            "receiver": "recommendation_service",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "database_recommendation_service",
            "receiver": "recommendation_service",
            "stereotypes": [
                "jdbc",
                "plaintext_credentials_link"
            ],
            "tagged_values": {
                "'Username'": "\"neo4j\"",
                " 'Password'": "\"root\""
            }
        },
        {
            "sender": "eureka_service",
            "receiver": "recommendation_client",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "user",
            "receiver": "recommendation_client",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "recommendation_client",
            "receiver": "user",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "config_service",
            "receiver": "recommendation_client",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "recommendation_client",
            "receiver": "recommendation_service",
            "stereotypes": [
                "restful_http",
                "circuit_breaker_link",
                "load_balanced_link",
                "feign_connection"
            ],
            "tagged_values": {
                "'Circuit Breaker'": "\"Hystrix\"",
                " 'Load Balancer'": "\"Ribbon\""
            }
        },
        {
            "sender": "recommendation_client",
            "receiver": "movie_service",
            "stereotypes": [
                "restful_http",
                "circuit_breaker_link",
                "load_balanced_link",
                "feign_connection"
            ],
            "tagged_values": {
                "'Circuit Breaker'": "\"Hystrix\"",
                " 'Load Balancer'": "\"Ribbon\""
            }
        },
        {
            "sender": "recommendation_client",
            "receiver": "user_service",
            "stereotypes": [
                "restful_http",
                "load_balanced_link",
                "circuit_breaker_link",
                "feign_connection"
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

The Application consists of a total of 122 elements:

Element | Count
-- | --
Services | 6
External Entities | 5
Information Flows | 18
Annotations | 93
Total Items | 122

### Model Representations {#representations}

Open the model in the following formats:

- [JSON model](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/mdeket_spring-cloud-movie-recommendation/mdeket_spring-cloud-movie-recommendation.json)
- [PlantUML description](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/mdeket_spring-cloud-movie-recommendation/mdeket_spring-cloud-movie-recommendation.txt)
- [PNG graph](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/mdeket_spring-cloud-movie-recommendation/mdeket_spring-cloud-movie-recommendation.png)
- [CodeableModels](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/mdeket_spring-cloud-movie-recommendation/mdeket_spring-cloud-movie-recommendation.py)

### Traceability

Open the traceability information for all model items:

- [Traceability](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/mdeket_spring-cloud-movie-recommendation/mdeket_spring-cloud-movie-recommendation_traceability.json)

## Security Rules

The following table shows the application's adherence to the 17 architectural security rules. The last column provides model variants that adhere to the rule for each rule that is initially violated.

Rule ID &nbsp;&nbsp;| Verdict &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| Evidence &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| Model Variant &nbsp;&nbsp;&nbsp;|
-- | -- | -- | -- |
**R1** | <i class="fa fa-warning" style="color: #bfc600;"> | <a href="#rule01">Evidence |  |
**R2** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule02">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/mdeket_spring-cloud-movie-recommendation/model_variants/2.txt) |
**R3** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule03">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/mdeket_spring-cloud-movie-recommendation/model_variants/3.txt) |
**R4** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule04">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/mdeket_spring-cloud-movie-recommendation/model_variants/4.txt) |
**R5** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule05">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/mdeket_spring-cloud-movie-recommendation/model_variants/5.txt) |
**R6** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule06">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/mdeket_spring-cloud-movie-recommendation/model_variants/6.txt) |
**R7** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule07">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/mdeket_spring-cloud-movie-recommendation/model_variants/7.txt) |
**R8** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule08">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/mdeket_spring-cloud-movie-recommendation/model_variants/8.txt) |
**R9** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule09">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/mdeket_spring-cloud-movie-recommendation/model_variants/9.txt) |
**R10** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule10">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/mdeket_spring-cloud-movie-recommendation/model_variants/10.txt) |
**R11** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule11">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/mdeket_spring-cloud-movie-recommendation/model_variants/11.txt) |
**R12** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule12">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/mdeket_spring-cloud-movie-recommendation/model_variants/12.txt) |
**R13** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule13">Evidence |  |
**R14** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule14">Evidence |  |
**R16** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule16">Evidence |  |
**R17** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule17">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/mdeket_spring-cloud-movie-recommendation/model_variants/17.txt) |
**R18** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule18">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/mdeket_spring-cloud-movie-recommendation/model_variants/18.txt) |



### Evidence and explanations for rule decisions

#### R1 {#rule01}

Rule is adhered to: User only communicates with the Zuul gateway server. The API gateway used does not perform any authentication/authorization for requests.

Artifacts:
- RecommendationClientApplication.java: Line: [12](https://github.com/mdeket/spring-cloud-movie-recommendation/blob/master/recommendation-client/src/main/java/com/example/RecommendationClientApplication.java#L12)

#### R2  {#rule02}

Rule is violated: Services communicate internally over plain HTTP (See example artifacts). The communication is not authenticated.

Artifacts:
- RecommendationClientService.java: Lines: [42](https://github.com/mdeket/spring-cloud-movie-recommendation/blob/master/recommendation-client/src/main/java/com/example/service/RecommendationClientService.java#L42), [54](https://github.com/mdeket/spring-cloud-movie-recommendation/blob/master/recommendation-client/src/main/java/com/example/service/RecommendationClientService.java#L54), [87](https://github.com/mdeket/spring-cloud-movie-recommendation/blob/master/recommendation-client/src/main/java/com/example/service/RecommendationClientService.java#L87)
- MyConfiguration.java: Line: [33](https://github.com/mdeket/spring-cloud-movie-recommendation/blob/master/recommendation-service/src/main/java/com/example/MyConfiguration.java#L33)

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

#### R8 {#rule08}

Rule is violated: All internal services communicate over insecure HTTP connections.



#### R9 {#rule09}

Rule is violated: No central logging system is deployed.

#### R10 {#rule10}

Rule is violated: No central logging system is deployed. Two internal services perform local logging, however none of the logs are consumed and accessed through monitoring software.

Artifacts:
- MainController.java: Line: [51](https://github.com/mdeket/spring-cloud-movie-recommendation/blob/master/recommendation-client/src/main/java/com/example/MainController.java#L51)
- RecommendationClientService.java: Lines: [38](https://github.com/mdeket/spring-cloud-movie-recommendation/blob/master/recommendation-client/src/main/java/com/example/service/RecommendationClientService.java#L38), [43](https://github.com/mdeket/spring-cloud-movie-recommendation/blob/master/recommendation-client/src/main/java/com/example/service/RecommendationClientService.java#L43), [50](https://github.com/mdeket/spring-cloud-movie-recommendation/blob/master/recommendation-client/src/main/java/com/example/service/RecommendationClientService.java#L50), [56](https://github.com/mdeket/spring-cloud-movie-recommendation/blob/master/recommendation-client/src/main/java/com/example/service/RecommendationClientService.java#L56), [80](https://github.com/mdeket/spring-cloud-movie-recommendation/blob/master/recommendation-client/src/main/java/com/example/service/RecommendationClientService.java#L80), [88](https://github.com/mdeket/spring-cloud-movie-recommendation/blob/master/recommendation-client/src/main/java/com/example/service/RecommendationClientService.java#L88)

#### R11 {#rule11}

Rule is violated: Logs are not sanitized and could possibly contain sensitive information when exceptions in the recommendation service are logged.

Artifacts:
- MainController.java: Line: [51](https://github.com/mdeket/spring-cloud-movie-recommendation/blob/master/recommendation-client/src/main/java/com/example/MainController.java#L51)

#### R12 {#rule12}

Rule is violated: No logs are collected and no message broker is deployed.



#### R13 {#rule13}

Rule is adhered to: [Hystrix](https://cloud.spring.io/spring-cloud-netflix/multi/multi__router_and_filter_zuul.html#netflix-zuul-reverse-proxy) is deployed as a circuit breaker on the gateway server.

Artifacts:
- RecommendationClientApplication.java: Line: [12](https://github.com/mdeket/spring-cloud-movie-recommendation/blob/master/recommendation-client/src/main/java/com/example/RecommendationClientApplication.java#L12)
- RecommendationClientApplication.java: Line: [15](https://github.com/mdeket/spring-cloud-movie-recommendation/blob/master/recommendation-client/src/main/java/com/example/RecommendationClientApplication.java#L15)

#### R14 {#rule14}

Rule is adhered to: The gateway server uses load balancing via [Ribbon](https://cloud.spring.io/spring-cloud-netflix/multi/multi__router_and_filter_zuul.html#netflix-zuul-reverse-proxy) to access dependent services.

Artifacts:
- RecommendationClientApplication.java: Line: [12](https://github.com/mdeket/spring-cloud-movie-recommendation/blob/master/recommendation-client/src/main/java/com/example/RecommendationClientApplication.java#L12)

#### R15 {#rule15}

This rule is not applicable: Not a service mesh deployment.



#### R16 {#rule16}

Rule is adhered to:
1. Registry Service (Eureka Server) with @EnableEurekaServer present.
1. Project is missing infrastructure description, not certain if and how the discovery server is deployed.
1. Services are not explicitly registered with Eureka and wont be secured by default.

Artifacts:
- EurekaServiceApplication.java: Line: [7](https://github.com/mdeket/spring-cloud-movie-recommendation/blob/master/eureka-service/src/main/java/com/example/EurekaServiceApplication.java#L7)
- eureka-service-default.yml: [File](https://github.com/mdeket/spring-cloud-example-config-repo/blob/master/eureka-service-default.yml)

#### R17 {#rule17}

Rule is violated: No [HTTP basic password](https://cloud.spring.io/spring-cloud-netflix/reference/html/#authenticating-with-the-eureka-server)  listed in any YML-Configuration of format username:password@here-location-of-eureka-server at "eureka.client.serviceUrl.defaultZone".

Artifacts:
- EurekaServiceApplication.java: Line: [7](https://github.com/mdeket/spring-cloud-movie-recommendation/blob/master/eureka-service/src/main/java/com/example/EurekaServiceApplication.java#L7)
- movie-service-default.yml: [File](https://github.com/mdeket/spring-cloud-example-config-repo/blob/master/movie-service-default.yml)



#### R18 {#rule18}

Rule is violated: No secret manager is deployed. The deployed git configuration server is not a secrets manager.

Artifacts:
- application.properties: Line: [3](https://github.com/mdeket/spring-cloud-movie-recommendation/blob/master/config-service/src/main/resources/application.properties#L3)
