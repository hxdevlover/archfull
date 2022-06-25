#!/usr/bin/fish

sudo pacman -Sy emacs
git clone --depth 1 https://github.com/doomemacs/doomemacs ~/.emacs.d
~/.emacs.d/bin/doom install
fish_add_path ~/.emacs.d/bin
doom sync
alias emacs "/usr/bin/emacsclient -c -a 'emacs'"
funcsave emacs

sudo cp $HOME/archfull/emacsclient.desktop /usr/share/applications/
