# CONST

ERROR_REQUIRES_ARG="Error: requires an argument"

# WELCOME

date

# PATHS
export PATH="$PATH:~/Qt/Tools/QtCreator/bin"

# docker 

alias dock_prune="docker system prune -a"
alias dock_stop="docker stop $(docker ps -q)"

# github

alias gl="git log"
alias gd="git diff"
alias gs="git status"

alias ga="git add"
alias gc="git commit -m"
alias gp="git push"

alias gca="git commit --amend"

alias grmc="git rm --cached"

alias gitsubmoduleup="git submodule update --init --recursive"

gt() {
	if [ -z $1 ]; then
		echo $ERROR_REQUIRES_ARG
	else
		ga . && gc "$1" && git push
	fi
}


# Command functions

file_line_sep(){
	python3 $HOME/.MyShellEnv/scripts/file_line_sep.py $@
}

build_dojo_dir(){
	python3 $HOME/.MyShellEnv/scripts/build_dojo_dir.py $@
}

process_grep(){
	ps aux | grep $@ | grep -v "grep"
}

i2p_start(){
	$HOME/.MyShellEnv/scripts/i2p_start.sh
}

stderrnull() {
	"$@" 2>/dev/null
}

stdoutnull() {
	"$@" 1>/dev/null
}

outnull() {
	"$@" 2>/dev/null 1>/dev/null
}

touchx() {
	touch "$@" && chmod u+x "$@"
}

cdup() {
	parent=""
	for ((i=1; i<=$1; i++));
	do
		parent+="../"
	done;
	cd "$parent"
}

# alias

alias rm="gio trash"

alias reset_dns='echo "nameserver 1.1.1.1" | sudo tee /etc/resolv.conf'

alias p="python3"

alias set_gnome_icons="gsettings set org.gnome.desktop.interface icon-theme"

alias Obsidian="nohup ~/.local/bin/Obsidian-1.8.7.AppImage &"
alias Joplin="nohup ~/.local/bin/Joplin-3.2.12.AppImage &"

# dnf

install() {
	sudo dnf install $1 -y
}

alias remove="sudo dnf remove"
alias upgrade="sudo dnf upgrade -y"


