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
  if (/listen_address/) {          $address_file = "@$lref[$Pos]";  $file_pos           = $Pos; }
  if (/force_dot_files/) {         $dot_file     = "@$lref[$Pos]";  $format_pos         = $Pos; }
  if (/anon_max_rate/) {           $anon_file    = "@$lref[$Pos]";  $anon_pos           = $Pos; }
  if (/local_max_rate/) {          $local_file   = "@$lref[$Pos]";  $local_pos          = $Pos; }
  if (/hide_file/) {               $hide_file    = "@$lref[$Pos]";  $hide_pos           = $Pos; }
  if (/tcp_wrappers/) {            $tcp          = "@$lref[$Pos]";  $tcp_pos            = $Pos; }

  if (/ssl_enable/) {              $ssl          = "@$lref[$Pos]";  $ssl_pos            = $Pos; }
  if (/force_local_data_ssl/) {    $force_data   = "@$lref[$Pos]";  $force_data_pos     = $Pos; }
  if (/force_local_logins_ssl/) {  $force_logins = "@$lref[$Pos]";  $force_logins_pos   = $Pos; }
  if (/rsa_cert_file/)          {  $rsa_cert_file = "@$lref[$Pos]"; $rsa_cert_file_pos   = $Pos; }

  $Pos++;
}

  @address_file = split(/\=/, $address_file);
  $address_file = $address_file[1];

  @dot_file = split(/\=/, $dot_file);
  $dot_file = $dot_file[1];


  @anon_file = split(/\=/, $anon_file);
  $anon_file = $anon_file[1];

  @local_file = split(/\=/, $local_file);
  $local_file = $local_file[1];

  @hide_file = split(/\=/, $hide_file);
  $hide_file = $hide_file[1];

  @tcp = split(/\=/, $tcp);
  $tcp = $tcp[1];


# new ssl stuff

  @ssl = split(/\=/, $ssl);
  $ssl = $ssl[1];

  @force_local_data = split(/\=/, $force_data);
  $force_local_data = $force_local_data[1];

  @force_local_logins = split(/\=/, $force_logins);
  $force_local_logins = $force_local_logins[1];

  @rsa_cert_file = split(/\=/, $rsa_cert_file);
  $rsa_cert_file = $rsa_cert_file[1];


if (($dot_file eq "NO") or ($dot_file eq "No") or ($dot_file eq "")){
 $check1 ="checked";
} else {
 $check2 ="checked";
}

if (($tcp eq "NO") or ($tcp eq "No") or ($tcp eq "")){
 $check3 ="checked";
} else {
 $check4 ="checked";
}

if (($ssl eq "NO") or ($ssl eq "No") or ($ssl eq "")){
 $check5 ="checked";
} else {
 $check6 ="checked";
}


if (($force_local_data eq "NO") or ($force_local_data eq "No") or ($force_local_data eq "")){
 $check7 ="checked";
} else {
 $check8 ="checked";
}

if (($force_local_logins eq "NO") or ($force_local_logins eq "No") or ($force_local_logins eq "")){
 $check9 ="checked";
} else {
 $check10 ="checked";
}


if ($rsa_cert_file == "") {
 $rsa_cert_file  = "/etc/vsftpd/ssl/vsftpd.pem";
}


vsftpd_header();


print "<hr>\n";
print"<br><br>";


print "<form action=\"save_misc.cgi\" method=\"post\" name=\"form\" autocomplete=\"OFF\" target=\"_self\">";
print "<table border width=100%>\n";
print "<tr $tb> <td><b>$text{'misc_headline'}</b></td> </tr>\n";
print "<tr $cb> <td><table width=100%>\n";
print "<tr><td>";


print <<EOM;

<table width="100%" border="0" cellpadding="0" cellspacing="0">
  <tr>
    <td width="21%" height="30">Force dot files</td>
    <td width="79%" height="30">
    $text{'log_no'} <input name="force_dot_files" type="radio" value="NO" $check1>$text{'log_yes'} <input type="radio" name="force_dot_files" value="YES" $check2>
    </td>
  </tr>
  <tr>

    <tr>
    <td width="21%" height="30">TCP Wrapper enabled</td>
    <td width="79%" height="30">
    $text{'log_no'} <input name="tcp" type="radio" value="NO" $check3>$text{'log_yes'} <input type="radio" name="tcp" value="YES" $check4>
    </td>
  </tr>
  <tr>

        <td width="21%" height="30">Listen Address</td>
    <td width="79%" height="30">
    <input name="listen_address" type="text" maxlength="15" value="$address_file">

   </tr>
   <tr>
     <td width="21%" height="30">Hide File(s)</td>
     <td width="79%" height="30">
    <input name="hide_file" type="text" value="$hide_file">
    </td>
   </tr>
      
   <tr>
     <td width="21%" height="30">Anon max rate in Bytes/sec</td>
     <td width="79%" height="30">
    <input name="anon_max_rate" type="text" value="$anon_file"> (0 for unlimited)
    </td>
   </tr>

   <tr>
     <td width="21%" height="30">Local max rate in Bytes/sec</td>
     <td width="79%" height="30">
    <input name="local_max_rate" type="text" value="$local_file"> (0 for unlimted)
    </td>
   </tr>


   <tr>
     <td width="21%" height="30">&nbsp;</td>
     <td width="79%" height="30">&nbsp;</td>
   </tr>


   <tr>
     <td width="21%" height="30">SSL enable</td>
     <td width="79%" height="30">$text{'log_no'} <input name="ssl_enable" type="radio" value="NO" $check5>$text{'log_yes'} <input type="radio" name="ssl_enable" value="YES" $check6></td>
   </tr>

   <tr>
     <td width="21%" height="30">Force local data ssl</td>
     <td width="79%" height="30">$text{'log_no'} <input name="force_local_data_ssl" type="radio" value="NO" $check7>$text{'log_yes'} <input type="radio" name="force_local_data_ssl" value="YES" $check8></td>
   </tr>

   <tr>
     <td width="21%" height="30">Force local logins ssl</td>
     <td width="79%" height="30">$text{'log_no'} <input name="force_local_logins_ssl" type="radio" value="NO" $check9>$text{'log_yes'} <input type="radio" name="force_local_logins_ssl" value="YES" $check10></td>
   </tr>

   <tr>
     <td width="21%" height="30">rsa cert file</td>
     <td width="79%" height="30"><input name="rsa_cert_file" type="text" value="$rsa_cert_file"></td>
   </tr>

   <tr>
     <td width="21%" height="30">&nbsp;</td>
     <td width="79%" height="30">&nbsp;</td>
   </tr>

  <tr>
    <td width="21%" height="30">&nbsp;</td>
    <td width="79%" height="30"><input name="submit" type="submit" value="$text{'log_save'}"></td>
  </tr>
  </table>
    <input name="file_pos" type="hidden" value="$file_pos">
    <input name="format_pos" type="hidden" value="$format_pos">
    <input name="anon_pos" type="hidden" value="$anon_pos">
    <input name="local_pos" type="hidden" value="$local_pos">
    <input name="hide_pos" type="hidden" value="$hide_pos">
	<input name="tcp_pos" type="hidden" value="$tcp_pos">
	<input name="ssl_pos" type="hidden" value="$ssl_pos">
	<input name="force_data_pos" type="hidden" value="$force_data_pos">
	<input name="force_logins_pos" type="hidden" value="$force_logins_pos">
	<input name="rsa_cert_file_pos" type="hidden" value="$rsa_cert_file_pos">

EOM


    print "</table></td></tr></table>\n";
        print "</form>";




&footer("index.cgi", "vsftpd");
