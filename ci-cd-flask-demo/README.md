# Flask CI/CD Demo

Minimal Flask API with a full GitHub Actions pipeline demonstrating:

- Lint → Test → Security scan (parallel) → Build/Push → Manual-gated Deploy
- Immutable image tagging (git SHA, not `latest`)
- SAST (bandit) + dependency/image scanning (Trivy)
- Secrets management via GitHub Actions secrets (no hardcoded credentials)
- Environment protection rule for production approval gate

## Pipeline

```
lint ─┬─> test ────┐
      └─> security ┴─> build-and-push (GHCR) ─> deploy (manual approval)
```

## Local run

```bash
pip install -r requirements-dev.txt
pytest -v
flake8 app.py tests/

docker build -t flask-cicd-demo .
docker run -p 5000:5000 flask-cicd-demo
curl localhost:5000/health
```

## Setup for full pipeline

1. Push to a GitHub repo.
2. Settings → Environments → create `production` → add yourself as required reviewer.
3. (Optional, for real deploy) add repo secrets: `DEPLOY_HOST`, `DEPLOY_SSH_KEY`.
4. Push to `main` → watch Actions tab.