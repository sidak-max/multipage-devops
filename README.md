# Multi-page App

Three Flask versions with separate Git commits and tags:

| Version | Behavior | Local URL |
| --- | --- | --- |
| v1 | Home page only; `/about` returns 404 | http://localhost:8084 |
| v2 | Home and About; no navigation links | http://localhost:8082 |
| v3 | Home and About linked by navigation | http://localhost:8083 |

Jenkins already occupies port 8081 on this laptop, so v1 uses 8084.

## Pipeline

Create a Jenkins Pipeline job using **Pipeline script from SCM**, Git repository
`https://github.com/sidak-max/multipage-devops.git`, branch `*/main`, and script path
`Jenkinsfile`. A Windows agent needs Git, Docker and kubectl on PATH, access to the
Docker engine, and a kubeconfig for the intended local cluster. Configure the
DockerHub username/password credential as `dockerhub-creds` (use an access token
as the password). Do not commit credentials.

The pipeline checks out source, builds and pushes the three image tags, applies
the manifests, and waits for all deployments to become ready. The manifests use
`sidaksingh1/multipage-app:v1`, `:v2`, and `:v3`.

## Manual verification

```powershell
kubectl get nodes
kubectl get deployments,pods,services
kubectl rollout status deployment/multipage-v1
kubectl rollout status deployment/multipage-v2
kubectl rollout status deployment/multipage-v3
Invoke-RestMethod http://localhost:8084/health
Invoke-RestMethod http://localhost:8082/health
Invoke-RestMethod http://localhost:8083/health
```

All three images were built locally, pushed to DockerHub, deployed to Kubernetes,
and verified on localhost on 2026-10-29. The updated Jenkinsfile still requires an
actual Jenkins job run; manual build/deployment does not establish pipeline success.
