# 1. SQL 语句则使用英文分号;
# 2.SQL 语句中含有字符串的时候，需要像 'abc' 这样，使用英文单引号'将字符串括起来，用来标识这是一个字符串。
# 3.SQL 不区分关键字的大小写
# 4.SQL 语句中含有日期的时候，同样需要使用英文单引号将其括起来。日期的格式有很多种（'26 Jan 2010' 或者'10/01/26' 等），本教程统一使用 '2020-01-26' 这种'年-月-日'的格式。
# 5.在 SQL 语句中书写数字的时候，不需要使用任何符号标识，直接写成 1000 这样的数字即可。

# 如需从 Company" 列中仅选取唯一不同的值，我们需要使用 SELECT DISTINCT 语句：
"SELECT DISTINCT Company FROM Orders;"

# 有条件地从表中选取数据: = > < >= <=	<> BETWEEN LIKE
# 如果只希望选取居住在城市 "Beijing" 中的人，我们需要向 SELECT 语句添加 WHERE 子句：
"SELECT * FROM Persons WHERE City='Beijing';"

# AND 和 OR 可在 WHERE 子语句中把两个或多个条件结合起来
# 可以把 AND 和 OR 结合起来（使用圆括号来组成复杂的表达式）:
"SELECT * FROM Persons WHERE (FirstName='Thomas' OR FirstName='William') AND LastName='Carter';"

# ORDER BY 语句用于根据指定的列对结果集进行排序
# 以逆字母顺序显示公司名称，并以数字顺序显示顺序号：
"SELECT Company, OrderNumber FROM Orders ORDER BY Company DESC, OrderNumber ASC;"

# INSERT INTO 语句用于向表格中插入新的行。
# INSERT INTO table_name (列1, 列2,...) VALUES (值1, 值2,....)
"INSERT INTO Persons (LastName, Address) VALUES ('Wilson', 'Champs-Elysees');"

# Update 语句用于修改表中的数据
# UPDATE 表名称 SET 列名称 = 新值 WHERE 列名称 = 某值
"UPDATE Person SET Address = 'Zhongshan 23', City = 'Nanjing' WHERE LastName = 'Wilson';"
# 可以在不删除表的情况下删除所有的行。这意味着表的结构、属性和索引都是完整的：
"DELETE FROM table_name;"

# DELETE 语句用于删除表中的行
# DELETE FROM 表名称 WHERE 列名称 = 值
"DELETE FROM Person WHERE LastName = 'Wilson';"

# 用于规定要返回的记录的数目
# SELECT column_name(s) FROM table_name LIMIT number
"SELECT * FROM Persons LIMIT 5"

# LIKE 操作符用于在 WHERE 子句中搜索列中的指定模式。
# "Persons" 表中选取居住在以 "N" 开始的城市里的人
"SELECT * FROM Persons WHERE City LIKE 'N%';"
# 从 "Persons" 表中选取居住在以 "g" 结尾的城市里的人
"SELECT * FROM Persons WHERE City LIKE '%g';"
# 从 "Persons" 表中选取居住在包含 "lon" 的城市里的人
"SELECT * FROM Persons WHERE City LIKE '%lon%';"
# 从 "Persons" 表中选取居住在不包含 "lon" 的城市里的人
"SELECT * FROM Persons WHERE City NOT LIKE '%lon%';"
# 从上面的 "Persons" 表中选取名字的第一个字符之后是 "eorge" 的人
"SELECT * FROM Persons WHERE FirstName LIKE '_eorge';"
# 从 "Persons" 表中选取的这条记录的姓氏以 "C" 开头，然后是一个任意字符，然后是 "r"，然后是任意字符，然后是 "er"：
"SELECT * FROM Persons WHERE LastName LIKE 'C_r_er';"
# "Persons" 表中选取居住的城市以 "A" 或 "L" 或 "N" 开头的人
"SELECT * FROM Persons WHERE City LIKE '[ALN]%';"
# 从上面的 "Persons" 表中选取居住的城市不以 "A" 或 "L" 或 "N" 开头的人
"SELECT * FROM Persons WHERE City LIKE '[!ALN]%';"


# IN 操作符允许我们在 WHERE 子句中规定多个值
# SELECT column_name(s) FROM table_name WHERE column_name IN (value1,value2,...)
# 选取姓氏为 Adams 和 Carter 的人
"SELECT * FROM Persons WHERE LastName IN ('Adams','Carter');"


# 操作符 BETWEEN ... AND 会选取介于两个值之间的数据范围。这些值可以是数值、文本或者日期
# SELECT column_name(s) FROM table_name WHERE column_name BETWEEN value1 AND value2
# 介于 "Adams"（包括）和 "Carter"（不包括）之间的人
"SELECT * FROM Persons WHERE LastName BETWEEN 'Adams' AND 'Carter'"
# 不介于 "Adams"（包括）和 "Carter"（不包括）之间的人
"SELECT * FROM Persons WHERE LastName NOT BETWEEN 'Adams' AND 'Carter'"

# SQL join 用于根据两个或多个表中的列之间的关系，从这些表中查询数据。
"SELECT Persons.LastName, Persons.FirstName, Orders.OrderNo FROM Persons INNER JOIN Orders ON Persons.Id_P = Orders.Id_P ORDER BY Persons.LastName"
# JOIN: 如果表中有至少一个匹配，则返回行
# LEFT JOIN: 即使右表中没有匹配，也从左表返回所有的行
# RIGHT JOIN: 即使左表中没有匹配，也从右表返回所有的行
# FULL JOIN: 只要其中一个表中存在匹配，就返回行

# 内建 SQL 函数的语法是：
# SELECT function(列) FROM 表
# Aggregate 函数的操作面向一系列的值，并返回一个单一的值。
# 注释：如果在 SELECT 语句的项目列表中的众多其它表达式中使用 SELECT 语句，则这个 SELECT 必须使用 GROUP BY 语句！
# AVG(column)	返回某列的平均值
# COUNT(column)	返回某列的行数（不包括 NULL 值）
# COUNT(*)	返回被选行数
# FIRST(column)	返回在指定的域中第一个记录的值
# LAST(column)	返回在指定的域中最后一个记录的值
# MAX(column)	返回某列的最高值
# MIN(column)	返回某列的最低值
# SUM(column)	返回某列的总和

# 找到 OrderPrice 值高于 OrderPrice 平均值的客户
"SELECT Customer FROM Orders WHERE OrderPrice>(SELECT AVG(OrderPrice) FROM Orders);"
# 计算客户 "Carter" 的订单数
"SELECT COUNT(Customer) AS CustomerNilsen FROM Orders WHERE Customer='Carter'"
# 表中的总行数
"SELECT COUNT(*) AS NumberOfOrders FROM Orders;"
# 计算 "Orders" 表中不同客户的数目
"SELECT COUNT(DISTINCT Customer) AS NumberOfCustomers FROM Orders;"
# 查找 "OrderPrice" 列的第一个值
"SELECT FIRST(OrderPrice) AS FirstOrderPrice FROM Orders;"  "==>" "LAST(),Max(),MIN()"
# SUM 函数返回数值列的总数（总额）
# 查找 "OrderPrice" 字段的总数
"SELECT SUM(OrderPrice) AS OrderTotal FROM Orders;"

# GROUP BY 语句用于结合合计函数，根据一个或多个列对结果集进行分组。  关键字“每个”
# 希望查找每个客户的总金额（总订单）
"SELECT Customer,SUM(OrderPrice) FROM Orders GROUP BY Customer;"
# 对一个以上的列应用 GROUP BY 语句，就像这样：
"SELECT Customer,OrderDate,SUM(OrderPrice) FROM Orders GROUP BY Customer,OrderDate"

# 在 SQL 中增加 HAVING 子句原因是，WHERE 关键字无法与合计函数一起使用。
# 查找订单总金额少于 2000 的客户
"SELECT Customer,SUM(OrderPrice) FROM Orders GROUP BY Customer HAVING SUM(OrderPrice)<2000"
# 查找客户 "Bush" 或 "Adams" 拥有超过 1500 的订单总金额
"SELECT Customer,SUM(OrderPrice) FROM Orders WHERE Customer='Bush' OR Customer='Adams' GROUP BY Customer HAVING SUM(OrderPrice)>1500"





















