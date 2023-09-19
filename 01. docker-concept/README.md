# Konsep Dasar dan Instruksi Docker
#### By Ahmad Zein Al Wafi
## Image
A Docker image is a file used to execute code in a Docker container. Docker images act as a set of instructions to build a Docker container, like a template. Docker images also act as the starting point when using Docker. An image is comparable to a snapshot in virtual machine (VM) environments.
### ls
Melihat daftar image di docker
> docker image ls
### pull
Mengambil image dari hosting registry
> docker pull tensorflow/tensorflow
### push
Mengunggah docker image ke docker registry
> docker push docker.io/username/imagename
### rm 
Menghapus docker image
> docker rm IMAGE
## Container
A Docker container image is a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries and settings.
### ls
Melihat daftar container di docker
> docker container ls

> docker ps

> docker ps -a
### run 
Membuat dan menjalankan container dari image
> docker run --name CONTAINERNAME IMAGE
Run dapat memiliki banyak argumen, contohnya sebagai berikut
> docker run -it -p 8888:8888 tensorflow/tensorflow:latest-jupyter 
### stop
Menghentikan container dengan sopan
> docker container stop CONTAINER
### kill
Menghentikan container tanpa etika
> docker container kill CONTAINER
### restart
Menyalakan ulang container
> docker container restart CONTAINER
### port
Melihat port yang dipakai container
> docker container port CONTAINER
## Referensi Tambahan
- [What's the difference between docker stop and docker kill?](https://superuser.com/questions/756999/whats-the-difference-between-docker-stop-and-docker-kill)
- [Learn to build and deploy your distributed applications easily to the cloud with Docker](https://docker-curriculum.com/)