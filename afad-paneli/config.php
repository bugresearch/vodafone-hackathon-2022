<?php
 $user = "deniz";
 $pass = "03010504";

 session_start();
 ob_start();

 function verilerigetir(){
     $url = "http://10.1.1.1/afad?apikey=002d6844dce5dded232842347a8c9222";
     $veri  = file_get_contents($url);
     $json_list = json_decode($veri);
     return $json_list;

 }
?>