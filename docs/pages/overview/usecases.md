---
title: Use-Cases
keywords: Architecture Reconstruction, Feature Detection, Software Security Assessment Techniques
sidebar: datasetdoc_sidebar
permalink: usecases.html
datatable: true
---

The models presented in this dataset can be used by researchers and others for multiple things. Apart from serving as reference set for architectural design decisions and implementations of security features, we see use-cases in architecture reconstruction and feature detection close to code, in work on the model-level, and in work on software security assessment techniques.

## Architecture Reconstruction and Feature Detection

In previous work, we used the DFDs as groundtruth to evaluate the performance of Code2DFD, a tool that implements our approach of extracting DFDs automatically from source code. With its manual creation, the dataset can be used in the validation of multiple related techniques, and this is surely its prime use-case. \
While our mentioned tool is built to extract DFDs with the same items as the ones in our dataset, other researchers might use only a subset of the items or might add further information. For example, the DFDs can be stripped of their annotations to obtain the plain architectural layout of the corresponding application. The fields of architecture recovery and feature detection both need good quality data to compare new approaches against, especially for microservices, where not much research has been done in these fields yet.

## Work on the Model-Level

The dataset can also be used on a higher abstraction level, i.e. in research about architectural security patterns and best-practices without direct connection to code. Our <a href="https://dl.acm.org/doi/abs/10.1145/3538969.3543807" target="_blank">previous work</a> on a set of architectural security rules for microservice applications was the initial source for the annotations in the DFDs. Based on this and with the mapping of which of the presented rules are adhered to by which application, our dataset can be used in the validation of techniques that check microservice applications for conformance to architectural best-practices. \
The model variants add further value to the use-case of research on architectural security. They open the possibility of delta-evaluations between model variants. Further, detectors for singular rules can be validated precisely with those applications that do not follow the rule in the ground model, since they have a variant that does.

## Research of Software Security Assessment Techniques

Finally, many security assessment techniques use DFDs or similar models as a starting point. Research on these techniques can use our models, for example for empirical studies where their creation is infeasible in a constrained time and the focus lies on the later parts of the assessment techniques.
