# opti-flex

## 1. Implementation of the Optimizer

- The `app` folder contains the source code of the Optimizer. The `main.py` file serves as the application entry point.
- The `test_data` folder contains synthetic optimization files for demonstration purposes. The
  `obfuscation_<obfuscation_type>` subfolders contain additional optimization files for demonstrating obfuscation. For
  each obfuscation type, the corresponding subfolder contains two optimization files: one configured to use the Privacy
  Engine (which is expected to be available at `http://127.0.0.1:80`) and the encoding service (which is expected to be
  available at `http://127.0.0.1:88`), and another configured to simulate the Privacy Engine.
- The `config.properties` file supports two configurable settings: the application mode and whether all individuals are
  included in the optimization statistics.
    - The application mode can be set to either `dev` or `ops`: In `dev` mode, the Optimizer generates the same UUID for
      every optimization run. In `ops` mode, the Optimizer generates a unique UUID for every optimization run.
    - The `individuals` setting is a boolean (`True` or `False`) that determines whether the full population is included
      in the optimization statistics: If `True`, all individuals are included in the statistics; otherwise, dominated
      individuals are not included. By default, this setting is `False` to minimize storage usage.
- The `Dockerfile` can be used to build a Docker image for the Optimizer.
- The `requirements.txt` file contains the dependencies required by the Optimizer.

**Note:** The statistics never include the encoding of individuals to minimize storage usage. The encoding is only
available for individuals in the optimization result. If you need access to the encoding of individuals in the
optimization statistics, you must:

1. Remove the `encoding` attribute from the `Individual` class,
2. Add the `encoding` attribute to the `IndividualBase` class, and
3. Add a corresponding mapping from the `encoding` attribute of the `Individual` class to the `encoding` attribute of
   the `IndividualDTO` class in the `to_dto` function of the `IndividualMapper` class, i.e.,
   `return IndividualDTO(encoding=obj.encoding, ...)`.

## 2. Running the Optimizer

### 2.1. API

The Optimizer is implemented using FastAPI and provides the following endpoints. Swagger documentation is available at
`/docs`:

- `GET /optimizations`: Retrieves all optimizations.
- `GET /optimizations/{optimization_id}`: Retrieves a specific optimization.
- `GET /optimizations/{optimization_id}/statistics`: Retrieves the statistics for a specific optimization.
- `GET /optimizations/{optimization_id}/result`: Retrieves the result of a specific optimization.
- `POST /optimizations`: Creates a new optimization. Requires an optimization file in the request body.
- `PUT /optimizations/{optimization_id}/start`: Starts a specific optimization asynchronously.
- `PUT /optimizations/{optimization_id}/start/wait`: Starts a specific optimization synchronously and waits for it to
  complete.
- `PUT /optimizations/{optimization_id}/abort`: Aborts a specific running optimization.
- `DELETE /optimizations/{optimization_id}`: Deletes a specific optimization.

### 2.2. Docker

#### 2.2.1. Build the Image

```bash
docker build -t <IMAGE-NAME> .
```

#### 2.2.2. Run the Container

```bash
docker run -d --name <CONTAINER-NAME> -p 8001:8001 <IMAGE-NAME>
```

Uvicorn server for the Optimizer will be running on `http://127.0.0.1:8001`.

## 3. Run an Optimization

You can run optimizations using the optimization files from `test_data`, for example, via the Swagger UI:

1. Create the optimization by sending an HTTP `POST` request to `/optimizations` and providing the contents of an
  optimization file in the request body. The Optimizer returns a UUID as the optimization ID.
2. Start the optimization by sending an HTTP `PUT` request to `/optimizations/{optimization_id}/start` (asynchronously)
  or `/optimizations/{optimization_id}/start/wait` (synchronously).
3. Retrieve the current optimization result by sending an HTTP `GET` request to
  `/optimizations/{optimization_id}/result`.
4. Retrieve the optimization statistics by sending an HTTP `GET` request to
  `/optimizations/{optimization_id}/statistics`.

If an objective in an optimization file does not specify a Privacy Engine, the Privacy Engine is not used for that
objective.

If an objective does not configure an obfuscation method, the evaluation results for that objective are not obfuscated.

### 3.1. Run an Optimization with a simulated Privacy Engine

If an objective specifies an obfuscation method but does not specify a Privacy Engine, the Optimizer simulates the
Privacy Engine.

Use the files from the `obfuscation_<obfuscation_type>` subfolders that include `_simulated.json` in the filename.
Follow the procedure described above.

### 3.2. Run an Optimization with the Privacy Engine

If an objective specifies a Privacy Engine, the Privacy Engine is used.

Download and run the [Privacy Engine](https://doi.org/10.5281/zenodo.20748035). Use the files from the
`obfuscation_<obfuscation_type>` subfolders that include `_privacy_engine.json` in the filename. Follow the procedure
described above.