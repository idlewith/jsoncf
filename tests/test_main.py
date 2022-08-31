import sys
from unittest.mock import patch

from jsoncf.main import prettify

text_origin = (
    '{"employees":[  {"name":"Shyam", "email":"shyamjaiswal@gmail.com"},  '
    ' {"name":"Bob", "email":"bob32@gmail.com"},  {"name":"Jai", "email":"jai87@gmail.com"}  ]} '
)

expected = """{
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


def test_argv():
    test_args = ["-", text_origin]
    with patch.object(sys, "argv", test_args):
        actual = prettify()
        assert actual == expected
