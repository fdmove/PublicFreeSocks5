CREATE TABLE `socks5` (`idx` INTEGER not null primary key autoincrement, 
`ip` TEXT not NULL,
`port` INTEGER not NULL,
`star` INTEGER DEFAULT 0,
`status` INTEGER DEFAULT 0
);
CREATE UNIQUE INDEX idx_1st_main on socks5 (ip,port);
