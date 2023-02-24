---
title: sqshq/piggymetrics
keywords: model
tags: [docker, eureka, hystrix, maven, rabbitmq, ribbon, spring_config, spring_oauth, turbine, zuul]
sidebar: datasetdoc_sidebar
permalink: sqshq_piggymetrics.html
toc: false
---

## General Information

The repository for this application ([open on GitHub](https://github.com/sqshq/piggymetrics)) has 12108 stars and was forked 5791 times. The codebase consists of 9977 lines of code and makes use of the following technologies:

<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_docker.html">Docker</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_eureka.html">Eureka</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_hystrix.html">Hystrix</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_maven.html">Maven</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_rabbitmq.html">RabbitMQ</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_ribbon.html">Ribbon</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_spring_config.html">Spring Config</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_spring_oauth.html">Spring OAuth</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_turbine.html">Turbine</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_zuul.html">Zuul</a>

## Data Flow Diagram

![Dataflow Diagram](./sqshq_piggymetrics.png)

Download the following model file [here](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/sqshq_piggymetrics/sqshq_piggymetrics.json).
Other formats are provided below.

```json
{
    "services": [
        {
            "name": "config",
            "stereotypes": [
                "configuration_server",
                "plaintext_credentials",
                "infrastructural",
                "csrf_disabled",
                "basic_authentication"
            ],
            "tagged_values": {
                "Port": 8888,
                "Configuration Server": "Spring Cloud Config",
                "Username": "user",
                "Password": "password"
            }
        },
        {
            "name": "registry",
            "stereotypes": [
                "service_discovery",
                "plaintext_credentials",
                "infrastructural"
            ],
            "tagged_values": {
                "Service Discovery": "Eureka",
                "Port": 8761
            }
        },
        {
            "name": "monitoring",
            "stereotypes": [
                "monitoring_dashboard",
                "infrastructural"
            ],
            "tagged_values": {
                "Monitoring Dashboard": "Hystrix",
                "Port": 8080
            }
        },
        {
            "name": "turbine_stream_service",
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
            "name": "rabbitmq",
            "stereotypes": [
                "message_broker",
                "infrastructural"
            ],
            "tagged_values": {
                "Message Broker": "RabbitMQ",
                "Port": 15672
            }
        },
        {
            "name": "auth_service",
            "stereotypes": [
                "authorization_server",
                "pre_authorized_endpoints",
                "infrastructural",
                "token_server",
                "encryption",
                "local_logging",
                "resource_server",
                "csrf_disabled",
                "authentication_scope_all_requests"
            ],
            "tagged_values": {
                "Authorization Server": "Spring OAuth2",
                "Port": 5000,
                "Pre-authorized Endpoints": [
                    "/users"
                ],
                "Endpoints": [
                    "/users",
                    "/users/current"
                ]
            }
        },
        {
            "name": "account_service",
            "stereotypes": [
                "internal",
                "pre_authorized_endpoints",
                "local_logging",
                "resource_server",
                "circuit_breaker"
            ],
            "tagged_values": {
                "Port": 6000,
                "Pre-authorized Endpoints": [
                    "/{name}"
                ],
                "Circuit Breaker": "Hystrix",
                "Endpoints": [
                    "/{name}",
                    "/",
                    "/uaa/users",
                    "/statistics/{accountName}",
                    "/current"
                ]
            }
        },
        {
            "name": "notification_service",
            "stereotypes": [
                "internal",
                "local_logging",
                "resource_server"
            ],
            "tagged_values": {
                "Port": 8000,
                "Endpoints": [
                    "/accounts/{accountName}",
                    "/recipients/current",
                    "/recipients"
                ]
            }
        },
        {
            "name": "statistics_service",
            "stereotypes": [
                "internal",
                "local_logging",
                "pre_authorized_endpoints",
                "resource_server"
            ],
            "tagged_values": {
                "Port": 7000,
                "Pre-authorized Endpoints": [
                    "/{accountName}"
                ],
                "Endpoints": [
                    "/latest",
                    "/current",
                    "/{accountName}"
                ]
            }
        },
        {
            "name": "auth_mongodb",
            "stereotypes": [
                "database",
                "plaintext_credentials"
            ],
            "tagged_values": {
                "Database": "MongoDB",
                "Username": "user",
                "Password": "password"
            }
        },
        {
            "name": "account_mongodb",
            "stereotypes": [
                "database",
                "plaintext_credentials"
            ],
            "tagged_values": {
                "Database": "MongoDB",
                "Username": "user",
                "Password": "password"
            }
        },
        {
            "name": "statistics_mongodb",
            "stereotypes": [
                "database",
                "plaintext_credentials"
            ],
            "tagged_values": {
                "Database": "MongoDB",
                "Username": "user",
                "Password": "password"
            }
        },
        {
            "name": "notification_mongodb",
            "stereotypes": [
                "database",
                "plaintext_credentials"
            ],
            "tagged_values": {
                "Database": "MongoDB",
                "Username": "user",
                "Password": "password"
            }
        },
        {
            "name": "gateway",
            "stereotypes": [
                "gateway",
                "infrastructural",
                "load_balancer"
            ],
            "tagged_values": {
                "Gateway": "Zuul",
                "Port": 4000,
                "Load Balancer": "Ribbon"
            }
        }
    ],
    "information_flows": [
        {
            "sender": "config",
            "receiver": "registry",
            "stereotypes": [
                "restful_http",
                "plaintext_credentials_link"
            ],
            "tagged_values": {}
        },
        {
            "sender": "config",
            "receiver": "monitoring",
            "stereotypes": [
                "restful_http",
                "plaintext_credentials_link"
            ],
            "tagged_values": {}
        },
        {
            "sender": "turbine_stream_service",
            "receiver": "registry",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "config",
            "receiver": "turbine_stream_service",
            "stereotypes": [
                "restful_http",
                "plaintext_credentials_link"
            ],
            "tagged_values": {}
        },
        {
            "sender": "turbine_stream_service",
            "receiver": "monitoring",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "rabbitmq",
            "receiver": "turbine_stream_service",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "auth_service",
            "receiver": "registry",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "config",
            "receiver": "auth_service",
            "stereotypes": [
                "plaintext_credentials_link",
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "account_service",
            "receiver": "registry",
            "stereotypes": [
                "restful_http",
                "circuit_breaker_link"
            ],
            "tagged_values": {
                "'Circuit Breaker'": "\"Hystrix\""
            }
        },
        {
            "sender": "auth_service",
            "receiver": "account_service",
            "stereotypes": [
                "restful_http",
                "plaintext_credentials_link",
                "auth_provider",
                "authentication_with_plaintext_credentials"
            ],
            "tagged_values": {}
        },
        {
            "sender": "account_service",
            "receiver": "auth_service",
            "stereotypes": [
                "restful_http",
                "feign_connection",
                "load_balanced_link"
            ],
            "tagged_values": {
                "'Load Balancer'": "\"Ribbon\""
            }
        },
        {
            "sender": "config",
            "receiver": "account_service",
            "stereotypes": [
                "plaintext_credentials_link",
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "account_service",
            "receiver": "rabbitmq",
            "stereotypes": [
                "restful_http",
                "circuit_breaker_link"
            ],
            "tagged_values": {}
        },
        {
            "sender": "notification_service",
            "receiver": "registry",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "auth_service",
            "receiver": "notification_service",
            "stereotypes": [
                "restful_http",
                "plaintext_credentials_link",
                "auth_provider",
                "authentication_with_plaintext_credentials"
            ],
            "tagged_values": {}
        },
        {
            "sender": "config",
            "receiver": "notification_service",
            "stereotypes": [
                "plaintext_credentials_link",
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "notification_service",
            "receiver": "rabbitmq",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "notification_service",
            "receiver": "mail_server",
            "stereotypes": [
                "plaintext_credentials_link",
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "statistics_service",
            "receiver": "registry",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "auth_service",
            "receiver": "statistics_service",
            "stereotypes": [
                "restful_http",
                "plaintext_credentials_link",
                "auth_provider",
                "authentication_with_plaintext_credentials"
            ],
            "tagged_values": {}
        },
        {
            "sender": "config",
            "receiver": "statistics_service",
            "stereotypes": [
                "plaintext_credentials_link",
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "statistics_service",
            "receiver": "rabbitmq",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "external_website",
            "receiver": "statistics_service",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "account_service",
            "receiver": "statistics_service",
            "stereotypes": [
                "restful_http",
                "feign_connection",
                "circuit_breaker_link",
                "load_balanced_link"
            ],
            "tagged_values": {
                "'Circuit Breaker'": "\"Hystrix\"",
                " 'Load Balancer'": "\"Ribbon\""
            }
        },
        {
            "sender": "notification_service",
            "receiver": "account_service",
            "stereotypes": [
                "restful_http",
                "feign_connection",
                "load_balanced_link"
            ],
            "tagged_values": {
                "'Load Balancer'": "\"Ribbon\""
            }
        },
        {
            "sender": "account_mongodb",
            "receiver": "account_service",
            "stereotypes": [
                "jdbc",
                "plaintext_credentials_link"
            ],
            "tagged_values": {}
        },
        {
            "sender": "notification_mongodb",
            "receiver": "notification_service",
            "stereotypes": [
                "jdbc",
                "plaintext_credentials_link"
            ],
            "tagged_values": {}
        },
        {
            "sender": "statistics_mongodb",
            "receiver": "statistics_service",
            "stereotypes": [
                "jdbc",
                "plaintext_credentials_link"
            ],
            "tagged_values": {}
        },
        {
            "sender": "auth_mongodb",
            "receiver": "auth_service",
            "stereotypes": [
                "jdbc",
                "plaintext_credentials_link"
            ],
            "tagged_values": {}
        },
        {
            "sender": "registry",
            "receiver": "gateway",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "user",
            "receiver": "gateway",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "gateway",
            "receiver": "user",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "config",
            "receiver": "gateway",
            "stereotypes": [
                "plaintext_credentials_link",
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "gateway",
            "receiver": "account_service",
            "stereotypes": [
                "restful_http",
                "circuit_breaker_link",
                "load_balanced_link"
            ],
            "tagged_values": {
                "'Load Balancer'": "\"Ribbon\"",
                " 'Circuit Breaker'": "\"Hystrix\""
            }
        },
        {
            "sender": "gateway",
            "receiver": "statistics_service",
            "stereotypes": [
                "restful_http",
                "circuit_breaker_link",
                "load_balanced_link"
            ],
            "tagged_values": {
                "'Load Balancer'": "\"Ribbon\"",
                " 'Circuit Breaker'": "\"Hystrix\""
            }
        },
        {
            "sender": "gateway",
            "receiver": "notification_service",
            "stereotypes": [
                "restful_http",
                "circuit_breaker_link",
                "load_balanced_link"
            ],
            "tagged_values": {
                "'Load Balancer'": "\"Ribbon\"",
                " 'Circuit Breaker'": "\"Hystrix\""
            }
        },
        {
            "sender": "gateway",
            "receiver": "auth_service",
            "stereotypes": [
                "restful_http",
                "circuit_breaker_link",
                "load_balanced_link",
                "auth_provider"
            ],
            "tagged_values": {
                "'Load Balancer'": "\"Ribbon\"",
                " 'Circuit Breaker'": "\"Hystrix\""
            }
        }
    ],
    "external_entities": [
        {
            "name": "mail_server",
            "stereotypes": [
                "mail_server",
                "plaintext_credentials",
                "exitpoint",
                "entrypoint"
            ],
            "tagged_values": {
                "Mail Server": "Gmail",
                "Host": "smtp.gmail.com",
                "Port": 465,
                "Username": "dev-user",
                "Password": "dev-password"
            }
        },
        {
            "name": "external_website",
            "stereotypes": [
                "external_website",
                "entrypoint",
                "exitpoint"
            ],
            "tagged_values": {
                "URL": "https://api.exchangeratesapi.io"
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
    ]
}
```

### Model Items

The Application consists of a total of 246 elements:

Element | Count
-- | --
Services | 14
External Entities | 3
Information Flows | 37
Annotations | 192
Total Items | 246

### Model Representations {#representations}

Open the model in the following formats:

- [JSON model](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/sqshq_piggymetrics/sqshq_piggymetrics.json)
- [PlantUML description](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/sqshq_piggymetrics/sqshq_piggymetrics.txt)
- [PNG graph](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/sqshq_piggymetrics/sqshq_piggymetrics.png)
- [CodeableModels](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/sqshq_piggymetrics/sqshq_piggymetrics.py)

### Traceability

Open the traceability information for all model items:

- [Traceability](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/sqshq_piggymetrics/sqshq_piggymetrics_traceability.json)

## Security Rules

The following table shows the application's adherence to the 17 architectural security rules. The last column provides model variants that adhere to the rule for each rule that is initially violated.

Rule ID &nbsp;&nbsp;| Verdict &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| Evidence &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| Model Variant &nbsp;&nbsp;&nbsp;|
-- | -- | -- | -- |
**R1** | <i class="fa fa-warning" style="color: #bfc600;"> | <a href="#rule01">Evidence |  |
**R2** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule02">Evidence |  |
**R3** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule03">Evidence |  |
**R4** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule04">Evidence |  |
**R5** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule05">Evidence |  |
**R6** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule06">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/sqshq_piggymetrics/model_variants/6.txt) |
**R7** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule07">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/sqshq_piggymetrics/model_variants/7.txt) |
**R8** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule08">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/sqshq_piggymetrics/model_variants/8.txt) |
**R9** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule09">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/sqshq_piggymetrics/model_variants/9.txt) |
**R10** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule10">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/sqshq_piggymetrics/model_variants/10.txt) |
**R11** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule11">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/sqshq_piggymetrics/model_variants/11.txt) |
**R12** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule12">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/sqshq_piggymetrics/model_variants/12.txt) |
**R13** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule13">Evidence |  |
**R14** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule14">Evidence |  |
**R16** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule16">Evidence |  |
**R17** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule17">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/sqshq_piggymetrics/model_variants/17.txt) |
**R18** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule18">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/sqshq_piggymetrics/model_variants/18.txt) |



### Evidence and explanations for rule decisions

#### R1 {#rule01}

This rule is partially adhered to:
1. The [@EnableZuulProxy](https://cloud.spring.io/spring-cloud-netflix/multi/multi__router_and_filter_zuul.html#netflix-zuul-reverse-proxy) annotation is present,
1. No evidence of separate access to authorization server,
1. Authorization server route in YML of API Gateway
1. only file in whole directory is the main class and there is no [@EnableResourceServer](https://docs.spring.io/spring-security-oauth2-boot/docs/current/reference/html5/#boot-features-security-oauth2-resource-server) annotation,
which shows that there is no authentication/authorization at the API gateway.

Artifacts:
- GatewayApplication.java: Line: [10](https://github.com/sqshq/piggymetrics/blob/master/gateway/src/main/java/com/piggymetrics/gateway/GatewayApplication.java#L10)
- gateway.yml: Lines: [13](https://github.com/sqshq/piggymetrics/blob/master/config/src/main/resources/shared/gateway.yml#L13), [45](https://github.com/sqshq/piggymetrics/blob/master/config/src/main/resources/shared/gateway.yml#L45)

#### R2  {#rule02}

Rule is adhered to:
1. The [@EnableResourceServer](https://docs.spring.io/spring-security-oauth2-boot/docs/current/reference/html5/#boot-features-security-oauth2-resource-server) annotation is present at every downstream service > tokens are required for incoming requests for authorization even between requests between services
1. Tokens need specific scope to be accepted

Artifacts:
- ResourceServerConfig.java: Line: [23](https://github.com/sqshq/piggymetrics/blob/master/account-service/src/main/java/com/piggymetrics/account/config/ResourceServerConfig.java#L23)
- AuthApplication.java: Line: [10](https://github.com/sqshq/piggymetrics/blob/master/auth-service/src/main/java/com/piggymetrics/auth/AuthApplication.java#L10)
- ResourceServerConfig.java: Line: [18](https://github.com/sqshq/piggymetrics/blob/master/notification-service/src/main/java/com/piggymetrics/notification/config/ResourceServerConfig.java#L18)
- ResourceServerConfig.java: Line: [15](https://github.com/sqshq/piggymetrics/blob/master/statistics-service/src/main/java/com/piggymetrics/statistics/config/ResourceServerConfig.java#L15)
- StatisticsController.java: Line: [25](https://github.com/sqshq/piggymetrics/blob/master/statistics-service/src/main/java/com/piggymetrics/statistics/controller/StatisticsController.java#L25)

#### R3 {#rule03}

This rule is adhered to:
1. The [@EnableAuthorizationServer](https://docs.spring.io/spring-security-oauth2-boot/docs/current/reference/html5/#oauth2-boot-authorization-server-minimal) annotation is present
1. No [JwtAccessTokenConverter -> Opaque Tokens](https://docs.spring.io/spring-security-oauth2-boot/docs/current/reference/html5/#oauth2-boot-authorization-server-spring-security-oauth2-resource-server-jwk)
1. Endpoint for validating user in tokens present

Artifacts:
- OAuth2AuthorizationConfig.java: Line: [22](https://github.com/sqshq/piggymetrics/blob/master/auth-service/src/main/java/com/piggymetrics/auth/config/OAuth2AuthorizationConfig.java#L22)
- UserController.java: Line: [27](https://github.com/sqshq/piggymetrics/blob/master/auth-service/src/main/java/com/piggymetrics/auth/controller/UserController.java#L27)

#### R4 {#rule04}

This rule is adhered to: Identity representations (opaque token) are used at all downstream services and between services for authorization due to @EnableResourceServer annotation, however no indication of a transformation present (see Rule 2 arguments).

#### R5 {#rule05}

Rule is adhered to:
1. Endpoint for validating is there per Rule 3 in the Authorization Server,
1. Endpoint is listed under "security.oauth2.resource.user-info-uri" in application.yml at the config-server,
1. See Rule 3 argumentation.

Artifacts:
- application.yml: Line: [23](https://github.com/sqshq/piggymetrics/blob/master/config/src/main/resources/shared/application.yml#L23)

#### R6 {#rule06}

Rule is violated: There is no functionality present that enforces any consequences for a specific amount of failed login attempts



#### R7 {#rule07}

Rule is violated:
1. There are no certificates in the repository and no "server.ssl.key-store"/"server.ssl.trust-store" arguments inserted in the yml of the API gateway.
1. The "server.ssl.enabled" is set, but only in test-suite YML-Configurations

Artifacts:
- gateway.yml: [File](https://github.com/sqshq/piggymetrics/blob/master/config/src/main/resources/shared/gateway.yml)

#### R8 {#rule08}

Rule is violated: See Rule 7 argumentation.

Artifacts:
- gateway.yml: [File](https://github.com/sqshq/piggymetrics/blob/master/config/src/main/resources/shared/gateway.yml)



#### R9 {#rule09}

Rule is violated: The README.md mentions centralized logging with elasticsearch, but there is no artifact in the repository to confirm.

Artifacts:
- README.md: Line: [192](https://github.com/sqshq/piggymetrics/blob/master/README.md#L192)

#### R10 {#rule10}

Rule is violated: No central logging system is deployed.

#### R11 {#rule11}

Rule is violated: Logs are not explicitly sanitized.

#### R12 {#rule12}

Rule is violated: No message broker is deployed and no logs are collected.



#### R13 {#rule13}

Rule is adhered to: Hystrix is deployed as a circuit breaker on the gateway server with the [@EnableZuulProxy](https://cloud.spring.io/spring-cloud-netflix/multi/multi__router_and_filter_zuul.html#netflix-zuul-reverse-proxy) annotation.

Artifacts:
- GatewayApplication.java: Line: [10](https://github.com/sqshq/piggymetrics/blob/master/gateway/src/main/java/com/piggymetrics/gateway/GatewayApplication.java#L10)
- AccountApplication.java: Line: [15](https://github.com/sqshq/piggymetrics/blob/master/account-service/src/main/java/com/piggymetrics/account/AccountApplication.java#L15)

#### R14 {#rule14}

Rule is adhered to: The gateway server uses load balancing via [Ribbon](https://cloud.spring.io/spring-cloud-netflix/multi/multi__router_and_filter_zuul.html#netflix-zuul-reverse-proxy) to access dependent services.

Artifacts:
- GatewayApplication.java: Line: [10](https://github.com/sqshq/piggymetrics/blob/master/gateway/src/main/java/com/piggymetrics/gateway/GatewayApplication.java#L10)

#### R15 {#rule15}

This rule is not applicable: Not a service mesh deployment.



#### R16 {#rule16}

Rule is adhered to:
1. Registry Service (Eureka Server) present with [@EnableEurekaServer](https://docs.spring.io/spring-cloud-netflix/docs/4.0.1-SNAPSHOT/reference/html/#spring-cloud-running-eureka-server) annotation.
1. Eureka Server deployed in Docker Compose -> able to start on dedicated server

Artifacts:
- RegistryApplication.java: Line: [8](https://github.com/sqshq/piggymetrics/blob/master/registry/src/main/java/com/piggymetrics/registry/RegistryApplication.java#L8)
- docker-compose.yml: Line: [23](https://github.com/sqshq/piggymetrics/blob/master/docker-compose.yml#L23)

#### R17 {#rule17}

Rule is violated: No [HTTP basic password](https://cloud.spring.io/spring-cloud-netflix/reference/html/#authenticating-with-the-eureka-server) listed in any YML-Configuration of format username:password@here-location-of-eureka-server at "eureka.client.serviceUrl.defaultZone".

Artifacts:
- application.yml: Line: [13](https://github.com/sqshq/piggymetrics/blob/master/config/src/main/resources/shared/application.yml#L13)



#### R18 {#rule18}

Rule is violated: No secret manager is deployed.
