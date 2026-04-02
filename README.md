# opti-flex

## Implementation of the Optimizer
- The folder app contains the source code.
- The folder test_data contains synthetic optimization files for demonstration. The subfolders obfuscation_<obfuscation_type> provide additional optimization files for demonstrating obfuscation. For each obfuscation type, the corresponding subfolder contains two optimization files: one configured for use with the Privacy Engine, and another configured for simulating the Privacy Engine.
- The Docker file may be used to create an image of the Optimizer
- The requirements file contains the requirements to be installed.

## For local development
### Set up virtual environment and install requirements
```bash
pip install -r requirements.txt
```

### Activate the virtual environment
```bash
source .venv/bin/activate
```

### Run the live server
```bash
uvicorn uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

## Docker
### Build the image
```bash
docker build -t <IMAGE-NAME> .
```

### Run the container
```bash
docker run -d --name <CONTAINER-NAME> -p 8001:8001 <IMAGE-NAME>
```

Uvicorn server for the optimizer will be running on **http://localhost:8001**.
