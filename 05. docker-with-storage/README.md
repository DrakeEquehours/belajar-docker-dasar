# Penyimpanan di Docker
## Docker Volume

### Build Aplikasi NLP terbaru
```
docker build -t USERNAME/nlp-server:v2 ./"05. docker-with-storage"/app
```
### Jalankan Container
```
docker run -d -p 5000:3000 --name nlp-server-v2 equehours/nlp-server:v2
```
### Mounting data
#### Menjalankan dengan volume
```
docker run -d -p 5000:3000 -v history-request:/app/data --name nlp-server-v2 equehours/nlp-server:v2
```
#### Menjalankan tanpa volume
```
docker run -d -p 5000:3000 -v --name nlp-server-v2 equehours/nlp-server:v2
```