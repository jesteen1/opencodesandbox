# Docker Setup & Usage Guide

Follow these instructions to build and run the application using **Docker Compose**.

---

## Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running on your system.
- [Git](https://git-scm.com/) installed (to clone the repository).

---

## Getting Started

### 1. Clone the Repository
Open your terminal (PowerShell, Command Prompt, or Linux/macOS terminal) and clone the repository:
```bash
git clone <YOUR-REPOSITORY-URL>
cd <YOUR-REPOSITORY-FOLDER>
```

---

### 2. Build the Docker Image
To compile and build the Docker image with Docker Compose, run:

```bash
docker compose up opencodesandbox --build
```

> **Note:** The `--build` flag ensures Docker compiles the latest version of your `Dockerfile` and dependencies before starting the service.

---

### 3. Run the Application Interactively
To launch and attach to the interactive `opencode` environment inside the container, run:

```bash
docker compose run opencodesandbox
```

---

## Quick Reference

| Action | Command |
| :--- | :--- |
| **Build & Start** | `docker compose up opencodesandbox --build` |
| **Run Interactively** | `docker compose run opencodesandbox` |
| **Stop Stack** | `docker compose down` |