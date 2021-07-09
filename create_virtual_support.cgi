#!/usr/bin/perl


use WebminCore;
do './vsftpd-lib.pl';
$|=1;
&init_config("vsftpd");

%access=&get_module_acl;
if($ENV{'REQUEST_METHOD'} eq 'GET') { &redirect("") }
&ReadParse();


### Activate Virtual Support ################

if (-e $config{'virtual'}) {

open(VIRTUAL,">>$config{'path'}");
print VIRTUAL "### VIRTUAL USER SUPPORT CREATED BY WEBMINMODULE VSFTPD ###\n";
print VIRTUAL "\n";
print VIRTUAL "pam_service_name=vsftpd\n";
print VIRTUAL "nopriv_user=vsftpd\n";
print VIRTUAL "guest_enable=YES\n";
print VIRTUAL "guest_username=vsftpd\n";
print VIRTUAL "user_sub_token=\$USER\n";
print VIRTUAL "virtual_use_local_privs=YES\n";
print VIRTUAL "user_config_dir=/etc/vsftpd/vsftpd_user_conf \n";
print VIRTUAL "\n";
print VIRTUAL "### END VIRTUAL USER SUPPORT CREATED BY WEBMINMODULE VSFTPD ###\n";
close(VIRTUAL);

#### TODO

system("useradd -m -d /var/vsftpd -s /sbin/nologin -g ftp -c 'vsftpd user' vsftpd");

}


###########################################################


&redirect("../virtual.cgi");




