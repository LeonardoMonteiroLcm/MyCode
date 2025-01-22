<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Send e-mail</title>
    </head>
    <body>
        <?php
            $to = "leonardo.monteiro.lcm@gmail.com";
            $subject = "PHP e-mail test";

            $message = "<b>This is HTML message.</b>";
            $message .= "<h1>This is headline.</h1>";
            $message .= "Hello dude!";

            $header = "From:abc@somedomain.com\r\n";
            $header .= "Cc:afgh@somedomain.com\r\n";
            $header .= "MIME-Version: 1.0\r\n";
            $header .= "Content-type: text/html\r\n";

            $retval = mail($to, $subject, $message, $header);

            if($retval == true)
            {
                echo "Message sent successfully...";
            }
            else
            {
                echo "Message could not be sent...";
            }
         ?>
    </body>
</html>

