# Update and install snap
apt update
apt install snapd
# Install apps
snap install discord-canary
snap install --classic code
snap install brave
# Edit .vimrc
cd $HOME
# Edit .bashrc
echo 'export PS1="\[\033[01;32m\]\@\[\033[00m\] | \[\033[01;34m\]\W\[\033[00m\] $ "' >> .bashrc
# Map keys
#apt-get install x11-xkb-utils
#setxkbmap -option caps:backspace
#setxkbmap -option backspace:caps
#setxkbmap -option tab:swapescape
#setxkbmap -option swapescape:tab
