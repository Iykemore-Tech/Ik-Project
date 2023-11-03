create database if not exists myProject1;

-- Or

-- create schema if not exists myProject1

USE myProject1;

create table Students
(
rollNo int primary key,
name varchar(100),
email varchar(100),
gender varchar(100),
contact varchar(100),
dob varchar(100),
address varchar(200)
);

select * from Students;


Use myProject1;

create table Users
(
userId int primary key,
name varchar(100),
email varchar(100),
username varchar(100),
password varchar(100),
contact varchar(100),
dob varchar(100),
status varchar(100),
gender varchar(100),
address varchar(200)
);

select * from Users

create table Product
(
productId int primary key,
name varchar(100),
category varchar(100),
description varchar(100),
rate int
);

select * from Product;