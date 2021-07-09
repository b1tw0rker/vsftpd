#!/usr/bin/perl

use WebminCore;
$|=1;
&init_config("vsftpd");

%access=&get_module_acl;
if($ENV{'REQUEST_METHOD'} eq 'GET') { &redirect("") }
&ReadParse();



&replace_file_line ("$config{'path'}", $in{'chroot_pos'}, "chroot_local_user=$in{'local_chroot'}\n");
&replace_file_line ("$config{'path'}", $in{'enable_pos'}, "local_enable=$in{'local_enable'}\n");
&replace_file_line ("$config{'path'}", $in{'write_pos'}, "write_enable=$in{'local_write'}\n");

#&redirect("index.cgi?reload=1");
&redirect("index.cgi");
exit;