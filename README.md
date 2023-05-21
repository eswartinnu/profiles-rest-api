# Creating the first project for Django

Installed VirtualBox and Vagrant before proceeding to the project

Virtual box: [link] https://www.virtualbox.org/wiki/Downloads
Vagrant: [link] https://releases.hashicorp.com/vagrant/2.3.6/ 
Note: Git terminal and Vagrant terminal must be different. Git is not configured in vagrant.

Step 1: created a Git Repository

Step 2: Created a vagrant file using "vagrant init ubuntu/bionic64" at parent repository

Step 3: Move to vagrant -> create a vagrant file with an OS in it
        Command We used: vagrant init ubuntu/bionic64

Step 4: Configure the vagrant file and up the vagrant system

        ```
        # -*- mode: ruby -*-
        # vi: set ft=ruby :

        # All Vagrant configuration is done below. The "2" in Vagrant.configure
        # configures the configuration version (we support older styles for
        # backwards compatibility). Please don't change it unless you know what
        # you're doing.
        Vagrant.configure("2") do |config|
        # The most common configuration options are documented and commented below.
        # For a complete reference, please see the online documentation at
        # https://docs.vagrantup.com.
        
        # Every Vagrant development environment requires a box. You can search for
        # boxes at https://vagrantcloud.com/search.
        config.vm.box = "ubuntu/bionic64"
        config.vm.box_version = "~> 20200304.0.0"
        
        config.vm.network "forwarded_port", guest: 8000, host: 8000
        
        config.vm.provision "shell", inline: <<-SHELL
            systemctl disable apt-daily.service
            systemctl disable apt-daily.timer
        
            sudo apt-get update
            sudo apt-get install -y python3-venv zip
            touch /home/vagrant/.bash_aliases
            if ! grep -q PYTHON_ALIAS_ADDED /home/vagrant/.bash_aliases; then
            echo "# PYTHON_ALIAS_ADDED" >> /home/vagrant/.bash_aliases
            echo "alias python='python3'" >> /home/vagrant/.bash_aliases
            fi
        SHELL
        end
        ```
        Command: vagrant up


Step 5: Work under vagrant machine
        Command: vagrant ssh
        For exit: exit

Step 6: Create a virtual env in vagrant machine so that all the deps are stored there and we can activate the same when required.
        Command: python -m venv ~/env
        Notes: Since /vagrant folder is in complete sync with out local folder we create venv out of the scope of our local machine and store it in root folder (~/env -> env is the venv)

Step 7: Activate the virtual env
        Command: source ~/env/bin/activate
        For exiting from this venv: deactivate

Step 8: Installing python packages
        - creating requirement.txt 
        Move to vagrant location: cd /vagrant
        Install all the requirements: pip install -r requirments.txt 