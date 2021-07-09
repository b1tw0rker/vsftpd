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

## do the disable action
if ($in{'do'} eq 1) {

$lref = &read_file_lines("$config{'path'}");
for (@$lref)
{
  if (/\#\#\# VIRTUAL USER SUPPORT/) {                    $line1 = "@$lref[$Pos]";  $pos1 = $Pos; }
  if (/pam_service_name=vsftpd/) {                        $line2 = "@$lref[$Pos]";  $pos2 = $Pos; }
  if (/nopriv_user=vsftpd/) {                             $line3 = "@$lref[$Pos]";  $pos3 = $Pos; }
  if (/guest_enable=YES/) {                               $line4 = "@$lref[$Pos]";  $pos4 = $Pos; }
  if (/guest_username=vsftpd/) {                          $line5 = "@$lref[$Pos]";  $pos5 = $Pos; }
  if (/user_sub_token=\$USER/) {                          $line6 = "@$lref[$Pos]";  $pos6 = $Pos; }
  if (/virtual_use_local_privs=YES/) {                    $line7 = "@$lref[$Pos]";  $pos7 = $Pos; }
  if (/user_config_dir=\/etc\/vsftpd/) {                  $line8 = "@$lref[$Pos]";  $pos8 = $Pos; }
  if (/\#\#\# END VIRTUAL USER /) {                       $line9 = "@$lref[$Pos]";  $pos9 = $Pos; }

  $Pos++;
}

&replace_file_line ("$config{'path'}", $pos1, "\n");
&replace_file_line ("$config{'path'}", $pos2, "\n");
&replace_file_line ("$config{'path'}", $pos3, "\n");
&replace_file_line ("$config{'path'}", $pos4, "\n");
&replace_file_line ("$config{'path'}", $pos5, "\n");
&replace_file_line ("$config{'path'}", $pos6, "\n");
&replace_file_line ("$config{'path'}", $pos7, "\n");
&replace_file_line ("$config{'path'}", $pos8, "\n");
&replace_file_line ("$config{'path'}", $pos9, "\n");





 &redirect("index.cgi");
}

vsftpd_header();

if (-e $config{'path'}) {

##FORM
 print "<br><br>\n";
 print "This action will delete the following lines from your $config{'path'}<br><br>";
 print "### VIRTUAL USER SUPPORT CREATED BY WEBMINMODULE VSFTPD ###<br>\n";
 print "<br>\n";
 print "pam_service_name=vsftpd<br>\n";
 print "nopriv_user=vsftpd<br>\n";
 print "guest_enable=YES<br>\n";
 print "guest_username=vsftpd<br>\n";
 print "user_sub_token=\$USER<br>\n";
 print "virtual_use_local_privs=YES<br>\n";
 print "user_config_dir=/etc/vsftpd/vsftpd_user_conf<br>\n";
 print "<br><br>\n";
 print "### END VIRTUAL USER SUPPORT CREATED BY WEBMINMODULE VSFTPD ###<br>\n";
 print "<br><br>";
 print "<a href=\"virtual_disable.cgi?do=1\" target=\"_self\">DISABLE NOW</a>";
 print "<br><br>";
} else {
 print "<br><br>";
 print "Could not find the folder for the virtual User. Please check your <a href=\"../config.cgi?vsftpd\" target=\"_self\">Module Configuration</a>.";
 print "<br><br>";
}

print "<hr>\n";
&footer("virtual.cgi", "Virtual User");


