import subprocess
import argparse
import sys

def install_docker():
    subprocess.run(["sudo", "apt-get", "update"])
    subprocess.run(["sudo", "apt-get", "install", "-y", "docker.io"])
    subprocess.run(["sudo", "systemctl", "start", "docker"])
    subprocess.run(["sudo", "systemctl", "enable", "docker"])

def install_docker_compose():
    subprocess.run(["sudo", "apt-get", "install", "-y", "docker-compose"])

def uninstall_all():
    subprocess.run(["sudo", "apt-get", "purge", "-y", "docker.io", "docker-compose"])
    subprocess.run(["sudo", "rm", "-rf", "/usr/local/aws", "/usr/local/bin/aws"])

def uninstall(args):
    uninstall_all()

def main():
    parser = argparse.ArgumentParser(description="Install and uninstall Docker and Docker Compose.")
    parser.add_argument("--uninstall", action="store_true", help="Uninstall all components before installing.")
    args = parser.parse_args()

    if args.uninstall:
        uninstall(args)
    else:
        install_docker()
        install_docker_compose()

if __name__ == "__main__":
    main()
