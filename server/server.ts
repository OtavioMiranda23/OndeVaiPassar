import {Request, Response} from 'express';
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
    database: 'transmissoesserieb'
})

app.use(cors());
app.use(express.json());
app.use(bodyParser.urlencoded({ extended: true }));


app.get("/api/get", (req: Request, res: Response) => {
    //Pega transmissoes do banco de dados
    const sqlSelect = "SELECT * FROM tablepartidas";
    db.query(sqlSelect, (err: Error, result: String ) => {
        res.send(result)
    })
})

app.post("/api/insert", (req: Request, res: Response) => {
    //Insere informações no banco de dados

    for (const propriedade in jsonTransmissoes) {
        //Chave => propriedade; Valor => json[propriedade]
        let confronto = propriedade;
        let transmissao = jsonTransmissoes[propriedade];
        const sqlInsert = "INSERT INTO table_serie_b (Equipes, Transmissao) VALUES (?, ?)";

        db.query(sqlInsert, [confronto, transmissao], (err: Error, result: String) => {
            console.log(result);
        })
    }


})

app.delete("/api/delete", (req: Request, res: Response) => {
    //Deleta informações no banco de dados
})

app.put("/api/update", (req: Request, res: Response) => {
    //Atualiza informações no banco de dados
})

console.log(jsonTransmissoes)
app.listen(3333, () => {

    console.log('Server is running on port 3333')

});