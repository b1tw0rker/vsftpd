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
 if (/^chroot_local_user/) { $local_chroot = "@$lref[$Pos]";  $chroot_pos = $Pos; }
 if (/^local_enable/) {      $local_enable = "@$lref[$Pos]";  $enable_pos = $Pos; }
 if (/^write_enable/) {      $local_write = "@$lref[$Pos]";   $write_pos = $Pos; }
 
 $Pos++;
}

# Set max per IP Pos to the end of the file
$End_Pos_1 = $Pos + 1;
if ($chroot_pos eq "") {
 $chroot_pos = $End_Pos_1;
}

# Set ftp username Pos to the end of the file
$End_Pos_2 = $Pos + 2;
if ($enable_pos eq "") {
 $enable_pos = $End_Pos_2;
}

# Set local unmask Pos to the end of the file
$End_Pos_3 = $Pos + 3;
if ($write_pos eq "") {
 $write_pos= $End_Pos_3;
}


@local_enable = split(/\=/, $local_enable);
$local_enable = $local_enable[1];

@local_chroot = split(/\=/, $local_chroot);
$local_chroot = $local_chroot[1];

@local_write = split(/\=/, $local_write);
$local_write = $local_write[1];


vsftpd_header();


print "<hr>\n";
print"<br><br>";


print "<form action=\"save_local.cgi\" method=\"post\" name=\"form\" autocomplete=\"OFF\"  target=\"_self\">";
print "<table border width=100%>\n";
print "<tr $tb> <td><b>$text{'local_headline'}</b></td> </tr>\n";
print "<tr $cb> <td><table width=100%>\n";
print "<tr><td>";

## Set the checked marke
if (($local_enable eq "NO") or ($local_enable eq "No") or ($local_enable eq "")) {
$check1 ="checked";
} else {
$check2 ="checked";
}
if (($local_chroot eq "NO") or ($local_chroot eq "No") or ($local_chroot eq "")) {
$check3 ="checked";
} else {
$check4 ="checked";
}
if (($local_write eq "NO") or ($local_write eq "No") or ($local_write eq "")) {
$check5 ="checked";
} else {
$check6 ="checked";
}



print <<EOM;
<table width="100%" border="0" cellpadding="0" cellspacing="0">
  <tr>
        <td width="21%" height="30">$text{'local_enable'}</td>
    <td width="79%" height="30">

    $text{'local_no'} <input name="local_enable" type="radio" value="NO" $check1>$text{'local_yes'} <input type="radio" name="local_enable" value="YES" $check2>
    </td>
  </tr>
  <tr>
        <td width="21%" height="30">$text{'local_chroot'}</td>
    <td width="79%" height="30">
   $text{'local_no'} <input name="local_chroot" type="radio" value="NO" $check3>$text{'local_yes'} <input type="radio" name="local_chroot" value="YES" $check4>

    </td>
  </tr>
  <tr>
    <td width="21%" height="30">$text{'local_write'}</td>
        <td width="79%" height="30">

        $text{'local_no'} <input name="local_write" type="radio" value="NO" $check5>$text{'local_yes'} <input type="radio" name="local_write" value="YES" $check6>
        </td>
  </tr>
  <tr>
    <td width="21%" height="30">&nbsp;</td>
    <td width="79%" height="30"><input name="submit" type="submit" value="$text{'local_save'}"></td>
  </tr>
  </table>
    <input name="enable_pos" type="hidden" value="$enable_pos">
    <input name="chroot_pos" type="hidden" value="$chroot_pos">
    <input name="write_pos" type="hidden" value="$write_pos">

EOM


    print "</tr></td>";
    print "</table></td></tr></table>\n";
        print "</form>";




&footer("index.cgi", "vsftpd");
