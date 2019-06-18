#!/usr/bin/env bash
log_file="/home/mysql/mysql_bak/mysql_bak.log"
DATE=`date "+%Y-%m-%d %H:%M:%S"`

# 检测日志文件
if [ -e $log_file ];then
    echo "$DATE 脚本开始执行..." >> $log_file
else
    touch $log_file
    echo "$DATE 脚本开始执行..." >> $log_file
fi

# 运行脚本时是否传入参数
if [ $# == 2 ];then
    db_name=$1
    table_name=$2
    echo "开始备份"
    echo "数据库名为：${db_name} 表名为：${table_name}"
     `mysqldump -h 127.0.0.1 -uroot -p123456 ${db_name} ${table_name} > /home/mysql/mysql_bak/${db_name}_${table_name}.sql`
     echo "$DATE 备份完成，数据库名为${db_name} 表名为${table_name} 文件名为${db_name}_${table_name}.sql" >> $log_file
else
    read -t 86400 -p "请输入要备份的数据库名": db_name
    read -t 86400 -p "请输入要备份的表名": table_name
    `mysqldump -h 127.0.0.1 -uroot -p123456 ${db_name} ${table_name} > /home/mysql/mysql_bak/${db_name}_${table_name}.sql`
     echo "$DATE 备份完成，数据库名为${db_name} 表名为${table_name} 文件名为${db_name}_${table_name}.sql" >> $log_file
fi
if test -e /home/mysql/mysql_bak/${db_name}_${table_name}.sql
then
    echo "备份完成，文件名为${db_name}_${table_name}.sql"
fi

echo "是否恢复表(y/n)"
while :
do
    read result
    case $result in
        "y") `mysql -h 127.0.0.1 -uroot -p123456 ${db_name} < ${db_name}_${table_name}.sql`
        echo "$DATE 恢复完成，数据库名为${db_name} 表名为${table_name} 文件名为${db_name}_${table_name}.sql" >> $log_file
        break
        ;;
        "n") echo "退出"
        break
        ;;
        *) echo "输入错误，请重新输入"
        ;;
    esac
done
