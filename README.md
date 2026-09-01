# GDBChEMBL similarity search

The model identifies the 100 nearest neighbors of a molecule based on ECFP4 Tanimoto similarity within the GDBChEMBL database. GDBChEMBL is a 10M molecule subset of GDB17 (which contains 166.4B molecules up to 17 heavy atoms). Compounds were selected using a ChEMBL-likeness score to prioritize synthetic accessibility and bioactivity while maintaining broad chemical space coverage. Note: The database is not stored locally; using the model sends queries to an external server outside the Ersilia ecosystem.

This model was incorporated on 2022-08-15.Last packaged on 2026-09-01.

## Information
### Identifiers
- **Ersilia Identifier:** `eos4b8j`
- **Slug:** `gdbchembl-similarity`

### Domain
- **Task:** `Sampling`
- **Subtask:** `Similarity search`
- **Biomedical Area:** `Any`
- **Target Organism:** `Any`
- **Tags:** `Similarity`, `ChEMBL`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `100`
- **Output Consistency:** `Fixed`
- **Interpretation:** List of 100 nearest neighbors

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| smi_00 | string |  | Sampled smiles 0 from a similarity search in GDBChEMBL |
| smi_01 | string |  | Sampled smiles 1 from a similarity search in GDBChEMBL |
| smi_02 | string |  | Sampled smiles 2 from a similarity search in GDBChEMBL |
| smi_03 | string |  | Sampled smiles 3 from a similarity search in GDBChEMBL |
| smi_04 | string |  | Sampled smiles 4 from a similarity search in GDBChEMBL |
| smi_05 | string |  | Sampled smiles 5 from a similarity search in GDBChEMBL |
| smi_06 | string |  | Sampled smiles 6 from a similarity search in GDBChEMBL |
| smi_07 | string |  | Sampled smiles 7 from a similarity search in GDBChEMBL |
| smi_08 | string |  | Sampled smiles 8 from a similarity search in GDBChEMBL |
| smi_09 | string |  | Sampled smiles 9 from a similarity search in GDBChEMBL |

_10 of 100 columns are shown_
### Source and Deployment
- **Source:** `Online`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos4b8j](https://hub.docker.com/r/ersiliaos/eos4b8j)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos4b8j.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos4b8j.zip)

### Resource Consumption
- **Model Size (Mb):** `1`
- **Environment Size (Mb):** `315`
- **Image Size (Mb):** `315.95`

**Computational Performance (seconds):**
- 10 inputs: `35.71`
- 100 inputs: `270.19`
- 10000 inputs: `-1`

### References
- **Source Code**: [https://gdb-chembl-simsearch.gdb.tools/](https://gdb-chembl-simsearch.gdb.tools/)
- **Publication**: [https://doi.org/10.3389/fchem.2020.00046](https://doi.org/10.3389/fchem.2020.00046)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2020`
- **Ersilia Contributor:** [Amna-28](https://github.com/Amna-28)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [None](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos4b8j
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos4b8j
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
