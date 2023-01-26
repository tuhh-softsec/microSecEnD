---
title: microSecEnD - A Dataset of Manually Created, Security-Enriched Dataflow Diagrams
keywords: code2DFD introduction
sidebar: datasetdoc_sidebar
permalink: index.html
toc: false
---

&nbsp;
{% include image.html file="Logo_TUHH_SoftSEC.svg" alt="Logo" max-width="750" %}
&nbsp;

This is microSecEnD, a dataset containing security-enriched Dataflow Diagrams (DFDs) of microservices written in Java. \
The DFDs correspond to actual implementation code of open-source applications found on GitHub.
They are presented in multiple formats and contain full traceability of all model items to code, indicating the evidence for their implementation.

Additionally to the models themselves, we present a mapping to a list of 17 architectural security best-practices, i.e. a table indicating whether each rule is followed or not. For those that are not followed, we created model variants that do follow the rule. These variants were crafted purely on the model-level and the added items do not correspond to code anymore.

All artifacts were created manually by researchers of the <a href="https://www.tuhh.de/softsec/homepage.html" target="_blank">Institute of Software Security</a> at <a href="https://www.tuhh.de/tuhh/startseite.html" target="_blank">Hamburg University of Technology</a>.

## Table of Contents

- [Introduction](index.html)
- [Description of DFDs](dfds.html)
- [Use-Cases](usecases.html)
- [Security Rules](rules.html)
- [Dataset](models.html)
- [Model Conversion](conversion.html)
