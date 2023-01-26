---
title: Converting Model Representations
keywords: model conversion
sidebar: datasetdoc_sidebar
permalink: conversion.html
datatable: false
---


The DFDs are presented in different formats (CodeableModels, JSON, PlantUML). If changes are made to a DFD in one of the formats, they should be easily mapped to the others as well. For this, we provide a script that converts any format into any other.

The tool is a simple command-line interface written in Python.
It can be downloaded [here](https://github.com/tuhh-softsec/microSecEnD/blob/main/convert_model.py).

## Usage
To convert a model, you have to run the tool and specify the path to the input model and the output format:

    python3 convert_model.py /path/to/input/model output_format

You can also specify the path where the output model should be stored:

    python3 convert_model.py /path/to/output/model /path/to/input/model output_format

To display a help message showing this information, run:

    python3 convert_model.py -h
