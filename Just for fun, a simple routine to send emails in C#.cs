using System;
using System.Net;
using System.Net.Mail;

namespace Application.Utils
{
    public enum EmailStatusResult
    {
        OK,
        ErrorSMTP,
        ErrorOther
    }

    public class EmailResult
    {
        public EmailStatusResult Status;
        public string Error;

        public EmailResult(EmailStatusResult status, string error)
        {
            Status = status;
            Error = error;
        }
    }

    public static class EmailUtil
    {
        public static EmailResult SendEmail(
            string fromAddr,
            string toAddr,
            string subject,
            string body,
            string host,
            int port,
            int timeout, // in seconds
            bool ssl,
            bool html,
            string userName,
            string password)
        {
            EmailResult result = new EmailResult(EmailStatusResult.OK, "");

            // Create the e-mail message.
            MailMessage mail = new MailMessage(fromAddr, toAddr, subject, body)
            {
                SubjectEncoding = System.Text.Encoding.Default,
                BodyEncoding = System.Text.Encoding.Default,
                IsBodyHtml = html,
                Priority = MailPriority.Normal
            };

            // Set the cliente e-mail server.
            SmtpClient client = new SmtpClient(host, port)
            {
                Credentials = new NetworkCredential(userName, password),
                DeliveryMethod = SmtpDeliveryMethod.Network,
                EnableSsl = ssl,
                Timeout = timeout * 1000
            };

            // Send the e-mail.
            try
            {
                client.Send(mail);
            }
            catch (SmtpException ex)
            {
                Console.WriteLine(ex.Message);
                result = new EmailResult(EmailStatusResult.ErrorSMTP, ex.ToString());
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
                result = new EmailResult(EmailStatusResult.ErrorOther, ex.ToString());
            }

            return result;
        }

        public static bool CheckAddress(string addr)
        {
            try
            {
                MailAddress mailAddr = new MailAddress(addr);
                return true;
            }
            catch
            {
                return false;
            }
        }
    }
}

