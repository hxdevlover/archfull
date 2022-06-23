#! /bin/bash

echo "Installing Pkgs..."
# Bases
sleep 5; sudo pacman -Sy --needed --noconfirm base-devel git xorg lightdm lightdm-gtk-greeter lightdm-gtk-greeter-settings

# WMs & Needed Pkgs
sleep 5; sudo pacman -S --needed --noconfirm awesome qtile firefox nitrogen picom pcmanfm lxappearance rofi kitty volumeicon network-manager-applet python-pip htop emacs neovim polkit lxsession xdg-user-dirs

# Wallpapers & Themes
sleep 5; sudo pacman -S --needed --noconfirm materia-gtk-theme papirus-icon-theme archlinux-wallpaper arc-gtk-theme

# VPN & PDF & Compression pkgs
sleep 5; sudo pacman -S --needed --noconfirm alsa-utils pamixer unrar unzip p7zip xarchiver openvpn networkmanager-openvpn xreader

# Fonts
sleep 5; sudo pacman -S --needed --noconfirm ttf-roboto ttf-roboto-mono ttf-font-awesome ttf-ubuntu-font-family nerd-fonts-fira-code ttf-fira-code ttf-fira-mono adobe-source-code-pro-fonts adobe-source-han-sans-otc-fonts adobe-source-han-serif-otc-fonts noto-fonts-cjk noto-fonts-emoji

# Other useful pkgs
sleep 5; sudo pacman -S --needed --noconfirm bleachbit gvfs ntfs-3g vi vim nano galculator brightnessctl font-manager sxiv yt-dlp xorg-xclipboard xclip feh acpid jedi-language-server curl wget go ripgrep fd

# TouchPad
sleep 5; sudo pacman -S --needed --noconfirm xorg-xinput

sudo chsh -s /usr/bin/fish

pip install psutil
