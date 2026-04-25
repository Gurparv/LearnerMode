#### Overview:
- Github Actions is a CI/CD Platform that allows you to automate your build, test, and deployment pipeline. You can create workflows that build and test every pull request to your repository, or deploy merged pull requests to production.
- GitHub Actions goes beyond just DevOps and lets you run workflows when other events happen in your repository. For example, you can run a workflow to automatically add the appropriate labels whenever someone creates a new issue in your repository.
- GitHub provides Linux, Windows, and macOS virtual machines to run your workflows, or you can host your own self-hosted runners in your own data center or cloud infrastructure.

#### Components of Github Actions
- You can configure a GitHub Actions workflow to be triggered when an event occurs in your repository, such as a pull request being opened or an issue being created. Your workflow contains one or more jobs which can run in sequential order or in parallel. Each job will run inside its own virtual machine runner, or inside a container, and has one or more steps that either run a script that you define or run an action, which is a reusable extension that can simplify your workflow.
- 
	1. Workflow 
	2. Event 
	3. Jobs 
	4. Action 
	5. Runner 
	6. Steps 
	7. Script

![[Pasted image 20260322233617.png]]

#### Components of Github Actions (detailed)
##### 1. Workflows (.yml files)
A workflow is a configurable automated process that will run one or more jobs. Workflows are defined by a YAML file checked in to your repository and will run when triggered by an event in your repository, or they can be triggered manually, or at a defined schedule. Workflows are defined in the .github/workflows directory in a repository. A repository can have multiple workflows, each of which can perform a different set of tasks
##### 2. Events (When workflow will trigger?)
An event is a specific activity in a repository that triggers a workflow run. For example, an activity can originate from GitHub when someone creates a pull request, opens an issue, or pushes a commit to a repository. You can also trigger a workflow to run on a schedule, by posting to a REST API, or manually. For a complete list of events that can be used to trigger workflows, see

##### 3. Jobs (Set of steps in a workflow)
A job is a set of steps in a workflow that is executed on the same runner. Each step is either a shell script that will be executed, or an action that will be run. Steps are executed in order and are dependent on each other. Since each step is executed on the same runner, you can share data from one step to another. For example, you can have a step that builds your application followed by a step that tests the application that was built. You can configure a job's dependencies with other jobs; by default, jobs have no dependencies and run in parallel. When a job takes a dependency on another job, it waits for the dependent job to complete before running. You can also use a matrix to run the same job multiple times, each with a different combination of variables—like operating systems or language versions. For example, you might configure multiple build jobs for different architectures without any job dependencies and a packaging job that depends on those builds. The build jobs run in parallel, and once they complete successfully, the packaging job runs.
##### 4. Actions (reusable set of jobs or code)
An action is a pre-defined, reusable set of jobs or code that performs specific tasks within a workflow, reducing the amount of repetitive code you write in your workflow files. Actions can perform tasks such as: Pulling your Git repository from GitHub Setting up the correct toolchain for your build environment Setting up authentication to your cloud provider You can write your own actions, or you can find actions to use in your workflows in the GitHub Marketplace.

##### 5. Runners (where your workflow runs)
A runner is a server that runs your workflows when they're triggered. Each runner can run a single job at a time. GitHub provides Ubuntu Linux, Microsoft Windows, and macOS runners to run your workflows. Each workflow run executes in a fresh, newly-provisioned virtual machine. GitHub also offers larger runners, which are available in larger configurations. For more information, see Using larger runners. If you need a different operating system or require a specific hardware configuration, you can host your own runners.

#### Github Actions Quickstart documentation

##### 1. Using Workflow templates 
These workflow templates are designed to help you get up and running quickly, offering a range of configurations such as: CI: Continuous Integration workflows Deployments: Deployment workflows Automation: Automating workflows Code Scanning: Code Scanning workflows Pages: Pages workflows (You can check them out)
##### 2. Creating your first workflow
You can give the workflow file any name you like, but you must use .yml or .yaml as the file name extension. YAML is a markup language that's commonly used for configuration files.