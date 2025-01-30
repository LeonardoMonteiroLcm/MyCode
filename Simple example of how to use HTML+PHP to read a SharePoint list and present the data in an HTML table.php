<?php
// Configuração do SharePoint
$siteUrl = "https://seu-dominio.sharepoint.com/sites/seu-site";
$listName = "NomeDaLista";
$accessToken = "SEU_ACCESS_TOKEN"; // Obtenha um token válido

// URL da API para obter os itens da lista
$apiUrl = "$siteUrl/_api/web/lists/getbytitle('$listName')/items";

// Configurar a requisição cURL
$ch = curl_init($apiUrl);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    "Accept: application/json;odata=verbose",
    "Authorization: Bearer $accessToken"
]);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

// Executar a requisição
$response = curl_exec($ch);
curl_close($ch);

// Converter JSON para array PHP
$data = json_decode($response, true);
$items = $data['d']['results'] ?? [];
?>

<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lista do SharePoint</title>
    <style>
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { border: 1px solid black; padding: 8px; text-align: left; }
        th { background-color: #f4f4f4; }
    </style>
</head>
<body>
    <h2>Dados da Lista do SharePoint</h2>
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Título</th>
                <th>Outro Campo</th>
            </tr>
        </thead>
        <tbody>
            <?php foreach ($items as $item): ?>
                <tr>
                    <td><?= htmlspecialchars($item['ID']) ?></td>
                    <td><?= htmlspecialchars($item['Title']) ?></td>
                    <td><?= htmlspecialchars($item['OutroCampo'] ?? 'N/A') ?></td>
                </tr>
            <?php endforeach; ?>
        </tbody>
    </table>
</body>
</html>
