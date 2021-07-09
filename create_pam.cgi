#!/usr/bin/perl


use WebminCore;
do './vsftpd-lib.pl';
$|=1;
&init_config("vsftpd");

%access=&get_module_acl;
if($ENV{'REQUEST_METHOD'} eq 'GET') { &redirect("") }
&ReadParse();


### Create PAM Support ################

if (-e $config{'pam'}) {
 system ("cp $config{'pam'} /etc/pam.d/vsftpd_ORIG");

if (-e "/etc/pam.d/vsftpd_ORIG") { 
 open(PAM,">>$config{'pam'}");
 print PAM "\n";
 print PAM "auth        sufficient    pam_mysql.so user=$config{'mysqluser'} passwd=$config{'mysqlpass'} host=localhost db=$config{'mysqldb'} table=passwd usercolumn=username passwdcolumn=passwd statcolumn=status crypt=3\n";
 print PAM "account     sufficient    pam_mysql.so user=$config{'mysqluser'} passwd=$config{'mysqlpass'} host=localhost db=$config{'mysqldb'} table=passwd usercolumn=username passwdcolumn=passwd statcolumn=status crypt=3\n";
 print PAM "\n";
 close(PAM);
}

}
###########################################################


&redirect("../virtual.cgi");




