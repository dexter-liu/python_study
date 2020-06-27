#!/usr/bin/env python
# -*- coding:utf-8 -*-


import pymongo


class MongoHelper(object):
    def __init__(self, dbhost, auth_user=None, auth_password=None, database=None):
        self.auth_user = auth_user
        self.auth_password = auth_password
        self.dbhost = dbhost
        self.database = database
        if self.auth_user and self.auth_password and self.database:
            self.cli_conn = pymongo.MongoClient('mongodb://' + self.auth_user + ':' + self.auth_password
                                                + '@' + self.dbhost + '/' + self.database)
        else:
            try:
                self.cli_conn = pymongo.MongoClient('mongodb://' + self.dbhost + '/' + self.database)
            except Exception as e:
                print(e, '输入参数有错')

    def select_coll(self, coll, db='admin'):
        self.col = self.cli_conn[db][coll]

    def ins_one(self, doc={}):
        doc_id = self.col.insert_one(doc).inserted_id
        return doc_id

    def ins_many(self, docs=[]):
        docs_id = self.col.insert_many(docs)
        for doc in docs_id:
            print(doc)
        return docs_id

    def query_one(self, fil={}):
        return self.col.find_one(fil)

    def query_any(self, fil={}, lim=0):
        return self.col.find(fil).limit(lim)

    def query_sort(self, fil={}, colu, direct=1):
        return self.col.find(fil).sort(colu, direct)

    def up_one(self, fil=None, upd):
        result = self.col.update_one(fil, upd)
        return result.matched_count

    def up_many(self, fil=None, upd):
        result = self.col.update_many(fil, upd)
        return result.matched_count

    def del_one(self, fil=None):
        result = self.col.delete_one(fil)
        print(result.deleted_count)

    def del_many(self, fil=None):
        # 当fil为{}， 删除集合中的所有文档
        result = self.col.delete_many(fil)
        print(result.deleted_count)

    def del_coll(self):
        return self.col.drop()

if __name__ == '__main__':
    main()