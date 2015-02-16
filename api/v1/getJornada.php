<?
session_start();
include_once("../../conexion/conexion.php");

//script que devuelve la jornada segun el id que le pasas en el data

//declaracion de variables
$data = json_decode($_GET["data"], true);
$ret = array();
$con = connectDB();

if(isset($data)){
	
	try{
		$stmt = $con->prepare("SELECT * FROM jornada where id=:id");
		$stmt->bindParam(":id", $data["id"]);
		$stmt->execute();

		$aux = array();
		foreach ($stmt as $file) {
			$aux["jornada"] = $file;
		}
		
		if(isset($aux["jornada"])){
			$stmt = $con->prepare("SELECT * FROM partido where jornada=:id");
			$stmt->bindParam(":id", $data["id"]);
			$stmt->execute();
			
			$aux1=array();
			foreach ($stmt as $file) {
				$aux1[]=$file;
			}
			$aux["partidos"]=$aux1;
			
			//if(count($aux1) != 15){
			//	$ret["estado"]="ERROR";
			//	$ret["message"]="Numero de partidos incorrectos para una jornada.";
			//}else{
				$ret["estado"]="OK";
				$ret["message"]="Todo correcto.";
				$ret["data"]=$aux;
			//}
			
		}else{
			$ret["estado"]="ERROR";
			$ret["message"]="No existe jornada con ese identificador";
		}
		$con = null;
	}catch(PDOException $e){
		$ret["estado"]="ERROR";
		$ret["message"]=$e->getMessage();
	}

}else{

	$ret["estado"]="ERROR";
	$ret["message"]="Los datos proporcionados no son correctos";

}

if(isset($_GET["jsoncallback"])){
	echo( $_GET["jsoncallback"] . "(" . json_encode($ret) .");" );
}else{
	echo( json_encode($ret) );
}


?>