# coding: utf-8

import uuid

import db_connect

# uuid_str = str(uuid.uuid1())

for i in range(1, 6):
    db_connect.UpdateInfo.objects.create(
        uuid='aaa-bbb-ccc-ddd-100{0}'.format(str(i)),
        sn='0000000{0}'.format(str(i)),
        idc='北京',
        private_ip='192.168.199.{0}'.format(str(i)),
    )
