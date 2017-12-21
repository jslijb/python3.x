# -*- coding: utf-8 -*-
CORE_list = []
import string
mbm_log = open('e:\\core','rb')
content = mbm_log.read()
mbm_log.close()
for line in mbm_log:
    if line.startswith('[CORE]',0,6):
        # print(line)
        CORE_list.append(line)
    if line.startswith('[MBM]', 0, 6):
        if line.startswith(''):
            continue
mbm_log.close()
core_log = open('e:\\log_core','wb+')
core_log.writelines(CORE_list)
core_log.close()


# print(CORE_list)


