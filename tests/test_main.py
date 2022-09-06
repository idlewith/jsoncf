import sys
from unittest.mock import patch

from jsoncf.main import prettify

text_origin1 = (
    '{"employees":[  {"name":"Shyam", "email":"shyamjaiswal@gmail.com"},  '
    ' {"name":"Bob", "email":"bob32@gmail.com"},  {"name":"Jai", "email":"jai87@gmail.com"}  ]} '
)
expected1 = """{
 "employees": [
  {
   "name": "Shyam",
   "email": "shyamjaiswal@gmail.com"
  },
  {
   "name": "Bob",
   "email": "bob32@gmail.com"
  },
  {
   "name": "Jai",
   "email": "jai87@gmail.com"
  }
 ]
}"""

text_origin2 = '{ "code": "1", "day": "04/ 28", "result": [{ "date": "1442年04月28日", "title": "英国国王爱德华四世出生" }, { "date": "1813年04月28日", "title": "俄国名将库图佐夫逝世" }, { "date": "1897年04月28日", "title": "中国军事家叶剑英出生" }, { "date": "1900年04月28日", "title": "荷兰天文学家简·亨德里克·奥尔特出生" }, { "date": "1903年04月28日", "title": "美国物理学家吉布斯逝世" }, { "date": "1906年04月28日", "title": "奥地利数学家库尔特·哥德尔出生" }, { "date": "1908年04月28日", "title": "德国商人奥斯卡·辛德勒出生" }, { "date": "1910年04月28日", "title": "南北战争的将领爱德华·波特·亚历山大逝世" }, { "date": "1920年04月28日", "title": "阿塞拜疆加入苏联" }, { "date": "1927年04月28日", "title": "中国革命家李大钊逝世" }, { "date": "1952年04月28日", "title": "《旧金山对日和平条约》正式生效" }, { "date": "1969年04月28日", "title": "戴高乐辞去法国总统职务" }, { "date": "1984年04月28日", "title": "邓小平会见罗纳德·威尔逊·里根" }, { "date": "1985年04月28日", "title": "中国作家张天翼逝世" }, { "date": "2001年04月28日", "title": "世界首位太空游客丹尼斯·蒂托前往太空站" } ] }'
expected2 = """{
 "code": "1",
 "day": "04/ 28",
 "result": [
  {
   "date": "1442年04月28日",
   "title": "英国国王爱德华四世出生"
  },
  {
   "date": "1813年04月28日",
   "title": "俄国名将库图佐夫逝世"
  },
  {
   "date": "1897年04月28日",
   "title": "中国军事家叶剑英出生"
  },
  {
   "date": "1900年04月28日",
   "title": "荷兰天文学家简·亨德里克·奥尔特出生"
  },
  {
   "date": "1903年04月28日",
   "title": "美国物理学家吉布斯逝世"
  },
  {
   "date": "1906年04月28日",
   "title": "奥地利数学家库尔特·哥德尔出生"
  },
  {
   "date": "1908年04月28日",
   "title": "德国商人奥斯卡·辛德勒出生"
  },
  {
   "date": "1910年04月28日",
   "title": "南北战争的将领爱德华·波特·亚历山大逝世"
  },
  {
   "date": "1920年04月28日",
   "title": "阿塞拜疆加入苏联"
  },
  {
   "date": "1927年04月28日",
   "title": "中国革命家李大钊逝世"
  },
  {
   "date": "1952年04月28日",
   "title": "《旧金山对日和平条约》正式生效"
  },
  {
   "date": "1969年04月28日",
   "title": "戴高乐辞去法国总统职务"
  },
  {
   "date": "1984年04月28日",
   "title": "邓小平会见罗纳德·威尔逊·里根"
  },
  {
   "date": "1985年04月28日",
   "title": "中国作家张天翼逝世"
  },
  {
   "date": "2001年04月28日",
   "title": "世界首位太空游客丹尼斯·蒂托前往太空站"
  }
 ]
}"""

text_origin3 = '{ "glossary": { "title": "example glossary", "GlossDiv": { "title": "S", "GlossList": { "GlossEntry": { "ID": "SGML", "SortAs": "SGML", "GlossTerm": "Standard Generalized Markup Language", "Acronym": "SGML", "Abbrev": "ISO 8879:1986", "GlossDef": { "para": "A meta-markup language, used to create markup languages such as DocBook.", "GlossSeeAlso": ["GML", "XML"] }, "GlossSee": "markup" } } } } }'
expected3 = """{
 "glossary": {
  "title": "example glossary",
  "GlossDiv": {
   "title": "S",
   "GlossList": {
    "GlossEntry": {
     "ID": "SGML",
     "SortAs": "SGML",
     "GlossTerm": "Standard Generalized Markup Language",
     "Acronym": "SGML",
     "Abbrev": "ISO 8879:1986",
     "GlossDef": {
      "para": "A meta-markup language, used to create markup languages such as DocBook.",
      "GlossSeeAlso": [
       "GML",
       "XML"
      ]
     },
     "GlossSee": "markup"
    }
   }
  }
 }
}"""

text_origin4 = '{"abc": false}'
expected4 = """{
 "abc": false
}"""

text_origin5 = '{"abc": null}'
expected5 = """{
 "abc": null
}"""

test_suite = [
    [text_origin1, expected1],
    [text_origin2, expected2],
    [text_origin3, expected3],
    [text_origin4, expected4],
    [text_origin5, expected5],
]


def test_argv():
    for text_origin, expected in test_suite:
        test_args = ["-", text_origin]
        with patch.object(sys, "argv", test_args):
            actual = prettify()
            assert actual == expected
