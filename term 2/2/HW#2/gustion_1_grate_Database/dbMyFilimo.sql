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
	[password] varchar(50) not NULL Check ([password] like'%[a-z]%' and [password] like'%[A-Z]%' and [password] like'%[0-9]%' and[password] like'%[^a-zA-Z0-9]%'),
	timeRegister datetime,
	isActive bit default(1),
	Email Varchar(30),
	RoleId int,
	constraint FK_users_Roles foreign key (RoleId) references Roles(RoleId)
)
go
insert into Users([Name], [Family], [mobileNumber], [password], [timeRegister], [Email], [RoleId]) 
			values ('ali','alaie','091000','ab$c45D',getdate(),'ali@yahoo.com',1),
					('sahar','ghavi','092000','Ddf234&',getdate(),'sahar@gmail.com',2),
					('mehdi','mahdavi','031000','w12E#r',getdate(),'mehdi@hotmail.com',2),
					('arash','hasani','094000','zxB98@c',getdate(),'arash@yahoo.com',1),
					('ali','hashemi','097000','YUc65%',getdate(),'alih@yahoo.com',2)
go
insert into Users ([Name], [Family], [mobileNumber], [password], [timeRegister], [isActive], [Email], [RoleId])
	values ('shohreh','shahi','0950000','Fhgfd$86',getdate(),0,'shohre@gmail.com',1),
			('ebi','ebrahimi','0960000','hgffR%976',getdate(),0,'ebi@gmail.com',2)
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
	constraint FK_filmes_users foreign key (RegeisterId) references users(userId) on delete Cascade,
	constraint FK_filmes_types foreign key (typeID) references [types](typeID)on delete Cascade
)
go

insert into filmes ([filmeTitle], [directorName], [WritersName], [StarsName], [language], [shortStory],[dateOfProduced], [country],[RegeisterId], [typeID]) values 
('The Mother','Niki Caro','Misha Green,Andrea Berloff,Peter Craig','Jennifer Lopez,Lucy Paez,Omari Hardwick','English, Ukraine',
'While fleeing from dangerous assailants,an assassin comes out of hiding to protect the daughter she left earlier in life.','2023','The UK',1000,1)
go
insert into filmes([filmeTitle], [directorName], [WritersName], [StarsName], [language], [shortStory], [description], [dateOfProduced], [country], [RegeisterId], [typeID]) values 
('The Covenant','Guy Ritchie','Guy Ritchie,Ivan Atkinson,Marn Davies','Jake Gyllenhaal,Dar Salim,Sean Sagar','English',
'During the war in Afghanistan, a local interpreter risks his own life to carry an injured sergeant across miles of grueling terrain.','age 16+','2022','Spain',1000,1)
go
insert into filmes ([filmeTitle], [directorName], [WritersName], [StarsName], [language], [shortStory], [description], [dateOfProduced], [country], [RegeisterId], [typeID]) values
('The Evil Dead ','Sam Raimi','Sam Raimi','Bruce Campbell,Ellen Sandweiss,Richard DeManincor','English',
'Five friends travel to a cabin in the woods, where they unknowingly release flesh-possessing demons.','age 17+','1981','The USA',1003,1)
go
insert into filmes ([filmeTitle], [directorName], [StarsName], [language], [shortStory], [dateOfProduced], [country], [RegeisterId], [typeID], [Season]) values 
('Ted Lasso','Brendan Hunt, Joe Kelly, Bill Lawrence',' Jason Sudeikis, Hannah Waddingham, Brendan Hunt','English',
'American college football coach Ted Lasso heads to London to manage AFC Richmond, a struggling English Premier League football team.','2020-','The USA',1003,2,2)
go
insert into filmes ([filmeTitle], [directorName], [WritersName], [StarsName], [language], [shortStory], [description], [dateOfProduced], [country], [RegeisterId], [typeID]) values 
('Tombstone','Quentin Tarantino ','Kevin Jarre','Kurt Russell,Val Kilmer,Sam Elliott','English',
'With the help of a German bounty-hunter, a freed slave sets out to rescue his wife from a brutal plantation owner in Mississippi.','age 14+','2012','The USA',1000,1)
go
insert into filmes([filmeTitle], [directorName], [StarsName], [language], [shortStory], [dateOfProduced], [country], [RegeisterId], [typeID], [Season]) values 
('The Great','Elle Fanning','Elle Fanning, Phoebe Fox, Gwilym Lee','English',
'A royal woman living in rural Russia during the 18th century is forced to choose between her own personal happiness and the future of Russia, when she marries an Emperor.','2021-','The UK, Australia',1003,2,1)
go
insert into filmes ([filmeTitle], [directorName], [WritersName], [StarsName], [language], [shortStory], [dateOfProduced], [country], [RegeisterId], [typeID]) values
('It"s Murder!','Sam Raimi','Sam Raimi,Scott Spiegel','Scott Spiegel,Sam Raimi,Cheryl Guttridge','English',
'The film tells the story of a family whose uncle is murdered. The son gets everything because he is in the will. A detective is trying to find out who murdered the uncle while avoiding ending up dead as well.','1977','The USA',1000,1)
go
-----------------------------------------------------------------------------------------------------------------------
create table filmGenres(
	filmeId int,
	genreId int,
	constraint FK_filmeGenre_genre foreign key (genreId) references genres(genreId)on delete Cascade,
	constraint FK_filmeGenre_filme foreign key (filmeId) references filmes(filmeId)on delete Cascade
)
go
insert into filmGenres values (100,1),(100,2),(101,1),(101,2),(102,3),
								(103,2),(103,4),(104,5),(104,1),(105,4),(105,6),
								(106,2),(106,3)
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
create table RateTitle(
RateId int primary key not NULL,
rateTitle varchar(50) not NULL
)
go
insert into RateTitle values (1,'very bad'),(2,'bad'),(3,'quite good'),(4,'very good'),(5,'excellent')
go
----------------------------------------------------------------------
create table seenLikeDislike (
filmeId int not NULL,
userId int not NULL,
RateId int not NULL,
constraint FK_seenLikeDislike_filmes foreign key (filmeId) references filmes(filmeId) on delete Cascade,
constraint FK_seenLikeDislike_Users foreign key (userId) references Users(userId) on delete Cascade,
constraint FK_seenLikeDislike_RateTitle foreign key (RateId) references RateTitle(RateId) on delete Cascade
)
go
insert into seenLikeDislike ([filmeId], [userId], [RateId]) values (100,1003,5),(100,1006,2),
																	(104,1006,3),(104,1006,4),(104,1005,1),
																	(101,1001,1),
																	(103,1005,5),(103,1004,2)
go

--------------------------------------------------------------
select * from comments
go
select * from filmes
go
select * from filmGenres
go
select * from genres
go
select * from Roles
go
select * from [types]
go
select * from Users
go
select * from seenLikeDislike
go