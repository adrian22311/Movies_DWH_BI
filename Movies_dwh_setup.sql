go
use Movies_dwh
go

--CREATE TABLE DateDimension
--(
--  DateID              INT         NOT NULL PRIMARY KEY,
--  [Date]              DATE        NOT NULL,
--  [Day]               TINYINT     NOT NULL,
--  DaySuffix           CHAR(2)     NOT NULL,
--  [Weekday]           TINYINT     NOT NULL,
--  WeekDayName         VARCHAR(10) NOT NULL,
--  IsWeekend           BIT         NOT NULL,
--  IsHoliday           BIT         NOT NULL,
--  HolidayText         VARCHAR(64) SPARSE,
--  DOWInMonth          TINYINT     NOT NULL,
--  [DayOfYear]         SMALLINT    NOT NULL,
--  WeekOfMonth         TINYINT     NOT NULL,
--  WeekOfYear          TINYINT     NOT NULL,
--  ISOWeekOfYear       TINYINT     NOT NULL,
--  [Month]             TINYINT     NOT NULL,
--  [MonthName]         VARCHAR(10) NOT NULL,
--  [Quarter]           TINYINT     NOT NULL,
--  QuarterName         VARCHAR(6)  NOT NULL,
--  [Year]              INT         NOT NULL,
--  MMYYYY              CHAR(6)     NOT NULL,
--  MonthYear           CHAR(7)     NOT NULL,
--  FirstDayOfMonth     DATE        NOT NULL,
--  LastDayOfMonth      DATE        NOT NULL,
--  FirstDayOfQuarter   DATE        NOT NULL,
--  LastDayOfQuarter    DATE        NOT NULL,
--  FirstDayOfYear      DATE        NOT NULL,
--  LastDayOfYear       DATE        NOT NULL,
--  FirstDayOfNextMonth DATE        NOT NULL,
--  FirstDayOfNextYear  DATE        NOT NULL
--);
--GO

create table Countries
(
	CountryID int not null IDENTITY(1,1) primary key,
	CountryName nvarchar(50) not null,
	Region varchar(50) not null,
	SubRegion varchar(50) not null,
	CountryCode char(2) not null
)
go

create table People
(
	PersonSKID int not null IDENTITY(1,1) primary key,
	PersonID int not null,
	Name nvarchar(100) not null,
	Birthday int not null foreign key references DateDimension(DateID),
	KnownFor varchar(50) not null,
	Deathday int not null foreign key references DateDimension(DateID),
	Gender varchar(10) not null,
	IMDBID char(9) not null,
	Popularity float not null,
	ValidFrom datetime not null,
	ValidTo datetime not null,
	Status char(4) not null
)
go

create table MovieDetails
(
	MovieID int not null primary key,
	MovieTitle nvarchar(100) not null,
	OriginalLanguage varchar(30) not null,
	ReleaseDateID int not null foreign key references DateDimension(DateID),
	Adult varchar(3) not null,
	PrimaryGenreName nvarchar(20) not null,
	SecondaryGenreName nvarchar(20) not null,
	MinorGenreName nvarchar(20) not null
)
go

create table Movie
(
	MovieFactID int not null IDENTITY(1,1) primary key,
	MovieID int not null foreign key references MovieDetails(MovieID),
	TMDBRating float not null,
	IMDBRating float not null,
	MovieLensRating float not null,
	Revenue money not null,
	Budget money not null,
	Popularity float not null,
	NumberOfCrewMembers int not null,
	NumberOfActors int not null,
	RuntimeInMinutes int not null,
	CountryID int not null foreign key references Countries(CountryID),
	UpdateDateID int not null foreign key references DateDimension(DateID)
)
go

create table MoviePeople
(
	SKID int not null IDENTITY(1,1) primary key,
	MovieID int not null foreign key references MovieDetails(MovieID),
	PersonID int not null, --foreign key references People(PersonID),
	PopularityOnRelease float not null,
	Job varchar(50) not null,
	Department varchar(30) not null
)
go