# Docker Setup & Usage Guide

Follow these instructions to build and run the application using **Docker Compose**.

---

## Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running on your system.
- [Git](https://git-scm.com/) installed (to clone the repository).

---

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/jesteen1/opencodesandbox.git
cd opencodesandbox
```

### 2. Build the Docker Image
```bash
docker compose build opencodesandbox
```

> **Note:** This command builds or rebuilds the Docker image for the `opencodesandbox` service using the latest `Dockerfile` and dependencies without starting it immediately.

### 3. Run the Application Interactively
```bash
docker compose run opencodesandbox
```

### 4. Stop the Docker Container / Server
To stop and clean up containers or running services:
```bash
docker compose down
```

> **Note:** `docker compose down` gracefully stops running containers and cleans up the associated networks and resources.

---

## Workspace

All files created, edited, or used by **OpenCode AI** live in the `workspace/` folder.

- On your machine: `./workspace` (in the project root)
- Inside the container: `/workspace`

The folder is mounted as a volume, so:

- Files OpenCode generates appear in `./workspace` on your host.
- Anything you put in `./workspace` is immediately visible to OpenCode.
- Your files **persist** after the container stops or is removed.

> **Tip:** Put the project you want OpenCode to work on inside `workspace/`. Files outside this folder are not accessible to the container.

---

## Quick Reference

| Action | Command |
| :--- | :--- |
| **Build Image** | `docker compose build opencodesandbox` |
| **Run Interactively** | `docker compose run opencodesandbox` |
| **Stop Container / Server** | `docker compose down` |
| **Workspace Location** | `./workspace` (host) → `/workspace` (container) |
