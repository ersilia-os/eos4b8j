# GDBChEMBL similarity search

The model looks for 100 nearest neighbors of a given molecule, according to ECFP4 Tanimoto similarity, in the GDBChEMBL database. GDBChEMBL is a 10M molecule-sampling from GDB17, a database containing all the enumerated molecules of up to 17 atoms heavy atoms (166.4B molecules). GDBChEMBL compounds were selected using a ChEMBL-likeness score, with the objective of having a collection with higher synthetic accessibility and high bioactivity while maintaining continuous coverage of the GDB17 chemical space. The whole GDBChEMBL database is not downloaded with the model, by using it you post queries to an online server external to Ersilia.

## Identifiers

* EOS model ID: `eos4b8j`
* Slug: `gdbchembl-similarity`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Similarity`
* Output: `Compound`
* Output Type: `String`
* Output Shape: `List`
* Interpretation: List of 100 nearest neighbors

## References

* [Publication](https://www.frontiersin.org/articles/10.3389/fchem.2020.00046/full)
* [Source Code](https://gdb-chembl-simsearch.gdb.tools/)
* Ersilia contributor: [Amna-28](https://github.com/Amna-28)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos4b8j)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos4b8j.zip)
* [DockerHub](https://hub.docker.com/r/ersiliaos/eos4b8j) (AMD64, ARM64)

## Citation

If you use this model, please cite the [original authors](https://www.frontiersin.org/articles/10.3389/fchem.2020.00046/full) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a None license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!