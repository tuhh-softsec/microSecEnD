---
title: Security Rules
keywords: Security Rules, Microservices
sidebar: datasetdoc_sidebar
permalink: rules.html
datatable: true
---

All presented models were checked against a list of 17 architectural security rules for microservices. We presented the list of rules in a <a href="https://dl.acm.org/doi/abs/10.1145/3538969.3543807" target="_blank">previous publication</a> at ARES'22. Since rule R15 does not apply to the applications in our dataset, it is omitted in our analysis.
The rules are grouped into six categories:

## Authentication / Authorization
**R1**: An API Gateway or similar facade should exist as a single entry point to the system and perform authorization and authentication of external requests to avoid external entities directly accessing services.

**R2**: Services should mutually authenticate and authorize requests from other services.

**R3**: Authorization and authentication processes should be decoupled from other services and should be implemented at platform level to enable reuse by different services.

**R4**: All the external entity identity representations should be transformed into an extendable internal identity representation. The internal identity representations should be secured with signatures and propagated but not exposed outside. They should be used for authentication and authorization at all levels.

**R5**: Authentication tokens should be validated.

**R6**: A limit for the maximum number of login attempts before preventive measures are taken should exist.

## Encryption
**R7**: All communication traffic from external users and entities should be encrypted using secure communication protocols.

**R8**: All communication between the services should be encrypted using secure communication protocols.

## Logging
**R9**: A central logging subsystem which includes a monitoring dashboard should exist.

**R10**: For all microservices, there should exist a local logging agent decoupled from the microservice but deployed on the same host. Log data from microservices should not be send to the central logging system directly, but collected by the logging agent, written to a local file, and eventually send to the central system by it.

**R11**: The local logging agent should sanitize the log data and remove any PII, passwords, API keys, etc.

**R12**: A message broker should be used to realize the communication between local logging agent and central logging system. These two should use mutual authentication and encrypt all transmitted data and availability should be ensured by providing periodic health and status data.

## Availability
**R13**: A circuit breaker should be used at the proxy.

**R14**: The API gateway should perform load balancing.

## Service Registry
**R16**: Service registry services should be deployed on dedicated servers or as part of a service mesh architecture.

**R17**: Service registry services should have validation checks to ensure that only legitimate services are performing the registration, refresh operations, and database queries to discover services.

## Secret Management
**R18**: Secrets should be managed centrally following the Secret as a Service principle.
