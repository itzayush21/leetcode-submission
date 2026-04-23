Select user_id,Count(*) as followers_count
from followers
group by user_id
order by user_id;