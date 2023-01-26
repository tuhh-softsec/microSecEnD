---
title: georgwittberger/apache-spring-boot-microservice-example
keywords: model
tags: [apache_httpd, maven]
sidebar: datasetdoc_sidebar
permalink: georgwittberger_apache-spring-boot-microservice-example.html
toc: false
---

## General Information

The repository for this application ([open on GitHub](https://github.com/georgwittberger/apache-spring-boot-microservice-example)) has 7 stars and was forked 9 times. The codebase consists of 604 lines of code and makes use of the following technologies:

<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_apache_httpd.html">Apache httpd</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_maven.html">Maven</a>

## Data Flow Diagram

![Dataflow Diagram](./georgwittberger_apache-spring-boot-microservice-example.png)

Download the following model file [here](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/georgwittberger_apache-spring-boot-microservice-example/georgwittberger_apache-spring-boot-microservice-example.json).
Other formats are provided below.

```json
{
    "services": [
        {
            "name": "apache_server",
            "stereotypes": [
                "web_server",
                "infrastructural"
            ],
            "tagged_values": {
                "Web Server": "Apache httpd"
            }
        },
        {
            "name": "content_service",
            "stereotypes": [
                "internal"
            ],
            "tagged_values": {
                "Port": 11080
            }
        },
        {
            "name": "product_service",
            "stereotypes": [
                "internal"
            ],
            "tagged_values": {
                "Port": 11081
            }
        },
        {
            "name": "cart_service",
            "stereotypes": [
                "internal"
            ],
            "tagged_values": {
                "Port": 11082
            }
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
    ],
    "information_flows": [
        {
            "sender": "user",
            "receiver": "apache_server",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "apache_server",
            "receiver": "user",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "cart_service",
            "receiver": "product_service",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "apache_server",
            "receiver": "cart_service",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "apache_server",
            "receiver": "product_service",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "apache_server",
            "receiver": "content_service",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        }
    ]
}
```

### Model Items

The Application consists of a total of 29 elements:

Element | Count
-- | --
Services | 4
External Entities | 1
Information Flows | 6
Annotations | 18
Total Items | 29

### Model Representations {#representations}

Open the model in the following formats:

- [JSON model](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/georgwittberger_apache-spring-boot-microservice-example/georgwittberger_apache-spring-boot-microservice-example.json)
- [PlantUML description](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/georgwittberger_apache-spring-boot-microservice-example/georgwittberger_apache-spring-boot-microservice-example.txt)
- [PNG graph](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/georgwittberger_apache-spring-boot-microservice-example/georgwittberger_apache-spring-boot-microservice-example.png)
- [CodeableModels](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/georgwittberger_apache-spring-boot-microservice-example/georgwittberger_apache-spring-boot-microservice-example.py)

### Traceability

Open the traceability information for all model items:

- [Traceability](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/georgwittberger_apache-spring-boot-microservice-example/georgwittberger_apache-spring-boot-microservice-example_traceability.json)

## Security Rules

The following table shows the application's adherence to the 17 architectural security rules. The last column provides model variants that adhere to the rule for each rule that is initially violated.

Rule ID &nbsp;&nbsp;| Verdict &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| Evidence &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| Model Variant &nbsp;&nbsp;&nbsp;|
-- | -- | -- | -- |
**R1** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule01">Evidence |  |
**R2** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule02">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/georgwittberger_apache-spring-boot-microservice-example/model_variants/2.txt) |
**R3** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule03">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/georgwittberger_apache-spring-boot-microservice-example/model_variants/3.txt) |
**R4** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule04">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/georgwittberger_apache-spring-boot-microservice-example/model_variants/4.txt) |
**R5** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule05">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/georgwittberger_apache-spring-boot-microservice-example/model_variants/5.txt) |
**R6** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule06">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/georgwittberger_apache-spring-boot-microservice-example/model_variants/6.txt) |
**R7** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule07">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/georgwittberger_apache-spring-boot-microservice-example/model_variants/7.txt) |
**R8** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule08">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/georgwittberger_apache-spring-boot-microservice-example/model_variants/8.txt) |
**R9** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule09">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/georgwittberger_apache-spring-boot-microservice-example/model_variants/9.txt) |
**R10** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule10">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/georgwittberger_apache-spring-boot-microservice-example/model_variants/10.txt) |
**R11** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule11">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/georgwittberger_apache-spring-boot-microservice-example/model_variants/11.txt) |
**R12** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule12">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/georgwittberger_apache-spring-boot-microservice-example/model_variants/12.txt) |
**R13** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule13">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/georgwittberger_apache-spring-boot-microservice-example/model_variants/13.txt) |
**R14** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule14">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/georgwittberger_apache-spring-boot-microservice-example/model_variants/14.txt) |
**R16** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule16">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/georgwittberger_apache-spring-boot-microservice-example/model_variants/16.txt) |
**R17** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule17">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/georgwittberger_apache-spring-boot-microservice-example/model_variants/17.txt) |
**R18** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule18">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/georgwittberger_apache-spring-boot-microservice-example/model_variants/18.txt) |



### Evidence and explanations for rule decisions

#### R1 {#rule01}

Rule is adhered to: The application uses Apache httpd as a gateway server.

Artifacts:
- httpd-microservice-example.conf: Line: [22](https://github.com/georgwittberger/apache-spring-boot-microservice-example/blob/master/apache-configuration/httpd-microservice-example.conf#L22)

#### R2  {#rule02}

Rule is violated: Services communicate internally over plain HTTP (See example artifacts). The communication is not authenticated.

Artifacts:
- httpd-microservice-example.conf: Lines: [27](https://github.com/georgwittberger/apache-spring-boot-microservice-example/blob/master/apache-configuration/httpd-microservice-example.conf#L27), [31](https://github.com/georgwittberger/apache-spring-boot-microservice-example/blob/master/apache-configuration/httpd-microservice-example.conf#L31), [35](https://github.com/georgwittberger/apache-spring-boot-microservice-example/blob/master/apache-configuration/httpd-microservice-example.conf#L35)

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
- httpd-microservice-example.conf: Line: [22](https://github.com/georgwittberger/apache-spring-boot-microservice-example/blob/master/apache-configuration/httpd-microservice-example.conf#L22)

#### R8 {#rule08}

Rule is violated: All internal services communicate over insecure HTTP connections.

Artifacts:
- application.yml: Line: [2](https://github.com/georgwittberger/apache-spring-boot-microservice-example/blob/master/cart-service/src/main/resources/application.yml#L2)
- application.yml: Line: [2](https://github.com/georgwittberger/apache-spring-boot-microservice-example/blob/master/content-service/src/main/resources/application.yml#L2)
- application.yml: Line: [2](https://github.com/georgwittberger/apache-spring-boot-microservice-example/blob/master/product-service/src/main/resources/application.yml#L2)



#### R9 {#rule09}

Rule is violated: No central logging system is deployed.

#### R10 {#rule10}

Rule is violated: No central logging system is deployed.

#### R11 {#rule11}

Rule is violated: No logs are generated by the application.

#### R12 {#rule12}

Rule is violated: No message broker is deployed and no logging is performed.



#### R13 {#rule13}

Rule is violated: No explicit circuit breaker is deployed.

#### R14 {#rule14}

Rule is violated: No load balancing is deployed.

#### R15 {#rule15}

This rule is not applicable: Not a service mesh deployment.



#### R16 {#rule16}

Rule is violated: No service registry service is deployed. Services are statically linked.

Artifacts:
- httpd-microservice-example.conf: Lines: [27](https://github.com/georgwittberger/apache-spring-boot-microservice-example/blob/master/apache-configuration/httpd-microservice-example.conf#L27), [31](https://github.com/georgwittberger/apache-spring-boot-microservice-example/blob/master/apache-configuration/httpd-microservice-example.conf#L31), [35](https://github.com/georgwittberger/apache-spring-boot-microservice-example/blob/master/apache-configuration/httpd-microservice-example.conf#L35)

#### R17 {#rule17}

Rule is violated: No service registry service is deployed. Services are statically linked.

Artifacts:
- httpd-microservice-example.conf: Lines: [27](https://github.com/georgwittberger/apache-spring-boot-microservice-example/blob/master/apache-configuration/httpd-microservice-example.conf#L27), [31](https://github.com/georgwittberger/apache-spring-boot-microservice-example/blob/master/apache-configuration/httpd-microservice-example.conf#L31), [35](https://github.com/georgwittberger/apache-spring-boot-microservice-example/blob/master/apache-configuration/httpd-microservice-example.conf#L35)



#### R18 {#rule18}

Rule is violated: No secret manager is deployed.
