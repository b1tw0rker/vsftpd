#!/usr/bin/perl

#    vsftpd
#    version: 1.3
#    (C) 2003 - 2009 by NH (Nick Herrmann)
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.



do '../../web-lib.pl';
do '../vsftpd-lib.pl';
$|=1;
&init_config("vsftpd");

%access=&get_module_acl;


## Suche nach user_config_dir=/etc/vsftpd/vsftpd_user_conf

$USER_CONFIG_DIR=$config{'virtual'};

$lref = &read_file_lines("$config{'path'}");
for (@$lref)
{
if (/^user_config_dir=$USER_CONFIG_DIR/) { 
	 $user_config_reihe = "@$lref[$Pos]";
     $user_config_reihe_2  = $Pos;  
	}
    $Pos++;
}
### end suche nach user_config_dir=/etc/vsftpd/vsftpd_user_conf

print "<hr>\n";
print"<br><br>";

if ($user_config_reihe_2 eq "") {
	print "$text{'virtual_description_1'}\n";
	print "\n";
	print "pam_service_name=vsftpd<br>\n";
	print "nopriv_user=vsftpd\n";
	print "<br>\n";
    print "guest_enable=YES\n";
	print "<br>\n";
    print "guest_username=vsftpd\n";
	print "<br>\n";
    print "user_sub_token=\$USER\n";
	print "<br>\n";
    print "virtual_use_local_privs=YES\n";
	print "<br>";
    print "user_config_dir=/etc/vsftpd/vsftpd_user_conf\n";
	print "<br>\n";
	print "<br>\n";
	print "$text{'virtual_description_2'}\n";
    print "<br>\n";
    print "<br>\n";
	print "<a href=\"create_virtual_support.cgi\" target=\"_self\">$text{'virtual_description_3'} &gt;&gt;</a>";
	print "<hr>\n";

	$ERR=1;
}

## Check auf PAM Datei
if (!-e $config{'pam'} || $config{'pam'} eq "" ) {
  print "$text{'virtual_description_4'} <a href=\"../config.cgi?vsftpd\" target=\"_self\">Module Configuration</a>.";
  print "<hr>\n";

  $ERR=1;
}

## Testconnection to the mysql DB

&vsftpd_mysql_connect();

## Test Table structure for mysql support

$sth = $dbh->prepare('SELECT username FROM passwd');
$sth->execute();
$result = $sth->fetchrow_hashref();
#print "Value returned: $result->{username}\n";
$sth->finish();

if ($result->{username} eq "") {
	print "$text{'virtual_description_5'} <a href=\"create_mysql_tables.cgi\" target=\"_self\" >$text{'virtual_description_6'}</a>";
	print "<hr>\n";

	$ERR=1;
}

## Test auch korrekte /etc/pam.d/vsftpd

$lref = &read_file_lines("$config{'pam'}");
$Pos=0;
for (@$lref)
{
  if (/pam_mysql.so/) { $pam_reihe = "@$lref[$Pos]";  $pam_pos = $Pos; }
  $Pos++;
}


if ($pam_reihe eq "") {
	print "$text{'virtual_description_7'}\n";
	print "<br>\n";
	print "$text{'virtual_description_8'} <a href=\"create_pam.cgi\" target=\"_self\" >$text{'virtual_description_6'}</a>\n";
    print "<br>\n";
	print "$text{'virtual_description_9'}\n";
	print "<br>\n";
	print "$text{'virtual_description_10'}\n";
    print "<br>\n";
	print "<br>\n";
	print "<font size=\"1\">auth        sufficient    pam_mysql.so user=$config{'mysqluser'} passwd=$config{'mysqlpass'} host=localhost db=$config{'mysqldb'} table=passwd usercolumn=username passwdcolumn=passwd statcolumn=status crypt=3</font>\n";
    print "<br>\n";
	print "<font size=\"1\">account     sufficient    pam_mysql.so user=$config{'mysqluser'} passwd=$config{'mysqlpass'} host=localhost db=$config{'mysqldb'} table=passwd usercolumn=username passwdcolumn=passwd statcolumn=status crypt=3</font>\n";
    print "<br>\n";

	print "<hr>\n";

	$ERR=1;
}


### Teste auf /lib/security/pam_mysql.so
###
###
if (!-e "/lib/security/pam_mysql.so" && !-e "/lib64/security/pam_mysql.so") {
	print "$text{'virtual_description_11'}\n";
	print "<br>\n";
	print "$text{'virtual_description_12'}\n";
	print "<br>\n";
	print "$text{'virtual_description_13'}\n";
	print "<br>\n";
	print "<hr>\n";

	$ERR=1;
}
