-- 1. get 2 columns for term counts for same terms for each article
-- 2. multiply columns within each row and take sum of the result
select 
    sum(src.count * dst.count) as mul 
from 
    Frequency src, 
    Frequency dst 
where 
    src.term=dst.term 
    and src.docid='10080_txt_crude' 
    and dst.docid='17035_txt_earn';
