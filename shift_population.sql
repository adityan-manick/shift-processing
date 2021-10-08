use ETL;

create table holiday (holi_id int primary key, date date, reason varchar(50));

insert into holiday (holi_id, date, reason) values
(101, '2021-01-1', 'New Year'),
(102, '2021-01-12', 'Shankaranthi'),
(103, '2021-01-26', 'Republic Day'),
(104, '2021-02-18', 'ID Day'),
(105, '2021-05-1', 'May Day'),
(106, '2021-08-15', 'Independence Day'),
(107, '2021-11-1', 'Founders  Day'),
(108, '2021-12-25', 'Christmas Day'),
(109, '2022-01-1', 'New Year'),
(110, '2021-01-16', 'Shankaranthi');

update holiday set date = '2022-01-16' where holi_id = 110;

select * from holiday;

create table shifts(shift_id int primary key auto_increment, date date, start_time varchar(10), end_time varchar(10));

create table shift_types(shift_desc int, start_time varchar(10), end_time varchar(10));

insert into shift_types(shift_desc, start_time, end_time) values
('Morning shift','6.00 AM', '2.00 PM'),
('Morning shift','2.00 PM', '10.00 PM');