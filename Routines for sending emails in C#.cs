using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Text;
using System.Runtime.InteropServices;
using System.IO;
using System.Net;
using System.Net.Mail;

namespace Server.Util
{
    public enum StatusResultEmail
    {
        [Description("OK")]
        OK,
        [Description("Error SMTP")]
        ErrorSMTP,
        [Description("Another Error")]
        ErrorAnother
    }

    public class ResultEmail
    {
        public StatusResultEmail Status;
        public string Error;

        public ResultEmail(StatusResultEmail status, string error)
        {
            Status = status;
            Error = error;
        }
    }

    public static class EmailUtil
    {
        public static ResultEmail EnviarMsg(
            string fromAddr,
            string toAddr,
            string subject,
            string body,
            string server,
            int port,
            int timeout,
            bool ssl,
            bool html,
            string login,
            string passw)
        {
            ResultEmail result = new ResultEmail(StatusResultEmail.OK, "0");

            MailMessage mail = new MailMessage(fromAddr, toAddr, subject, body);
            mail.SubjectEncoding = System.Text.Encoding.Default;
            mail.BodyEncoding = System.Text.Encoding.Default;
            mail.IsBodyHtml = html;
            mail.Priority = MailPriority.Normal;

            SmtpClient client = new SmtpClient(server, port);
            client.Credentials = new NetworkCredential(login, passw);
            client.DeliveryMethod = SmtpDeliveryMethod.Network;
            client.EnableSsl = ssl;
            client.Timeout = timeout * 1000;

            try
            {
                client.Send(mail);
            }
            catch (SmtpException ex)
            {
                result = new ResultEmail(StatusResultEmail.ErrorSMTP, ex.ToString());
            }
            catch (Exception ex)
            {
                result = new ResultEmail(StatusResultEmail.ErrorAnother, ex.ToString());
            }

            return result;
        }

        public static bool CheckAddr(string addrToCheck)
        {
            try
            {
                MailAddress addr = new MailAddress(addrToCheck);
                return true;
            }
            catch
            {
                return false;
            }
        }
    }
}

