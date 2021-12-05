# EstudiaMate

## How to develop

### Prerequisites
You must have `pip-tools` installed in your venv. It will install the project dependencies.

### Basic Setup
1. Clone the repo
    ```
    git clone git@github.com:GbNok/IWG101-Proyecto.git
    ```
1. Create a virtual environment
    ```
    python3 -m venv .venv
    source .venv/bin/activate
    ```
1. Install `pip-tools`
    ```
    python3 -m pip install pip-tools
    ```
1. Install project dependencies
    ```
    pip-sync
    ```
1. Apply database migrations
    ```
    python manage.py migrate
    ```
1. Start webserver
    ```
    python3 manage.py runwebserver
    ```

### Installing new dependencies
1. Add your dependency to `requirement.in`
1. Compile a new requirements.txt with `pip-compile`:
    ```
    pip-compile requirements.in > requirements.txt
    ```
1. Commit the changes. From now on, when a new developer syncs the dependencies they shall be the same versions of all the dependency closure of the application as everyone else.