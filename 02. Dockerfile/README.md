# Dockerfile
#### By Ahmad Zein Al Wafi
## Membuat Image
### Build
```
docker build -t USERNAME/IMAGENAME:TAG ./app
```
### Mengecek image saat ini
```
docker image ls
``` 
### Menjalankan container
- --name : nama container
- -d : membebaskan terminal client dari container yang berjalan
```
docker container run -d --name USERNAME-nlp-server USERNAME/IMAGENAME:TAG
```
## Referensi tambahan
- [Intro Guide to Dockerfile Best Practices](https://www.docker.com/blog/intro-guide-to-dockerfile-best-practices/)