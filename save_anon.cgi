#!/usr/bin/perl

use WebminCore;
$|=1;
&init_config("vsftpd");

%access=&get_module_acl;
if($ENV{'REQUEST_METHOD'} eq 'GET') { &redirect("") }
&ReadParse();



&replace_file_line ("$config{'path'}", $in{'enable_pos'}, "anonymous_enable=$in{'anon_enable'}\n");
&replace_file_line ("$config{'path'}", $in{'upload_pos'}, "anon_upload_enable=$in{'anon_upload'}\n");
&replace_file_line ("$config{'path'}", $in{'write_pos'}, "anon_mkdir_write_enable=$in{'anon_write'}\n");
&replace_file_line ("$config{'path'}", $in{'other_pos'}, "anon_other_write_enable=$in{'anon_other'}\n");

&redirect("index.cgi");
exit;