### Header
sub vsftpd_header
{
 &header($text{'index_title'}, "", "intro", 1, 1, undef, "<A HREF=\"http://provider4u.de\" target=\"_blank\">Home</A> v. 1.4");
}


### Reload ###############################################################################################
  sub vsftpd_reload
  {

    if (-e "/etc/xinetd.d/vsftpd") {
      system ("/etc/init.d/xinetd restart"); 
	  
    }
  
   

   #if (-e "/etc/xinetd.d/ftp") {
   #   system ("/etc/init.d/xinetd restart");
   # }


    if (-e "/etc/init.d/vsftpd" && !-e "/etc/xinetd.d/vsftpd" ) {
     system ("/etc/init.d/vsftpd restart");
    }


  }
### Start ################################################################################################
  sub vsftpd_start
  {
    if (-e "/etc/init.d/vsftpd") {
      system ("/etc/init.d/vsftpd start");
    }
  }

### Stop #################################################################################################
  sub vsftpd_stop
  {

    if (-e "/etc/init.d/vsftpd") {
      system ("/etc/init.d/vsftpd stop");
    }


  }


### MYSQL CONNECT

sub vsftpd_mysql_connect {
 use DBI;
 $PORT="";
 $dbh=DBI->connect("DBI:mysql:$config{'mysqldb'}:$config{'mysqlhost'}$PORT",$config{'mysqluser'},$config{'mysqlpass'},{PrintError => 0, RaiseError => 0 }) || &error('could not connect to vsftpd database. You may start your MySQL database or check the MySQL config in the <a href="../config.cgi?vsftpd">module config.</a>');
}


