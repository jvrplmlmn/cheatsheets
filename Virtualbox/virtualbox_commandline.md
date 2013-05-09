# Virtualbox CommandLine

## Commands to create a Virtualbox VM running Ubuntu from the commandline in Mac OS X

### Example: Create, configure and start up an Ubuntu 13 VM

	VBoxManage createvm --name "Ubuntu 13.04 WKS" --register
	VBoxManage modifyvm "Ubuntu 13.04 WKS" --memory 256 --acpi on --boot1 dvd --nic1 bridged --bridgedadapter1 eth0
	VBoxManage createhd --filename Ubuntu_13_04_WKS.vdi --size 8000
	VBoxManage storagectl "Ubuntu 13.04 WKS" --name "IDE Controller" --add ide
	VBoxManage storageattach "Ubuntu 13.04 WKS" --storagectl "IDE Controller" --port 0 --device 0 --type hdd --medium Ubuntu_13_04_WKS.vdi
	VBoxManage storageattach "Ubuntu 13.04 WKS" --storagectl "IDE Controller" --port 1 --device 0 --tyoe dvddrive --medium /path_to_the_iso/ubuntu-13.04-server-amd64.iso
	VBoxManage modifyvm "Ubuntu 13.04 WKS" --vrde on
	VBoxHeadless --startvm "Ubuntu 13.04 WKS"
