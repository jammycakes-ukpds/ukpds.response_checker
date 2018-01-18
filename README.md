## Response Checker
Response Checker is a Go script designed to retrieve a list of working routes and check how these are responding, reporting back all URLs that have been visited, along with their status code.

### Requirements
Response Checker requires [Go](https://golang.org/doc/install) to be installed.

The Python version requires Python 3 and the package(s) listed in requirements.txt.
It is recommended that you run the script in a virtual environment:

    virtualenv -p python3 .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    python3 main.py

### Usage
1. Set up this repository
```kernal
git clone https://github.com/jennaramdenee/response_checker
cd response_checker
```

2. Set base URL in `src/main.go` file

3. Run the script
```kernal
go run main.go
```

4. Two files will be created in your directory
  * `output.txt` - list of all routes
  * `results.txt` - list of URLs that have been visited, along with their status code

### Testing
Tests can be run by using the following command:
```kernal
go test -v
```

### Caveats
Currently, this script only supports the latin alphabet and not all Unicode characters.
