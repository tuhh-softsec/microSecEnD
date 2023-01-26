---
title: Items in our DFDS
keywords: Dataflow Diagrams, DFDs, source code, model items, nodes, edges, architectural layout, security features, services, databases, external entities, information flows, stereotypes, tagged values
sidebar: datasetdoc_sidebar
permalink: dfds.html
datatable: true
---

&nbsp;
Dataflow Diagrams (DFDs) are depictions of software systems as directed graphs. As such, they can be extracted from source code, as we did manually to create this dataset. For this, evidence for the implementation of model items needs to be found in code. The DFDs' basic structure (its nodes and edges) show the architectural layout of the system. Added annotations provide further information about employed (security and other) features. It varies largely, what is included in a DFD and how the granularity is chosen.
Here, we describe what items we include in our DFDs.


We consider **services**, **databases**, and **external entities** as nodes in the DFD and **information flows** as edges.
They are annotated with **stereotypes** and **tagged values**.

{% include image.html file="DFD_components.svg" alt="DFD Items" caption="Examples of how all DFD items are visualized." max-width="650" %}

## Services

Services correspond to the application's microservices. They are visualized as rectangles with rounded corners. We distinguish internal services (those realizing the business logic) from infrastructural services (those building the supporting infrastructure by using mainly existing code libraries with only marginal alterations). Databases are microservices that are used to store data. As such, they are represented as services with the stereotype (see below) --database--.

## External entities

External entities are software components that are not deployed with the application, for example public mail servers, websites, or other code repositories. They are visualized as rectangles. External entities are called from the application without a deployment descriptor or other implementation in the codebase. Additionally, an external component *user* representing the human user is added implicitly.

## Information flows

Information flows are connections between two nodes (services and external entities) over which information is sent. They are visualized as arrows. Information flows can be explicit requests to other services as part of the business logic as well as communication happening in the infrastructural working, for example registrations with service discovery mechanisms, sending of logs, or retrieval of configuration data.

## Annotations

Annotations are made to the model items described above in the form of *stereotypes* and *tagged values*. Stereotypes (visualized as --stereotype--) enrich the model with semantic or non-functional information about items. Tagged values (visualized as *key = value* pairs) present additional attributes that are infeasible to capture in a finite list of stereotypes.
