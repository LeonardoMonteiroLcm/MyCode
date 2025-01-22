function validaCPF(ocpf)
{
	var cpf = ocpf.value;
	var erro = new String;
	var x, y, i;

	if (cpf.length < 11)
	{
		erro += "São necessários 11 dígitos para verificação do CPF! ";
	}

	var nonNumbers = /\D/;
	if (nonNumbers.test(cpf))
	{
		erro += "A verificação de CPF suporta apenas números! ";
	}

	if (cpf == "00000000000" ||
		cpf == "11111111111" ||
		cpf == "22222222222" ||
		cpf == "33333333333" ||
		cpf == "44444444444" ||
		cpf == "55555555555" ||
		cpf == "66666666666" ||
		cpf == "77777777777" ||
		cpf == "88888888888" ||
		cpf == "99999999999")
	{
		erro += "Número de CPF inválido!"
	}

	var a = [];
	var b = new Number;
	var c = 11;
	for (i = 0; i < 11; i++)
	{
		a[i] = cpf.charAt(i);
		if (i < 9) b += (a[i] * --c);
	}

	if ((x = b % 11) < 2)
	{
		a[9] = 0
	}
	else
	{
		a[9] = 11 - x
	}

	b = 0;
	c = 11;
	for (y = 0; y < 10; y++)
	{
		b += (a[y] * c--);
	}

	if ((x = b % 11) < 2)
	{
		a[10] = 0;
	}
	else
	{
		a[10] = 11 - x;
	}

	if ((cpf.charAt(9) != a[9]) || (cpf.charAt(10) != a[10]))
	{
		erro +="CPF inválido!";
	}

	if (erro.length > 0)
	{
		alert(erro);
		ocpf.focus();
		return false;
	}

	return true;
}
