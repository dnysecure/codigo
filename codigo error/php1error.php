<?php
//Connect to the database
mysql_connect(“[database]”, “[user]”, “[password]”) or//Error checking in case the database
is not accessible
die(“Could not connect:”. mysql_error());
//Select the database
mysql_select_db(“[database_name]”);
//We retrieve category value from the GET request
$category = $_GET[“category”];
//Create and execute the SQL statement
$result = mysql_query(“SELECT ∗ from products where category=‘$category’”);
//Loop on the results
while ($row = mysql_fetch_array($result, MYSQL_NUM)) {printf(“ID: %s Name: %s”, $row[0],
$row[1]);
}
//Free result set
mysql_free_result($result);
?>