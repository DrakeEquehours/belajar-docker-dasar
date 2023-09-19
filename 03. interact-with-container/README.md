# Berinteraksi Dengan Container
#### By Ahmad Zein Al Wafi
## Docker Port
### Port forwarding
- --publish/-p : untuk mempublish port dari docker daemon

Publish dapat dilakukan dengan instruksi seperti berikut
> docker run -p HOSTPORT:DOCKERPORT --name belajar-docker USERNAME/IMAGENAME:TAG
## Docker Exec
- exec : masuk ke dalam container
- -i : menjaga input tetap aktif
- -t : alokasi untuk pseudo-TTY (akses terminal)
Docker Exec dapat dilakukan dengan instruksi berikut
> docker exec -it NAMACONTAINER
## Docker Logs
- -f : melihat log secara realtime
Log dari container dapat dilihat dengan instruksi berikut
```
docker container logs NAMACONTAINER
```

## Hands-on
Jalankan container dari image hasil 02. Dockerfile dengan menggunakan port forwarding
```
docker run -d -p 5000:3000 --name CONTAINERNAME USERNAME/IMAGENAME:TAG
```

Akses dengan URL seperti berikut ```localhost:5000/prediction/sentiment-analysis?sentence=Keep_learning_stay_awesome```

Jika JSON telah diterima, coba masuk ke ke container
```
docker exec -it CONTAINERNAME bash
```

Masuk ke folder app dan install nano sebagai code editor
```
apt-get update
apt-get install nano
```
Buka file ```app.py``` dengan code editor nano menggunakan instruksi ```nano app.py``` kemudian cari kode berikut 
```
@app.route('/prediction/sentiment-analysis', methods=['GET', 'POST'])
def sentiment_analysis():
```
Kita akan ubah endpointnya untuk melakukan eksperimen, maka ubahlah kode tadi seperti berikut
```
@app.route('/predict/sentiment', methods=['GET', 'POST'])
def sentiment_analysis():
```
Jalankan ulang container
```
docker restart CONTAINERNAME
```
Kemudian akses dengan URL seperti berikut ```localhost:5000/prediction/sentiment-analysis?sentence:Keep_learning_stay_awesome```

Niscaya akan menghasilkan JSON seperti berikut
```
{message: url not found}
```
Namun jika diakses dengan URL seperti berikut ```localhost:5000/predict/sentiment?sentence=Keep_learning_stay_awesome```

Niscaya akan tidak akan menghasilkan error dan dibalas dengan prediksi sentimennya. 
```
{"label":"POSITIVE","score":0.999859094619751}
```
Namun jika container itu dihentikan kemudian dijalankan kembali apakah perubahan yang tadi akan disimpan? Selamat mencoba

