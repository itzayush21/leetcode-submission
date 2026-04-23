SELECT
    person_name
from QUEUE
where turn=
    (
            SELECT max(turn)
            from
                (
                    SELECT
                        person_id,turn,
                        SUM(weight) OVER(order BY turn) as cum_sum
                    from QUEUE   
                ) t
            Where cum_sum<=1000        
    );