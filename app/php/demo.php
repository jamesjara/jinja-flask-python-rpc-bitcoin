<?php
require_once('easybitcoin.php');
 
// Optionally, you can specify a host and port.
$bitcoin = new Bitcoin('whatever','whatever','127.0.0.1','7244');
 
$bitcoin->getbalance();  

 