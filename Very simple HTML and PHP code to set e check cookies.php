<!DOCTYPE html>
<?php
$cookie_name = "user";
$cookie_value = "John Doe";
setcookie($cookie_name, $cookie_value, time() + (24 * 60 * 60), "/"); // Note: The setcookie() function must appear BEFORE the <html> tag.
//setcookie($cookie_name, "", time() - (60 * 60)); // To delete a cookie, use the setcookie() function with an expiration date in the past
?>
<html>
<head>
    <title>Cookies</title>
</head>
<body>
    <?php
    // Cookies
    if(isset($_COOKIE[$cookie_name]))
    {
        echo "Cookie '" . $cookie_name . "' is set!<br>";
        echo "Value is: '" . $_COOKIE[$cookie_name] . "'";
    }
    else
    {
        echo "Cookie named '" . $cookie_name . "' is not set!";
    }
    ?>
</body>
</html>

