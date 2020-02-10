-- 建表
create external table person(
name string,
idcard string)
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY '\t'
STORED as TEXTFILE;


-- 检测身份证合法性
select idcard,
case when length(idcard) = 18 then
	case when substring(idcard,-2,1) % 2 = 1 then '男' 
	case when substring(idcard,-2,1) % 2 = 0 then '女' 
    else 'unknown' end 
case when length(idcard) = 15 then 
	case when substring(idcard,-1,1) % 2 = 1 then '男'
	case when substring(idcard,-1,1) % 2 = 0 then '女'
	else 'unknown' end
else '不合法' end 
from person;

