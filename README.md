# argo-acc-library

ARGO Accounting Service library: A simple python library for interacting with the ARGO Accounting Service REST API

The Accounting System is the platform responsible for collecting, aggregating, and exchanging metrics between different infrastructures, providers, and projects. The main functions of the platform are expressed by a REST API, which may be accessed by using the library in question.

You may find more information pertaining to the service on the [ARGO Accounting Service documentation](https://argoeu.github.io/argo-accounting/).

## Library installation

The library been tested with Python versions 3.9, 3.11, and 3.12 on Rocky 9. In order to install the library, you'll need to check out the source, have python setuptools installed and run

```bash
python3 ./setup.py build && \
  sudo python3 ./setup.py install
```

Alternatively, on RHEL-based systems you may run

```bash
python3 ./setup.py build && \
  sudo python3 ./setup.py bdist_rpm
```

to create an RPM file and then use rpm / dnf to install the RPM package, which should be located under the `dist` folder of the checked out source directory, e.g.

```bash
sudo dnf install ./dist/argo-acc-library-0.1.0-1.noarch.rpm
```

for version `0.1.0-1` of the library.

## Authentication

The Argo Accounting library needs a valid JSON Web Token (JWT) to authenticate against the Argo Accounting service's REST API. A JWT with a one-hour validity may be obtained by following the instructions under the `Authenticating Clients` section of the [online service documentation](https://argoeu.github.io/argo-accounting/docs/authentication/authenticating_clients). Once a valid JWT has been obtained, an accounting service object may be initialized as follows:

```python
from argo_acc_library import ArgoAccountingService
acc = ArgoAccountingService(endpoint="acc_endpoint", token="your_jwt")
```

## Examples

In the `examples` folder, you may find the following library usage examples:

* getting a JSON list of registered installations (`examples/get_installations.py`)
* getting a type / value list of metrics for a specific installation (`examples/get_installation_metrics.py`)
* assigning a new metric entry to an installation
* getting a title / ID list of registed projects
* getting a type / value list of metrics for a specific project
* getting a name / ID list of registed providers
* getting a type / value list of metrics for a specific project / provider combination

Help on running each example is available by running the example with `-h`.

### Listing installations

Assuming you've saved your valid JWT in a file under `~/acc.jwt`, you may run the first example against the development instance of the service with

```bash
python3 ./examples/get_installations.py --host api.devel.acc.argo.grnet.gr --token ~/acc.jwt -f | jq .
```

where piping to the command-line JSON processor [jq](https://jqlang.org/) in order to pretty-print the output may be omitted, if jq is not installed.

### Listing installation metrics

Assuming you've saved your valid JWT in a file under `~/acc.jwt`, you may run the second example against the development instance of the service with

```bash
python3 ./examples/get_installation_metrics.py --host api.devel.acc.argo.grnet.gr --token ~/acc.jwt -f --installation ...
```

where `...` should be replaced by a valid installation ID from the output of the previous example, in order to get a type / value list for all metrics of the specific installation.

### Assigning installation metrics

Assuming you've saved your valid JWT in a file under `~/acc.jwt`, you may run the third example against the development instance of the service with

```bash
python3 ./examples/add_installation_metric.py --host api.devel.acc.argo.grnet.gr --token ~/acc.jwt -f --installation ... --metricdefid METRICDEFID --tstart TSTART --tend TEND --value VALUE --gid GID --uid UID
```

where `...` should be replaced by a valid installation ID from the output of the first example and the rest of the parameters should be supplied with the new metric properties, as described in the example's help message (via `--help`)

### Getting a title / ID list of registered projects

Assuming you've saved your valid JWT in a file under `~/acc.jwt`, you may run the fourth example against the development instance of the service with

```bash
python3 ./examples/get_projects.py --host api.devel.acc.argo.grnet.gr --token ~/acc.jwt -f
```

### Getting a type / value list of metrics for a specific project

Assuming you've saved your valid JWT in a file under `~/acc.jwt`, you may run the fifth example against the development instance of the service with

```bash
python3 ./examples/get_project_metrics.py --host api.devel.acc.argo.grnet.gr --token ~/acc.jwt -f --project ...
```

where `...` should be replaced by a valid project ID from the output of the previous example

### Getting a name / ID list of registered providers

Assuming you've saved your valid JWT in a file under `~/acc.jwt`, you may run the sixth example against the development instance of the service with

```bash
python3 ./examples/get_providers.py --host api.devel.acc.argo.grnet.gr --token ~/acc.jwt -f
```

### Getting a type / value list of metrics for a specific project / provider combination

Assuming you've saved your valid JWT in a file under `~/acc.jwt`, you may run the seventh example against the development instance of the service with

```bash
python3 ./examples/get_provider_metrics.py --host api.devel.acc.argo.grnet.gr --token ~/acc.jwt -f --project ... --provider ...
```

where `...` should be replaced by a valid project ID and provider ID, respectively, from the output of the previous examples

## Environment variables

* `DEBUG`: Set to any truthy value in order to have debugging information printed to stdout, for development pusposes.
