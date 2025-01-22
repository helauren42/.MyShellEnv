ERROR_REQUIRES_ARG="Error: requires an argument"

# PATHS
export PATH="/home/helauren/.MyEnv/bin:$PATH"
export PATH="$PATH:~/Qt/Tools/QtCreator/bin"

# Command functions

touchx() {
	touch "$1" && chmod u+x "$1"
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

alias reset_dns='echo "nameserver 1.1.1.1" | sudo tee /etc/resolv.conf'

alias p="python3"

alias cg="sudo cyberghostvpn --connect --country-code BE"
alias cg_streaming="sudo cyberghostvpn --connect --country-code BE --streaming"
alias cg_torrent="sudo cyberghostvpn --connect --country-code BE --torrent"

alias set_gnome_icons="gsettings set org.gnome.desktop.interface icon-theme"

# dnf

install() {
	sudo dnf install $1 -y
}

alias remove="sudo dnf remove"
alias upgrade="sudo dnf upgrade -y"

# github

alias gl="git log"
alias gd="git diff"
alias gpull="git pull"
alias gs="git status"

alias ga="git add"
alias gc="git commit -m"
alias gp="git push"

gt() {
	if [ -z $1 ]; then
		echo $ERROR_REQUIRES_ARG
	else
		ga . && gc "$1" && gp
	fi
}

grmc() {
	if [ -z $1 ]; then
		echo $ERROR_REQUIRES_ARG
	else
		git rm --cached $1
	fi
}
