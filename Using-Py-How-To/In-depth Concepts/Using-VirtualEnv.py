# Fix:: Unable to Install a Python Package on Linux: 

## Option 1: Use a Python virtual environment

- A virtual environment is the best practice for Python development. 
- It creates an isolated directory for your project, allowing you to install packages without affecting the global system.

```
sudo apt install python3-venv

Create Environment using module mode (-m)👇 
python3 -m venv <Environment-Name>

Activate the Environment 👇 
source <env-name>/bin/activate

```

## Option 2: Use pipx for standalone applications
- If you want to install <Pkg> as a standalone command-line application that is globally accessible, pipx is the tool for that purpose.

- eg. sudo apt install pipx > pipx install <pkg>

## Option 3: Force Installation of the Pkg
- eg. python3 -m pip install <pkg-name> --break-system-packages



