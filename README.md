# SNCF Api

[![Build Status](https://travis-ci.com/matthew73210/sncf_api.svg?branch=master)](https://travis-ci.com/matthew73210/sncf_api)

[![DeepSource](https://static.deepsource.io/deepsource-badge-light-mini.svg)](https://deepsource.io/gh/matthew73210/sncf_api/?ref=repository-badge)

[![CodeFactor](https://www.codefactor.io/repository/github/matthew73210/sncf_api/badge)](https://www.codefactor.io/repository/github/matthew73210/sncf_api)

A class of methods that can call the different SNCF API's from [SNCF Open Data](https://data.sncf.com/), returns data as a [Pandas](https://pandas.pydata.org/) dataframe or .json() object.

That Pandas dataframe has some elements clipped.

Some of the calls can be huge, as SNCF has put a lot of data up. Some calls may even max out the api interface. **list line** by type is an example.

## Requirements

- Pandas
- Requests
- Python 3.8

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install.

```bash
NOT ON PYPI YET
```

## Usage

Import the class.

```python
import sncf_api as sncf
```

Call the class (with or without the line code).

```python
sncf = sncf(903000)
```

Or

```python
sncf = sncf()
```

Call methods.

```python
db = sncf.list_construction_site()
```

To get a list of methods from class.

```python
help(sncf)
```

## Notes

Methods don't need to be called with arguments, only the class.
The **convert_to_pandas_db()** method with used the data from the last method called and return a pandas dataframe.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## URL's

[SNCF Open Data](https://data.sncf.com/)

[Pandas](https://pandas.pydata.org/)

[Pip](https://pip.pypa.io/en/stable/)

[Make a readme](https://www.makeareadme.com/)
