#!/usr/bin/perl


use WebminCore;
do './vsftpd-lib.pl';
$|=1;
&init_config("vsftpd");

%access=&get_module_acl;
if($ENV{'REQUEST_METHOD'} eq 'GET') { &redirect("") }
&ReadParse();


if ($in{'xfer_format'} eq "NO") {
 &replace_file_line ("$config{'path'}", $in{'format_pos'}, "xferlog_std_format=NO\n");
} else {
 &replace_file_line ("$config{'path'}", $in{'format_pos'}, "xferlog_std_format=YES\n");
}

if ($in{'xfer_file'} ne "") {
 &replace_file_line ("$config{'path'}", $in{'file_pos'}, "xferlog_file\=$in{'xfer_file'}\n");
} else {
 &replace_file_line ("$config{'path'}", $in{'file_pos'}, "#xferlog_file\=/var/log/vsftpd.log\n");
}

### check if xfer.log is present
if (-e "$in{'xfer_file'}") { } else {
system ("touch $in{'xfer_file'}");
}

### Activate /Deactivate Webalizer Support ################

if ($in{'webalizer'} eq "1") {
 system ("touch webalizer.log");
   if (-e "webalizer/index.html") { } else {
      system ("touch webalizer/index.html");

open(INDEX,">webalizer/index.html");
print INDEX "<HTML>\n";
print INDEX "<HEAD>\n";
print INDEX " <TITLE>isp4you Webstats</TITLE>\n";
print INDEX "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=iso-8859-1\">\n";
print INDEX " <style type=\"text/css\">\n";
print INDEX ".Stil2  { font-family: Verdana, Arial, Helvetica, sans-serif;color: #CCCCCC; font-size: 10px; }\n";
print INDEX ".border { border: 1px solid #aaaaFF;}\n";
print INDEX ".Stil1  { font-size: 10px; font-family: Verdana, Arial, Helvetica, sans-serif; }\n";
print INDEX ".Stil3  { color: #333333}\n";
print INDEX "</style>\n";
print INDEX "</HEAD>\n";
print INDEX "<BODY BGCOLOR=\"#E8E8E8\" TEXT=\"#000000\" LINK=\"#0000FF\" VLINK=\"#FF0000\" SCROLL=\"NO\">\n";
print INDEX "<table width=\"60%\" height=\"70\"  border=\"0\" align=\"center\" cellpadding=\"0\" cellspacing=\"0\" class=\"border\">\n";
print INDEX "  <tr>\n";
print INDEX "    <td valign=\"top\"><table width=\"100%\"  border=\"0\" cellpadding=\"0\" cellspacing=\"0\" bgcolor=\"#CCCCCC\">\n";
print INDEX "      <tr>\n";
print INDEX "        <td height=\"20\" valign=\"middle\">&nbsp;<span class=\"Stil2\">&nbsp;<span class=\"Stil3\">Message</span></span></td>\n";
print INDEX "      </tr>\n";
print INDEX "    </table>\n";
print INDEX "    <p class=\"Stil1\">&nbsp;&nbsp;No Webalizer Webstats generated till now.<br>\n";
print INDEX "    &nbsp;&nbsp;Webstats will be generated once per day in the night.</p>\n";
print INDEX "    <p class=\"Stil1\">&nbsp;</p>\n";
print INDEX "    <p class=\"Stil1\">&nbsp; </p></td>\n";
print INDEX "  </tr>\n";
print INDEX "</table>\n";
print INDEX "<p>&nbsp;</p>\n";
print INDEX "<p>&nbsp;</p>\n";
print INDEX "</BODY>\n";
print INDEX "</HTML>\n";
close (INDEX);
    }



open(WEBALIZER,">/etc/cron.daily/webalizer_ftp");
print WEBALIZER "#!/bin/sh\n";
print WEBALIZER "\n";
print WEBALIZER "if \[ -s $root_directory/vsftpd/webalizer/xfer_log \] \; then\n";
print WEBALIZER "/usr/bin/webalizer -c $root_directory/vsftpd/webalizer/xfer_log > /dev/null 2>&1\n";
print WEBALIZER "\n";
print WEBALIZER "fi\n\n";
print WEBALIZER "exit 0\n\n";
close(WEBALIZER);

system ("chmod 700 /etc/cron.daily/webalizer_ftp");


open(XFER,">webalizer/xfer_log");
print XFER "LogFile $in{'xfer_file'}\n";
print XFER "OutputDir $root_directory/vsftpd/webalizer\n";
print XFER "Hostname FTP-TRAFFIC\n";
print XFER "HistoryName $root_directory/vsftpd/webalizer/webalizer.hist\n";
print XFER "Incremental yes\n";
print XFER "IncrementalName $root_directory/vsftpd/webalizer/webalizer.current\n";
print XFER "FoldSeqErr yes\n";
print XFER "ReallyQuiet yes\n";
print XFER "\n";
print XFER "LogType ftp\n";
print XFER "ReportTitle FTP Stats\n";
print XFER "HourlyGraph no\n";
print XFER "HourlyStats no\n";
print XFER "TimeMe yes\n";
print XFER "\n";
print XFER "GraphLegend no\n";
print XFER "CountryGraph no\n";
print XFER "DailyGraph no\n";
print XFER "DailyStats no\n";
print XFER "PageType htm*\n";
print XFER "PageType php\n";
print XFER "\n";
print XFER "TopAgents 0\n";
print XFER "TopSearch 0\n";
print XFER "TopReferrers 0\n";
print XFER "TopSites 0\n";
print XFER "TopKSites no\n";
print XFER "TopCountries 0\n";
print XFER "TopURLs 0\n";
print XFER "TopKURLs 0\n";
print XFER "\n";
print XFER "TopUsers 3000\n";
print XFER "AllUsers yes\n";
close(XFER);

} # end activate webalizer support


###########################################################

if ($in{'webalizer'} eq "0") {
  unlink "webalizer.log"; 
  unlink "/etc/cron.daily/webalizer_ftp";
 }


###########################################################


#&redirect("index.cgi?reload=1");
&redirect("index.cgi");

exit;


