---
title: apssouza22/java-microservice
keywords: model
tags: [docker, docker_compose, eureka, hystrix, kafka, logstash, maven, nginx, spring_admin, spring_config, spring_oauth, zookeeper]
sidebar: datasetdoc_sidebar
permalink: apssouza22_java-microservice.html
toc: false
---

## General Information

The repository for this application ([open on GitHub](https://github.com/apssouza22/java-microservice)) has 308 stars and was forked 231 times. The codebase consists of 5283 lines of code and makes use of the following technologies:

<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_docker.html">Docker</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_docker_compose.html">Docker Compose</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_eureka.html">Eureka</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_hystrix.html">Hystrix</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_kafka.html">Kafka</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_logstash.html">Logstash</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_maven.html">Maven</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_nginx.html">Nginx</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_spring_admin.html">Spring Admin</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_spring_config.html">Spring Config</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_spring_oauth.html">Spring OAuth</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_zookeeper.html">ZooKeeper</a>

## Data Flow Diagram

![Dataflow Diagram](./apssouza22_java-microservice.png)

Download the following model file [here](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/apssouza22_java-microservice/apssouza22_java-microservice.json).
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
            "name": "admin",
            "stereotypes": [
                "administration_server",
                "infrastructural"
            ],
            "tagged_values": {
                "Administration Server": "Spring Boot Admin",
                "Port": 8026
            }
        },
        {
            "name": "eureka_server",
            "stereotypes": [
                "service_discovery",
                "infrastructural"
            ],
            "tagged_values": {
                "Service Discovery": "Eureka",
                "Port": 8010
            }
        },
        {
            "name": "user_service",
            "stereotypes": [
                "internal"
            ],
            "tagged_values": {
                "Port": 8016
            }
        },
        {
            "name": "kafka",
            "stereotypes": [
                "message_broker",
                "infrastructural"
            ],
            "tagged_values": {
                "Message Broker": "Kafka",
                "Port": 9092
            }
        },
        {
            "name": "mailer",
            "stereotypes": [
                "internal",
                "local_logging"
            ],
            "tagged_values": {
                "Port": 8020
            }
        },
        {
            "name": "reminder",
            "stereotypes": [
                "internal",
                "local_logging"
            ],
            "tagged_values": {
                "Port": 8015
            }
        },
        {
            "name": "api_gateway",
            "stereotypes": [
                "gateway",
                "circuit_breaker",
                "resource_server",
                "infrastructural",
                "csrf_disabled"
            ],
            "tagged_values": {
                "Circuit Breaker": "Hystrix",
                "Port": 8018
            }
        },
        {
            "name": "oauth",
            "stereotypes": [
                "authorization_server",
                "tokenstore",
                "infrastructural",
                "circuit_breaker"
            ],
            "tagged_values": {
                "Authorization Server": "Spring OAuth2",
                "Port": 8017,
                "Circuit Breaker": "Hystrix"
            }
        },
        {
            "name": "proxy",
            "stereotypes": [
                "web_application",
                "infrastructural"
            ],
            "tagged_values": {
                "Web Application": "Nginx",
                "Port": 80
            }
        },
        {
            "name": "zookeeper",
            "stereotypes": [
                "configuration_server",
                "infrastructural"
            ],
            "tagged_values": {
                "Configuration Server": "ZooKeeper",
                "Port": 2181
            }
        },
        {
            "name": "jmx_monitoring",
            "stereotypes": [
                "internal"
            ],
            "tagged_values": {}
        },
        {
            "name": "todo_infra",
            "stereotypes": [
                "internal"
            ],
            "tagged_values": {}
        }
    ],
    "information_flows": [
        {
            "sender": "admin",
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
            "sender": "eureka_server",
            "receiver": "admin",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "admin",
            "receiver": "user_service",
            "stereotypes": [
                "restful_http"
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
            "sender": "admin",
            "receiver": "mailer",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "config_server",
            "receiver": "mailer",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "mailer",
            "receiver": "eureka_server",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "kafka",
            "receiver": "mailer",
            "stereotypes": [
                "restful_http",
                "message_consumer_kafka"
            ],
            "tagged_values": {
                "'Consumer Topic'": "\"todo-mail\""
            }
        },
        {
            "sender": "reminder",
            "receiver": "eureka_server",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "admin",
            "receiver": "reminder",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "config_server",
            "receiver": "reminder",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "reminder",
            "receiver": "kafka",
            "stereotypes": [
                "restful_http",
                "message_producer_kafka"
            ],
            "tagged_values": {
                "'Producer Topic'": "\"todo-mail\""
            }
        },
        {
            "sender": "eureka_server",
            "receiver": "api_gateway",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "admin",
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
                "load_balanced_link",
                "feign_connection"
            ],
            "tagged_values": {
                "'Load Balancer'": "\"Ribbon\""
            }
        },
        {
            "sender": "config_server",
            "receiver": "oauth",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "oauth",
            "receiver": "user_service",
            "stereotypes": [
                "restful_http",
                "auth_provider",
                "load_balanced_link",
                "feign_connection"
            ],
            "tagged_values": {
                "'Load Balancer'": "\"Ribbon\""
            }
        },
        {
            "sender": "oauth",
            "receiver": "eureka_server",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "admin",
            "receiver": "oauth",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "user",
            "receiver": "proxy",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "proxy",
            "receiver": "user",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "proxy",
            "receiver": "api_gateway",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "zookeeper",
            "receiver": "kafka",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "proxy",
            "receiver": "logstash",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "user_service",
            "receiver": "logstash",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "reminder",
            "receiver": "logstash",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "eureka_server",
            "receiver": "logstash",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "api_gateway",
            "receiver": "logstash",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "oauth",
            "receiver": "logstash",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "admin",
            "receiver": "logstash",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "config_server",
            "receiver": "logstash",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "mailer",
            "receiver": "logstash",
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
        },
        {
            "name": "logstash",
            "stereotypes": [
                "logging_server",
                "exitpoint"
            ],
            "tagged_values": {
                "Logging Server": "Logstash",
                "Port": 5044
            }
        }
    ]
}
```

### Model Items

The Application consists of 149 elements:

Element | Count
-- | --
Services | 13
External Entities | 2
Information Flows | 34
Annotations | 100
Total Items | 149

### Model Representations {#representations}

Open the model in the following formats:

- [JSON model](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/apssouza22_java-microservice/apssouza22_java-microservice.json)
- [PlantUML description](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/apssouza22_java-microservice/apssouza22_java-microservice.txt)
- [PNG graph](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/apssouza22_java-microservice/apssouza22_java-microservice.png)
- [CodeableModels](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/apssouza22_java-microservice/apssouza22_java-microservice.py)

### Traceability

Open the traceability information for all model items:

- [Traceability](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/apssouza22_java-microservice/apssouza22_java-microservice_traceability.json)

## Security Rules

The following table shows the application's adherence to the 17 architectural security rules. The last column provides model variants that adhere to the rule for each rule that is initially violated.

Rule ID &nbsp;&nbsp;| Verdict &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| Evidence &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| Model Variant &nbsp;&nbsp;&nbsp;|
-- | -- | -- | -- |
**R1** | <i class="fa fa-warning" style="color: #bfc600;"> | <a href="#rule01">Evidence |  |
**R2** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule02">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/apssouza22_java-microservice/model_variants/2.txt) |
**R3** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule03">Evidence |  |
**R4** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule04">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/apssouza22_java-microservice/model_variants/4.txt) |
**R5** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule05">Evidence |  |
**R6** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule06">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/apssouza22_java-microservice/model_variants/6.txt) |
**R7** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule07">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/apssouza22_java-microservice/model_variants/7.txt) |
**R8** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule08">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/apssouza22_java-microservice/model_variants/8.txt) |
**R9** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule09">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/apssouza22_java-microservice/model_variants/9.txt) |
**R10** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule10">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/apssouza22_java-microservice/model_variants/10.txt) |
**R11** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule11">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/apssouza22_java-microservice/model_variants/11.txt) |
**R12** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule12">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/apssouza22_java-microservice/model_variants/12.txt) |
**R13** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule13">Evidence |  |
**R14** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule14">Evidence |  |
**R16** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule16">Evidence |  |
**R17** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule17">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/apssouza22_java-microservice/model_variants/17.txt) |
**R18** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule18">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/apssouza22_java-microservice/model_variants/18.txt) |



### Evidence and explanations for rule decisions


#### R1 {#rule01}

Rule is partially adhered to:
1. API-Gateway provided by @EnableFeignClients and the annotated @FeignClients,
1. No single-entry point as separate access to auth-server as defined in README.md authentication/retrieving token process uses two different ports (8017 is auth server, 8018 is api gateway),
1. authorizes with @EnableResourceServer annotation

Artifacts:
- BasicApplication.java: Line: [8](https://github.com/apssouza22/java-microservice/blob/master/api-gateway/src/main/java/com/apssouza/BasicApplication.java#L8)
- TodoClient.java: Line: [16](https://github.com/apssouza22/java-microservice/blob/master/api-gateway/src/main/java/com/apssouza/clients/TodoClient.java#L16)
- UserClient.java: Line: [16](https://github.com/apssouza22/java-microservice/blob/master/api-gateway/src/main/java/com/apssouza/clients/UserClient.java#L16)
- oauth.properties: Line: [1](https://github.com/apssouza22/java-microservice/blob/master/config-server/src/main/resources/offline-repository/oauth.properties#L1)
- api-gateway.properties: Line: [1](https://github.com/apssouza22/java-microservice/blob/master/config-server/src/main/resources/offline-repository/api-gateway.properties#L1)
- OAuth2ResourceServerConfiguration.java: Line: [19](https://github.com/apssouza22/java-microservice/blob/master/api-gateway/src/main/java/com/apssouza/configuration/OAuth2ResourceServerConfiguration.java#L19)

#### R2  {#rule02}

Rule is violated:
1. Gateway does authorize per @EnableResourceServer annotation,
1. Downstream services do not include annotation anywhere

Artifacts:
- OAuth2ResourceServerConfiguration.java: Line: [19](https://github.com/apssouza22/java-microservice/blob/master/api-gateway/src/main/java/com/apssouza/configuration/OAuth2ResourceServerConfiguration.java#L19)

#### R3 {#rule03}

Rule is adhered to:
1. The @EnableAuthorizationServer annotation is present,
1. JWT as tokens as JwtAuthenticationConverter at the authorization server function present,
1. JWTs are validated by Gateway as JwtAuthenticationConverter includes insertion of public key and @EnableResourceServer annotation. Thus decoupled from the auth server.

Artifacts:
- OAuth2ServerConfiguration.java: Line: [24](https://github.com/apssouza22/java-microservice/blob/master/oauth-server/src/main/java/com/apssouza/configuration/OAuth2ServerConfiguration.java#L24)
- JwtServerConfiguration.java: Line: [27](https://github.com/apssouza22/java-microservice/blob/master/oauth-server/src/main/java/com/apssouza/configuration/JwtServerConfiguration.java#L27)
- OAuth2ResourceServerConfiguration.java: Line: [19](https://github.com/apssouza22/java-microservice/blob/master/api-gateway/src/main/java/com/apssouza/configuration/OAuth2ResourceServerConfiguration.java#L19)
- JwtConfiguration.java: Line: [35](https://github.com/apssouza22/java-microservice/blob/master/api-gateway/src/main/java/com/apssouza/configuration/JwtConfiguration.java#L35)

#### R4 {#rule04}

Rule is violated: Identity representations are not used for all levels of authorization and authentication as only API Gateway authorizes and does not get transformed. See Rule 2 arguments.

#### R5 {#rule05}

Rule is adhered to: Tokens are validated at the API Gateway per annotation and public key inserted at JwtAuthenticationConverter.

#### R6 {#rule06}

Rule is violated: There is no functionality present that enforcecs any consequences for a specific amount of failed login attempts



#### R7 {#rule07}

Rule is violated: There are no certificates in the repository and no "server.ssl.key-store"/"server.ssl.trust-store" arguments inserted in the yml of the API gateway

Artifacts:
- api-gateway.properties: Line: [1](https://github.com/apssouza22/java-microservice/blob/master/config-server/src/main/resources/offline-repository/api-gateway.properties#L1)

#### R8 {#rule08}

Rule is violated: See Rule 7 comment, but the arguments are not existent in any other yml configuration



#### R9 {#rule09}

Rule is adhered to: This microservice application deploys the ELK stack (Elasticsearch, Logstash, Kibana) as a logging mechanism. Logstash is deployed as a central logging subsystem. Logstash then sends the formatted data to an Elasticsearch indexing server. Additionally Kibana is deployed as a monitoring dashboard on top of the indexing server.

Artifacts:
- infra-docker-compose.yml: Line: [4](https://github.com/apssouza22/java-microservice/blob/master/assets/infra-docker-compose.yml#L4)

#### R10 {#rule10}

Rule is adhered to:
1. Beats configuration in each service that specifies the ElasticSearch container,
1. Dockerfile that installs beats with said configuration,
1. then starts own service in Dockerfile

Artifacts:
- filebeat.yml: Line: [2](https://github.com/apssouza22/java-microservice/blob/master/config-server/src/main/resources/docker/filebeat.yml#L2)
- Dockerfile: Lines: [25](https://github.com/apssouza22/java-microservice/blob/master/eureka-server/src/main/resources/docker/Dockerfile#L25), [30](https://github.com/apssouza22/java-microservice/blob/master/eureka-server/src/main/resources/docker/Dockerfile#L30)
- start.sh: Line: [5](https://github.com/apssouza22/java-microservice/blob/master/eureka-server/src/main/resources/docker/start.sh#L5)

#### R11 {#rule11}

Rule is violated: No sanitization mechanism to be found, but also not needed as there is no sensitive data logged.

Artifacts:
- filebeat.yml: Line: [11](https://github.com/apssouza22/java-microservice/blob/master/proxy/filebeat.yml#L11)
- filebeat.yml: Line: [11](https://github.com/apssouza22/java-microservice/blob/master/api-gateway/src/main/resources/docker/filebeat.yml#L11)
- filebeat.yml: Line: [11](https://github.com/apssouza22/java-microservice/blob/master/mail-service/src/main/resources/docker/filebeat.yml#L11)

#### R12 {#rule12}

Rule is violated: Kafka is used as message broker, however between services and not used for the logging subsystem.

Artifacts:
- WebSocketConfig.java: Line: [11](https://github.com/apssouza22/java-microservice/blob/master/remainder-service/src/main/java/com/apssouza/configuration/WebSocketConfig.java#L11)



#### R13 {#rule13}

Rule is adhered to: Hystrix is enabled using the [@EnableHystrix](https://cloud.spring.io/spring-cloud-netflix/multi/multi_spring-cloud-feign.html#spring-cloud-feign-hystrix) annotation for any routes retrieved by integrated Load balancer from Feign which is Ribbon.

Artifacts:
- BasicApplication.java: Line: [10](https://github.com/apssouza22/java-microservice/blob/master/api-gateway/src/main/java/com/apssouza/BasicApplication.java#L10)

#### R14 {#rule14}

Rule is adhered to: The gateway automatically performs load balancing [using Ribbon](https://cloud.spring.io/spring-cloud-netflix/multi/multi_spring-cloud-feign.html#netflix-feign-starter) integrated into Feign clients.

Artifacts:
- BasicApplication.java: Line: [9](https://github.com/apssouza22/java-microservice/blob/master/api-gateway/src/main/java/com/apssouza/BasicApplication.java#L9)

#### R15 {#rule15}

This rule is not applicable: Not a service mesh deployment.



#### R16 {#rule16}

Rule is adhered to:
1. Registry Service (Eureka) present with @EnableEurekaServer
1. Starting the Eureka Server via Docker-Compose -> Deployment on dedicated server possible

Artifacts:
- Application.java: Line: [8](https://github.com/apssouza22/java-microservice/blob/master/eureka-server/src/main/java/com/apssouza/discovery/Application.java#L8)
- docker-compose.yml: Line: [16](https://github.com/apssouza22/java-microservice/blob/master/docker-compose.yml#L16)

#### R17 {#rule17}

Rule violated: There is no [HTTP basic password](https://cloud.spring.io/spring-cloud-netflix/reference/html/#authenticating-with-the-eureka-server) password listed in any YML-Configuration of format username:password@here-location-of-eureka-server at "eureka.client.serviceUrl.defaultZone".

Artifacts:
- api-gateway.properties: Line: [3](https://github.com/apssouza22/java-microservice/blob/master/config-server/src/main/resources/offline-repository/api-gateway.properties#L3)



#### R18 {#rule18}

Rule is violated: No secret manager is deployed.
