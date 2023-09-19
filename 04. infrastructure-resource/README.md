# Mengelola sumber daya infrastruktur
#### By Ahmad Zein Al Wafi

## Melihat statistik penggunaan sumber daya
```
docker container stats
```
## Membatasi penggunaan sumber daya container
- --memory : membatasi memori yang digunakan
- --cpus : membatasi jumlah cpu yang digunakan
```
docker container create --name nlp-server -p 5000:3000 --memory 200m --cpus 1.5 equehours/nlp-server:v1
```