const express = require('express')
const path = require('path');
const app = express()
const port = 3001

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname+'/views/home.html'))
})
app.listen(port, '0.0.0.0',  () => {
  console.log(`This app listening on port ${port}`)
})