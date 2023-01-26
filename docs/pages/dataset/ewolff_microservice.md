---
title: ewolff/microservice
keywords: model
tags: [eureka, hystrix, maven, ribbon, turbine, zuul]
sidebar: datasetdoc_sidebar
permalink: ewolff_microservice.html
toc: false
---

## General Information

The repository for this application ([open on GitHub](https://github.com/ewolff/microservice)) has 666 stars and was forked 333 times. The codebase consists of 3117 lines of code and makes use of the following technologies:

<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_eureka.html">Eureka</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_hystrix.html">Hystrix</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_maven.html">Maven</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_ribbon.html">Ribbon</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_turbine.html">Turbine</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_zuul.html">Zuul</a>

## Data Flow Diagram

![Dataflow Diagram](./ewolff_microservice.png)

Download the following model file [here](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/ewolff_microservice/ewolff_microservice.json).
Other formats are provided below.

```json
{
    "services": [
        {
            "name": "eureka",
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
            "name": "zuul",
            "stereotypes": [
                "gateway",
                "load_balancer",
                "infrastructural"
            ],
            "tagged_values": {
                "Gateway": "Zuul",
                "Load Balancer": "Ribbon",
                "Port": 8080
            }
        },
        {
            "name": "turbine",
            "stereotypes": [
                "monitoring_server",
                "monitoring_dashboard",
                "infrastructural"
            ],
            "tagged_values": {
                "Monitoring Server": "Turbine",
                "Monitoring Dashboard": "Hystrix",
                "Port": 8989
            }
        },
        {
            "name": "catalog",
            "stereotypes": [
                "internal"
            ],
            "tagged_values": {
                "Port": 8080,
                "Endpoints": [
                    "/catalog",
                    "/{id}.html",
                    "/list.html",
                    "/form.html",
                    "/searchForm.html",
                    "/searchByName.html"
                ]
            }
        },
        {
            "name": "customer",
            "stereotypes": [
                "internal"
            ],
            "tagged_values": {
                "Port": 8080,
                "Endpoints": [
                    "/form.html",
                    "/list.html",
                    "/{id}.html",
                    "/customer"
                ]
            }
        },
        {
            "name": "order",
            "stereotypes": [
                "internal",
                "load_balancer",
                "circuit_breaker",
                "local_logging"
            ],
            "tagged_values": {
                "Load Balancer": "Ribbon",
                "Circuit Breaker": "Hystrix",
                "Port": 8080,
                "Endpoints": [
                    "/",
                    "/form.html",
                    "/{id}",
                    "/line",
                    "/order"
                ]
            }
        }
    ],
    "information_flows": [
        {
            "sender": "eureka",
            "receiver": "zuul",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "user",
            "receiver": "zuul",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "zuul",
            "receiver": "user",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "turbine",
            "receiver": "eureka",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "catalog",
            "receiver": "eureka",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "customer",
            "receiver": "eureka",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "order",
            "receiver": "eureka",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "order",
            "receiver": "catalog",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "order",
            "receiver": "customer",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "order",
            "receiver": "turbine",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "zuul",
            "receiver": "customer",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "zuul",
            "receiver": "catalog",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "zuul",
            "receiver": "order",
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
        }
    ]
}
```

### Model Items

The Application consists of a total of 66 elements:

Element | Count
-- | --
Services | 6
External Entities | 1
Information Flows | 13
Annotations | 46
Total Items | 66

### Model Representations {#representations}

Open the model in the following formats:

- [JSON model](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/ewolff_microservice/ewolff_microservice.json)
- [PlantUML description](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/ewolff_microservice/ewolff_microservice.txt)
- [PNG graph](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/ewolff_microservice/ewolff_microservice.png)
- [CodeableModels](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/ewolff_microservice/ewolff_microservice.py)

### Traceability

Open the traceability information for all model items:

- [Traceability](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/ewolff_microservice/ewolff_microservice_traceability.json)

## Security Rules

The following table shows the application's adherence to the 17 architectural security rules. The last column provides model variants that adhere to the rule for each rule that is initially violated.

Rule ID &nbsp;&nbsp;| Verdict &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| Evidence &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| Model Variant &nbsp;&nbsp;&nbsp;|
-- | -- | -- | -- |
**R1** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule01">Evidence |  |
**R2** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule02">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/ewolff_microservice/model_variants/2.txt) |
**R3** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule03">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/ewolff_microservice/model_variants/3.txt) |
**R4** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule04">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/ewolff_microservice/model_variants/4.txt) |
**R5** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule05">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/ewolff_microservice/model_variants/5.txt) |
**R6** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule06">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/ewolff_microservice/model_variants/6.txt) |
**R7** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule07">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/ewolff_microservice/model_variants/7.txt) |
**R8** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule08">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/ewolff_microservice/model_variants/8.txt) |
**R9** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule09">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/ewolff_microservice/model_variants/9.txt) |
**R10** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule10">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/ewolff_microservice/model_variants/10.txt) |
**R11** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule11">Evidence |  |
**R12** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule12">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/ewolff_microservice/model_variants/12.txt) |
**R13** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule13">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/ewolff_microservice/model_variants/13.txt) |
**R14** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule14">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/ewolff_microservice/model_variants/14.txt) |
**R16** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule16">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/ewolff_microservice/model_variants/16.txt) |
**R17** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule17">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/ewolff_microservice/model_variants/17.txt) |
**R18** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule18">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/ewolff_microservice/model_variants/18.txt) |



### Evidence and explanations for rule decisions

#### R1 {#rule01}

Rule is adhered to:
1. The @EnableZuulProxy annotation is present,
1. No Authorization Server present
1. No Resource Server present

Artifacts:
- ZuulApplication.java: Line: [8](https://github.com/ewolff/microservice/blob/master/microservice-demo/microservice-demo-zuul-server/src/main/java/com/ewolff/microservice/zuulserver/ZuulApplication.java#L8)

#### R2  {#rule02}

Rule is violated: No authorization or authentication present due to no authorization

#### R3 {#rule03}

Rule is violated: See rule 2.

#### R4 {#rule04}

Rule is violated: See rule 2.

#### R5 {#rule05}

Rule is violated: See rule 2.

#### R6 {#rule06}

Rule is violated: See rule 2.



#### R7 {#rule07}

Rule is violated: No mention of SSL, TLS, keystores or trust-stores in application.

#### R8 {#rule08}

Rule is violated: See rule 7.



#### R9 {#rule09}

Rule is violated: No central logging system is deployed.

#### R10 {#rule10}

Rule is violated: See rule 9.

#### R11 {#rule11}

Rule is violated: See rule 9.

#### R12 {#rule12}

Rule is violated: See rule 9.



#### R13 {#rule13}

Rule is adhered to: The @EnableZuulProxy annotation enables Hystrix and its circuit breaker functionality.

Artifacts:
- ZuulApplication.java: Line: [9](https://github.com/ewolff/microservice/blob/master/microservice-demo/microservice-demo-zuul-server/src/main/java/com/ewolff/microservice/zuulserver/ZuulApplication.java#L9)

#### R14 {#rule14}

Rule is adhered to: The @EnableZuulProxy annotation enables Ribbon and its load balancing functionality.

Artifacts:
- ZuulApplication.java: Line: [9](https://github.com/ewolff/microservice/blob/master/microservice-demo/microservice-demo-zuul-server/src/main/java/com/ewolff/microservice/zuulserver/ZuulApplication.java#L9)

#### R15 {#rule15}

This rule is not applicable: Not a service mesh deployment.



#### R16 {#rule16}

Rule is adhered to:
1. Registry Service (Eureka Server) with @EnableEurekaServer present.
1. Started in Docker Container through Compose, thus deployable on dedicated server

Artifacts:
- EurekaApplication.java: Line: [8](https://github.com/ewolff/microservice/blob/master/microservice-demo/microservice-demo-eureka-server/src/main/java/com/ewolff/microservice/eurekaserver/EurekaApplication.java#L8)
- docker-compose.yml: Line: [3](https://github.com/ewolff/microservice/blob/master/docker/docker-compose.yml#L3)

#### R17 {#rule17}

Rule is violated: No HTTP basic password listed in any YML-Configuration of format username:password@here-location-of-eureka-server at "eureka.client.serviceUrl.defaultZone".

Artifacts:
- application.properties: Line: [6](https://github.com/ewolff/microservice/blob/master/microservice-demo/microservice-demo-order/src/main/resources/application.properties#L6)



#### R18 {#rule18}

Rule is violated: No secret manager is deployed.
