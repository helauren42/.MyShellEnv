# PATHS
export PATH="/home/helauren/.MyEnv/bin:$PATH"
export PATH="$PATH:~/Qt/Tools/QtCreator/bin"

# Command functions

touchx() {
	touch "$1" && chmod u+x "$1"
}

# github

alias ga="git add"
alias gc="git commit -m"
alias gp="git push"

gt() {
	ga . && gc "$1" && gp
}

alias gitcom="~/.MyShellEnv/bin/gitcom"

# Aliases

alias reset_dns='echo "nameserver 1.1.1.1" | sudo tee /etc/resolv.conf'

alias p="python3"

alias vpn_torrent="sudo cyberghostvpn --connect --country-code BE --torrent"

alias set_gnome_icons="gsettings set org.gnome.desktop.interface icon-theme"
