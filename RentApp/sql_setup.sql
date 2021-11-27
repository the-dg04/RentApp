#create database rentApp;
create table rents(
	id int not null primary key auto_increment,renter varchar(50) not null,
	rentee varchar(50),address varchar(50),
	status varchar(50) default 'available');

insert into rents(renter,address) values('Sam','adr1');
insert into rents(renter,address) values('Tom','adr2');
insert into rents(renter,address) values('John','adr3');
insert into rents(renter,address) values('John','adr4');
insert into rents(renter,address) values('Sam','adr5');
insert into rents(renter,address) values('Toby','adr6');
insert into rents(renter,address) values('Bill','adr7');
insert into rents(renter,address) values('Sam','adr8');
insert into rents(renter,address) values('Alex','adr9');
insert into rents(renter,address) values('John','adr10');
insert into rents(renter,address) values('Toby','adr11');
insert into rents(renter,address) values('Dave','adr12');