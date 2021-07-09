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
if (/^local_umask/)            { $local_umask = "@$lref[$Pos]";               $umask_pos              = $Pos;  }
if (/idle_session_timeout/)    { $idle_session_timeout = "@$lref[$Pos]";      $idle_pos               = $Pos;  }
if (/data_connection_timeout/) { $data_connection_timeout = "@$lref[$Pos]";   $data_pos               = $Pos;  }
if (/ftpd_banner/)             { $ftpd_banner = "@$lref[$Pos]";               $banner_pos             = $Pos;  }
if (/ftp_username/)            { $user = "@$lref[$Pos]";                      $user_pos               = $Pos;  }
if (/max_per_ip/)              { $max_per_ip = "@$lref[$Pos]";                $max_per_ip_pos         = $Pos;  }
if (/pam_service_name/)        { $pam_service_name = "@$lref[$Pos]";          $pam_service_name_pos   = $Pos;  }
 $Pos++;
}

# Set max per IP Pos to the end of the file
$End_Pos_1 = $Pos + 1;
if ($max_per_ip_pos eq "") {
 $max_per_ip_pos = $End_Pos_1;
}

# Set ftp username Pos to the end of the file
$End_Pos_2 = $Pos + 2;
if ($user_pos eq "") {
 $user_pos = $End_Pos_2;
}

# Set local unmask Pos to the end of the file
$End_Pos_3 = $Pos + 3;
if ($umask_pos eq "") {
 $umask_pos = $End_Pos_3;
}


@local_umask = split(/\=/, $local_umask);
$local_umask = $local_umask[1];

@idle_session_timeout = split(/\=/, $idle_session_timeout);
$idle_session_timeout = $idle_session_timeout[1];

@data_connection_timeout = split(/\=/, $data_connection_timeout);
$data_connection_timeout = $data_connection_timeout[1];

@ftpd_banner = split(/\=/, $ftpd_banner);
$ftpd_banner = $ftpd_banner[1];

@user = split(/\=/, $user);
$user = $user[1];

@max_per_ip = split(/\=/, $max_per_ip);
$max_per_ip = $max_per_ip[1];

@pam_service_name = split(/\=/, $pam_service_name);
$pam_service_name = $pam_service_name[1];


vsftpd_header();


print "<hr>\n";
print"<br><br>";


print "<form action=\"save_all.cgi\" method=\"post\" name=\"form\" autocomplete=\"OFF\" target=\"_self\">";
print "<table border width=100%>\n";
print "<tr $tb> <td><b>$text{'all_headline'}</b></td> </tr>\n";
print "<tr $cb> <td><table width=100%>\n";
print "<tr><td>";

print <<EOM;

<table width="100%" border="0" cellpadding="0" cellspacing="0">
        <tr>
         <td width="21%" height="30">$text{'all_unmask'}:</td>
         <td width="79%" height="30"><input name="umask" type="text" value="$local_umask" maxlength="3">&nbsp;<em>(Example 022)</em></td>
        </tr>

        <tr>
           <td width="21%" height="30">$text{'all_idle'}:</td>
           <td width="79%" height="30"><input name="idle" type="text" value="$idle_session_timeout">&nbsp;<em>(Seconds)</em></td>
        </tr>

        <tr>
         <td width="21%" height="30">$text{'all_data'}:</td>
         <td width="79%" height="30"><input name="data" type="text" value="$data_connection_timeout">&nbsp;<em>(Seconds)</em></td>
        </tr>

        <tr>
         <td width="21%" height="30">Max. Connections per IP:</td>
         <td width="79%" height="30"><input name="max_per_ip" type="text" maxlength="5" value="$max_per_ip"></td>
        </tr>

        <tr>
         <td width="21%" height="30">$text{'all_welcome'}:</td>
         <td width="79%" height="30"><input name="banner" type="text" value="$ftpd_banner"></td>
        </tr>

        <tr>
         <td width="21%" height="30">PAM Service Name:</td>
         <td width="79%" height="30"><input name="pam_service_name" type="text" value="$pam_service_name"></td>
        </tr>

       
        <tr>
         <td width="21%" height="30">$text{'all_username'}:</td>
         <td width="79%" height="30"><input name="user" type="text" value="$user">
EOM

print &user_chooser_button('user',0 ,0);
print <<EOF;
     </td>
             </tr>



        <tr>
         <td width="21%" height="30">&nbsp;</td>
         <td width="79%" height="30">&nbsp;</td>
        </tr>


         <tr>
    <td width="21%" height="30">&nbsp;</td>
    <td width="79%" height="30"><input name="submit" type="submit" value="$text{'all_save'}"></td>
    </tr>
</table>



<input name="umask_pos" type="hidden" value="$umask_pos">
<input name="idle_pos" type="hidden" value="$idle_pos">
<input name="data_pos" type="hidden" value="$data_pos">
<input name="banner_pos" type="hidden" value="$banner_pos">
<input name="user_pos" type="hidden" value="$user_pos">
<input name="max_per_ip_pos" type="hidden" value="$max_per_ip_pos">
<input name="pam_service_name_pos" type="hidden" value="$pam_service_name_pos">

EOF


print "</tr></td>";
print "</table></td></tr></table>\n";

print "</form>";





&footer("index.cgi", "vsftpd");


