# Update and install snap
apt update
apt install snapd
# Dev tools needed for the other installments
snap install node --classic
snap install git-ubuntu --classic
# Git setup
git config --global user.name "Noah Lloyd"
git config --global user.email "noahlloydrobson@gmail.com"
# Brave browser
git clone https://github.com/brave/browser-laptop.git  
cd browser-laptop
npm install
# Brave extensions
npm install -g chrome-ext-downloader  
cd app\extensions  
ced hdokiejnpimakedhajhdlcegeplioahd
# Install apps
snap install discord
snap install spotify
# Vscode
snap install --classic code

# Edit .vimrc
###
# Edit .bashrc
echo 'export PS1="\[\033[01;32m\]\@\[\033[00m\] | \[\033[01;34m\]\W\[\033[00m\] $ "' >> $HOME/.bashrc
# Map keys | Currently not working
#apt-get install x11-xkb-utils
#setxkbmap -option caps:backspace
#setxkbmap -option backspace:caps
#setxkbmap -option tab:swapescape
#setxkbmap -option swapescape:tab

# Programming languages, and other dev tools
snap install python38

echo "Run *vscode-extensions.sh* without sudo"
