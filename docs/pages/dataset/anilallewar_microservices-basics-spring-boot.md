---
title: anilallewar/microservices-basics-spring-boot
keywords: model
tags: [docker, docker_compose, eureka, gradle, hystrix, ribbon, spring_config, spring_oauth, turbine, zipkin, zuul]
sidebar: datasetdoc_sidebar
permalink: anilallewar_microservices-basics-spring-boot.html
toc: false
---

## General Information

The repository for this application ([open on GitHub](https://github.com/anilallewar/microservices-basics-spring-boot)) has 663 stars and was forked 425 times. The codebase consists of 4245 lines of code and makes use of the following technologies:

<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_docker.html">Docker</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_docker_compose.html">Docker Compose</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_eureka.html">Eureka</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_gradle.html">Gradle</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_hystrix.html">Hystrix</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_ribbon.html">Ribbon</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_spring_config.html">Spring Config</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_spring_oauth.html">Spring OAuth</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_turbine.html">Turbine</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_zipkin.html">Zipkin</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_zuul.html">Zuul</a>

## Data Flow Diagram

![Dataflow Diagram](./anilallewar_microservices-basics-spring-boot.png)


Download the following model file [here](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/anilallewar_microservices-basics-spring-boot/anilallewar_microservices-basics-spring-boot.json).
Other formats are provided below.

```json
{
    "services": [
        {
            "name": "configserver",
            "stereotypes": [
                "infrastructural",
                "configuration_server"
            ],
            "tagged_values": {
                "Port": 8888,
                "Configuration Server": "Spring Cloud Config"
            }
        },
        {
            "name": "webservice_registry",
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
            "name": "zipkin_tracing",
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
            "name": "mysqldb",
            "stereotypes": [
                "database",
                "plaintext_credentials"
            ],
            "tagged_values": {
                "Port": 3306,
                "Database": "MySQL",
                "Password": "password"
            }
        },
        {
            "name": "auth_server",
            "stereotypes": [
                "infrastructural",
                "authorization_server",
                "resource_server",
                "authentication_scope_all_requests",
                "plaintext_credentials"
            ],
            "tagged_values": {
                "Port": 8899,
                "Authorization Server": "Spring OAuth2",
                "Endpoints": [
                    "/me"
                ],
                "Username": "user",
                "Password": "password"
            }
        },
        {
            "name": "web_portal",
            "stereotypes": [
                "infrastructural",
                "monitoring_dashboard",
                "monitoring_server",
                "authentication_scope_all_requests"
            ],
            "tagged_values": {
                "Port": 8090,
                "Monitoring Server": "Turbine",
                "Monitoring Dashboard": "Hystrix"
            }
        },
        {
            "name": "user_webservice",
            "stereotypes": [
                "internal",
                "local_logging",
                "resource_server",
                "authentication_scope_all_requests"
            ],
            "tagged_values": {
                "Port": 8091,
                "Endpoints": [
                    "/",
                    "/{userName}"
                ]
            }
        },
        {
            "name": "comments_webservice",
            "stereotypes": [
                "internal",
                "local_logging",
                "resource_server"
            ],
            "tagged_values": {
                "Port": 8083,
                "Endpoints": [
                    "/comments",
                    "/comments/{taskId}"
                ]
            }
        },
        {
            "name": "task_webservice",
            "stereotypes": [
                "internal",
                "local_logging",
                "authentication_scope_all_requests",
                "resource_server",
                "circuit_breaker",
                "load_balancer"
            ],
            "tagged_values": {
                "Port": 8082,
                "Circuit Breaker": "Hystrix",
                "Endpoints": [
                    "/",
                    "/{taskId}",
                    "/usertask/{userName}"
                ],
                "Load Balancer": "Spring Cloud"
            }
        },
        {
            "name": "api_gateway",
            "stereotypes": [
                "infrastructural",
                "gateway",
                "load_balancer",
                "circuit_breaker",
                "csrf_disabled"
            ],
            "tagged_values": {
                "Port": 8765,
                "Gateway": "Zuul",
                "Load Balancer": "Ribbon",
                "Circuit Breaker": "Hystrix"
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
                "URL": "https://github.com/anilallewar/microservices-basics-cloud-config"
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
            "receiver": "configserver",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "configserver",
            "receiver": "webservice_registry",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "configserver",
            "receiver": "zipkin_tracing",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "configserver",
            "receiver": "auth_server",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "mysqldb",
            "receiver": "auth_server",
            "stereotypes": [
                "restful_http",
                "plaintext_credentials_link"
            ],
            "tagged_values": {
                "'Username'": "\"root\"",
                " 'Password'": "\"password\""
            }
        },
        {
            "sender": "auth_server",
            "receiver": "webservice_registry",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "web_portal",
            "receiver": "webservice_registry",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "configserver",
            "receiver": "web_portal",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "user_webservice",
            "receiver": "zipkin_tracing",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "configserver",
            "receiver": "user_webservice",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "user_webservice",
            "receiver": "webservice_registry",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "auth_server",
            "receiver": "user_webservice",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "comments_webservice",
            "receiver": "zipkin_tracing",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "configserver",
            "receiver": "comments_webservice",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "comments_webservice",
            "receiver": "webservice_registry",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "task_webservice",
            "receiver": "zipkin_tracing",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "configserver",
            "receiver": "task_webservice",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "auth_server",
            "receiver": "task_webservice",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "task_webservice",
            "receiver": "webservice_registry",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "task_webservice",
            "receiver": "web_portal",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "task_webservice",
            "receiver": "comments_webservice",
            "stereotypes": [
                "restful_http",
                "circuit_breaker_link",
                "load_balanced_link"
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
            "sender": "configserver",
            "receiver": "api_gateway",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "webservice_registry",
            "receiver": "api_gateway",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "api_gateway",
            "receiver": "zipkin_tracing",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "auth_server",
            "receiver": "api_gateway",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "api_gateway",
            "receiver": "user_webservice",
            "stereotypes": [
                "restful_http",
                "load_balanced_link",
                "circuit_breaker_link"
            ],
            "tagged_values": {}
        },
        {
            "sender": "api_gateway",
            "receiver": "task_webservice",
            "stereotypes": [
                "restful_http",
                "load_balanced_link",
                "circuit_breaker_link"
            ],
            "tagged_values": {}
        }
    ]
}

```

### Model Items

The Application consists of 149 items:

Item Group | Count
-- | --
Services | 10
External Entities | 2
Information Flows | 29
Annotations | 108
Total Items | 149

### Model Representations {#representations}

Open the model in the following formats:

- [JSON model](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/anilallewar_microservices-basics-spring-boot/anilallewar_microservices-basics-spring-boot.json)
- [PlantUML description](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/anilallewar_microservices-basics-spring-boot/anilallewar_microservices-basics-spring-boot.txt)
- [PNG graph](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/anilallewar_microservices-basics-spring-boot/anilallewar_microservices-basics-spring-boot.png)
- [CodeableModels](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/anilallewar_microservices-basics-spring-boot/anilallewar_microservices-basics-spring-boot.py)

### Traceability

Open the traceability information for all model items:

- [Traceability](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/anilallewar_microservices-basics-spring-boot/anilallewar_microservices-basics-spring-boot_traceability.json)

## Security Rules

The following table shows the application's adherence to the 17 architectural security rules. The last column provides model variants that adhere to the rule for each rule that is initially violated.

Rule ID &nbsp;&nbsp;| Verdict &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| Evidence &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| Model Variant &nbsp;&nbsp;&nbsp;|
-- | -- | -- | -- |
**R1** | <i class="fa fa-warning" style="color: #bfc600;"> | <a href="#rule01">Evidence |  |
**R2** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule02">Evidence |  |
**R3** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule03">Evidence |  |
**R4** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule04">Evidence | [Variant]() |
**R5** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule05">Evidence |  |
**R6** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule06">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/anilallewar_microservices-basics-spring-boot/model_variants/6.txt) |
**R7** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule07">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/anilallewar_microservices-basics-spring-boot/model_variants/7.txt) |
**R8** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule08">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/anilallewar_microservices-basics-spring-boot/model_variants/8.txt) |
**R9** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule09">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/anilallewar_microservices-basics-spring-boot/model_variants/9.txt) |
**R10** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule10">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/anilallewar_microservices-basics-spring-boot/model_variants/10.txt) |
**R11** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule11">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/anilallewar_microservices-basics-spring-boot/model_variants/11.txt) |
**R12** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule12">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/anilallewar_microservices-basics-spring-boot/model_variants/12.txt) |
**R13** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule13">Evidence |  |
**R14** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule14">Evidence |  |
**R16** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule16">Evidence |  |
**R17** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule17">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/anilallewar_microservices-basics-spring-boot/model_variants/17.txt) |
**R18** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule18">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/anilallewar_microservices-basics-spring-boot/model_variants/18.txt) |



### Evidence and explanations for rule decisions

#### R1 {#rule01}

Rule is partially adhered to:
1. The [@EnableZuulProxy](https://cloud.spring.io/spring-cloud-netflix/multi/multi__router_and_filter_zuul.html#netflix-zuul-reverse-proxy) annotation is present.
1. The [@EnableOAuth2Sso](https://docs.spring.io/spring-security-oauth2-boot/docs/current/api/org/springframework/boot/autoconfigure/security/oauth2/client/EnableOAuth2Sso.html) annotation is present.
1. No routing to the authorization server as mentioned by author, thus no single entrypoint.
1. The README.md of the authorization server mentions request at port 8899, while API Gateway port is 8765.

Artifacts:
- Dockerfile: Line: [24](https://github.com/anilallewar/microservices-basics-spring-boot/blob/master/api-gateway/src/main/docker/Dockerfile#L24)
- bootstrap.yml: Line: [2](https://github.com/anilallewar/microservices-basics-spring-boot/blob/master/api-gateway/src/main/resources/bootstrap.yml#L2)
- GatewayApplication.java: Line: [48](https://github.com/anilallewar/microservices-basics-spring-boot/blob/master/api-gateway/src/main/java/com/anilallewar/microservices/gateway/GatewayApplication.java#L48)
- WebSecurityConfiguration.java: Line: [21](https://github.com/anilallewar/microservices-basics-spring-boot/blob/master/api-gateway/src/main/java/com/anilallewar/microservices/gateway/security/WebSecurityConfiguration.java#L21)
- README.md: Line: [93](https://github.com/anilallewar/microservices-basics-spring-boot/blob/master/auth-server/README.md#L93)
- api-gateway.yml: Lines: [59](https://github.com/anilallewar/microservices-basics-cloud-config/blob/master/api-gateway.yml#L59), [66](https://github.com/anilallewar/microservices-basics-cloud-config/blob/master/api-gateway.yml#L66)

#### R2 {#rule02}

Rule is adhered to: All downstream services are resource servers per [@EnableResourceServer](https://docs.spring.io/spring-security-oauth2-boot/docs/current/reference/html5/#oauth2-boot-resource-server-minimal) annotation, meaning even requests between services need to be authenticated/authorized.

Artifacts:
- WebSecurityConfiguration.java: Line: [21](https://github.com/anilallewar/microservices-basics-spring-boot/blob/master/api-gateway/src/main/java/com/anilallewar/microservices/gateway/security/WebSecurityConfiguration.java#L21)
- ResourceServerConfiguration.java: Line: [27](https://github.com/anilallewar/microservices-basics-spring-boot/blob/master/user-webservice/src/main/java/com/anilallewar/microservices/user/config/security/ResourceServerConfiguration.java#L27)
- ResourceServerConfiguration.java: Line: [27](https://github.com/anilallewar/microservices-basics-spring-boot/blob/master/task-webservice/src/main/java/com/anilallewar/microservices/task/config/security/ResourceServerConfiguration.java#L27)
- CommentsApplication.java: Line: [30](https://github.com/anilallewar/microservices-basics-spring-boot/blob/master/comments-webservice/src/main/java/com/anilallewar/microservices/comments/CommentsApplication.java#L30)
- AuthServerApplication.java: Line: [22](https://github.com/anilallewar/microservices-basics-spring-boot/blob/master/auth-server/src/main/java/com/anilallewar/microservices/auth/AuthServerApplication.java#L22)

#### R3 {#rule03}

Rule is adhered to:
1. The [@EnableAuthorizationServer](https://docs.spring.io/spring-security-oauth2-boot/docs/current/reference/html5/#oauth2-boot-authorization-server-minimal) annotation is present,
1. JwtAccessTokenConverter bean present, thus using JWTs,
1. Downstream services like API-Gateway have public key hardcoded in YML.

Artifacts:
- OAuthServerConfiguration.java: Lines: [52](https://github.com/anilallewar/microservices-basics-spring-boot/blob/master/auth-server/src/main/java/com/anilallewar/microservices/auth/config/OAuthServerConfiguration.java#L52), [67](https://github.com/anilallewar/microservices-basics-spring-boot/blob/master/auth-server/src/main/java/com/anilallewar/microservices/auth/config/OAuthServerConfiguration.java#L67)
- api-gateway.yml: Line: [54](https://github.com/anilallewar/microservices-basics-cloud-config/blob/master/api-gateway.yml#L54)

#### R4 {#rule04}

Rule is violated: As Rule 2 already confirms, every downstream service needs tokens for authorization/authentication. However, no evidence of tokens transferred to internal identity representations.

#### R5 {#rule05}

Rule is adhered to:
1. All resource servers have the [@EnableResourceServer](https://docs.spring.io/spring-security-oauth2-boot/docs/current/reference/html5/#oauth2-boot-resource-server-minimal) annotation.
1. The public key is hardcoded into each Resource Servers YML-Configuration.

Artifacts:
- TaskApplication.java: Line: [42](https://github.com/anilallewar/microservices-basics-spring-boot/blob/master/task-webservice/src/main/java/com/anilallewar/microservices/task/TaskApplication.java#L42)
- UserApplication.java: Line: [34](https://github.com/anilallewar/microservices-basics-spring-boot/blob/master/user-webservice/src/main/java/com/anilallewar/microservices/user/UserApplication.java#L34)
- api-gateway.yml: Line: [52](https://github.com/anilallewar/microservices-basics-cloud-config/blob/master/api-gateway.yml#L52)
- user-webservice.yml: Line: [23](https://github.com/anilallewar/microservices-basics-cloud-config/blob/master/user-webservice.yml#L23)
- comments-webservice.yml: Line: [22](https://github.com/anilallewar/microservices-basics-cloud-config/blob/master/comments-webservice.yml#L22)
- task-webservice.yml: Line: [23](https://github.com/anilallewar/microservices-basics-cloud-config/blob/master/task-webservice.yml#L23)

#### R6 {#rule06}

Rule is violated: No functionality of consequences for failed login attempts

#### R7 {#rule07}

Rule is violated: No mention of SSL, TLS, keystores or trust-stores in application

#### R8 {#rule08}

Rule is violated: See rule 7.

#### R9 {#rule09}

Rule is violated: No central logging system is deployed.

#### R10 {#rule10}

Rule is violated: No central logging system is deployed.

#### R11 {#rule11}

Rule is violated: Logs are not explicitly sanitized.

#### R12 {#rule12}

Rule is violated: No message broker is deployed and no logs are collected.

#### R13 {#rule13}

Rule is adhered to: [Hystrix Circuit Breaker](https://cloud.spring.io/spring-cloud-netflix/multi/multi__router_and_filter_zuul.html#netflix-zuul-reverse-proxy) enabled through @EnableZuulProxy annotation.

Artifacts:
- GatewayApplication.java: Line: [48](https://github.com/anilallewar/microservices-basics-spring-boot/blob/master/api-gateway/src/main/java/com/anilallewar/microservices/gateway/GatewayApplication.java#L48)

#### R14 {#rule14}

Rule is adhered to: The gateway server uses load balancing via Ribbon to access dependent services through [@EnableZuulProxy](https://cloud.spring.io/spring-cloud-netflix/multi/multi__router_and_filter_zuul.html#netflix-zuul-reverse-proxy) annotation.

Artifacts:
- GatewayApplication.java: Line: [48](https://github.com/anilallewar/microservices-basics-spring-boot/blob/master/api-gateway/src/main/java/com/anilallewar/microservices/gateway/GatewayApplication.java#L48)

#### R16 {#rule16}

Rule is adhered to:
1. Registry Service (Eureka Server) with [@EnableEurekaServer](https://docs.spring.io/spring-cloud-netflix/docs/4.0.1-SNAPSHOT/reference/html/#spring-cloud-eureka-server) present.
1. Started in Docker Container through Compose, thus deployable on dedicated server

Artifacts:
- RegistryApplication.java: Line: [19](https://github.com/anilallewar/microservices-basics-spring-boot/blob/master/webservice-registry/src/main/java/com/anilallewar/microservices/registry/RegistryApplication.java#L19)
- docker-compose.yml: Line: [33](https://github.com/anilallewar/microservices-basics-spring-boot/blob/master/docker-orchestration/docker-compose/docker-compose.yml#L33)

#### R17 {#rule17}


Rule is violated:

 There is no [HTTP basic password](https://cloud.spring.io/spring-cloud-netflix/reference/html/#authenticating-with-the-eureka-server) password listed in any YML-Configuration of format username:password@here-location-of-eureka-server at "eureka.client.serviceUrl.defaultZone".

Artifacts:
- api-gateway.yml: Line: [138](https://github.com/anilallewar/microservices-basics-cloud-config/blob/master/api-gateway.yml#L138)

#### R18 {#rule18}

Rule is violated: No secret manager is deployed. The deployed git configuration server is not a secrets manager.

Artifacts:
- application.yml: Line: [3](https://github.com/anilallewar/microservices-basics-spring-boot/blob/master/config-server/src/main/resources/application.yml#L3)
