--drop table countries;
--drop table continents;

create table countries (
    country varchar,
    territory int,
    population int,
    currency varchar
);
insert into countries values ('Ukraine', 50, 50, 'UAH');
insert into countries values ('Japan', 100, 200, 'Yenas');
insert into countries values ('England', 80, 40, 'GBP');
insert into countries values ('USA', 500, 150, 'USD');
alter table countries add capital varchar;
update countries set capital= 'Kyiv' where country= 'Ukraine';
update countries set capital= 'Tokio' where country= 'Japan';
update countries set capital= 'Washington' where country= 'USA';
update countries set capital= 'London' where country= 'England';

--Bonus

create table continents(
    continent varchar primary key,
    clymate varchar
);  
insert into continents values ('Europe', 'Cold');
insert into continents values ('Asia', 'Warm');
insert into continents values ('North America', 'Medium');
alter table countries add continent varchar references continents(continent);
update countries set continent= 'Europe' where country= 'Ukraine';
update countries set continent= 'Asia' where country= 'Japan';
update countries set continent= 'North America' where country= 'USA';
update countries set continent= 'Europe' where country= 'England';

select capital from countries where continent= 'Asia';
select capital from countries where continent= 'Europe';
select capital from countries where continent= 'North America';

select count(country) from countries where continent= 'Europe';
select count(country) from countries where continent= 'Asia';
select count(country) from countries where continent= 'North America';

select sum(population) from countries where continent= 'Europe';
select sum(population) from countries where continent= 'Asia';
select sum(population) from countries where continent= 'North America';



