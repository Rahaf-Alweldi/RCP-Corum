sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update -y
sudo apt install python3-pip -y
sudo apt install python3.8 -y
sudo apt install python3.8-distutils -y

# install awscli
sudo apt  install awscli -y

# install virtual env
sudo apt install python3-venv -y

# create virtual env
python3 -m venv venv
source venv/bin/activate

# Install dependencies
sudo apt-get install python3-bs4 -y
pip install -r requirements.txt

deactivate