#!/usr/bin/perl


use WebminCore;
do './vsftpd-lib.pl';
$|=1;
&init_config("vsftpd");

%access=&get_module_acl;
if($ENV{'REQUEST_METHOD'} eq 'GET') { &redirect("") }
&ReadParse();


### Create Tables Support ################

system ("mysql -u $config{'mysqluser'} -p$config{'mysqlpass'} -f $config{'mysqldb'} < lib/vsftpd.sql");

$PASS="1234";
use Digest::MD5 qw(md5_hex);
$digest = md5_hex($PASS);

&vsftpd_mysql_connect();

$dbh->do("INSERT INTO passwd VALUES ('', '0', 'testuser' , '$digest' , '/home/' , 'A')");

###########################################################


&redirect("../virtual.cgi");




