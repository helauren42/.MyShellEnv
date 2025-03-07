 install() {
     sudo dnf install $1 -y
}

alias remove="sudo dnf remove"
alias upgrade="sudo dnf upgrade -y"

