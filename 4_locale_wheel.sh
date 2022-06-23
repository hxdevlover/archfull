#!/bin/bash

sudo sed -i '177s/.//' /etc/locale.gen
sudo sed -i '233s/.//' /etc/locale.gen
sudo locale-gen

sudo gpasswd -a hx wheel
sudo sed -i '85s/.//' /etc/sudoers
