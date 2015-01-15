<?
session_start();
include_once("../../conexion/conexion.php");

//funcion para realizar login desde appMovil

//declaracion de variables
$data = json_decode($_GET["data"],true);
$ret = [];
$con = connectDB();

if(isset($data)){
	
	try{
		$stmt = $con->prepare("SELECT * FROM user where username=:username");
		$stmt->bindParam(":username", $data["username"]);
		$stmt->excecute();

		$aux=[];
		foreach ($stmt as $file) {
			$aux = $file;
		}
		if($data["password"] == $aux["password"]){
			$ret["estado"]="OK";
			$ret["message"]="El usuario esta logado.";
			$ret["data"]=$aux;
		}else{
			$ret["estado"]="ERROR";
			$ret["message"]="Los datos proporcionados no son correctos";
		}
		
	}catch(PDOException $e){
		$ret["estado"]="ERROR";
		$ret["message"]=$e->getMessage();
	}

}else{

	$ret["estado"]="ERROR";
	$ret["message"]="Los datos proporcionados no son correctos";

}

echo( $_GET["jsoncallback"] + "(" + json_encode($ret) +");" );
?>