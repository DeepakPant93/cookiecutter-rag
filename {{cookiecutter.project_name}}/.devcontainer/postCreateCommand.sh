#! /usr/bin/env bash

# Install fish terminal
sudo apt update -y
sudo apt-get install fish -y

# Repo Initialization
make init-repo
git config --global --add safe.directory /workspaces/{{cookiecutter.project_name}}

# Install Dependencies
make reset-env
