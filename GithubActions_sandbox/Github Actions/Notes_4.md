# ------------------- Topic -------------------

# GitHub Runner :
    - A runner is a server that runs your workflows when they're triggered. Each runner can run a single job at a time.
    - Github provides Ubuntu , Windows and MacOS runners to run your workflows.
    - Each workflow run executes in a fresh, newly-provisioned virtual machine.

# Two types of Runner Types:
    1. Github Hosted Runner: 
        - Github automatically provisions a new VM with Ubuntu, Windows or MacOS operating systems.
        - Machine maintainence and upgrades are taken care by Github.
        - Free Github plan + per-minute rates.
    2. Self Hosted Runner: 
        - A self hosted runner is a system that you deploy and manage to execute jobs for Github Actions.
        - Customizable to your hardware, operating system, software , and security requirements.
        - Are free to use with Github Actions.

# Why use Self-Hosted Runners:
    - Dealing with Proprietary software.
    - VM Size and Configuration.
    - Secure Access and Networking.
    - Large Workload Support.

--------------------------------------------------------------------------

# Adding a Self Hosted Runner to Github Runner:
TODO : Add your machine as a self hosted runner to Github.
TODO : Run a simple workflow/job on your self hosted runner.
