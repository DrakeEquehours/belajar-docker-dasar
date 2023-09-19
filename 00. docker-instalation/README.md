# Instalasi Docker Windows
#### By Ahmad Zein Al Wafi
## Konfigurasi WSL
### Perkenalan
 Windows Subsistem untuk Linux (WSL) memungkinkan pengembang menjalankan lingkungan GNU/Linux -- termasuk sebagian besar alat, utilitas, dan aplikasi baris perintah -- langsung di Windows, tanpa modifikasi, tanpa overhead mesin virtual tradisional atau pengaturan dualboot.
### Langkah - Langkah
#### Memperbarui WSL 
- Unduh berkas exe dari [link berikut](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi)
- Install berkas yang tadi telah diunduh
#### Konfigurasi WSL dan Windows
- Jalankan PowerShell as Administrator
- Salin instruksi di bawah ini ke PowerShell
- > dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
- > dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
- > wsl --set-default-version 2
- > wsl --list --all
- > wsl --install -d Ubuntu-22.04
#### Unduh Docker Desktop for Windows
- Unduh docker desktop pada [link berikut](https://www.docker.com/products/docker-desktop/)
#### Instalasi Docker Desktop
- Buka berkas DockerDesktopInstaller.exe
- Lakukan instalasi Docker Desktop
- Restart Laptop 
#### Verifikasi Instalasi Docker
Buka cmd lalu ketik instruksi di bawah ini 
> docker --version

Jika outputnya seperti ini
```
Docker version 24.0.5, build ced0996
```
Selamat, Anda berhasil melakukan instalasi Docker pada OS Windows kalian

### Referensi Lanjutan
- [Enable virtualization on Windows 11 PCs](https://support.microsoft.com/en-us/windows/enable-virtualization-on-windows-11-pcs-c5578302-6e43-4b4b-a449-8ced115f58e1)
- [How to install Linux on Windows with WSL](https://learn.microsoft.com/en-us/windows/wsl/install)
- [Set up a WSL development environment](https://learn.microsoft.com/en-us/windows/wsl/setup/environment)