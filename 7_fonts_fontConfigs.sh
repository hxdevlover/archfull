#!/bin/bash

mkdir $HOME/.local/share/fonts
mkdir $HOME/.config/fontconfig/

cp -r $HOME/archfull/fonts/* $HOME/.local/share/fonts
cp $HOME/archfull/fonts.conf $HOME/.config/fontconfig/
