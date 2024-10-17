CREATE PROCEDURE UnpivotProducts()
BEGIN
	set group_concat_max_len = 1000000;
	set @sql = null;
	with stores as (SELECT COLUMN_NAME store from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME='products' and COLUMN_NAME<>'product_id')
	select group_concat(concat('select product_id, "', store, '" ', 'as store, ', store, ' ','as price from products where ', store, ' is not null union') order by store separator ' ') 
	into @sql
	from stores;

	set @sql = SUBSTRING(@sql, 1, LENGTH(@sql)-6);
	prepare stmt from @sql;
	execute stmt;
END