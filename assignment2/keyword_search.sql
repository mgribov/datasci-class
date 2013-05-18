select * 
from (
    select 
        docid, 
        sum(count) as match 
    from Frequency 
    where 
        term='washington' 
        or term='taxes' 
        or term='treasury' 
    group by docid
) tmp 
order by tmp.match desc 
limit 10;
