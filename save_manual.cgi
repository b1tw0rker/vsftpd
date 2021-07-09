#!/usr/bin/perl

use WebminCore;
do './vsftpd-lib.pl';
$|=1;
&init_config("vsftpd");

%access=&get_module_acl;
if($ENV{'REQUEST_METHOD'} eq 'GET') { &redirect("") }
&ReadParse();



$in{'manual'} =~ s/\r//g;
open(FILE, ">$config{'path'}");
 print FILE $in{'manual'};
 close(FILE);



#&redirect("index.cgi?reload=1");
&redirect("index.cgi");
exit;