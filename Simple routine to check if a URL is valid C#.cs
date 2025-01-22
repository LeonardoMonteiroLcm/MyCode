using System;
using System.Net;

namespace Server.Util
{
    public class WebUtil
    {
        public static bool CheckUrl(string url)
        {
            try
            {
                url = url.Trim();
                if (!(url.StartsWith("http://") || url.StartsWith("https://")))
                {
                    url = "http://" + url;
                }
                WebRequest req = WebRequest.Create(url);
                return (req != null);
            }
            catch
            {
                return false;
            }
        }
    }
}
