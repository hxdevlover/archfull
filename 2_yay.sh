#!/bin/bash

mkdir $HOME/tmp
sudo pacman -S --noconfirm --needed base-devel git
git clone https://aur.archlinux.org/yay.git $HOME/tmp
sudo chown -R  hx:hx $HOME/tmp/yay
cd $HOME/tmp/yay
makepkg -si
