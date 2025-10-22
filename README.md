| Command                                                        | Description                                                                                                              |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `docker compose -f docker-compose.dev.yml up -d`               | 🟢 Builds (if needed) and starts all services **in detached mode (background)** using the `docker-compose.dev.yml` file. |
| `docker compose -f docker-compose.dev.yml ps`                  | 📋 Lists all **currently running containers** defined in the compose file.                                               |
| `docker compose -f docker-compose.dev.yml ps -a`               | 📋 Lists **all containers (running + stopped)** for the compose project.                                                 |
| `docker compose -f docker-compose.dev.yml exec django_project` | 🧑‍💻 Opens an **interactive shell** (by default `/bin/sh` or `/bin/bash`) **inside the `django_project` container**.    |
| `docker compose -f docker-compose.dev.yml stop`                | 🛑 **Stops** all running containers **without removing** them (they can be restarted).                                   |
| `docker compose -f docker-compose.dev.yml start`               | ▶️ **Restarts previously stopped containers** without rebuilding or re-creating them.                                    |
| `docker compose -f docker-compose.dev.yml down`                | 🧹 **Stops and removes** all containers, networks, and temporary volumes created by the compose project.                 |
