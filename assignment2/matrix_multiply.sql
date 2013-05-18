-- 5x5 sparse matrix
CREATE TABLE a (
    row_num int,
    col_num int,
    value int,
    primary key (row_num, col_num)
);

CREATE TABLE b (
    row_num int,
    col_num int,
    value int,
    primary key (row_num, col_num)
);

-- example: select * from A;
row     |   col     |   val
----------------------------
0       |   3       |   55
0       |   4       |   78
1       |   0       |   19
1       |   2       |   21
1       |   3       |   3
1       |   4       |   81
2       |   1       |   48
2       |   2       |   50
2       |   3       |   1
3       |   2       |   33
3       |   4       |   67
4       |   0       |   95
4       |   4       |   31



select * from (
    select 
        A.row_num a_row, 
        B.col_num b_col, 
        sum(A.value * B.value) as mul 
    from A, B 
    where 
        A.col_num=B.row_num 
    group by A.row_num, B.col_num
) tmp 
group by a_row;

-- return
a_row   |   b_row   |   mull
-----------------------------
0       |   4       |   234
1       |   4       |   1041
2       |   3       |   2874
3       |   4       |   201
4       |   4       |   4083

-- cell(a_row=2, b_row=3) is the answer == 2874
