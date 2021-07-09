--
-- Table structure for table `passwd`
--

CREATE TABLE `passwd` (
`id` int(11) NOT NULL auto_increment,
`dom_id` int(11) default NULL,
`username` char(255) default NULL,
`passwd` char(80) default NULL,
`rootdir` char(255) default NULL,
`status` char(1) NOT NULL default 'A',
PRIMARY KEY  (`id`)
) ENGINE=MyISAM;

--
-- Table structure for table `passwd_logs`
--

CREATE TABLE `passwd_logs` (
`id` int(11) NOT NULL auto_increment,
`msg` char(255) default NULL,
`user` char(255) default NULL,
`pid` char(255) default NULL,
`host` char(255) default NULL,
`rhost` char(255) default NULL,
`logtime` char(255) default NULL,
PRIMARY KEY  (`id`)
) ENGINE=MyISAM;