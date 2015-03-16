<?
session_start();
include_once("../../conexion/conexion.php");

//script que devuelve la jornada segun el id que le pasas en el data

//declaracion de variables
$data = json_decode($_GET["data"], true);
$ret = array();
$con = connectDB();

if(isset($data)){

	foreach ($data["data"] as $partido) {

		try{
			$stmt = $con->prepare("SELECT * FROM apuesta_partido where user=:user and partido=:partido");
			$stmt->bindParam(":user", $data["idUser"]);
			$stmt->bindParam(":partido", key($data["data"]));
			$stmt->execute();

			$aux = array();
			foreach ($stmt as $file) {
				$aux["jornada"] = $file;
			}
			
			if (isset($aux["jornada"])) {

				$stmt = $con->prepare("UPDATE apuesta_partido SET valor=:valor where user=:user and partido=:partido");
				$stmt->bindParam(":user", $data["idUser"]);
				$stmt->bindParam(":partido", key($data["data"]));
				$stmt->bindParam(":valor", $partido);
				$stmt->execute();

			}else{

				$stmt = $con->prepare("INSERT INTO apuesta_partido VALUES ('', :user, :partido, :valor)");
				$stmt->bindParam(":user", $data["idUser"]);
				$stmt->bindParam(":partido", key($data["data"]));
				$stmt->bindParam(":valor", $partido);
				$stmt->execute();

				

			}

			$stmt = $con->prepare("SELECT * FROM apuesta_partido where partido=:partido");
			$stmt->bindParam(":partido", key($data["data"]));
			$stmt->execute();

			$aux = array();
			foreach ($stmt as $file) {
				$aux[] = $file;
			}

			$count= 0;
			$countUno = 0;
			$countDos = 0;
			$countX = 0;

			foreach ($aux as $apuesta) {
				$valor= $apuesta["valor"];
				if($valor == 1){
					$countUno+=1;
				}elseif ($valor == 2) {
					$countDos+=1;
				}elseif ($valor == 3) {
					$countX+=1;
				}
				$count+=1;
			}

			$countUno = ($countUno/$count) * 100;
			$countDos = ($countDos/$count) * 100;
			$countX = ($countX/$count) * 100;

			$stmt = $con->prepare("UPDATE partido SET xcomun=:xcomun, ycomun=:ycomun, zcomun=:zcomun where id=:partido");
			$stmt->bindParam(":partido", key($data["data"]));
			$stmt->bindParam(":xcomun", $countUno);
			$stmt->bindParam(":ycomun", $countX);
			$stmt->bindParam(":zcomun", $countDos);

			$stmt->execute();

			$ret["estado"]="OK";
			$ret["message"]="Los datos han sido guardados";

		}catch(PDOException $e){
			$ret["estado"]="ERROR";
			$ret["message"]=$e->getMessage();
		}
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