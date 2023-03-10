---
title: koushikkothagal/spring-boot-microservices-workshop
keywords: model
tags: [eureka, maven]
sidebar: datasetdoc_sidebar
permalink: koushikkothagal_spring-boot-microservices-workshop.html
toc: false
---

## General Information

The repository for this application ([open on GitHub](https://github.com/koushikkothagal/spring-boot-microservices-workshop)) has 655 stars and was forked 1037 times. The codebase consists of 638 lines of code and makes use of the following technologies:

<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_eureka.html">Eureka</a>
<a class="btn btn-primary" style="margin-bottom: 5px" role="button" href="tag_maven.html">Maven</a>

## Data Flow Diagram

![Dataflow Diagram](./koushikkothagal_spring-boot-microservices-workshop.png)

Download the following model file [here](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/koushikkothagal_spring-boot-microservices-workshop/koushikkothagal_spring-boot-microservices-workshop.json).
Other formats are provided below.

```json
{
    "services": [
        {
            "name": "discovery_server",
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
            "name": "ratings_data_service",
            "stereotypes": [
                "internal"
            ],
            "tagged_values": {
                "Port": 8083,
                "Endpoints": [
                    "/ratingsdata",
                    "/ratingsdata/movies/{movieId}",
                    "/ratingsdata/user/{userId}"
                ]
            }
        },
        {
            "name": "movie_info_service",
            "stereotypes": [
                "internal"
            ],
            "tagged_values": {
                "Port": 8082,
                "Endpoints": [
                    "/movies",
                    "/movies/{movieId}"
                ]
            }
        },
        {
            "name": "movie_catalog_service",
            "stereotypes": [
                "internal",
                "load_balancer"
            ],
            "tagged_values": {
                "Port": 8081,
                "Load Balancer": "Spring Cloud",
                "Endpoints": [
                    "/catalog",
                    "/catalog/{userId}"
                ]
            }
        }
    ],
    "information_flows": [
        {
            "sender": "ratings_data_service",
            "receiver": "discovery_server",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "movie_info_service",
            "receiver": "discovery_server",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "external_website",
            "receiver": "movie_info_service",
            "stereotypes": [
                "restful_http"
            ],
            "tagged_values": {}
        },
        {
            "sender": "movie_catalog_service",
            "receiver": "discovery_server",
            "stereotypes": [
                "restful_http",
                "load_balanced_link"
            ],
            "tagged_values": {}
        },
        {
            "sender": "movie_catalog_service",
            "receiver": "ratings_data_service",
            "stereotypes": [
                "restful_http",
                "load_balanced_link"
            ],
            "tagged_values": {}
        },
        {
            "sender": "movie_catalog_service",
            "receiver": "movie_info_service",
            "stereotypes": [
                "restful_http",
                "load_balanced_link"
            ],
            "tagged_values": {}
        }
    ],
    "external_entities": [
        {
            "name": "external_website",
            "stereotypes": [
                "external_website"
            ],
            "tagged_values": {
                "URL": "https://api.themoviedb.org"
            }
        }
    ]
}
```

### Model Items

The Application consists of a total of 37 elements:

Element | Count
-- | --
Services | 4
External Entities | 1
Information Flows | 6
Annotations | 26
Total Items | 37

### Model Representations {#representations}

Open the model in the following formats:

- [JSON model](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/koushikkothagal_spring-boot-microservices-workshop/koushikkothagal_spring-boot-microservices-workshop.json)
- [PlantUML description](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/koushikkothagal_spring-boot-microservices-workshop/koushikkothagal_spring-boot-microservices-workshop.txt)
- [PNG graph](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/koushikkothagal_spring-boot-microservices-workshop/koushikkothagal_spring-boot-microservices-workshop.png)
- [CodeableModels](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/koushikkothagal_spring-boot-microservices-workshop/koushikkothagal_spring-boot-microservices-workshop.py)

### Traceability

Open the traceability information for all model items:

- [Traceability](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/koushikkothagal_spring-boot-microservices-workshop/koushikkothagal_spring-boot-microservices-workshop_traceability.json)

## Security Rules

The following table shows the application's adherence to the 17 architectural security rules. The last column provides model variants that adhere to the rule for each rule that is initially violated.

Rule ID &nbsp;&nbsp;| Verdict &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| Evidence &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| Model Variant &nbsp;&nbsp;&nbsp;|
-- | -- | -- | -- |
**R1** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule01">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/koushikkothagal_spring-boot-microservices-workshop/model_variants/1.txt) |
**R2** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule02">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/koushikkothagal_spring-boot-microservices-workshop/model_variants/2.txt) |
**R3** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule03">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/koushikkothagal_spring-boot-microservices-workshop/model_variants/3.txt) |
**R4** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule04">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/koushikkothagal_spring-boot-microservices-workshop/model_variants/4.txt) |
**R5** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule05">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/koushikkothagal_spring-boot-microservices-workshop/model_variants/5.txt) |
**R6** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule06">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/koushikkothagal_spring-boot-microservices-workshop/model_variants/6.txt) |
**R7** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule07">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/koushikkothagal_spring-boot-microservices-workshop/model_variants/7.txt) |
**R8** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule08">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/koushikkothagal_spring-boot-microservices-workshop/model_variants/8.txt) |
**R9** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule09">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/koushikkothagal_spring-boot-microservices-workshop/model_variants/9.txt) |
**R10** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule10">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/koushikkothagal_spring-boot-microservices-workshop/model_variants/10.txt) |
**R11** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule11">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/koushikkothagal_spring-boot-microservices-workshop/model_variants/11.txt) |
**R12** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule12">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/koushikkothagal_spring-boot-microservices-workshop/model_variants/12.txt) |
**R13** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule13">Evidence  | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/koushikkothagal_spring-boot-microservices-workshop/model_variants/13.txt) |
**R14** |<i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule14">Evidence  | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/koushikkothagal_spring-boot-microservices-workshop/model_variants/14.txt) |
**R16** | <i class="fa fa-check-square-o" style="color: #6be16d;"></i> | <a href="#rule16">Evidence |  |
**R17** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule17">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/koushikkothagal_spring-boot-microservices-workshop/model_variants/17.txt) |
**R18** | <i class="fa fa-exclamation-circle" style="color: #d72b28;"> | <a href="#rule18">Evidence | [Variant](https://github.com/tuhh-softsec/microSecEnD/blob/main/dataset/koushikkothagal_spring-boot-microservices-workshop/model_variants/18.txt) |



### Evidence and explanations for rule decisions

#### R1 {#rule01}

Rule is violated: All three services marked as *internal* can be accessed independently.

Artifacts:
- MovieCatalogServiceApplication.java: Line: [10](https://github.com/koushikkothagal/spring-boot-microservices-workshop/blob/master/movie-catalog-service/src/main/java/io/javabrains/moviecatalogservice/MovieCatalogServiceApplication.java#L10)
- MovieInfoServiceApplication.java: Line: [9](https://github.com/koushikkothagal/spring-boot-microservices-workshop/blob/master/movie-info-service/src/main/java/io/javabrains/movieinfoservice/MovieInfoServiceApplication.java#L9)
- RatingsDataServiceApplication.java: Line: [7](https://github.com/koushikkothagal/spring-boot-microservices-workshop/blob/master/ratings-data-service/src/main/java/io/javabrains/ratingsdataservice/RatingsDataServiceApplication.java#L7)

#### R2  {#rule02}

Rule is violated: Unauthenticated requests are sent from the catalog service to other services.

Artifacts:
- CatalogResource.java: Line: [36](https://github.com/koushikkothagal/spring-boot-microservices-workshop/blob/master/movie-catalog-service/src/main/java/io/javabrains/moviecatalogservice/resources/CatalogResource.java#L36)
- CatalogResource.java: Line: [32](https://github.com/koushikkothagal/spring-boot-microservices-workshop/blob/master/movie-catalog-service/src/main/java/io/javabrains/moviecatalogservice/resources/CatalogResource.java#L32)

#### R3 {#rule03}

Rule is violated: No authentication mechanism is deployed.

#### R4 {#rule04}

Rule is violated: External entities are not represented in the application.

#### R5 {#rule05}

Rule is violated: No authentication tokens are used.

#### R6 {#rule06}

Rule is violated: No rate limiting of any means is deployed.



#### R7 {#rule07}

Rule is violated: User external entities can call the gateway service using an unencrypted HTTP connection.

#### R8 {#rule08}

Rule is violated: All internal services communicate over insecure HTTP connections.

Artifacts:
- CatalogResource.java: Lines: [32](https://github.com/koushikkothagal/spring-boot-microservices-workshop/blob/master/movie-catalog-service/src/main/java/io/javabrains/moviecatalogservice/resources/CatalogResource.java#L32), [36](https://github.com/koushikkothagal/spring-boot-microservices-workshop/blob/master/movie-catalog-service/src/main/java/io/javabrains/moviecatalogservice/resources/CatalogResource.java#L36), [46](https://github.com/koushikkothagal/spring-boot-microservices-workshop/blob/master/movie-catalog-service/src/main/java/io/javabrains/moviecatalogservice/resources/CatalogResource.java#L46)



#### R9 {#rule09}

Rule is violated: No central logging system is deployed.

#### R10 {#rule10}

Rule is violated: No central logging system is deployed.

#### R11 {#rule11}

Rule is violated: Logs are not explicitly sanitized.

#### R12 {#rule12}

Rule is violated: No explicit logging mechanism is deployed.



#### R13 {#rule13}

Rule is violated: No explicit circuit breaker is deployed.

#### R14 {#rule14}

Rule is violated: There exists no API gateway since each service is accessed on a different user-facing port. The movie catalog service performs load balancing, but the ratings and movie info services do not.

Artifacts:
- MovieCatalogServiceApplication.java: Line: [18](https://github.com/koushikkothagal/spring-boot-microservices-workshop/blob/master/movie-catalog-service/src/main/java/io/javabrains/moviecatalogservice/MovieCatalogServiceApplication.java#L18)

#### R15 {#rule15}

This rule is not applicable: Not a service mesh deployment.



#### R16 {#rule16}

Rule is adhered to:
1. Registry Service (Eureka Server) with [@EnableEurekaServer](https://docs.spring.io/spring-cloud-netflix/docs/4.0.1-SNAPSHOT/reference/html/#spring-cloud-eureka-server) present.
1. Project is missing infrastructure description, not certain if and how the discovery server is deployed.

Artifacts:
- DiscoveryServerApplication.java: Line: [8](https://github.com/koushikkothagal/spring-boot-microservices-workshop/blob/master/discovery-server/src/main/java/io/javabrains/discoveryserver/DiscoveryServerApplication.java#L8)

#### R17 {#rule17}

Rule is violated: No [HTTP basic password](https://cloud.spring.io/spring-cloud-netflix/reference/html/#authenticating-with-the-eureka-server)   listed in any YML-Configuration of format username:password@here-location-of-eureka-server at "eureka.client.serviceUrl.defaultZone".

Artifacts:
- DiscoveryServerApplication.java: Line: [8](https://github.com/koushikkothagal/spring-boot-microservices-workshop/blob/master/discovery-server/src/main/java/io/javabrains/discoveryserver/DiscoveryServerApplication.java#L8)



#### R18 {#rule18}

Rule is violated: No secret manager is deployed. The secret API key used for the external movie database API is stored as a configuration key in the service instance.

Artifacts:
- application.properties: Line: [4](https://github.com/koushikkothagal/spring-boot-microservices-workshop/blob/master/movie-info-service/src/main/resources/application.properties#L4)
