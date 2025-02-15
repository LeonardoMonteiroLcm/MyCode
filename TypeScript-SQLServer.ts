import { ConnectionPool, config, IResult, Request } from "mssql";

namespace SqlServerEnvironment
{
    export const databaseConfig: config = {
        server: process.env.DB_SERVER || "my_dev_server",
        user: process.env.DB_USER || "my_dev_user",
        password: process.env.DB_PASSWORD || "my_dev_password",
        database: process.env.DB_NAME || "my_dev_database",
        options: {
            encrypt: true,
            trustServerCertificate: process.env.DB_TRUST_CERT === "true",
        },
    };

    export const queryUsers: string = process.env.DB_QUERY_ALL_USERS || "SELECT * FROM Users";
}

namespace SqlServer
{
    let pool: ConnectionPool | null = null;

    const cleanup = async () =>
    {
        if (pool)
        {
            await pool.close();
            console.log("SQL Server connection closed.");
        }
    };

    process.on("exit", cleanup);
    process.on("SIGINT", cleanup);
    process.on("SIGTERM", cleanup);

    async function connectDatabase(): Promise<ConnectionPool>
    {
        if (!pool)
        {
            pool = new ConnectionPool(SqlServerEnvironment.databaseConfig);
            await pool.connect();
            console.log("Connected to SQL Server successfully!");
        }
        return pool;
    }

    async function executeQuery(query: string): Promise<IResult<any>>
    {
        const pool = await connectDatabase();
        try
        {
            console.log(`Executing query: ${query}`);
            const request: Request = pool.request();
            const result = await request.query(query);
            console.log(`Query executed successfully. Rows returned: ${result.recordset.length}`);
            return result;
        }
        catch (error)
        {
            console.error("Query execution error:", error);
            throw new Error("Failed to execute query.");
        }
    }

    async function getQueryData(query: string): Promise<any[]>
    {
        const result = await executeQuery(query);
        return result.recordset ?? [];
    }

    export async function getQueryJSON(query: string): Promise<string>
    {
        try
        {
            const data = await getQueryData(query);
            return JSON.stringify(data, null, 4);
        }
        catch (error)
        {
            console.error("Error getting JSON from query:", error);
            throw new Error("Failed to convert query result to JSON.");
        }

    }
}

(async () =>
{
    try
    {
        console.log("Testing getQueryJSON()...");
        const json = await SqlServer.getQueryJSON(SqlServerEnvironment.queryUsers);
        console.log(json);
    }
    catch (error)
    {
        console.error("Error fetching query JSON:", error);
    }
})();

