# CONST

ERROR_REQUIRES_ARG="Error: requires an argument"

# WELCOME

# PATHS

export PATH="$PATH:~/Qt/Tools/QtCreator/bin"
export PATH=$HOME/.local/bin:$PATH

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

detach() {
	$@ &
	disown
}

drawio() {
	outnull detach ~/.local/drawio.AppImage
}
recpp() {
  clear && c++ *.cpp && ./a.out
}

basegitignore() {
  cp $HOME/.MyShellEnv/files/basegitignore ./.gitignore
}

basemakefile() {
  cp $HOME/.MyShellEnv/files/basemakefile ./Makefile
}

filelinesep() {
  python3 $HOME/.MyShellEnv/scripts/file_line_sep.py $@
}

builddojo() {
  python3 $HOME/.MyShellEnv/scripts/build_dojo_dir.py $@
}

processgrep() {
  ps aux | grep $@ | grep -v "grep"
}

i2pstart() {
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
  for ((i = 1; i <= $1; i++)); do
    parent+="../"
  done
  cd "$parent"
}

# alias

alias p="python3"
alias pymenv="python3 -m venv venv"
alias pyenv="source venv/bin/activate"
alias pipr="pip install -r requirements.txt"

alias rm="gio trash"

alias Obsidian="nohup ~/.local/bin/Obsidian-1.8.7.AppImage &"
alias Joplin="nohup ~/.local/bin/Joplin-3.2.12.AppImage &"

alias sozsh="source ~/.zshrc"
alias sobash="source ~/.bashrc"

alias nv="nvim"

# current

source ~/.MyShellEnv/debian.sh
