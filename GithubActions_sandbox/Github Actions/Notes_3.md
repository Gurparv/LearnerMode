# ------- Github Actions Features ----------

# Environment Variables:
    - Variables are used to store information to be referenced and manipulated in a program.
    - Setting and Retrieving environment variables syntaxes.
    - Scope of Environment variables Job level, scope level, global level etc.


TODO - Create simple workflow scripts to understand scope of environment variables

# Default Environment Variables:
    - Whats the use of Default Environment variables.
    - How to print all the Default Environment variables.

# Github Actions Secrets(credentials):
    - Environment secrets
    - Repository secrets
TODO - How to access Environment secrets and Repository secrets from your `.yml` file.
TODO - How to create Github Actions Secret and use it in your workflow file.(Even you cant print the secret value)

# Github Artifacts:
    - Artifacts allows us to share data between jobs in a workflow and store data once that workflow has completed. Basically to persist the data after the execution is over.
    - Examples of common artifacts that we can upload 
        1. Log files.
        2. Test Results, failures and screenshots.
        3. Binary or Compressed files.
        4. Stress test performance output and code coverage results.
TODO - Create simple workflow script to upload and download the artifacts file.
TODO - Create simple workflow that consumes the artifacts.

# Github Environments(Using them for deployment) | How to add manual approvals:
    - We can configure environments with protection rules and secrets.
    - A workflow job that references an environment must follow any protection rules for the environment before running or accessing the environment's secrets.

# Sharing Variables between Steps and Jobs
TODO - Create a simple workflow script to share values between different Steps.
TODO - Create a simple workflow script to share values between different Jobs.

