# flights_liquibase

The 'flights_liquibase' project showcases a simple example on a Databricks Job and a schema managed by Liquibase.

On a PR, a GH Action gets trigger that connects to Liquibase and applies the changelog in the target env, then runs the local tests and the Job. 

## GH setup
3 secrets are needed in your project:
- DATABRICKS_HOST: e.g. dbc-eae35cd0-9e95.cloud.databricks.com
- DATABRICKS_TOKEN_TST: <token>
- DATABRICKS_JDBC_URL: e.g. jdbc:databricks://dbc-eae35cd0-9e95.cloud.databricks.com:443/default;transportMode=http;ssl=1;AuthMech=3;httpPath=/sql/1.0/warehouses/863bcc7ff8fea25b;

## tests
You can run tests by setting up a local virtual environment with databricks-connect and running `py.test`. That will run the unit tests within `tests/unit_utils` and `tests/unit_transforms`.  

Another option to run tests is using a notebook, demonstrated by `tests/pyspark_testing_notebook.py`.

## resources
Various types of jobs are demonstrated in the `resources` directory.
- `flights_notebook_job_serverless.yml` shows a serverless notebook job with a few parameters.

## Getting started

1. Install the Databricks CLI from https://docs.databricks.com/dev-tools/cli/databricks-cli.html

2. Authenticate to your Databricks workspace:
    ```
    $ databricks configure
    ```

3. Go to root project directory then deploy a development copy of this project, type:
    ```
    $ databricks bundle deploy --target dev
    ```
    (Note that "dev" is the default target, so the `--target` parameter
    is optional here.)

    This deploys everything that's defined for this project.
    You can find the jobs by opening your workspace and clicking on **Workflows**.

4. Similarly, to deploy a production copy, type:
   ```
   $ databricks bundle deploy --target prod
   ```

5. To run a job or pipeline, use the "run" command:
   ```
   $ databricks bundle run notebook_validation_job
   ```

6. Optionally, install developer tools such as the Databricks extension for Visual Studio Code from
   https://docs.databricks.com/dev-tools/vscode-ext.html. Or read the "getting started" documentation for
   **Databricks Connect** for instructions on running the included Python code from a different IDE.

7. For documentation on the Databricks asset bundles format used
   for this project, and for CI/CD configuration, see
   https://docs.databricks.com/dev-tools/bundles/index.html.
