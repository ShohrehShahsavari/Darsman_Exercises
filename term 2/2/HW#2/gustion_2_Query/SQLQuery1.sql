use dbMyFilimo
go

--Query 1
select [Name],Family,mobileNumber
from Users
where isActive=1
go

/***********************************************************************************************/
go
--Query 2 ( Sam Raimi INSTED اصغر فرهادی) 

select f.filmeTitle 'نام فیلم',f.dateOfProduced ' سال ساخت', G.genreTitle 'ژانر فیلم'
from filmes F inner join filmGenres FG
on F.filmeId=FG.filmeId inner join genres G
on FG.genreId=G.genreId
where directorName='Sam Raimi'
go
/***********************************************************************************************/
go
--Query 3 ( 2015 INSTED 1400) AND (Western INSTED کمدی)

select count(*) as 'تعداد فیلم های وسترن قبل از 2015'
from filmes F inner join filmGenres FG
on F.filmeId=FG.filmeId
where F.dateOfProduced<='2015'and F.typeID=1 and  FG.genreId=(select genreId from genres
																where genreTitle='Western')
go

/***********************************************************************************************/
go
--Query 4 ( contact name 'Shohreh Shahi' INSTED مهدی عباسی)

select f.filmeTitle 'نام فیلم',f.directorName 'نام کارگردان',U.[Name],u.Family as [نام فرد بیننده]
from filmes f inner join seenLikeDislike SLD
on  F.filmeId=SLD.filmeId inner join Users U
on SLD.userId=U.userId
where u.userId=(select userId from Users
				where [Name]='shohreh' and Family='shahi')
go

/***********************************************************************************************/
go
-- Query 5
select filmeTitle 'لیست نام فیلم های دیده نشده'
from filmes
where filmeId not in (select F.filmeId
						from filmes F inner join  seenLikeDislike SLD
						on F.filmeId=SLD.filmeId)
go

/***********************************************************************************************/
go
-- Query 6

select f.filmeTitle 'لیست فیلم های مشاهده شده توسط بیش از 2 کاربر'
from filmes f inner join (
		select filmeId from seenLikeDislike
		group by filmeId
		having count(filmeId)>=2) T2
on f.filmeId=T2.filmeId
go

/***********************************************************************************************/
go
-- Query 7

select f.filmeId,f.filmeTitle,T2.[تعداد مشاهده شده توسط کاربران]
from filmes F inner join (select filmeId, count(filmeId)'تعداد مشاهده شده توسط کاربران'
	from seenLikeDislike
	group by filmeId
	order by count(filmeId) desc
	offset 0 rows
	fetch next 3 rows only) T2
on f.filmeId=T2.filmeId
go

/***********************************************************************************************/
go
-- Query 8

select genreTitle 'پربیننده ترین ژانر با توجه به تعداد بازدید مدیاها' from genres
where genreId=(select fG.genreId
				from filmGenres FG inner join (select filmeId
					from seenLikeDislike
					group by filmeId
					order by count(filmeId) desc
					offset 0 rows
					fetch next 3 rows only) T2
				on FG.filmeId=T2.filmeId
				group by FG.genreId
				order by count(FG.genreId) desc
				offset 0 rows
				fetch next 1 rows only)
go

/***********************************************************************************************/
go
-- Query 9
----- List of media befor deleting
select * from filmes
go
-----------
delete from filmes
where typeID=2 and filmeId in (select f.filmeId 
								from filmes F inner join filmGenres FG
								on f.filmeId=FG.filmeId
								where FG.genreId=(select genreId from genres
												where genreTitle='Comedy'))
go
----- List of media after deleting
select * from filmes
go

/***********************************************************************************************/
go
-- Query 10

update Users set isActive=1
where isActive=0
go
