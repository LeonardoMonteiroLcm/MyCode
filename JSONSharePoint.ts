import { spfi, SPFx } from "@pnp/sp";
import "@pnp/sp/webs";
import "@pnp/sp/lists";
import "@pnp/sp/items";
import "@pnp/sp/fields"; // Importe o módulo de campos
import * as fs from "fs";
import { WebPartContext } from "@microsoft/sp-webpart-base";

// Caminho para o arquivo JSON
const jsonFilePath = "./data.json";

// Função para inicializar o contexto do SharePoint dentro de um projeto SPFx
export function initializeSP(context: WebPartContext)
{
    return spfi().using(SPFx(context));
}

// Lê e trata o arquivo JSON
let jsonData: any[];
try
{
    const fileContent = fs.readFileSync(jsonFilePath, "utf-8");
    jsonData = JSON.parse(fileContent);
    if (!Array.isArray(jsonData) || jsonData.length === 0)
    {
        throw new Error("O arquivo JSON deve conter um array de objetos.");
    }
}
catch (error)
{
    console.error("Erro ao ler o arquivo JSON:", error.message);
    process.exit(1);
}

// Obtém o nome da lista a partir do nome do arquivo (sem extensão)
const listName = jsonFilePath.split("/").pop()?.split(".")[0] ?? "DefaultList";

// Função para verificar se a lista já existe
async function listExists(sp: ReturnType<typeof spfi>, name: string): Promise<boolean>
{
    try
    {
        await sp.web.lists.getByTitle(name)();
        return true;
    }
    catch
    {
        return false;
    }
}

// Função para criar uma lista no SharePoint
async function createList(sp: ReturnType<typeof spfi>, name: string): Promise<void>
{
    try
    {
        await sp.web.lists.add(name, "", 100, false);
        console.log(`Lista '${name}' criada com sucesso.`);
    }
    catch (error)
    {
        console.error(`Erro ao criar a lista '${name}':`, error);
        throw error;
    }
}

// Função para adicionar colunas à lista
async function addColumnsToList(sp: ReturnType<typeof spfi>, listName: string, fields: Record<string, any>): Promise<void>
{
    const list = sp.web.lists.getByTitle(listName);

    for (const key of Object.keys(fields))
    {
        try
        {
            // Verifica se o campo já existe na lista
            const existingFields = await list.fields();
            const fieldExists = existingFields.some((f: { Title: string }) => f.Title === key);

            if (fieldExists)
            {
                console.log(`O campo '${key}' já existe na lista '${listName}'.`);
                continue;
            }

            // Adiciona uma nova coluna de texto à lista
            await list.fields.addText(key);
            console.log(`Campo '${key}' adicionado à lista '${listName}'.`);
        }
        catch (error)
        {
            console.error(`Erro ao adicionar campo '${key}':`, error);
        }
    }
}

// Função para adicionar itens à lista
async function addItemsToList(sp: ReturnType<typeof spfi>, name: string, items: any[]): Promise<void>
{
    const list = sp.web.lists.getByTitle(name);

    for (const item of items)
    {
        try
        {
            await list.items.add(item);
            console.log(`Item adicionado: ${JSON.stringify(item)}`);
        }
        catch (error)
        {
            console.error("Erro ao adicionar item:", error);
        }
    }
}

// Função principal para executar o fluxo
export async function main(context: WebPartContext)
{
    const sp = initializeSP(context); // Inicializa o contexto do SPFx

    try
    {
        const exists = await listExists(sp, listName);

        if (!exists)
        {
            await createList(sp, listName);
            await addColumnsToList(sp, listName, jsonData[0]);
        }
        else
        {
            console.log(`A lista '${listName}' já existe.`);
        }

        await addItemsToList(sp, listName, jsonData);
        console.log("Todos os itens foram adicionados com sucesso.");
    }
    catch (error)
    {
        console.error("Erro na execução do script:", error);
    }
}

// Simula um WebPartContext para testes
const mockContext: WebPartContext = {
    pageContext: {
        web: {
            absoluteUrl: "https://seusite.sharepoint.com", // Substitua pela URL do seu site
        },
    },
    // Outras propriedades do contexto podem ser simuladas aqui
} as WebPartContext;

// Chama a função main com o contexto simulado
main(mockContext)
    .then(() =>
    {
        console.log("Função main executada com sucesso.");
    })
    .catch((error) =>
    {
        console.error("Erro ao executar a função main:", error);
    });