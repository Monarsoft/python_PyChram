Mysql -hlocalhost -P3306 -uroot -p	�����ͻ���
Mysqld --defaults -file="C:\MySQL\my.ini"	���������

Create database  DB_1; 	 �������ݿ�
Create database `123`; 	�������������Ҫ�ӷ����Ű���
Create database `create`;	�Թؼ��ִ���Ҳ��Ҫ���Ϸ����Ű���

Create database `�༶`;	 ���� Ҳ��Ҫ�ӷ�����

Create table  db_one.db_class(class_on varchar(30),Date_start date );	�������ݱ�
Create table `create`.create_one(class_create varchar(20), date_start date);	�ڹؼ����������ݿ��д�����(Ҳ��Ҫ���� ``������)


/* ѧ������*/
create table info_student(
name varchar(20),
student_ID varchar(20)
);

/* ���Թ���*/
create table exam_student(
name varchar(20),
student_ID varchar(20),
scor varchar(20)
);
create table exam_question(
content varchar(30),
answer varchar(30)
);

/�� xx %�ٷֺŵ�ʹ�á�/
show database like `db_%`;
show table like `exam_%`;

show create table exam_student;

describe exam_sudent \g /*��ѯ��Ľṹ*/
drop table infor_class \g /*ɾ����*/
drop database aa \g /*ɾ�����ݿ�*/ 
drop table if exists infor_class \g /*ɾ����������Ҳ���ᱨ��*/
rename table infor_class to exam_class, infor_student to bogy\g /* ͬʱ�޸Ķ����
alter table exam_student modify student_ID(30);
show create table exam_student\g	��ѯ������
alter table exam_student character set utf8\g �޸� 
alter table exam_andy add get varchar(100)\g 	������  add \modify \change

/*�������ݣ��У�*/
insert into exam_student (name,student_ID) values ("xiaoming","1406011")\g ���һ����¼

select * from exam_student where 1; 	��ѯ�����ֶ�ֵ ��1��ʾ����

update exam_student set name="xiaoling" where name="xiaoming";	�޸��ֶ�ֵ

����
create table exam_1 (aa_1 int );
create table exam_2 (aa_2 int );

rename table exam_1 to exam_3, exam_2 to exam_1, exam_3 to exam_2;	������������ֶ�ֵ�����ݣ�

insert into exam_int (aa,bb) values (255,-128);
 
������
alter table exam_int add db double(8,3);
update exam_int set db = 12345.113\g
alter table exam_int add ft float(8,2)\g
update exam_int set ft = 1.2345E4\g

alter table exam_int add money decimal(8,3) zerofill\g 
insert into exam_int (money) values (123.12)\g 

ʱ�����ڱ�
create table exam_date (a datetime,b timestamp)\g  ���� ʱ�����ڱ�
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

#�ַ�������
create table exam_st (name char(19), notes varchar(33));
insert into exam_st values ("XiaoMing","new money");
alter table exam_st modify name char(5);
alter table exam_st modify notes varchar(8); 


create table exam_v (a varchar(65533) not null character set latin1;

create table exam_tx (a text, b text) character set latin1;
insert into exam_tx values ("nale",);

#ö��
create table exam_8 (gender enum("female", "male"));
insert into exam_8 values ('male');
����
create table exam_9 ( hobby set('basket', 'football','pingpang') );
insert into exam_9 values ('basket');

# ������
create table exam_php1 (a int not null, b int );
insert into exam_php1 (a) values (10);
insert into exam_php1 (b) values (11);
update exam_php1 set b = 11 where a=10;

create table exam_php2 (a int default 101, b int default 102);
insert int exam_php2 values (101);

create table exam_py3 (a int not null default 10, 
b int default 11);

#primary key ,MySQL�涨ֻ����һ����������������
create table teacher(t_id int primary key,
t_name varchar(5),
class_name varchar(6),
days tinyint unsigned);
insert into teacher values(1,'LiXia','0331',25);
set names gbk;
update teacher set t_name = '����' where t_id=1;
insert into teacher values(3,'����','0228',22);
insert into teacher values(5,'�ϴ�','0228',24);
insert into teacher values(8,'����','0332',22);

#primary key(�������)��
create table teacher_1(t_id int,
t_name varchar(5),
class_name varchar(6),
days tinyint unsigned,
primary key (t_id));

# ����ֶ��������һ��������
create table teacher_2(t_id int,
t_name varchar(5),
class_name varchar(6),
days tinyint unsigned,
primary key (t_id,class_name));

# �Զ�����
create table teacher_3 (t_id int primary key auto_increment,
t_name varchar(5), class_name varchar(6),
days tinyint unsigned);
insert into teacher_3 values (null,'��B','0335',34); #��ʽ1
insert into teacher_3 (t_name, class_name,
days) values ('��B','0335',34); # ��ʽ2

alter table teacher_3 auto_increment = 10;  # ����������10 ��ʼ����
insert into teacher_3 values (null,'��B','0335',34);

alter table teacher_3 auto_increment = 5;   
insert into teacher_3 values (null,'��B','305',43); # ע�����ﲻ����5��ʼ��֮ǰ������10��ʼ�����Դ�

# ���													#5 ��ʼ�����ͻ���10������ͻ��
drop table if exists monarsoft_class;
create table monarsoft_class (
class_id int primary key auto_increment,
class_name varchar(10) not null default 'monarsoft_py' comment '�༶����'
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
(class_id) on delete set null;  // ɾ��ʱ�� �� �ӱ����������Ϊnull

delete from monarsoft_class where class_id = 1010101;

alter table monarsoft_student add foreign key (class_id) references monarsoft_class
(class_id) on delete cascade;  // ɾ��ʱ�� �� �ӱ������cascade(��ͬ���Ĳ���<����>)

alter table monarsoft_student add foreign key (class_id) references monarsoft_class
(class_id) on delete cascade on update restrict;

alter table monarsoft_student add foreign key (class_id) references monarsoft_class
(class_id) on update restrict;

update monarsoft_class set class_id=2 where class_name="pake";

//
alter table itcast_class engine myisam;


create table class_room (room_id int primary key auto_increment,
room_no char(3))engine myisam character set utf8;

insert into from class_room values ('����');




