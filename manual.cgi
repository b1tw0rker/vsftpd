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


print "<hr>\n";
print"<br><br>";
print "<b>$text{'manual_headline'}</b>";

print "<form action=\"save_manual.cgi\" method=\"post\" name=\"form\" autocomplete=\"OFF\" target=\"_self\">";

open (FILE, "$config{'path'}");
@lines = <FILE>;
close(FILE);
print "<textarea name=\"manual\" wrap=\"OFF\" cols=\"80\" rows=\"20\" class=\"input2\">", join("", @lines),"</textarea>";
print "<br><br>";
print "<input type=\"submit\" name=\"Submit\" value=\"$text{'manual_save'}\">";
        print "</form>";


#print "<hr>\n";
&footer("index.cgi", "vsftpd");
