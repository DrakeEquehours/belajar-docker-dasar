# Instalasi Docker Windows
### By Ahmad Zein Al Wafi
## Konfigurasi WSL
### Introduction
The Windows Subsystem for Linux lets developers run a GNU/Linux environment -- including most command-line tools, utilities, and applications -- directly on Windows, unmodified, without the overhead of a traditional virtual machine or dualboot setup.
### Step
#### Update WSL 2
Unduh berkas exe dari (link berikut)[https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi]
#### Konfigurasi
- Run PowerShell as Administrator
- Salin instruksi di bawah ini ke PowerShell

- > dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
- > dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
- > wsl --set-default-version 2
- > wsl --list --all
- > wsl --install -d Ubuntu-22.04
####
Unduh docker desktop pada [link berikut](https://www.docker.com/products/docker-desktop/)
