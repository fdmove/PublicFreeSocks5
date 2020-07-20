# PublicFreeSocks5
Get the public free socks5 ip:port from some websites 

apt-get update  
apt-get install python3 
apt-get install python3-pip
pip3 install requests
pip3 install pysocks
apt-get install sqlite3 


bash db_init.sh  # 初始化本地的数据库


sqlite3 ./mySocks5.db
CREATE TABLE `socks5` (`idx` INTEGER not null primary key autoincrement, 
`ip` TEXT not NULL,
`port` INTEGER not NULL,
`star` INTEGER DEFAULT 0
`status` INTEGER DEFAULT 0
);
CREATE UNIQUE INDEX idx_1st_main on socks5 (ip,port);


表的列的信息
idx 主键索引
ip socks5服务器的ip地址
port socks5服务器的端口
star 可用统计
// 自动检测socks5程序,每次运行后,
// 如果线路可用,则star数字加1,
// 如果不可用,则star数字减1,
status 取值-1 0 1  
// -1 表示本次检测 该socks5不可用
// 0  表示本次检测 该socks5刚刚入库 初始值0
// 1  表示本次检测 该socks5可用


root@debian:~/PublicFreeSocks5# sqlite3 mySocks5.db
SQLite version 3.27.2 2019-02-25 16:06:06
Enter ".help" for usage hints.
sqlite> .table
socks5
sqlite> .schema socks5
CREATE TABLE `socks5` (`idx` INTEGER not null primary key autoincrement, 
`ip` TEXT not NULL,
`port` INTEGER not NULL,
`star` INTEGER DEFAULT 0,
`status` INTEGER DEFAULT 0
);
CREATE UNIQUE INDEX idx_1st_main on socks5 (ip,port);
sqlite> 
