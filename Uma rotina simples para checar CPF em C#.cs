using System;

namespace Application.Utils
{
    public static class CPFUtil
    {
        public static bool CheckCPF(string cpf)
        {
            const string digits = "0123456789";
            const int cpfLength = 11;
            const int dvLength = 2;
            const int numberLength = cpfLength - dvLength;

            string parsedCpf = string.Empty;
            for (int i = 0; i < cpf.Length; i++)
            {
                if (digits.IndexOf(cpf[i]) >= 0)
                {
                    parsedCpf += cpf[i];
                }
            }
            if (parsedCpf.Length < cpfLength)
            {
                parsedCpf = new string('0', cpfLength - parsedCpf.Length) + parsedCpf;
            }
            if (parsedCpf.Length > cpfLength)
            {
                parsedCpf = parsedCpf.Substring(parsedCpf.Length - cpfLength);
            }

            switch (parsedCpf)
            {
                case "00000000000":
                case "11111111111":
                case "22222222222":
                case "33333333333":
                case "44444444444":
                case "55555555555":
                case "66666666666":
                case "77777777777":
                case "88888888888":
                case "99999999999":
                    return false;
            }

            string tempCpf = parsedCpf.Substring(0, numberLength);

            int firstSum = 0;
            for (int i = 0; i < tempCpf.Length; i++)
            {
                firstSum += int.Parse(tempCpf[i].ToString()) * (10 - i);
            }

            int firstDvDigit = 0;
            int firstRemainder = firstSum % 11;
            if (firstRemainder >= 2)
            {
                firstDvDigit = 11 - firstRemainder;
            }

            tempCpf += firstDvDigit.ToString();

            int secondSum = 0;
            for (int i = 0; i < tempCpf.Length; i++)
            {
                secondSum += int.Parse(tempCpf[i].ToString()) * (11 - i);
            }

            int secondDvDigit = 0;
            int secondRemainder = secondSum % 11;
            if (secondRemainder >= 2)
            {
                secondDvDigit = 11 - secondRemainder;
            }

            string dv = firstDvDigit.ToString() + secondDvDigit.ToString();

            return parsedCpf.EndsWith(dv);
        }
    }
}

