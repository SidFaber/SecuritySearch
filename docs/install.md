# Installation Instructions

## WSL
Prerequisites when installing on WSL

1. Install Ubuntu from the Microsoft app store
1. Install Microsoft Visual Studio Code (download from the web site, single user version)
1. Launch Ubuntu and create a symlink to run VSCode from in WSL (check the executable directory)

```bash
cd ~/.local/bin
ln -s /mnt/c/Users/[userid]/AppData/Local/Programs/Microsoft\ VS\ Code/Code.exe code
```

## Installing on Ubuntu

1. Update and install pip

```bash
sudo apt-get update
sudo apt upgrade
sudo apt install python3-pip
```

2. Install flask

```bash
pip install flask
```

3. Set up your github keys
4. Clone the source code

```bash
mkdir -p ~/Workspace/SecuritySearch/src
cd ~/Workspace/SecuritySearch/src
git clone git@github.com:SidFaber/SecuritySearch.git
```

## Start the Web Server

```bash
cd ~/Workspace/SecuritySearch/src/SecuritySearch/src
./launch.sh
```
