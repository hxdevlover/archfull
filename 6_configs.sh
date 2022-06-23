#!/bin/bash

cp -r $HOME/archfull/configs/* $HOME/.config/

cp $HOME/archfull/.xprofile $HOME/

sudo rm -rf /etc/xdg/picom.conf
sudo cp $HOME/archfull/picom.conf /etc/xdg/
