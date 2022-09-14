const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const mySql = require('mysql');
const app = express();

const jsonTransmissoes = require('../jsonScrap/Json_Transmissoes.json');
const { json, response } = require('express');

const db = mySql.createPool({
    host: 'localhost',
    user: 'root',
    password: '',
    database: 'transmissoes'
})

app.use(cors());
app.use(express.json());
app.use(bodyParser.urlencoded({ extended: true }));




app.get("/api/get", (req, res) => {
    //Pega transmissoes do banco de dados
    const sqlSelect = "SELECT * FROM tablepartidas";
    db.query(sqlSelect, (err, result) => {
        res.send(result)
    })
})

app.post("/api/insert", (req, res) => {
    //Insere informações no banco de dados

    for (const propriedade in jsonTransmissoes) {
        //Chave => propriedade; Valor => json[propriedade]
        let confronto = propriedade;
        let transmissao = jsonTransmissoes[propriedade];
        const sqlInsert = "INSERT INTO tablepartidas (Equipes, Transmissao) VALUES (?, ?)";

        db.query(sqlInsert, [confronto, transmissao], (err, result) => {
            console.log(result);
        })
    }


})

app.delete("/api/delete", (req, res) => {
    //Deleta informações no banco de dados
})

app.put("/api/update", (req, res) => {
    //Atualiza informações no banco de dados
})

console.log(jsonTransmissoes)
app.listen(3333, () => {

    console.log('Server is running on port 3333')

});