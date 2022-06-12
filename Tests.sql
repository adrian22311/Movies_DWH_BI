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
where PersonID in (4091, 2160);


select *
from Movie;

select *
from MoviePeople
where PersonID in (4091, 2160);

