go
use Movies_dwh
go


select
	(select count(*) from Countries) as Count_Countries,
	(select count(*) from DateDimension) as Count_DateDimension,
	(select count(*) from Movie) as Count_Movie,
	(select count(*) from MovieDetails) as Count_MovieDetails,
	(select count(*) from MoviePeople) as Count_MoviePeople,
	(select count(*) from People) as Count_People


select sum(NumberOfActors), sum(NumberOfCrewMembers) from Movie



select *
from MovieDetails

select * 
from People
where PersonID in (4091, 2151819);


select *
from Movie;

select *
from MoviePeople
where PersonID in (4091, 2151819);


select c.SubRegion, avg(m.IMDBRating) as IMDBRating, avg(m.TMDBRating) as TMDBRating, avg(m.MovieLensRating) as MovieLensRating
from Movie m
inner join Countries c on m.CountryID=c.CountryID
group by c.SubRegion

select *
from Movie


select *
from MovieDetails

--update People 
--set ValidTo = ?,
--      Status='Hist' 
--where PersonID = ? and Status = 'Curr'

--update Movie 
--set IMDBRating = ?,
--	Revenue = ?,
--	Budget = ?
--where MovieID = ?