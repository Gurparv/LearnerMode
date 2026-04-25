
"Computing Orchestration"
## Introduction to Kubernetes.
- Kubernetes is a container management system.
- It runs and manages containerized applications on a cluster (one or more servers)
- Often this is simply called "container orchestration"
- Sometimes shortened to K8s.

## Basic Use-case for Kubernetes:
- It can take 1 image and run multiple containers from it.
- It can place an internal load balancer in front of these containers.
- It can take another image and start 10 containers from it.
- Place a public load balancer in front of these containers. (coz its accessible from outside the cluster. )
- In festivals season, we see spike and want to grow our cluster we can do it.
- New Release ! Replace my containers with the new Image.
- Keep processing requests during the upgrade; upgrade my containers one at a time.