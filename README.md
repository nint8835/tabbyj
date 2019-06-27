# tabbyj

![Azure DevOps builds](https://img.shields.io/azure-devops/build/rileyflynn/e1079463-149d-46ee-9240-6ee3c6e3f14e/1.svg?style=for-the-badge)
![Azure DevOps tests](https://img.shields.io/azure-devops/tests/rileyflynn/tabbyj/1.svg?style=for-the-badge)
![Azure DevOps coverage](https://img.shields.io/azure-devops/coverage/rileyflynn/TabbyJ/1.svg?style=for-the-badge)

meowj & catj, but in Python.

## Installation

### Via Pip (Recommended)

```bash
python -m pip install tabbyj
```

### From source (For development)

1. Install [Poetry](https://poetry.eustace.io/)
2. `git clone https://github.com/nint8835/tabbyj.git`
3. `cd tabbyj`
4. `poetry install`

Please note that this will create a virtualenv and install the package into it. If you wish to use the package globally, please install it via Pip.

## Usage

### Piping

Tabbyj allows the user to simply pipe data into it in order to process it. For example:

```bash
curl https://api.github.com/gists | tabbyj
```

### Reading from a file

Tabbyj allows the user to easily read the data to process from a file via a command line argument. For example:

```bash
tabbyj --file example.json
```
