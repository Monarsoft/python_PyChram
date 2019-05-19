# Mysql -hlocalhost -P3306 -uroot -p	启动客户端
# Mysqld --defaults -file="C:\MySQL\my.ini"	启动服务端

Create database  DB_1; 	 #创建数据库
Create database `123`; #	以特殊的命名需要加反引号包裹
Create database `create`;#	以关键字创建也需要跟上反引号包裹

Create database `班级`;	 #中文 也需要加反引号

Create table  db_one.db_class(class_on varchar(30),Date_start date );	#创建数据表
Create table `create`.create_one(class_create varchar(20), date_start date);	#在关键字名的数据库中创建表(也需要加上 ``反引号)


/* 学生管理*/
create table info_student(
name varchar(20),
student_ID varchar(20)
);

#/* 考试管理*/
create table exam_student(
name varchar(20),
student_ID varchar(20),
scor varchar(20)
);
create table exam_question(
content varchar(30),
answer varchar(30)
);

-- #/× xx %百分号的使用×/
show database like `db_%`;
show table like `exam_%`;

show create table exam_student;

describe exam_sudent; #/*查询表的结构*/
drop table infor_class ; #/*删除表*/
drop database aa ; # /*删除数据库*/
drop table if exists infor_class ; --#*删除表，表不存在也不会报错*/
rename table infor_class to exam_class, infor_student to bogy; #* 同时修改多个表
alter table exam_student modify student_ID(30);
show create table exam_student; #	查询表类型
alter table exam_student character set utf8; # 修改
alter table exam_andy add get varchar(100); # 	增加列  add \modify \change

-- /*插入类容（行）*/
insert into exam_student (name,student_ID) values ("xiaoming","1406011"); #添加一条记录

select * from exam_student where 1; 	--#查询所有字段值 ，1表示成立

update exam_student set name="xiaoling" where name="xiaoming";	#修改字段值

# 整型
create table exam_1 (aa_1 int );
create table exam_2 (aa_2 int );

rename table exam_1 to exam_3, exam_2 to exam_1, exam_3 to exam_2;	--#交换两个表的字段值（内容）

insert into exam_int (aa,bb) values (255,-128);
 
# 浮点型
alter table exam_int add db double(8,3);
update exam_int set db = 12345.113;
alter table exam_int add ft float(8,2);
update exam_int set ft = 1.2345E4;

alter table exam_int add money decimal(8,3) zerofill;
insert into exam_int (money) values (123.12);

# 时间日期表
create table exam_date (a datetime,b timestamp); #  创建 时间日期表
insert into exam_date  values ('2018-12-01 21:29:50','2018-12-01 11:21:55'); 
insert into exam_date values ('20181219031507','20181515052408');
insert into exam_date values (0,0);

create table exam_time( age time);
#insert into exam_time values ('23:12:36');
insert into exam_time valuse ('231211');
insert into exam_time values ('8 12:34:11');

create table exam_y (y year);
insert into exam_y values (2038);
insert into exam_y values (2034);

# 修改字段类型
create table exam_st (name char(19), notes varchar(33));
insert into exam_st values ("XiaoMing","new money");
alter table exam_st modify name char(5);
alter table exam_st modify notes varchar(8); 


create table exam_v (a varchar(65533) not null character set latin1;

create table exam_tx (a text, b text) character set latin1;
insert into exam_tx values ("nale",);

#枚举
create table exam_8 (gender enum("female", "male"));
insert into exam_8 values ('male');
集合
create table exam_9 ( hobby set('basket', 'football','pingpang') );
insert into exam_9 values ('basket');

# 列属性
create table exam_php1 (a int not null, b int );
insert into exam_php1 (a) values (10);
insert into exam_php1 (b) values (11);
update exam_php1 set b = 11 where a=10;

create table exam_php2 (a int default 101, b int default 102);
insert int exam_php2 values (101);

create table exam_py3 (a int not null default 10, 
b int default 11);

-- #primary key ,MySQL规定只能有一个主键，（索引）
create table teacher(t_id int primary key,
t_name varchar(5),
class_name varchar(6),
days tinyint unsigned);
insert into teacher values(1,'LiXia','0331',25);
set names gbk;
update teacher set t_name = '韩雯' where t_id=1;
insert into teacher values(3,'李敏','0228',22);
insert into teacher values(5,'孟达','0228',24);
insert into teacher values(8,'刘虎','0332',22);

-- #primary key(组合主键)，
create table teacher_1(t_id int,

t_name varchar(5),
class_name varchar(6),
days tinyint unsigned,
primary key (t_id));

-- # 多个字段类型组成一个主键，
create table teacher_2(t_id int,
t_name varchar(5),
class_name varchar(6),
days tinyint unsigned,
primary key (t_id,class_name));

-- # 自动增长
create table teacher_3 (t_id int primary key auto_increment,
t_name varchar(5), class_name varchar(6),
days tinyint unsigned);
insert into teacher_3 values (null,'韩B','0335',34); #方式1
insert into teacher_3 (t_name, class_name,
days) values ('韩B','0335',34); # 方式2

alter table teacher_3 auto_increment = 10;  # 设置主键从10 开始增长
insert into teacher_3 values (null,'韩B','0335',34);

alter table teacher_3 auto_increment = 5;   
insert into teacher_3 values (null,'云B','305',43); --# 注意这里不会以5开始，之前设置了10开始，所以从

-- # 外键													#5 开始增长就会与10发生冲突，
drop table if exists monarsoft_class;
create table monarsoft_class (
class_id int primary key auto_increment,
class_name varchar(10) not null default 'monarsoft_py' comment '班级名称'
)character set utf8;

drop table if exists monarsoft_student; 
create table monarsoft_student(
student_ID int primary key auto_increment,
student_name varchar(10) not null default '',
class_id int,
foreign key(class_id) references monarsoft_class(class_id)
)character set utf8;

insert into monarsoft_student values (null,'Roc',1010101);
insert into monarsoft_class values (1010101, 'zhudi');
insert into monarsoft_student values (null,'Roc',1010101);

alter table monarsoft_student drop foreign key monarsoft_student_ibfk_1;

alter table monarsoft_student add foreign key (class_id) references monarsoft_class
(class_id) on delete set null;  # 删除时， 将 从表外键，设置为null

delete from monarsoft_class where class_id = 1010101;

alter table monarsoft_student add foreign key (class_id) references monarsoft_class
(class_id) on delete cascade;  # 删除时， 将 从表外键，cascade(做同样的操作<级联>)

alter table monarsoft_student add foreign key (class_id) references monarsoft_class
(class_id) on delete cascade on update restrict;

alter table monarsoft_student add foreign key (class_id) references monarsoft_class
(class_id) on update restrict;

update monarsoft_class set class_id=2 where class_name="pake";

//
alter table itcast_class engine myisam;


create table class_room (room_id int primary key auto_increment,
room_no char(3))engine myisam character set utf8;

insert into from class_room values ('翰林');
-- # --------------------------------------------------------------------------------
create table teacher_class (id int primary key auto_increment,
t_name varchar (5), student_ID int (3), t_day int (3));

insert into from teacher_class values ("韩旭", 30453, 23);
insert into teacher_class(t_name,begin_date,end_date) values ("韩丽",4545,46) ;
insert into teacher_class(t_name,begin_date,end_date) values ("夏莉",23543,34);
## 排序
select * from teacher_class order by id desc;
select * from teacher_class order by t_day desc;
alter table teacher_class change t_day end_date int;
alter table teacher_class change class_id begin_date int;
select * from teacher_class group by t_name asc , end_date desc;

-- ## 限制记录获得的数量   limit 限量操作
offset | row-count
select * from teacher_class limit 1;      #只显示一条语句
select * from teacher_class limit 3, 3;
select * from teacher_class limit offset, row-count;
# // union 联合操作
select t_name, end_days  from teacher_class where begin_date = 'py0112' order by end_days desc ;
select t_name, end_days  from teacher_class where begin_date = "py0115" order by end_days desc ;
select t_name, end_days  from teacher_class where begin_date in ("py0112","py0115")  order by  end_days desc ;
select t_name, end_days  from teacher_class where begin_date = "py0115" or begin_date = "py0112" order by end_days;
select t_name, end_days  from teacher_class where begin_date in ("py0112","pdy0115")  order by  end_days desc limit 3;

(select t_name, end_days from teacher_class where begin_date = "py0115" order by  end_days desc limit 1)
union
(select t_name, end_days from teacher_class where begin_date = "py0112" order by  end_days desc limit 1);

-- # all
(select  t_name, end_days, t_sex from teacher_class where begin_date = "py0115")
union all
(select  t_name, end_days, t_sex from teacher_class where begin_date = "py0112" order by end_days desc );

-- # 使用 union 联合语句,  配合 limit 使用 否者 order by 被忽略
(select  t_name, end_days, t_sex from teacher_class where begin_date = "py0115" order by end_days limit 10) union all
(select  t_name, end_days, t_sex from teacher_class where begin_date = "py0112" order by end_days desc limit 10 );

-- 子语句的括号不是必须的
select  t_name, end_days, t_sex from teacher_class where begin_date = "py0115"
union
select  t_name, end_days, t_sex from teacher_class where begin_date = "py0112";

-- 检索结果的列明问题：
-- 第一条select语句的列明而定。
select  t_sex, end_days, t_sex from teacher_class where begin_date = "py0115"
union
select  t_name, end_days, t_name from teacher_class where begin_date = "py0112";

select * from teacher_class order by end_days desc  limit 1;

-- 子查询
select max(end_days) from teacher_class;
select * from teacher_class where end_days = (select max(end_days) from teacher_class);

select t_name from teacher_class where begin_date =  'py0113';
select t_name, begin_date, end_days from teacher_class where t_name in
(select t_name from teacher_class where begin_date =  'py0113');

select t_name, begin_date, end_days from teacher_class where t_name != any
(select t_name from teacher_class where begin_date =  'py0113');

-- 行查询(返回一行)
select distinct t_name, begin_date from teacher_class where begin_date  = "py0113" and t_name = "韩丽";
select * from teacher_class where (t_name,begin_date) = (select distinct t_name, begin_date from
teacher_class where begin_date  = "py0113" and t_name = "韩丽");

select distinct t_name, begin_date from teacher_class where begin_date  = "py0113" and t_name = "韩丽";
select * from teacher_class where (t_name,begin_date) = (select distinct t_name, begin_date from
 teacher_class where begin_date  = "py0113" and t_name = "韩丽");

-- 返回一个表
Select * from (select t_name, begin_date, end_days from teacher_class where end_days >15)
As temp where  t_name like "韩%";

select * from teacher_class where exists (select * from teacher where teacher_class.id = t_id);
||
select * from teacher_class where id in (select t_id from teacher);


-- enum 枚举类型(只能固定其中之一值)
create table join_teacher (
id int primary key auto_increment, t_name varchar(10),
 gender enum('male','female','secret')
) engine innodb character set utf8;
insert into join_teacher values
(1,'韩信','male'),
(2,'李白','female'),
(3,'韩非子','secret'),
(4,'孙武','male');

create table join_class (id int primary key auto_increment, c_name char (10),
room char (3)) engine innodb character set utf8;
insert into join_class values
(1,'py0115','207'),
(2,'py0113','104'),
(3,'py0112','102');

-- 代课时间表
create table join_teacher_class(
id int primary key auto_increment,
t_id int,
c_id int,
days tinyint,
begin_date date,
end_date date
) engine innodb character set utf8;
insert into join_teacher_class value
(1,1,1,15,'2013-01-15','2013-02-20'),
(2,1,2,18,'2013-02-15','2013-03-30'),
(3,1,3,22,'2013-03-15','2013-05-05'),
(4,1,1,20,'2013-02-15','2013-03-25'),
(5,1,2,22,'2013-03-15','2013-04-29'),
(6,3,1,15,'2013-03-15','2013-04-18'),
(7,1,1,15,'2013-04-15','2013-05-01'),
(8,3,3,15,'2013-05-15','2013-06-15'),
(9,2,1,5 ,'2013-05-15','2013-05-15');