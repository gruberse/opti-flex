# opti-flex

## Implementation of the Optimizer

- The folder `app` contains the source code. The `main.py` file is the application file.
- The folder `test_data` contains synthetic optimization files for demonstration. The subfolders `obfuscation_<obfuscation_type>` provide additional optimization files for demonstrating obfuscation. For each obfuscation type, the corresponding subfolder contains two optimization files: one configured for use with the Privacy Engine (expect the Privacy Engine to be available at `http://127.0.0.1:80` and the encoding service at `http://127.0.0.1:88`), and another configured for simulating the Privacy Engine.
- The file `config.properties` supports two configurable settings: application mode and individuals in statistics.
  - The application mode can be set to either `dev` or `ops`: In `dev` mode, the Optimizer generates the same UUID for every optimization run. In `ops` mode, the Optimizer generates a unique UUID for every optimization run.
  - The `individuals` setting is a boolean (`True` or `False`) that determines whether the full population is included in the optimization statistics: If `True`, all individuals are included in the statistics; otherwise, the individuals are not included. By default, this setting is `False` to minimize storage usage.
- **`False`**: Excludes the full population to reduce storage requirements.
- The file `Dockerfile` can be used to create a Docker image of the Optimizer.
- The file `requirements.txt` contains the requirements to be installed.

**Note:** The statistics never include the encoding of individuals to minimize storage usage. The encoding is only available for individuals in the result. If you need access to the encoding of individuals within the statistics, you must (1) remove the attribute `encoding` from class `Individual`, (2) add the attribute `encoding` to class `IndividualBase`, and (3) add a corresponding mapping from the attribute `encoding` in class `Individual` to attribute `encoding` in class `IndividualDTO` in the function `to_dto` in class `IndividualMapper`, i.e., `return IndividualDTO(encoding=obj.encoding, ...)`

## Running the Optimizer

### API

The Optimizer is implemented using FastAPI with the following interfaces (Swagger documentation available on /docs):

- GET /optimizations to retrieve all optimizations
- GET /optimizations/{optimization_id} to retrieve a specific optimization
- GET /optimizations/{optimization_id}/statistics to retrieve the statistics of a specific optimization
- GET /optimizations/{optimization_id}/result to retrieve the result of a specific optimization
- POST /optimizations to create an optimization (requires an optimization file in the request body)
- PUT /optimizations/{optimization_id}/start to start a specific optimization asynchronously
- PUT /optimizations/{optimization_id}/start/wait to start a specific optimization synchronously
- PUT /optimizations/{optimization_id}/abort to abort a specific running optimization
- DELETE /optimizations/{optimization_id} to delete a specific optimization

### Docker
#### Build the Image
```bash
docker build -t <IMAGE-NAME> .
```

#### Run the Container
```bash
docker run -d --name <CONTAINER-NAME> -p 8001:8001 <IMAGE-NAME>
```

Uvicorn server for the Optimizer will be running on `http://127.0.0.1:8001`.

#### Run an Optimization

You can run optimizations using the example optimization files from `test_data` via e.g. the Swagger UI:

- Create the optimization via HTTP POST /optimizations and provide the content of an optimization file in the request body. The Optimizer returns a UUID as the optimization ID.
- Start the optimization via HTTP PUT /optimizations/{optimization_id}/start (asynchronously) or /optimizations/{optimization_id}/start/wait (synchronously).
- You can request the current optimization result via HTTP GET /optimizations/{optimization_id}/result and statistics via HTTP GET /optimizations/{optimization_id}/statistics.
