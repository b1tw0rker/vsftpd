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
 if (/^anonymous_enable/) {          $anon_enable = "@$lref[$Pos]";  $enable_pos = $Pos; }
 if (/^anon_upload_enable/) {        $anon_upload = "@$lref[$Pos]";  $upload_pos = $Pos; }
 if (/^anon_mkdir_write_enable/) {   $anon_write = "@$lref[$Pos]";   $write_pos = $Pos; }
 if (/^anon_other_write_enable/) {   $anon_other = "@$lref[$Pos]";   $other_pos = $Pos; }
 $Pos++;
}

# Set anonymous_enable Pos to the end of the file
$End_Pos_1 = $Pos + 1;
if ($enable_pos eq "") {
 $enable_pos = $End_Pos_1;
}

# Set anon_upload_enable Pos to the end of the file
$End_Pos_2 = $Pos + 2;
if ($upload_pos eq "") {
 $upload_pos = $End_Pos_2;
}

# Set anon_mkdir_write_enable Pos to the end of the file
$End_Pos_3 = $Pos + 3;
if ($write_pos eq "") {
 $write_pos = $End_Pos_3;
}

# Set anon_other_write_enable Pos to the end of the file
$End_Pos_4 = $Pos + 4;
if ($other_pos eq "") {
 $other_pos = $End_Pos_4;
}


@anon_enable = split(/\=/, $anon_enable);
$anon_enable = $anon_enable[1];

@anon_upload = split(/\=/, $anon_upload);
$anon_upload = $anon_upload[1];

@anon_write = split(/\=/, $anon_write);
$anon_write = $anon_write[1];

@anon_other = split(/\=/, $anon_other);
$anon_other = $anon_other[1];

vsftpd_header();


print "<hr>\n";
print"<br><br>";


print "<form action=\"save_anon.cgi\" method=\"post\" name=\"form\" autocomplete=\"OFF\" target=\"_self\">";
print "<table border width=100%>\n";
print "<tr $tb> <td><b>$text{'anon_headline'}</b></td> </tr>\n";
print "<tr $cb> <td><table width=100%>\n";
print "<tr><td>";

## Set the checked marke
if (($anon_enable eq "NO") or ($anon_enable eq "No") or ($anon_enable eq "")) {
 $check1 ="checked";
} else {
 $check2 ="checked";
}

if (($anon_upload eq "NO") or ($anon_upload eq "No") or ($anon_upload eq "")) {
 $check3 ="checked";
} else {
 $check4 ="checked";
}

if (($anon_write eq "NO") or ($anon_write eq "No") or ($anon_write eq "")){
 $check5 ="checked";
} else {
 $check6 ="checked";
}

if (($anon_other eq "NO") or ($anon_other eq "No") or ($anon_other eq "")){
 $check7 ="checked";
} else {
 $check8 ="checked";
}

print <<EOM;

<table width="100%" border="0" cellpadding="0" cellspacing="0">
  <tr>
    <td width="30%" height="30">$text{'anon_enable'}</td>
    <td>
     $text{'anon_no'} <input name="anon_enable" type="radio" value="NO" $check1>$text{'anon_yes'} <input type="radio" name="anon_enable" value="YES" $check2>
    </td>
  </tr>
  <tr>
   <td height="30">$text{'anon_upload'}</td>
    <td>
     $text{'anon_no'} <input name="anon_upload" type="radio" value="NO" $check3>$text{'anon_yes'} <input type="radio" name="anon_upload" value="YES" $check4>
    </td>
  </tr>

  <tr>
    <td height="30">$text{'anon_make_dirs'}</td>
    <td>
     $text{'anon_no'} <input name="anon_write" type="radio" value="NO" $check5>$text{'anon_yes'} <input type="radio" name="anon_write" value="YES" $check6>
    </td>
  </tr>

  <tr>
    <td height="30">Anonymous can rename,delete files</td>
    <td>
     $text{'anon_no'} <input name="anon_other" type="radio" value="NO" $check7>$text{'anon_yes'} <input type="radio" name="anon_other" value="YES" $check8>&nbsp;($text{'anon_no'} is recommend!)
    </td>
  </tr>

  <tr>
    <td height="30">&nbsp;</td>
    <td>
    <input name="submit" type="submit" value="$text{'anon_save'}"></td>
  </tr>
  </table>
    <input name="enable_pos" type="hidden" value="$enable_pos">
    <input name="upload_pos" type="hidden" value="$upload_pos">
    <input name="write_pos" type="hidden" value="$write_pos">
	<input name="other_pos" type="hidden" value="$other_pos">

EOM


    print "</tr></td>";
    print "</table></td></tr></table>\n";
    print "</form>";



#print "<hr>\n";
&footer("index.cgi", "vsftpd");
