#!/bin/bash

# install rustup
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# install language servers
sudo pacman -Sy typescript-language-server typescript rust-analyzer python3 python-pip pyright

# install pyright
# rcommended to install anaconda3
pip3 install pyright mypy
