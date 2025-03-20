install() {
	sudo apt install $@ -y
}

remove() {
	sudo apt remove $@ -y
}

alias upgrade="sudo apt update -y && sudo apt upgrade -y"


