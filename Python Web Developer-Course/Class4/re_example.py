import re


re_obj = re.compile(r"(QingWen|JunJie).*?(large|small)")
some_string = "QingWen is very large in size,but JunJie is small"
print re_obj.findall(some_string)