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

##FORM
 print "<br><br>";
 print "COMMING SOON...";
 print "<br><br>";
} else {
 print "<br><br>";
 print "Could not find the folder for the virtual User. Please check your <a href=\"../config.cgi?vsftpd\" target=\"_self\">Module Configuration</a>.";
 print "<br><br>";
}

print "<hr>\n";
&footer("virtual.cgi", "Virtual User");


