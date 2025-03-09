install() {
	sudo apt install $@ -y
}

remove() {
	sudo apt remove $@ -y
}

upgrade() {
	sudo apt update -y apt upgrade -y
}

