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
&ReadParse();
#########################################################
if ($in{'reload'} eq 1) {
  vsftpd_reload();
}

if ($in{'start'} eq 1) {
  vsftpd_start();
}

if ($in{'stop'} eq 1) {
  vsftpd_stop();
}


vsftpd_header();
$up_vsftpd = &find_byname('vsftpd');

## Create a copy first
if (-e $config{'path'}) {
   if (-e "$config{'path'}.webmin.bak") { } else {
   system ("cp -r $config{'path'} $config{'path'}.webmin.bak");
   } 
}


########################################################

print "<hr>\n";
print"<br><br>";

if (-e $config{'path'}) {

push(@links, "all.cgi");
push(@titles, "$text{'index_allgemein'}");
push(@icons, "images/allgemein.gif");

push(@links, "anon.cgi");
push(@titles,"$text{'index_anonymous'}");
push(@icons, "images/anon.gif");

push(@links, "local.cgi");
push(@titles,"$text{'index_user'}");
push(@icons, "images/local_user.gif");

push(@links, "virtual.cgi");
push(@titles,"$text{'index_virtual'} (BETA)");
push(@icons, "images/virtual_mysql_user.png");

push(@links, "log.cgi");
push(@titles,"$text{'index_log'}");
push(@icons, "images/log.gif");

push(@links, "misc.cgi");
push(@titles,"$text{'index_misc'}");
push(@icons, "images/misc.gif");

push(@links, "manual.cgi");
push(@titles,"$text{'index_manual'}");
push(@icons, "images/manual.gif");

push(@links, "doc.cgi");
push(@titles,"vsftpd.conf Doc");
push(@icons, "images/edit.gif");

push(@links, "ssl.cgi");
push(@titles,"SSL CERT");
push(@icons, "images/ca.gif");

#&icons_table(\@links, \@titles, \@icons, scalar(@links));
&icons_table(\@links, \@titles, \@icons, 4);

} else {
 print "Could not find the vsftpd.conf file. Please check your <a href=\"../config.cgi?vsftpd\" target=\"_self\">Module Configuration</a>.";
 print "<br><br>";
}

print "<br>\n";

####print "val: $up_vsftpd";

if ($up_vsftpd ne 0) {
  print "<form action=\"index.cgi?reload=1\" target=\"_self\" method=\"post\">";
  print "<input type=\"submit\" name=\"Submit\" value=\"$text{'index_restart'}\">";
  print "</form>";
}

if (-e "/etc/init.d/vsftpd") {

 if ($up_vsftpd eq 0) {
    print "<form action=\"index.cgi?start=1\" target=\"_self\" method=\"post\">";
    print "<input type=\"submit\" name=\"Submit\" value=\"$text{'index_start'}\">";
    print "</form>";
 }


 if ($up_vsftpd >= 1) {
    print "<form action=\"index.cgi?stop=1\" target=\"_self\" method=\"post\">";
    print "<input type=\"submit\" name=\"Submit\" value=\"$text{'index_stop'}\">";
    print "</form>";
 }

} ## end check if /etc/init.d/vsftpd exists
print "<br>";


&footer("/", "$text{'index_home'}");
