# 🐳 GitLab CI/CD & Docker Container Registry Milestone

Welcome to my learning repository! This document tracks my progress, technical implementation, and hands-on practice for mastering **Dockerized CI/CD pipelines using GitLab CI**.

---

## 🎯 Milestone Goal
Automate the build, tagging, and publication of an application's Docker image to the **GitLab Container Registry** upon every `git push`.

### 🔄 The Pipeline Workflow
```
Git push
   ↓
GitLab CI (Runner triggers)
   ↓
Build Docker image locally
   ↓
Tag image dynamically (latest & $CI_COMMIT_SHA)
   ↓
Push to GitLab Container Registry
```

---

## 🛠️ Step 1: Project Source Files
To practice this milestone, I configured three essential files in the root of my project directory.

### 1. The Application File (`index.html`)
A basic entry point file to verify that content changes compile correctly.
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>GitLab CI/CD Practice</title>
</head>
<body>
    <h1>🚀 Hello World from GitLab CI/CD & Docker!</h1>
    <p>This image was automatically built and pushed by the pipeline.</p>
</body>
</html>
```

### 2. The Docker Environment (`Dockerfile`)
An production-ready multi-stage config or lightweight web server configuration using Nginx Alpine.
```dockerfile
FROM nginx:1.27-alpine
COPY index.html /usr/share/nginx/html/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

---

## 🚀 Step 2: The GitLab CI/CD Pipeline Code

Create a `.gitlab-ci.yml` file in your root folder. This pipeline uses **Docker-in-Docker (DinD)** to spin up a Docker engine inside the runner context securely.

```yaml
stages:
  - build

build_docker:
  stage: build
  image: docker:27.3.1  # The Docker client container
  services:
    - docker:27.3.1-dind  # The background Docker daemon service
  variables:
    DOCKER_TLS_CERTDIR: "/certs"  # Secures communication between daemon and client
  before_script:
    # Authenticate to GitLab's built-in registry using pre-defined system tokens
    - echo "$CI_REGISTRY_PASSWORD" | docker login $CI_REGISTRY -u $CI_REGISTRY_USER --password-stdin
  script:
    # 1. Build and apply dual tags: 'latest' for convenience, and the unique commit SHA for immutability
    - docker build -t $CI_REGISTRY_IMAGE:latest -t $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA .
    
    # 2. Upload both versions to the GitLab Container Registry
    - docker push $CI_REGISTRY_IMAGE:latest
    - docker push $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
```

---

## 🧪 Step 3: Verification & Best Practices

### Pre-requisites Checklist
* [ ] **Enable Registry:** Navigate to **Settings > General > Visibility, project features and permissions** in GitLab and confirm **Container Registry** is active.
* [ ] **Runners Available:** Ensure shared runners or a private GitLab Runner is configured to support Docker services.

### Immutability & Rolling Back
* **`myapp:latest`**: Used for pulling the absolute newest build instantly.
* **`myapp:$CI_COMMIT_SHA`**: Ensures production builds are fully traceable to the precise Git commit history, making immediate deployments rollbacks deterministic and safe.

---

### 📝 Reflections & Learning Notes
* Pre-defined variables such as `$CI_REGISTRY_IMAGE`, `$CI_REGISTRY_USER`, and `$CI_REGISTRY_PASSWORD` prevent the need to manually store hardcoded credentials inside CI variables.
* Incorporating DinD allows isolating container execution contexts cleanly between unique runner pipeline jobs.