# Write your MySQL query statement below
select DISTINCt author_id as id
from Views 
where author_id = viewer_id order by author_id;
