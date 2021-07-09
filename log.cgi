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


$lref = &read_file_lines("$config{'path'}");
for (@$lref)
{
if (/xferlog_file/) { $xfer_file = "@$lref[$Pos]";  $file_pos = $Pos; }
if (/xferlog_std_format/) { $xfer_format = "@$lref[$Pos]";  $format_pos = $Pos; }
$Pos++;
}
@xfer_file = split(/\=/, $xfer_file);
$xfer_file = $xfer_file[1];

@xfer_format = split(/\=/, $xfer_format);
$xfer_format = $xfer_format[1];

vsftpd_header();


print "<hr>\n";
print"<br><br>";


print "<form action=\"save_log.cgi\" method=\"post\" name=\"form\" autocomplete=\"OFF\" target=\"_self\">";
print "<table border width=100%>\n";
print "<tr $tb> <td><b>$text{'log_headline'}</b></td> </tr>\n";
print "<tr $cb> <td><table width=100%>\n";
print "<tr><td>";

if (($xfer_format eq "NO") or ($xfer_format eq "No") or ($xfer_format eq "")){
  $check1 ="checked";
   } else {
  $check2 ="checked";
}

if (-e "webalizer.log") {
 $lizer1 = "";
 $lizer2 = "checked";
   } else {
 $lizer1 = "checked";
 $lizer2 = "";
}


print <<EOM;

<table width="100%" border="0" cellpadding="0" cellspacing="0">
  <tr>
        <td width="21%" height="30">$text{'log_format'}</td>
    <td width="79%" height="30">

    $text{'log_no'} <input name="xfer_format" type="radio" value="NO" $check1>$text{'log_yes'} <input type="radio" name="xfer_format" value="YES" $check2>
    </td>
  </tr>
  <tr>
        <td width="21%" height="30">$text{'log_file'}</td>
    <td width="79%" height="30">
    <input name="xfer_file" type="text" value="$xfer_file">
EOM
print &file_chooser_button("xfer_file", 0, 0);
print "    </td>\n";

  if (-e "/usr/bin/webalizer") {
print"  </tr>";
print"      <td width=\"21%\" height=\"30\">Activate Webalizer Logging</td>";
print"    <td width=\"79%\" height=\"30\">Off <input name=\"webalizer\" type=\"radio\" value=\"0\" $lizer1>On <input type=\"radio\" name=\"webalizer\" value=\"1\" $lizer2></td>";

print"  </tr> ";
}

print <<EOF; 
  </tr>
      <td width="21%" height="30">&nbsp;</td>
    <td width="79%" height="30"><input name="submit" type="submit" value="$text{'log_save'}"></td>
  </tr>

EOF
  if (-e "webalizer.log") {
print"  </tr>";
print"      <td width=\"21%\" height=\"30\">&nbsp;</td>";
print"    <td width=\"79%\" height=\"30\"><a href=\"webalizer/index.html\" target=\"_blank\">FTP Stats</a> (will just work with setting 'Xfer Logformat' to yes)</td>";
print"  </tr> ";
}

print <<EOF;

</table>
<input name="file_pos" type="hidden" value="$file_pos">
<input name="format_pos" type="hidden" value="$format_pos">

EOF

print "</td></tr>";


   print "</table></td>\n";
   print "</tr></table>";
   print "</form>";



#print "<hr>\n";
&footer("index.cgi", "vsftpd");
