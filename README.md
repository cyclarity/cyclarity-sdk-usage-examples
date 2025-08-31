# CyClarity Component Package Example
This repository contains an example for a CyClarity component package with basic functionality usage.

## Installation
Each CyClarity component is a poetry project.

poetry can be installed with:
```bash
curl -sSL https://install.python-poetry.org | python3 - --version 1.8.5
```

## Initialization

to create a new poetry porject run:
```bash
poetry new <project-name>
```

## Dependencies management
You can add dependencies to your project using poetry.
the cyclarity-sdk is manadatory for all components.

```bash
poetry add cyclarity-sdk
```

in the same manner other desired python dependencies can be added to your component.
e.g. adding the CyClarity In-Vehicle SDK using poetry in your poetry project:

```bash
poetry add cyclarity-in-vehicle-sdk
```