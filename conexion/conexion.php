<?
	function connectDB(){
		$host = 'mysql:host=localhost;dbname=quinielasdb';
		$username = 'quinielasUser';
		$password = '9u1n1elasU5er';
		
		try{
			$con  = new PDO($host, $username, $password);
			$con -> setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
		}catch(PDOException $e){
			echo "Error en la conexion: ". $e->getMessage();
		}
		return $con;
	}
?>