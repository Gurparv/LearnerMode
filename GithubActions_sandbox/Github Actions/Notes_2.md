# Github Action Workflow :
    - Github Action Workflow Directory: `.github/workflows/`
    - File Extension: `.yml`

# Common Github Action Workflow tasks:
    - Build
    - Test
    - Deploy

# Terminology used in Workflows
    - Events : An event is a specific activity in a repo that triggers a workflow run. For example, activity can originate from Github when someone creates a pull request, opens an issue, or pushes a commit to a repo.
    - Job : A job is a set of steps in a workflow that execute on the same runner. Each step is either a shell script that will be executed, or an action that will be run. For eg -> Build code is a step, Test code is a step
    - Runners: A runner is a server that runs your workflows when they're triggered. Each runner can run a single job at a time.Github provides Ubuntu Linux, Microsoft Windows, and MacOS runners to run your workflows.Each workflow run executes in a fresh, newly-provisioned virtual machine.
    - Github Action : An action is a custom application for the Github Actions platform that performs a complex but frequently repeated task.Use an action to help reduce the amount of repetitive code that you write in your workflow files.An action can pull your git repo from Github, set up the correct toolchain for your build environment, or set up the authentication to your cloud provider.

TODO : Practice creating simple github workflow.
