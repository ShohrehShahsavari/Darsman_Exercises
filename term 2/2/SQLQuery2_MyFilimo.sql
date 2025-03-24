use master
go
drop database if exists dbMyFilimo
go
----------------------------------------------------
create database dbMyFilimo
go
use DbMyfilimo
go
---------------------------------------------------------
create table Roles (
	RoleId int primary key not NULL,
	RoleTitle varchar(50) not NULL
	)
go
insert into Roles values (1,'admin'),(2,'client')
go
-----------------------------------------------------------
create table Users(
	userId int primary key identity(1000,1),
	[Name] varchar(50) not NULL,
	Family varchar(50) not NULL,
	mobileNumber varchar(50) not NULL,
	[password] varchar(50) not NULL,
	timeRegister datetime,
	isActive bit default(1),
	Email Varchar(30),
	RoleId int,
	foreign key (RoleId) references Roles(RoleId)
)
go
insert into Users([Name], [Family], [mobileNumber], [password], [timeRegister], [Email], [RoleId]) 
			values ('ali','alaie','091000','abc',getdate(),'ali@yahoo.com',1),
					('sahar','ghavi','092000','edf',getdate(),'sahar@gmail.com',2),
					('mehdi','mahdavi','031000','wer',getdate(),'mehdi@hotmail.com',2),
					('arash','hasani','094000','zxc',getdate(),'arash@yahoo.com',1),
					('ali','alaie','091000','abc',getdate(),'ali@yahoo.com',2)
go
--------------------------------------------------------------------------------------------------
create table [types] (
typeID int primary key not NULL,
typeTitle varchar(100) not NULL
)
go
insert into [types] values (1,'Filmes'),
							(2,'Series')
go
-------------------------------------------------------------------
create table genres(
	genreId int primary key not NULL,
	genreTitle varchar(50) not NULL
)
go
insert into genres values (1,'Action'),(2,'Thriller'),(3,'Horror'),
						(4,'Comedy'),(5,'Western'),(6,'History')
go
----------------------------------------------------------------
create table filmes(
	filmeId int primary key identity(100,1) not NULL,
	filmeTitle varchar(100) not NULL,
	directorName varchar(50) not NULL,
	WritersName varchar(150) NULL,
	StarsName varchar(150) NULL,
	[language] varchar(30) NULL,
	shortStory varchar(1500) sparse,
	[description] varchar(500) sparse,
	dateOfProduced varchar(5),
	country varchar(30),
	imageName varchar(50) default('nophoto.png'),
	RegeisterId int,
	typeID int,
	Season varchar(30) NULL,
	foreign key (RegeisterId) references users(userId),
	foreign key (typeID) references [types](typeID)
)
go

insert into filmes ([filmeTitle], [directorName], [WritersName], [StarsName], [language], [shortStory],[dateOfProduced], [country],[RegeisterId], [typeID]) values 
('The Mother','Niki Caro','Misha GreenAndrea BerloffPeter Craig','Jennifer LopezLucy PaezOmari Hardwick','English, Ukraine',
'While fleeing from dangerous assailants,an assassin comes out of hiding to protect the daughter she left earlier in life.','2023','The UK',1000,1)
go
insert into filmes([filmeTitle], [directorName], [WritersName], [StarsName], [language], [shortStory], [description], [dateOfProduced], [country], [RegeisterId], [typeID]) values 
('The Covenant','Guy Ritchie','Guy RitchieIvan AtkinsonMarn Davies','Jake GyllenhaalDar SalimSean Sagar','English',
'During the war in Afghanistan, a local interpreter risks his own life to carry an injured sergeant across miles of grueling terrain.','age 16+','2022','Spain',1000,1)
go
insert into filmes ([filmeTitle], [directorName], [WritersName], [StarsName], [language], [shortStory], [description], [dateOfProduced], [country], [RegeisterId], [typeID]) values
('The Evil Dead ','Sam Raimi','Sam Raimi','Bruce CampbellEllen SandweissRichard DeManincor','English',
'Five friends travel to a cabin in the woods, where they unknowingly release flesh-possessing demons.','age 17+','1981','The USA',1003,1)
go
insert into filmes ([filmeTitle], [directorName], [StarsName], [language], [shortStory], [dateOfProduced], [country], [RegeisterId], [typeID], [Season]) values 
('Ted Lasso','Brendan Hunt, Joe Kelly, Bill Lawrence',' Jason Sudeikis, Hannah Waddingham, Brendan Hunt','English',
'American college football coach Ted Lasso heads to London to manage AFC Richmond, a struggling English Premier League football team.','2020-','The USA',1003,2,2)
go
insert into filmes ([filmeTitle], [directorName], [WritersName], [StarsName], [language], [shortStory], [description], [dateOfProduced], [country], [RegeisterId], [typeID]) values 
('Tombstone','Quentin Tarantino ','Kevin Jarre','Kurt RussellVal KilmerSam Elliott','English',
'With the help of a German bounty-hunter, a freed slave sets out to rescue his wife from a brutal plantation owner in Mississippi.','age 14+','2012','The USA',1000,1)
go
insert into filmes([filmeTitle], [directorName], [StarsName], [language], [shortStory], [dateOfProduced], [country], [RegeisterId], [typeID], [Season]) values 
('The Great','Elle Fanning','Elle Fanning, Phoebe Fox, Gwilym Lee','English',
'A royal woman living in rural Russia during the 18th century is forced to choose between her own personal happiness and the future of Russia, when she marries an Emperor.','2021-','The UK, Australia',1003,2,1)
go
-----------------------------------------------------------------------------------------------------------------------
create table filmGenres(
	filmeId int,
	genreId int,
	foreign key (genreId) references genres(genreId),
	foreign key (filmeId) references filmes(filmeId)
)
go
insert into filmGenres values (101,1),(101,2),(102,1),(102,2),(103,3),
								(104,2),(104,4),(107,4),(107,6),(105,5),(105,1)
go
--------------------------------------------------------------------------
create table comments(
commentId int primary key not NULL identity,
userId int not NULL,
filmeId int not NULL,
commentText varchar(2000),
RegisterDate date default(getdate()),
isActive bit default(0),
parentId int NULL,
foreign key (filmeId) references filmes(filmeId),
foreign key (userId) references Users(userId),
foreign key (parentId) references comments(commentId)
)
go
--------------------------------------------------------------
select * from filmes
go
select * from genres
go
select * from Roles
go
select * from [types]
go
select * from Users