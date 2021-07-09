#!/usr/bin/perl


use WebminCore;
do './vsftpd-lib.pl';
$|=1;
&init_config("vsftpd");

%access=&get_module_acl;
if($ENV{'REQUEST_METHOD'} eq 'GET') { &redirect("") }
&ReadParse();



$LineCount eq 0;
open (COUNT, $config{'path'});
while(<COUNT>) {
$LineCount = $LineCount +1;
}
close(COUNT);
$LineCount = $LineCount +1;
####################################################################################################

 if ($in{'file_pos'} eq "") {
  $file_pos = $LineCount +1;
   } else {
  $file_pos = $in{'file_pos'};
 }

 if ($in{'format_pos'} eq "") {
  $format_pos = $LineCount +2;
   } else {
  $format_pos = $in{'format_pos'};
 }

 if ($in{'hide_pos'} eq "") {
  $hide_pos = $LineCount +3; 
   } else {
  $hide_pos = $in{'hide_pos'}; 
 }

 if ($in{'local_pos'} eq "") {
  $local_pos = $LineCount +4;
 } else {
  $local_pos = $in{'local_pos'};
 }

 if ($in{'anon_pos'} eq "") {
  $anon_pos = $LineCount +5;
 } else {
  $anon_pos = $in{'anon_pos'};
 }

 if ($in{'tcp_pos'} eq "") {
  $tcp_pos = $LineCount +6;
 } else {
  $tcp_pos = $in{'tcp_pos'};
 }

## new ssl stuff

 if ($in{'ssl_pos'} eq "") {
  $ssl_pos = $LineCount +7;
 } else {
  $ssl_pos = $in{'ssl_pos'};
 }

 if ($in{'force_data_pos'} eq "") {
  $force_data_pos = $LineCount +8;
 } else {
  $force_data_pos = $in{'force_data_pos'};
 }

 if ($in{'force_logins_pos'} eq "") {
  $force_logins_pos = $LineCount +9;
 } else {
  $force_logins_pos = $in{'force_logins_pos'};
 }

 if ($in{'rsa_cert_file_pos'} eq "") {
  $rsa_cert_file_pos = $LineCount +10;
 } else {
  $rsa_cert_file_pos = $in{'rsa_cert_file_pos'};
 }

####################################################################################################

if ($in{'force_dot_files'} eq "NO") {
  &replace_file_line ("$config{'path'}", $format_pos, "force_dot_files=NO\n");
  } else {
  &replace_file_line ("$config{'path'}", $format_pos, "force_dot_files=YES\n");
}

if ($in{'tcp'} eq "NO") {
  &replace_file_line ("$config{'path'}", $tcp_pos, "tcp_wrappers=NO\n");
  } else {
  &replace_file_line ("$config{'path'}", $tcp_pos, "tcp_wrappers=YES\n");
}


if ($in{'listen_address'} ne "") {
  &replace_file_line ("$config{'path'}", $file_pos, "listen_address\=$in{'listen_address'}\n");
  } else {
  &replace_file_line ("$config{'path'}", $file_pos, "#listen_address\=\n");
}


if ($in{'hide_file'} ne "") {
  &replace_file_line ("$config{'path'}", $hide_pos, "hide_file\=$in{'hide_file'}\n");
  } else {
  &replace_file_line ("$config{'path'}", $hide_pos, "#hide_file\=\n");
}


if ($in{'anon_max_rate'} ne "") {
  &replace_file_line ("$config{'path'}", $anon_pos, "anon_max_rate\=$in{'anon_max_rate'}\n");
  } else {
  &replace_file_line ("$config{'path'}", $anon_pos, "#anon_max_rate\=\n");
}


if ($in{'local_max_rate'} ne "") {
  &replace_file_line ("$config{'path'}", $local_pos, "local_max_rate\=$in{'local_max_rate'}\n");
  } else {
  &replace_file_line ("$config{'path'}", $local_pos, "#local_max_rate\=\n");
}

## new ssl stuff
if (-e "$in{'rsa_cert_file'}") {

if ($in{'ssl_enable'} ne "") {
  &replace_file_line ("$config{'path'}", $ssl_pos, "ssl_enable\=$in{'ssl_enable'}\n");
  } else {
  &replace_file_line ("$config{'path'}", $ssl_pos, "#ssl_enable\=\n");
}

if ($in{'force_local_data_ssl'} ne "") {
  &replace_file_line ("$config{'path'}", $force_data_pos, "force_local_data_ssl\=$in{'force_local_data_ssl'}\n");
  } else {
  &replace_file_line ("$config{'path'}", $force_data_pos, "#force_local_data_ssl\=\n");
}

if ($in{'force_local_logins_ssl'} ne "") {
  &replace_file_line ("$config{'path'}", $force_logins_pos, "force_local_logins_ssl\=$in{'force_local_logins_ssl'}\n");
  } else {
  &replace_file_line ("$config{'path'}", $force_logins_pos, "#force_local_logins_ssl\=\n");
}

if ($in{'rsa_cert_file'} ne "") {
  &replace_file_line ("$config{'path'}", $rsa_cert_file_pos, "rsa_cert_file\=$in{'rsa_cert_file'}\n");
  } else {
  &replace_file_line ("$config{'path'}", $rsa_cert_file_pos, "#rsa_cert_file\=\n");
}

}











&redirect("index.cgi");
exit;
