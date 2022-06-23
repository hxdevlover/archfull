#!/bin/bash

fish
git clone --depth 1 https://github.com/doomemacs/doomemacs ~/.emacs.d
~/.emacs.d/bin/doom install
fish_add_path ~/.emacs.d/bin
doom sync

cp $HOME/archfull/emacsclient.desktop /usr/share/applications/
