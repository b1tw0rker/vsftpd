#!/usr/bin/perl


use WebminCore;
do './vsftpd-lib.pl';
$|=1;
&init_config("vsftpd");

%access=&get_module_acl;
if($ENV{'REQUEST_METHOD'} eq 'GET') { &redirect("") }
&ReadParse();


vsftpd_header();

$VERISIGN ="<a href=\"http://www.verisign.com\" target=\"_blank\">Verisign</a>";
$THAWTE   ="<a href=\"http://www.thawte.com\" target=\"_blank\">Thawte</a>";

print "<br>\n";

print "<table width=\"100%\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\">\n";
print " <tr>\n";
print "  <td width=\"60\" align=\"left\" valign=\"top\"><img src=\"images/ca.gif\" width=\"48\" height=\"48\"></td>\n";
print "  <td align=\"left\" valign=\"top\"> \n";
print "  <b>SSL CERTIFACTE IS READY TO GO</b>\n";
print " <br><br>\n";
print "You can optionally use the CERTIFICATE REQUEST below to sign your certificate<br>at $VERISIGN or $THAWTE for example.\n";
print " </td>\n";
print " </tr>\n";
print "</table>\n";


###########################################################################################################################################################


if (-e "/etc/vsftpd/ssl") { 

} else {
  system ("mkdir /etc/vsftpd/ssl");
}

 ### Setup our destinations. - der Pfad zur dem Homeverzeichnis des SSL Hostes, dann in der Ordner ssl gehen
 $server_cert = "/etc/vsftpd/ssl/certificate.pem";
 $server_key  = "/etc/vsftpd/ssl/key.pem";

  ### Setup temporary files.
  $cert_temp = &tempname();
  $key_temp = &tempname();

  # pipe to ssl

   $OPENSSLPRG = $config{'openssl'};

if (-e "$config{'openssl'}") {

    open CA, "| $OPENSSLPRG req -new -x509 -days 1460 -nodes -out $cert_temp -keyout $key_temp -config openssl.cnf > /dev/null 2>&1";
     print CA "$in{'country'}\n";
     print CA "$in{'state'}\n";
     print CA "$in{'city'}\n";
     print CA "$in{'organization'}\n";
     print CA "$in{'departement'}\n";
     print CA "$in{'authority'}\n";
     print CA "$in{'email'}\n";
    close CA;

  ### If they exist, move the two files into place.
  if (-r $cert_temp && -r $key_temp) {
    system "mv -f $cert_temp $server_cert";
    system "mv -f $key_temp $server_key";


   ## CAT certificate.pem into key.pem
   system ("cat $server_cert >> $server_key");

   unlink ("$server_cert"); 
   system "chmod 644 $server_key";
   system "cp $server_key /etc/vsftpd/ssl/vsftpd.pem";

  }

  unlink $cert_temp, $key_temp;


  ### do CSR for signing up a cert. ###############################################
    my $csr_temp = &tempname();

    ### Run openssl to generate it.
    open CSR, "| $OPENSSLPRG req -new -key $server_key -out $csr_temp > /dev/null 2>&1";
      print CSR "$in{'country'}\n";
      print CSR "$in{'state'}\n";
      print CSR "$in{'city'}\n";
      print CSR "$in{'organization'}\n";
      print CSR "$in{'departement'}\n";
      print CSR "$in{'authority'}\n"; 
      print CSR "$in{'email'}\n";
      print CSR "\n\n";
    close CSR;

    ### Read the CSR into $csr for displaying to user.
    open CSR, $csr_temp; while (<CSR>) { $csr .= $_; } close CSR;


    unlink $server_key;

##########################################################################################################################################

print "<br><br>";
print "&nbsp;&nbsp;<textarea ID=\"holdtext\" name=\"csr_field\" cols=\"80\" rows=\"15\" class=\"input2\">$csr</textarea>\n";


print "<br><br>";
print "<br><br>";
print "<br><br>";

print "The SSL CERT named: vsftpd.pem is ready to go in the folder: /etc/vsftpd/ssl";
print "<br><br>";
print "You may now activate your ssl cert - <a href=\"misc.cgi\" target=\"_self\">Click here</a>";

print "<br><br>";

} else {
 print "<br><br>";
 print "Could not find the ssl prog.<br>";
 print "You need openssl inorder to create a SSL CERT. Please check you <a href=\"../config.cgi?vsftpd\" target=\"_self\">module config</a><br>";
 print "<br><br>";
 print "<br><br>";
}





























print "<br><br>\n";
&footer("index.cgi", "vsftpd");
