<?
session_start();

//funcion para realizar login desde appMovil
$data = json_decode($_GET["data"],true);



echo($data["username"]);
?>