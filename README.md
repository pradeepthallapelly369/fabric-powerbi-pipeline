# Microsoft Fabric & Power BI Data Pipeline Development Environment

This environment is set up for developing Microsoft Fabric and Power BI data pipelines using Python and the Fabric CLI.

## Installed Tools & Libraries

- **Microsoft Fabric CLI (`fab`)**: `1.7.0` (accessible globally via `~/.local/bin/fab`)
- **SemPy (`semantic-link`)**: `0.14.2` (Microsoft Fabric Semantic Link)
- **SemPy Labs (`semantic-link-labs`)**: `0.17.1` (Fabric & Power BI automation utilities)
- **Azure Identity (`azure-identity`)**: `1.25.3` (DefaultAzureCredential, ServicePrincipal, DeviceCode)
- **Azure Storage DataLake (`azure-storage-file-datalake`)**: `12.25.0` (OneLake / ADLS Gen2 filesystem client)
- **Fabric CI/CD (`fabric-cicd`)**: `1.3.0`
- **Pandas & PyArrow**: Data analysis and Parquet/Delta table handling

## Quick Start

### 1. Microsoft Fabric CLI (`fab`)

Authenticate and explore Fabric workspaces:
```bash
# Log in to Microsoft Fabric
fab auth login

# Check authentication status
fab auth status

# List workspaces
fab ls

# Switch to a workspace
fab cd "My Workspace"
```

### 2. Python Virtual Environment

Activate the virtual environment:
```bash
cd /home/upc/every_thing_claude/fabric_pipeline_dev
source .venv/bin/activate
```

### 3. Example: OneLake / Lakehouse Access via Python

```python
from azure.identity import DefaultAzureCredential
from azure.storage.filedatalake import DataLakeServiceClient

# OneLake DFS endpoint
onelake_url = "https://onelake.dfs.fabric.microsoft.com"
credential = DefaultAzureCredential()

service_client = DataLakeServiceClient(account_url=onelake_url, credential=credential)

# List filesystems (Fabric workspaces)
file_systems = service_client.list_file_systems()
for fs in file_systems:
    print("Workspace:", fs.name)
```

### 4. Example: Power BI / Semantic Link (`sempy`)

```python
import sempy.fabric as fabric

# List datasets / semantic models in a workspace
datasets = fabric.list_datasets()
print(datasets)

# Execute DAX query on a Power BI semantic model
query = "EVALUATE TOPN(10, 'MyTable')"
df = fabric.evaluate_dax(dataset="MyDataset", dax_string=query)
print(df.head())
```
