#!/usr/bin/perl

use WebminCore;
do './vsftpd-lib.pl';
$|=1;
&init_config("vsftpd");

%access=&get_module_acl;
if($ENV{'REQUEST_METHOD'} eq 'GET') { &redirect("") }
&ReadParse();



&replace_file_line ("$config{'path'}", $in{'umask_pos'}, "local_umask=$in{'umask'}\n");

if ($in{'idle'} ne "") {
 &replace_file_line ("$config{'path'}", $in{'idle_pos'}, "idle_session_timeout=$in{'idle'}\n");
} else {
 &replace_file_line ("$config{'path'}", $in{'idle_pos'}, "#idle_session_timeout=\n");
}

if ($in{'data'} ne "") {
 &replace_file_line ("$config{'path'}", $in{'data_pos'}, "data_connection_timeout=$in{'data'}\n");
} else {
 &replace_file_line ("$config{'path'}", $in{'data_pos'}, "#data_connection_timeout=\n");
}

if ($in{'banner'} ne "") {
 &replace_file_line ("$config{'path'}", $in{'banner_pos'}, "ftpd_banner=$in{'banner'}\n");
} else {
 &replace_file_line ("$config{'path'}", $in{'banner_pos'}, "#ftpd_banner=\n");
}

if ($in{'user'} ne "") {
 &replace_file_line ("$config{'path'}", $in{'user_pos'}, "ftp_username=$in{'user'}\n");
} else {
 &replace_file_line ("$config{'path'}", $in{'user_pos'}, "#ftp_username=\n");
}

## Max per IP
if ($in{'max_per_ip'} ne "") {
 &replace_file_line ("$config{'path'}", $in{'max_per_ip_pos'}, "max_per_ip=$in{'max_per_ip'}\n");
} else {
 &replace_file_line ("$config{'path'}", $in{'max_per_ip_pos'}, "#max_per_ip=\n");
}


## pam_service_name
if ($in{'pam_service_name'} ne "") {
 &replace_file_line ("$config{'path'}", $in{'pam_service_name_pos'}, "pam_service_name=$in{'pam_service_name'}\n");
} else {
 &replace_file_line ("$config{'path'}", $in{'pam_service_name_pos'}, "#pam_service_name=\n");
}


&redirect("index.cgi");
exit;