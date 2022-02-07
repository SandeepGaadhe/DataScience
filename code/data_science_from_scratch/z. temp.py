# -*- coding: utf-8 -*-

"""
Created on Tue Dec 10 14:23:07 2019

@author: admin
"""

users	=	[
                {	"id":	0,	"name":	"Person0"	},
                {	"id":	1,	"name":	"Person1"	},
                {	"id":	2,	"name":	"Person2"	},
                {	"id":	3,	"name":	"Person3"	},
                {	"id":	4,	"name":	"Person4"	},
                {	"id":	5,	"name":	"Person5"	},
                {	"id":	6,	"name":	"Person6"	},
                {	"id":	7,	"name":	"Person7"	},
                {	"id":	8,	"name":	"Person8"	},
                {	"id":	9,	"name":	"Person9"	}
            ]

myDict = {"id" : 10, "name" : "Person10"}
users.append(myDict)

myfoafCount = {"id" : 100, "Count" : "200"}

for	user in	users:
    user["foafCount"]	= myfoafCount


print(users)