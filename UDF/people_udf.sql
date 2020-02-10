
-- transform 语法：
-- SELECT TRANSFORM (<columns>)
-- USING 'python <python_script>'
-- AS (<columns>)
-- FROM <table>;

-- 将udf函数文件上传文件到服务器指定目录
add file /Users/tinghai/Learning/Python/source/UDF/person.py

select transform(name,idcard) 
USING 'python person.py' 
AS (name,idcard,gender) 
from person;

