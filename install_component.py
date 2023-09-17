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

def install_aws_cli():
    subprocess.run(["curl", "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip", "-o", "awscliv2.zip"])
    subprocess.run(["unzip", "-o", "awscliv2.zip"])
    subprocess.run(["sudo", "./aws/install"])

def install_nginx():
    subprocess.run(["sudo", "apt-get", "install", "-y", "nginx"])
    subprocess.run(["sudo", "systemctl", "start", "nginx"])
    subprocess.run(["sudo", "systemctl", "enable", "nginx"])

def uninstall_all():
    subprocess.run(["sudo", "apt-get", "purge", "-y", "docker.io", "docker-compose", "nginx"])
    subprocess.run(["sudo", "rm", "-rf", "/usr/local/aws", "/usr/local/bin/aws"])

def check_and_install_unzip():
    try:
        subprocess.run(["unzip", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except FileNotFoundError:
        print("'unzip' command not found. Installing 'unzip'...")
        subprocess.run(["sudo", "apt-get", "install", "-y", "unzip"])
        print("'unzip' has been installed.")

def check_command_exists(command):
    try:
        subprocess.run([command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except FileNotFoundError:
        return False

def uninstall(args):
    uninstall_all()

def uninstall_and_install(args):
    if args.uninstall:
        uninstall(args)
    
    check_and_install_unzip()

    install_docker()
    install_docker_compose()
    install_aws_cli()
    install_nginx()

def main():
    parser = argparse.ArgumentParser(description="Install and uninstall Docker, Docker Compose, AWS CLI, and Nginx.")
    parser.add_argument("--uninstall", action="store_true", help="Uninstall all components before installing.")
    args = parser.parse_args()

    uninstall_and_install(args)

if __name__ == "__main__":
    main()
