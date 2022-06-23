#!/bin/bash

mkdir $HOME/.config/kitty
cp $HOME/archfull/configs/kitty/kitty.conf $HOME/.config/kitty
git clone --depth 1 https://github.com/dexpota/kitty-themes.git ~/.config/kitty/kitty-themes
cd ~/.config/kitty
ln -s ./kitty-themes/themes/Monokai.conf ~/.config/kitty/theme.conf
