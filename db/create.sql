create database if not exists blogdb;
use blogdb;

drop table if exists users;
create table users
(
	id int primary key not null auto_increment,
	username varchar(64) not null unique,
	email varchar(64) not null unique,
	passwd varchar(64) not null,
	role tinyint not null default 1,
	defines varchar(128)
)engine=myisam default charset=utf8 auto_increment=1;

drop table if exists blogs;
create table blogs
(
	id int primary key not null auto_increment,
	title varchar(64) not null,
	author_id int not null,
	content longtext not null,
	post_date datetime not null,
	category_id int not null,
	readtimes int not null default 0
)engine=myisam default charset=utf8 auto_increment=1;

drop table if exists category;
create table category
(
	id int primary key not null auto_increment,
	name varchar(64) not null,
	create_date datetime not null
)engine=myisam default charset=utf8 auto_increment=1;

drop table if exists comment;
create table comment
(
	id int(10) primary key not null auto_increment,
	content varchar(128) not null,
	com_date datetime not null,
	blog_id int not null,
	email varchar(64),
	name varchar(64) not null,
	reply_id int(10) not null default -1
)engine=myisam default charset=utf8 auto_increment=1;
