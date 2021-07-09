#!/usr/bin/perl

#    vsftpd
#    version: 1.4
#    (C) 2003 - 2010 by NH (Nick Herrmann)
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



use WebminCore;
do './vsftpd-lib.pl';
$|=1;
&init_config("vsftpd");

%access=&get_module_acl;


vsftpd_header();

if (-e $config{'path'}) {

## Do some checks
do 'lib/check_virtual.pl';


if ($ERR ne 1) {


## Here we list the users from the mysql db
push(@links, "virtual_create.cgi");
push(@titles, "Create New Virtual User");
push(@icons, "images/local_user.gif");

push(@links, "virtual_disable.cgi");
push(@titles, "Disable Virtual User Support");
push(@icons, "images/log.gif");


&icons_table(\@links, \@titles, \@icons, 4);

print "<br>\n";
my (@row);
$sth = $dbh->prepare('SELECT username,rootdir FROM passwd ORDER BY username');
$sth->execute();

while(@row = $sth->fetchrow) {
 $user = $row[0];
 #print $user;

push(@links2, "virtual_create.cgi");
push(@titles2, "$user");
push(@icons2, "images/local_user.gif");

}

$sth->finish();

&icons_table(\@links2, \@titles2, \@icons2, 5);
}

} else {
 print "<br><br>";
 print "Could not find the folder for the virtual User. Please check your <a href=\"../config.cgi?vsftpd\" target=\"_self\">Module Configuration</a>.";
 print "<br><br>";
}


&footer("index.cgi", "vsftpd");


