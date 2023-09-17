# Installation Script

This script allows you to install and uninstall various software components on your Linux system, including 
- Docker
- Docker Compose
It provides an option to uninstall and then reinstall these components.

## Prerequisites

- A Linux-based operating system (tested on Ubuntu).

## Usage

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/CyrilBaah/componentInstaller.git
    cd componentInstaller
    ```

2. Make the script executable:
    ```bash
    chmod +x install_component.py
    ```

3. Run
    ```bash
    python3 install_component.py
    ```

4. Uninstall
    ```bash
    python3 install_component.py --uninstall
    ```
