---
title: piomin/sample-spring-oauth2-microservices
keywords: model
tags: [eureka, ribbon, spring_oauth, zuul]
sidebar: datasetdoc_sidebar
permalink: piomin_sample-spring-oauth2-microservices.html
toc: false
---

## General Information

The repository for this application ([open on GitHub](https://github.com/piomin/sample-spring-oauth2-microservices)) has 120 stars and was forked 139 times. The codebase consists of 1028 lines of code and makes use of the following technologies:

<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_eureka.html">Eureka</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_ribbon.html">Ribbon</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_spring_oauth.html">Spring OAuth</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_zuul.html">Zuul</a>

## Data Flow Diagram

![Dataflow Diagram](./piomin_sample-spring-oauth2-microservices.png)

Download the following model file [here](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/piomin_sample-spring-oauth2-microservices/piomin_sample-spring-oauth2-microservices.json).
Other formats are provided below.

```json
{
    "services": [
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
            "name": "gateway_server",
            "stereotypes": [
                "gateway",
                "in_memory_authentication",
                "plaintext_credentials",
                "infrastructural",
                "authentication_scope_all_requests",
                "load_balancer"
            ],
            "tagged_values": {
                "Gateway": "Zuul",
                "Username": "root",
                "Password": "password",
                "Port": 8765,
                "Load Balancer": "Ribbon"
            }
        },
        {
            "name": "auth_server",
            "stereotypes": [
                "authorization_server",
                "encryption",
                "infrastructural",
                "resource_server",
                "token_server",
                "local_logging"
            ],
            "tagged_values": {
                "Authorization Server": "Spring OAuth2",
                "Port": 9999
            }
        },
        {
            "name": "account_service",
            "stereotypes": [
                "internal",
                "pre_authorized_endpoints",
                "resource_server"
            ],
            "tagged_values": {
                "Pre-authorized Endpoints": [
                    "/{id}",
                    "/"
                ],
                "Port": 8082
            }
        },
        {
            "name": "customer_service",
            "stereotypes": [
                "internal",
                "pre_authorized_endpoints",
                "resource_server",
                "local_logging"
            ],
            "tagged_values": {
                "Pre-authorized Endpoints": [
                    "/{id}"
                ],
                "Port": 8083
            }
        }
    ],
    "information_flows": [
        {
            "sender": "discovery_server",
            "receiver": "gateway_server",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "database_gateway_server",
            "receiver": "gateway_server",
            "stereotypes": [
                "jdbc",
                "plaintext_credentials_link"
            ],
            "tagged_values": {
                "'Password'": "\"default\"",
                " 'Username'": "\"default\""
            }
        },
        {
            "sender": "user",
            "receiver": "gateway_server",
            "stereotypes": [
                "restful_http",
                "authenticated_request"
            ],
            "tagged_values": {}
        },
        {
            "sender": "gateway_server",
            "receiver": "user",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "auth_server",
            "receiver": "discovery_server",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "database_auth_server",
            "receiver": "auth_server",
            "stereotypes": [
                "jdbc",
                "plaintext_credentials_link"
            ],
            "tagged_values": {
                "\"Username\"": "\"oauth2\"",
                " \"Password\"": "\"oauth2\""
            }
        },
        {
            "sender": "gateway_server",
            "receiver": "auth_server",
            "stereotypes": [
                "restful_http",
                "auth_provider"
            ],
            "tagged_values": {}
        },
        {
            "sender": "account_service",
            "receiver": "discovery_server",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "auth_server",
            "receiver": "account_service",
            "stereotypes": [
                "restful_http",
                "auth_provider"
            ],
            "tagged_values": {}
        },
        {
            "sender": "gateway_server",
            "receiver": "account_service",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "customer_service",
            "receiver": "discovery_server",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "customer_service",
            "receiver": "account_service",
            "stereotypes": [
                "restful_http",
                "authenticated_request",
                "feign_connection",
                "load_balanced_link"
            ],
            "tagged_values": {
                "'Load Balancer'": "\"Ribbon\""
            }
        },
        {
            "sender": "auth_server",
            "receiver": "customer_service",
            "stereotypes": [
                "restful_http",
                "auth_provider"
            ],
            "tagged_values": {}
        }
    ],
    "external_entities": [
        {
            "name": "database_gateway_server",
            "stereotypes": [
                "external_database",
                "entrypoint",
                "exitpoint",
                "plaintext_credentials"
            ],
            "tagged_values": {
                "Database": "MySQL",
                "Password": "default",
                "Username": "default"
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
        },
        {
            "name": "database_auth_server",
            "stereotypes": [
                "external_database",
                "entrypoint",
                "exitpoint",
                "plaintext_credentials",
                "tokenstore"
            ],
            "tagged_values": {
                "Database": "MySQL",
                "Username": "oauth2",
                "Password": "oauth2"
            }
        }
    ]
}
```

### Model Items

The Application consists of a total of 99 elements:

Element | Count
-- | --
Services | 5
External Entities | 3
Information Flows | 13
Annotations | 78
Total Items | 99

### Model Representations {#representations}

Open the model in the following formats:

- [JSON model](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/piomin_sample-spring-oauth2-microservices/piomin_sample-spring-oauth2-microservices.json)
- [PlantUML description](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/piomin_sample-spring-oauth2-microservices/piomin_sample-spring-oauth2-microservices.txt)
- [PNG graph](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/piomin_sample-spring-oauth2-microservices/piomin_sample-spring-oauth2-microservices.png)
- [CodeableModels](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/piomin_sample-spring-oauth2-microservices/piomin_sample-spring-oauth2-microservices.py)

### Traceability

Open the traceability information for all model items:

- [Traceability](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/piomin_sample-spring-oauth2-microservices/piomin_sample-spring-oauth2-microservices_traceability.json)

## Security Rules

The following table shows the application's adherence to the 17 architectural security rules. The last column provides model variants that adhere to the rule for each rule that is initially violated.

Rule ID &nbsp;&nbsp;| Verdict &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| Evidence &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| Model Variant &nbsp;&nbsp;&nbsp;|
-- | -- | -- | -- |
**R1** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule01">Evidence |  |
**R2** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule02">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/piomin_sample-spring-oauth2-microservices/model_variants/2.txt) |
**R3** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule03">Evidence |  |
**R4** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule04">Evidence |  |
**R5** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule05">Evidence |  |
**R6** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule06">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/piomin_sample-spring-oauth2-microservices/model_variants/6.txt) |
**R7** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule07">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/piomin_sample-spring-oauth2-microservices/model_variants/7.txt) |
**R8** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule08">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/piomin_sample-spring-oauth2-microservices/model_variants/8.txt) |
**R9** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule09">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/piomin_sample-spring-oauth2-microservices/model_variants/9.txt) |
**R10** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule10">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/piomin_sample-spring-oauth2-microservices/model_variants/10.txt) |
**R11** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule11">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/piomin_sample-spring-oauth2-microservices/model_variants/11.txt) |
**R12** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule12">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/piomin_sample-spring-oauth2-microservices/model_variants/12.txt) |
**R13** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule13">Evidence |  |
**R14** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule14">Evidence |  |
**R16** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule16">Evidence |  |
**R17** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule17">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/piomin_sample-spring-oauth2-microservices/model_variants/17.txt) |
**R18** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule18">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/piomin_sample-spring-oauth2-microservices/model_variants/18.txt) |



### Evidence and explanations for rule decisions

#### R1 {#rule01}

Rule is adhered to: User only communicates with the Zuul gateway server.

Artifacts:
- application.yml: Line: [2](https://github.com/piomin/sample-spring-oauth2-microservices/blob/with_database/gateway/src/main/resources/application.yml#L2)

#### R2  {#rule02}

Rule is violated: Services communicate internally over plain HTTP. The communication is not authenticated.

Artifacts:
- application.yml: Lines: [8](https://github.com/piomin/sample-spring-oauth2-microservices/blob/with_database/gateway/src/main/resources/application.yml#L8), [21](https://github.com/piomin/sample-spring-oauth2-microservices/blob/with_database/gateway/src/main/resources/application.yml#L21), [25](https://github.com/piomin/sample-spring-oauth2-microservices/blob/with_database/gateway/src/main/resources/application.yml#L25)

#### R3 {#rule03}

Rule is adhered to: Authentication and authorization via OAuth2 is implemented at the AuthServer instance. The AuthServer is a separate service at platform level that provides authentication to all internal services.

Artifacts:
- application.yml: Line: [2](https://github.com/piomin/sample-spring-oauth2-microservices/blob/with_database/auth/src/main/resources/application.yml#L2)
- OAuth2Config.java: Line: [18](https://github.com/piomin/sample-spring-oauth2-microservices/blob/with_database/auth/src/main/java/pl/piomin/services/auth/OAuth2Config.java#L18)

#### R4 {#rule04}

Rule is adhered to: Users are authenticated using JWT Tokens and identified by a unique username. All endpoints can verify authorization scopes with the central AuthServer.

Artifacts:
- OAuth2Config.java: Line: [28](https://github.com/piomin/sample-spring-oauth2-microservices/blob/with_database/auth/src/main/java/pl/piomin/services/auth/OAuth2Config.java#L28)

#### R5 {#rule05}

Rule is adhered to: The authentication tokens are verified by the all services.

Artifacts:
- AccountController.java: Lines: [17](https://github.com/piomin/sample-spring-oauth2-microservices/blob/with_database/account/src/main/java/pl/piomin/services/account/api/AccountController.java#L17), [23](https://github.com/piomin/sample-spring-oauth2-microservices/blob/with_database/account/src/main/java/pl/piomin/services/account/api/AccountController.java#L23)
- CustomerController.java: Line: [23](https://github.com/piomin/sample-spring-oauth2-microservices/blob/with_database/customer/src/main/java/pl/piomin/services/customer/api/CustomerController.java#L23)

#### R6 {#rule06}

Rule is violated: No rate limiting of any means is deployed.



#### R7 {#rule07}

Rule is violated: User external entities can call the gateway service using an unencrypted HTTP connection.

Artifacts:
- application.yml: Line: [2](https://github.com/piomin/sample-spring-oauth2-microservices/blob/with_database/gateway/src/main/resources/application.yml#L2)

#### R8 {#rule08}

Rule is violated: All internal services communicate over insecure HTTP connections.

Artifacts:
- application.yml: Lines: [21](https://github.com/piomin/sample-spring-oauth2-microservices/blob/with_database/gateway/src/main/resources/application.yml#L21), [25](https://github.com/piomin/sample-spring-oauth2-microservices/blob/with_database/gateway/src/main/resources/application.yml#L25)



#### R9 {#rule09}

Rule is violated: No central logging system is deployed.

#### R10 {#rule10}

Rule is violated: No central logging system is deployed. Two internal services perform local logging, however none of the logs are consumed and accessed through monitoring software.

Artifacts:
- CustomerController.java: Lines: [26](https://github.com/piomin/sample-spring-oauth2-microservices/blob/with_database/customer/src/main/java/pl/piomin/services/customer/api/CustomerController.java#L26), [28](https://github.com/piomin/sample-spring-oauth2-microservices/blob/with_database/customer/src/main/java/pl/piomin/services/customer/api/CustomerController.java#L28)
- UserDetailsServiceImpl.java: Line: [33](https://github.com/piomin/sample-spring-oauth2-microservices/blob/with_database/auth/src/main/java/pl/piomin/services/auth/security/UserDetailsServiceImpl.java#L33)

#### R11 {#rule11}

Rule is violated: Logs are not sanitized, but no PII or secrets are explicitly logged.

Artifacts:
- UserDetailsServiceImpl.java: Line: [33](https://github.com/piomin/sample-spring-oauth2-microservices/blob/with_database/auth/src/main/java/pl/piomin/services/auth/security/UserDetailsServiceImpl.java#L33)

#### R12 {#rule12}

Rule is violated: No logs are collected and no message broker is deployed.



#### R13 {#rule13}

Rule is adhered to: The Zuul API gateway includes the [Hystrix Circuit Breaker](https://cloud.spring.io/spring-cloud-netflix/multi/multi__router_and_filter_zuul.html#netflix-zuul-reverse-proxy) functionality.

#### R14 {#rule14}

Rule is adhered to: The gateway server uses load balancing via [Ribbon](https://cloud.spring.io/spring-cloud-netflix/multi/multi__router_and_filter_zuul.html#netflix-zuul-reverse-proxy) to access dependent services.

Artifacts:
- application.yml: Line: [16](https://github.com/piomin/sample-spring-oauth2-microservices/blob/with_database/gateway/src/main/resources/application.yml#L16)

#### R15 {#rule15}

This rule is not applicable: Not a service mesh deployment.



#### R16 {#rule16}

Rule is adhered to:
1. Registry Service (Eureka Server) with @EnableEurekaServer present.
1. Eureka is started on Port 8765 and can be deployed on a dedicated server.

Artifacts:
- DiscoveryServer.java: Line: [8](https://github.com/piomin/sample-spring-oauth2-microservices/blob/with_database/discovery/src/main/java/pl/piomin/services/discovery/DiscoveryServer.java#L8)
- application.yml: Line: [2](https://github.com/piomin/sample-spring-oauth2-microservices/blob/with_database/gateway/src/main/resources/application.yml#L2)

#### R17 {#rule17}

Rule is violated: No [HTTP basic password](https://cloud.spring.io/spring-cloud-netflix/reference/html/#authenticating-with-the-eureka-server) listed in any YML-Configuration of format username:password@here-location-of-eureka-server at "eureka.client.serviceUrl.defaultZone".

Artifacts:
- DiscoveryServer.java: Line: [8](https://github.com/piomin/sample-spring-oauth2-microservices/blob/with_database/discovery/src/main/java/pl/piomin/services/discovery/DiscoveryServer.java#L8)
- application.yml: Line: [15](https://github.com/piomin/sample-spring-oauth2-microservices/blob/with_database/discovery/src/main/resources/application.yml#L15)



#### R18 {#rule18}

Rule is violated: The OAuth client secrets and database access passwords are supplied via configuration files and hard-coded into the Java code.

Artifacts:
- application.yml: Lines: [10](https://github.com/piomin/sample-spring-oauth2-microservices/blob/with_database/gateway/src/main/resources/application.yml#L10), [36](https://github.com/piomin/sample-spring-oauth2-microservices/blob/with_database/gateway/src/main/resources/application.yml#L36)
- SecurityConfig.java: Line: [36](https://github.com/piomin/sample-spring-oauth2-microservices/blob/with_database/gateway/src/main/java/pl/piomin/services/gateway/SecurityConfig.java#L36)
- data.sql: Lines: [11](https://github.com/piomin/sample-spring-oauth2-microservices/blob/with_database/auth/src/main/resources/script/data.sql#L11), [13](https://github.com/piomin/sample-spring-oauth2-microservices/blob/with_database/auth/src/main/resources/script/data.sql#L13)
