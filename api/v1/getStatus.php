<?
session_start();
include_once("../../conexion/conexion.php");

//funcion para cargar el estado de la app

//declaracion de variables
$ret = array();
$con = connectDB();

try{
	$stmt = $con->prepare("SELECT * FROM configuracion_app");
	$stmt->execute();

	$aux = array();
	foreach ($stmt as $file) {
		$aux = $file;
	}
	if(isset($aux["estado"])){
		$ret["estado"]="OK";
		$ret["message"]="Estado cargado.";
		$ret["data"]=$aux;
	}else{
		$ret["estado"]="ERROR";
		$ret["message"]="No se ha podido cargar el estado de la aplicación";
	}
	$con = null;
}catch(PDOException $e){
	$ret["estado"]="ERROR";
	$ret["message"]="No se ha podido cargar el estado de la aplicación: " + $e->getMessage();
}


if(isset($_GET["jsoncallback"])){
	echo( $_GET["jsoncallback"] . "(" . json_encode($ret) .");" );
}else{
	echo( json_encode($ret) );
}


?>