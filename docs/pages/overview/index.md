---
title: microSecEnD - A Dataset of Security-Enriched Dataflow Diagrams for Microservice Applications
keywords: code2DFD introduction
sidebar: datasetdoc_sidebar
permalink: index.html
toc: false
---

&nbsp;
{% include image.html file="images/Logo_TUHH_SoftSEC.png" alt="Logo" max-width="750" %}

<img src="images/Logo_TUHH_SoftSEC.png"
     alt="Logo
     style="float: left; margin-right: 10px;" />
&nbsp;

This is microSecEnD, a dataset containing manually created, security-enriched Dataflow Diagrams (DFDs) of microservice applications written in Java.
The DFDs correspond to actual implementation code of open-source applications found on GitHub.
They are presented in multiple formats and contain full traceability of all model items to code, indicating the evidence for their implementation.

Additionally to the models themselves, we present a mapping to a list of 17 architectural security best-practices, i.e. a table indicating whether each rule is followed or not. For those that are not followed, we created model variants that do follow the rule. These variants were crafted purely on the model-level and the added items do not correspond to code anymore.

All artifacts were created manually by researchers of the <a href="https://www.tuhh.de/softsec/homepage.html" target="_blank">Institute of Software Security</a> at <a href="https://www.tuhh.de/tuhh/startseite.html" target="_blank">Hamburg University of Technology</a>.

The dataset is accompanying a publication at the 20<sup>th</sup> International Conference on Mining Software Repository (MSR'23).

If you use microSecEnD in academic context, please cite it as:
```bibtex
@inproceedings{microSecEnD23,
  title     = {microSecEnD: A Dataset of Security-Enriched Dataflow Diagrams for Microservice Applications},  
  author    = {Schneider, Simon and \"Ozen, Tufan and Chen, Michael and Scandariato, Riccardo},  
  booktitle = {2023 IEEE/ACM 20th International Conference on Mining Software Repositories (MSR)},   
  year      = {2023},
  doi       = {10.5281/zenodo.7574138}
}
```
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7574138.svg)](https://doi.org/10.5281/zenodo.7574138)

## Table of Contents

- [Introduction](index.html)
- [Description of DFDs](dfds.html)
- [Use-Cases](usecases.html)
- [Security Rules](rules.html)
- [Dataset](models.html)
- [Model Conversion](conversion.html)
