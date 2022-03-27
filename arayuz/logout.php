<?php
include("config.php");
session_destroy();
ob_flush();
header("Location: login.php");
?>