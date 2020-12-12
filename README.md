# ufs-workflow
Workflows for UFS applications

## Description
UFS-workflow is a package to configure and execute workflows for UFS applications.

## Dependencies
- python>=3.6
- pyyaml>=5.3.1

## Installation
UFS-workflow is a pure Python-3 package, with a standard Python setuptools install system. We recommended using pip to install ufs-workflow.  ufs-workflow can also be installed in a python virtualenv to avoid/resolve dependency issues.

```
git clone https://github.com/noaa-emc/ufs-workflow
pip install --user -U -e $PWD/ufs-workflow
```

Upon successful installation, a python module `ufs_workflow` will be available along with several stand-alone applications.

## Usage
The python module `ufs_workflow` can be imported via standard python module imports.

```
python
>>> import ufs_workflow

```
