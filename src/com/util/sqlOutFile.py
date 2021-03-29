#!/usr/bin/env/python
# -*- coding:utf-8 -*-
# Author:guoyuhang
from com.config.config import Config


class SqlOutFile(object):
    
    def __init__(self):
        self.config = Config.get_instance()

    def writeSqlFileToPath(self,sqlList,fileName):
        # 打开一个文件
        sqlFile = open(self.config.sqlFilePath+"/"+fileName+".sql", "w+")
        print("Write Sql to %s" %self.config.sqlFilePath+"/"+fileName+".sql")
        for sql in sqlList:
            sqlFile.write(sql+"\n")
        # 关闭打开的文件
        sqlFile.close()
        print("Write Sql Done. Path is %s" % self.config.sqlFilePath+"/"+fileName+".sql")
