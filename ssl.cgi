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


## Check if we have allread a cert and grep some data

if ((-e "/etc/vsftpd/ssl/vsftpd.pem") and (-e "$config{'openssl'}")) { 

 system ("$config{'openssl'} x509 -in /etc/vsftpd/ssl/vsftpd.pem -noout -text | grep Issuer > /tmp/ssl.txt");


 ## open for reading
 open (AP, "/tmp/ssl.txt");
 while(<AP>){
  $Line = $_;
  chomp($Line);
  $SSLLINE = $Line;
 }

 @S = split(/\,\ /, $SSLLINE);
 @M = split(/\/emailAddress=/, $SSLLINE);

$SSL_EMAIL = $M[1];
 

@SSL_COUNTRY = split(/=/, $S[0]);
$SSL_COUNTRY = $SSL_COUNTRY[1];

@SSL_STATE = split(/=/, $S[1]);
$SSL_STATE = $SSL_STATE[1];

@SSL_CITY = split(/=/, $S[2]);
$SSL_CITY = $SSL_CITY[1];

@SSL_COMPANY = split(/=/, $S[3]);
$SSL_COMPANY = $SSL_COMPANY[1];

@SSL_DEPARTEMENT = split(/=/, $S[4]);
$SSL_DEPARTEMENT = $SSL_DEPARTEMENT[1];

@SSL_CN = split(/=/, $S[5]);
$SSL_CN = $SSL_CN[1];
@SSL_CN = split(/\//, $SSL_CN);
$SSL_CN = $SSL_CN[0];



}


vsftpd_header();


print "<hr>\n";

if (-e "$config{'openssl'}") {

print"<br><br>";

print "<script language=\"javascript\" src=\"js/ssl.js\" type=\"text/javascript\"></script>\n";

print "<form action=\"save_ssl.cgi\" method=\"post\" name=\"formular1\" autocomplete=\"OFF\" target=\"_self\" onSubmit=\"return validate_form(this)\">\n";
print "<table border width=100%>\n";
print "<tr $tb> <td><b>SSL Certificate Creation</b></td> </tr>\n";
print "<tr $cb> <td><table width=100%>\n";
print "<tr><td>";

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

print <<EOM;

<table width="100%" border="0" cellpadding="0" cellspacing="0">
  <tr>
   <td width="21%" height="30">Servername:</td>
    <td width="79%" height="30">
    <input name="authority" type="text" value="$SSL_CN">

   </tr>
	  
   <tr>
     <td width="21%" height="30">E-Mail adress:</td>
     <td width="79%" height="30">
    <input name="email" type="text" value="$SSL_EMAIL">
    </td>
   </tr>
    
   <tr>
     <td width="21%" height="30">Name/Company:</td>
     <td width="79%" height="30">
    <input name="organization" type="text" value="$SSL_COMPANY">
    </td>
   </tr>

   <tr>
     <td width="21%" height="30">Department:</td>
     <td width="79%" height="30">
    <input name="departement" type="text" value="$SSL_DEPARTEMENT">
    </td>
   </tr>

   <tr>
     <td width="21%" height="30">City:</td>
     <td width="79%" height="30">
    <input name="city" type="text" value="$SSL_CITY">
    </td>
   </tr>

   <tr>
     <td width="21%" height="30">Federal state:</td>
     <td width="79%" height="30">
    <input name="state" type="text" value="$SSL_STATE">
    </td>
   </tr>

   <tr>
     <td width="21%" height="30">Country:</td>
     <td width="79%" height="30">
    <input name="country" type="text" maxlength="2" value="$SSL_COUNTRY">
    </td>
   </tr>

  <tr>
    <td width="21%" height="30">&nbsp;</td>
    <td width="79%" height="30">&nbsp;</td>
  </tr>

  <tr>
    <td width="21%" height="30">&nbsp;</td>
    <td width="79%" height="30"><input name="submit" type="submit" value="CREATE CERTIFICATE"></td>
  </tr>

  </table>


EOM


    print "</table></td></tr></table>\n";
        print "</form>";

} else {
 print "<br><br>";
 print "Could not find the ssl prog.<br>";
 print "You need openssl inorder to create a SSL CERT. Please check you <a href=\"../config.cgi?vsftpd\" target=\"_self\">module config</a><br>";
 print "<br><br>";
 print "<br><br>";
}


&footer("index.cgi", "vsftpd");
