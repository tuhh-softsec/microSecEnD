---
title: callistaenterprise/blog-microservices
keywords: model
tags: [docker_compose, elasticsearch, eureka, gradle, hystrix, kibana, logstash, rabbitmq, ribbon, spring_config, spring_oauth, turbine, zipkin, zuul]
sidebar: datasetdoc_sidebar
permalink: callistaenterprise_blog-microservices.html
toc: false
---

## General Information

The repository for this application ([open on GitHub](https://github.com/callistaenterprise/blog-microservices)) has 398 stars and was forked 308 times. The codebase consists of 2786 lines of code and makes use of the following technologies:

<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_docker_compose.html">Docker Compose</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_elasticsearch.html">Elasticsearch</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_eureka.html">Eureka</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_gradle.html">Gradle</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_hystrix.html">Hystrix</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_kibana.html">Kibana</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_logstash.html">Logstash</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_rabbitmq.html">RabbitMQ</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_ribbon.html">Ribbon</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_spring_config.html">Spring Config</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_spring_oauth.html">Spring OAuth</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_turbine.html">Turbine</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_zipkin.html">Zipkin</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_zuul.html">Zuul</a>

## Data Flow Diagram

![Dataflow Diagram](./callistaenterprise_blog-microservices.png)

Download the following model file [here](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/callistaenterprise_blog-microservices/callistaenterprise_blog-microservices.json).
Other formats are provided below.

```json
{
    "services": [
        {
            "name": "elasticsearch",
            "stereotypes": [
                "infrastructural",
                "search_engine"
            ],
            "tagged_values": {
                "Port": 9200,
                "Search Engine": "Elasticsearch"
            }
        },
        {
            "name": "kibana",
            "stereotypes": [
                "infrastructural",
                "monitoring_dashboard"
            ],
            "tagged_values": {
                "Port": 5601,
                "Monitoring Dashboard": "Kibana"
            }
        },
        {
            "name": "logstash",
            "stereotypes": [
                "infrastructural",
                "logging_server"
            ],
            "tagged_values": {
                "Port": 25826,
                "Logging Server": "Logstash"
            }
        },
        {
            "name": "rabbitmq",
            "stereotypes": [
                "infrastructural",
                "message_broker"
            ],
            "tagged_values": {
                "Port": 15672,
                "Message Broker": "RabbitMQ"
            }
        },
        {
            "name": "discovery_server",
            "stereotypes": [
                "infrastructural",
                "service_discovery",
                "plaintext_credentials"
            ],
            "tagged_values": {
                "Port": 8762,
                "Service Discovery": "Eureka",
                "Username": "user",
                "Password": "password"
            }
        },
        {
            "name": "config_server",
            "stereotypes": [
                "infrastructural",
                "configuration_server",
                "local_logging"
            ],
            "tagged_values": {
                "Port": 8888,
                "Configuration Server": "Spring Cloud Config"
            }
        },
        {
            "name": "auth_server",
            "stereotypes": [
                "infrastructural",
                "authorization_server",
                "resource_server",
                "local_logging",
                "plaintext_credentials"
            ],
            "tagged_values": {
                "Port": 9999,
                "Authorization Server": "Spring OAuth2",
                "Endpoints": [
                    "/user"
                ],
                "Username": "acme",
                "Password": "acmesecret"
            }
        },
        {
            "name": "monitor_dashboard",
            "stereotypes": [
                "infrastructural",
                "monitoring_dashboard",
                "local_logging"
            ],
            "tagged_values": {
                "Port": 7979,
                "Monitoring Dashboard": "Hystrix",
                "Endpoints": [
                    "/"
                ]
            }
        },
        {
            "name": "turbine_server",
            "stereotypes": [
                "infrastructural",
                "monitoring_server",
                "local_logging"
            ],
            "tagged_values": {
                "Port": 8989,
                "Monitoring Server": "Turbine"
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
            "name": "product_service",
            "stereotypes": [
                "internal",
                "local_logging"
            ],
            "tagged_values": {
                "Port": 8080,
                "Endpoints": [
                    "/product/{productId}",
                    "/set-processing-time"
                ]
            }
        },
        {
            "name": "recommendation_service",
            "stereotypes": [
                "internal",
                "local_logging"
            ],
            "tagged_values": {
                "Port": 8080,
                "Endpoints": [
                    "/recommendation",
                    "/set-processing-time"
                ]
            }
        },
        {
            "name": "review_service",
            "stereotypes": [
                "internal",
                "local_logging"
            ],
            "tagged_values": {
                "Port": 8080,
                "Endpoints": [
                    "/review",
                    "/set-processing-time"
                ]
            }
        },
        {
            "name": "composite_service",
            "stereotypes": [
                "internal",
                "local_logging",
                "load_balancer",
                "circuit_breaker",
                "resource_server"
            ],
            "tagged_values": {
                "Port": 8080,
                "Endpoints": [
                    "/",
                    "/{productId}"
                ],
                "Load Balancer": "Spring Cloud"
            }
        },
        {
            "name": "edge_server",
            "stereotypes": [
                "infrastructural",
                "gateway",
                "resource_server",
                "local_logging",
                "circuit_breaker",
                "load_balancer"
            ],
            "tagged_values": {
                "Port": 8765,
                "Gateway": "Zuul",
                "Load Balancer": "Ribbon"
            }
        }
    ],
    "information_flows": [
        {
            "sender": "elasticsearch",
            "receiver": "kibana",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "logstash",
            "receiver": "elasticsearch",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
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
            "sender": "config_server",
            "receiver": "rabbitmq",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "config_server",
            "receiver": "auth_server",
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
            "sender": "monitor_dashboard",
            "receiver": "discovery_server",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "rabbitmq",
            "receiver": "turbine_server",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "turbine_server",
            "receiver": "discovery_server",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "config_server",
            "receiver": "turbine_server",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "turbine_server",
            "receiver": "monitor_dashboard",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "rabbitmq",
            "receiver": "zipkin_server",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "config_server",
            "receiver": "product_service",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "product_service",
            "receiver": "discovery_server",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "config_server",
            "receiver": "recommendation_service",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "recommendation_service",
            "receiver": "discovery_server",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "config_server",
            "receiver": "review_service",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "review_service",
            "receiver": "discovery_server",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "config_server",
            "receiver": "composite_service",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "auth_server",
            "receiver": "composite_service",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "composite_service",
            "receiver": "discovery_server",
            "stereotypes": [
                "restful_http",
                "circuit_breaker_link",
                "load_balanced_link"
            ],
            "tagged_values": {}
        },
        {
            "sender": "composite_service",
            "receiver": "rabbitmq",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "composite_service",
            "receiver": "product_service",
            "stereotypes": [
                "restful_http",
                "load_balanced_link"
            ],
            "tagged_values": {}
        },
        {
            "sender": "composite_service",
            "receiver": "recommendation_service",
            "stereotypes": [
                "restful_http",
                "load_balanced_link"
            ],
            "tagged_values": {}
        },
        {
            "sender": "composite_service",
            "receiver": "review_service",
            "stereotypes": [
                "restful_http",
                "load_balanced_link"
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
            "sender": "user",
            "receiver": "edge_server",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "edge_server",
            "receiver": "composite_service",
            "stereotypes": [
                "restful_http",
                "circuit_breaker_link"
            ],
            "tagged_values": {}
        },
        {
            "sender": "discovery_server",
            "receiver": "edge_server",
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
            "receiver": "auth_server",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "discovery_server",
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
            "sender": "auth_server",
            "receiver": "logstash",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "product_service",
            "receiver": "logstash",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "recommendation_service",
            "receiver": "logstash",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "review_service",
            "receiver": "logstash",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "composite_service",
            "receiver": "logstash",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "monitor_dashboard",
            "receiver": "logstash",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "edge_server",
            "receiver": "logstash",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "zipkin_server",
            "receiver": "logstash",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
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
                "URL": "https://github.com/callistaenterprise/blog-microservices-config"
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

The Application consists of a total of 175 elements:

Element | Count
-- | --
Services | 15
External Entities | 2
Information Flows | 32
Annotations | 126
Total Items | 175

### Model Representations {#representations}

Open the model in the following formats:

- [JSON model](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/callistaenterprise_blog-microservices/callistaenterprise_blog-microservices.json)
- [PlantUML description](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/callistaenterprise_blog-microservices/callistaenterprise_blog-microservices.txt)
- [PNG graph](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/callistaenterprise_blog-microservices/callistaenterprise_blog-microservices.png)
- [CodeableModels](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/callistaenterprise_blog-microservices/callistaenterprise_blog-microservices.py)

### Traceability

Open the traceability information for all model items:

- [Traceability](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/callistaenterprise_blog-microservices/callistaenterprise_blog-microservices_traceability.json)

## Security Rules

The following table shows the application's adherence to the 17 architectural security rules. The last column provides model variants that adhere to the rule for each rule that is initially violated.

Rule ID &nbsp;&nbsp;| Verdict &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| Evidence &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| Model Variant &nbsp;&nbsp;&nbsp;|
-- | -- | -- | -- |
**R1** | <i class="fa fa-warning" style="color: #bfc600;"> | <a href="#rule01">Evidence |  |
**R2** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule02">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/callistaenterprise_blog-microservices/model_variants/2.txt) |
**R3** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule03">Evidence |  |
**R4** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule04">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/callistaenterprise_blog-microservices/model_variants/4.txt) |
**R5** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule05">Evidence |  |
**R6** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule06">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/callistaenterprise_blog-microservices/model_variants/6.txt) |
**R7** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule07">Evidence |  |
**R8** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule08">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/callistaenterprise_blog-microservices/model_variants/8.txt) |
**R9** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule09">Evidence |  |
**R10** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule10">Evidence |  |
**R11** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule11">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/callistaenterprise_blog-microservices/model_variants/11.txt) |
**R12** |  <i class="fa fa-exclamation-circle" style="color: #d72b28;">  | <a href="#rule12">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/callistaenterprise_blog-microservices/model_variants/17.txt) |  |
**R13** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule13">Evidence |  |
**R14** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule14">Evidence |  |
**R16** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule16">Evidence |  |
**R17** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule17">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/callistaenterprise_blog-microservices/model_variants/17.txt) |
**R18** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule18">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/callistaenterprise_blog-microservices/model_variants/18.txt) |



### Evidence and explanations for rule decisions

#### R1 {#rule01}

Rule is partially adhered to:
1. The @EnableZuulProxy annotation is present,
1. The @EnableResourceServer annotation is present,
1. Article of application does access authorization server directly instead over Gateway.

Artifacts:
- ZuulApplication.java: Line: [18](https://github.com/callistaenterprise/blog-microservices/blob/master/microservices/support/edge-server/src/main/java/se/callista/microservises/support/edge/ZuulApplication.java#L18)

#### R2  {#rule02}

Rule is violated: Only API gateway, product composite service and authorization server (which is accesses by other services) have @EnableResourceServer, other downstream services do not authorize the requests

Artifacts:
- AuthserverApplication.java: Line: [16](https://github.com/callistaenterprise/blog-microservices/blob/master/microservices/support/auth-server/src/main/java/se/callista/microservises/support/oauth/AuthserverApplication.java#L16)
- ZuulApplication.java: Line: [19](https://github.com/callistaenterprise/blog-microservices/blob/master/microservices/support/edge-server/src/main/java/se/callista/microservises/support/edge/ZuulApplication.java#L19)
- ProductCompositeServiceApplication.java: Line: [21](https://github.com/callistaenterprise/blog-microservices/blob/master/microservices/composite/product-composite-service/src/main/java/se/callista/microservices/composite/product/ProductCompositeServiceApplication.java#L21)

#### R3 {#rule03}

This rule is adhered to:
1. The @EnableAuthorizationServer annotation is present,
1. No JwtAccessTokenConverter, thus issues opaque token,
1. Endpoint for validating token present,
1. Endpoint mentioned at YML-Configuration of Resource Server.

Artifacts:
- AuthserverApplication.java: Line: [17](https://github.com/callistaenterprise/blog-microservices/blob/master/microservices/support/auth-server/src/main/java/se/callista/microservises/support/oauth/AuthserverApplication.java#L17)
- edge-server.yml: Line: [15](https://github.com/callistaenterprise/blog-microservices-config/blob/master/edge-server.yml#L15)

#### R4 {#rule04}

Rule is violated:
1. Identity representations are present in form of opaque tokens per Rule 3,
1. No transformation present,
1. No @EnableResourceServer present at every downstream service.

#### R5 {#rule05}

Rule is adhered to: Token are being validated on endpoint at authorization server and endpoint specified at server with @EnableResourceServer annotation.

#### R6 {#rule06}

Rule is violated: No mechanism in place for multiple failed login attempts.



#### R7 {#rule07}

Rule is adhered to: Keystore and Truststore of API Gateway has certificate included.

Artifacts:
- edge-server.yml: Line: [4](https://github.com/callistaenterprise/blog-microservices-config/blob/master/edge-server.yml#L4)

#### R8 {#rule08}

This rule is violated: Only edge-server, auth-server and config service have keystores included in their yml-configuration.

Artifacts:
- auth-server.yml: Line: [5](https://github.com/callistaenterprise/blog-microservices-config/blob/master/auth-server.yml#L5)
- edge-server.yml: Line: [4](https://github.com/callistaenterprise/blog-microservices-config/blob/master/edge-server.yml#L4)
- application.yml: Line: [3](https://github.com/callistaenterprise/blog-microservices/blob/master/microservices/support/config-server/src/main/resources/application.yml#L3)



#### R9 {#rule09}

Rule is adhered to: This microservice application deploys the ELK stack (Elasticsearch, Logstash, Kibana) as a logging mechanism. Logstash is deployed as a central logging subsystem. Logstash then sends the formatted data to an Elasticsearch indexing server. Additionally Kibana is deployed as a monitoring dashboard on top of the indexing server.

Artifacts:
- docker-compose-with-elk.yml: Line: [5](https://github.com/callistaenterprise/blog-microservices/blob/master/docker-compose-with-elk.yml#L5)

#### R10 {#rule10}

Rule is adhered to: The syslog driver at docker containers present.

Artifacts:
- docker-compose-with-elk.yml: Line: [81](https://github.com/callistaenterprise/blog-microservices/blob/master/docker-compose-with-elk.yml#L81)

#### R11 {#rule11}

Rule is violated: Logs are not explicitly sanitized.

#### R12 {#rule12}

Rule is violated: RabbitMQ present but not used for logging subsystem.



#### R13 {#rule13}

Rule is adhered to: The [@EnableZuulProxy](https://cloud.spring.io/spring-cloud-netflix/multi/multi__router_and_filter_zuul.html#netflix-zuul-reverse-proxy) annotation at the API Gateway enables Hystrix and its circuit breaker functionality.

Artifacts:
- ZuulApplication.java: Line: [18](https://github.com/callistaenterprise/blog-microservices/blob/master/microservices/support/edge-server/src/main/java/se/callista/microservises/support/edge/ZuulApplication.java#L18)

#### R14 {#rule14}

Rule is adhered to: The [@EnableZuulProxy](https://cloud.spring.io/spring-cloud-netflix/multi/multi__router_and_filter_zuul.html#netflix-zuul-reverse-proxy) annotation at the API Gateway enables Ribbon and its load balancing functionality.

Artifacts:
- ZuulApplication.java: Line: [18](https://github.com/callistaenterprise/blog-microservices/blob/master/microservices/support/edge-server/src/main/java/se/callista/microservises/support/edge/ZuulApplication.java#L18)

#### R15 {#rule15}

This rule is not applicable: Not a service mesh deployment.



#### R16 {#rule16}

Rule is adhered to:
1. Registry Service (Eureka Server) with @EnableEurekaServer present.
1. Started in Docker Container through Compose, thus deployable on dedicated server

Artifacts:
- EurekaApplication.java: Line: [9](https://github.com/callistaenterprise/blog-microservices/blob/master/microservices/support/discovery-server/src/main/java/se/callista/microservises/support/discovery/EurekaApplication.java#L9)
- docker-compose-with-elk.yml: Line: [51](https://github.com/callistaenterprise/blog-microservices/blob/master/docker-compose-with-elk.yml#L51)

#### R17 {#rule17}

Rule is violated: No [HTTP basic password](https://cloud.spring.io/spring-cloud-netflix/reference/html/#authenticating-with-the-eureka-server)  listed in any YML-Configuration of format username:password@here-location-of-eureka-server at "eureka.client.serviceUrl.defaultZone".

Artifacts:
- EurekaApplication.java: Line: [9](https://github.com/callistaenterprise/blog-microservices/blob/master/microservices/support/discovery-server/src/main/java/se/callista/microservises/support/discovery/EurekaApplication.java#L9)
- edge-server.yml: Line: [45](https://github.com/callistaenterprise/blog-microservices-config/blob/master/edge-server.yml#L45)



#### R18 {#rule18}

Rule is violated: No secret manager is deployed.
