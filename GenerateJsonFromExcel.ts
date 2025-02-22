import * as XLSX from 'xlsx';
import * as fs from 'fs';

// Caminho para o arquivo Excel
const excelFilePath = 'XPTO.xlsx';

// Caminho para o arquivo JSON
const jsonFilePath = 'XPTO.json';

// Ler o arquivo Excel
const workbook = XLSX.readFile(excelFilePath);

// Selecionar a planilha "XPTO1"
const sheetName = 'XPTO1';
const worksheet = workbook.Sheets[sheetName];

// Converter a planilha para JSON
const data: any[][] = XLSX.utils.sheet_to_json(worksheet, { header: 1, range: 9 }); // range: 9 para começar da linha 10

// Array para armazenar os objetos JSON
const jsonArray: any[] = [];

// Iterar sobre as linhas da planilha
data.forEach((row: any[], index: number) => {
    const id = index + 10; // id é o número da linha no Excel (começando da linha 10)
    const number1 = row[1] !== undefined ? row[1] : -666; // Coluna B
    const string1 = row[2] !== undefined ? row[2] : '';   // Coluna C
    const string2 = row[3] !== undefined ? row[3] : '';   // Coluna D
    const string3 = row[4] !== undefined ? row[4] : '';   // Coluna E
    const string4 = row[5] !== undefined ? row[5] : '';   // Coluna F
    const string5 = row[6] !== undefined ? row[6] : '';   // Coluna G

    // Criar o objeto JSON
    const jsonObject = {
        "id": id,
        "number1": number1,
        "string1": string1,
        "string2": string2,
        "string3": string3,
        "string4": string4,
        "string5": string5
    };

    // Adicionar o objeto ao array
    jsonArray.push(jsonObject);
});

// Converter o array para JSON
const jsonString = JSON.stringify(jsonArray, null, 2);

// Escrever o JSON no arquivo "XPTO.json"
fs.writeFileSync(jsonFilePath, jsonString, 'utf8');

console.log('Arquivo JSON gerado com sucesso!');