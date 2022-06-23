#!/bin/bash
sudo pacman -S base-devel git curl
mkdir $HOME/tmp
sudo pacman -S --noconfirm --needed base-devel git
git clone https://aur.archlinux.org/yay.git $HOME/tmp/yay
sudo chown -R  hx:hx $HOME/tmp/yay
cd $HOME/tmp/yay
makepkg -si
