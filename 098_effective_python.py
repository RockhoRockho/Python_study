import time
from datetime import timedelta

num = 8000000

start_time = time.time()
data = ""
for i in range(num):
    data = data + 'a'
end_time = time.time()
elapsed_time = end_time - start_time # 경과시간
print('str(+) x %d 경과시간 %s' % (num, timedelta(seconds=elapsed_time)))


start_time = time.time()
data = []
for i in range(num):
    data.append("a")
data = ''.join(data)
end_time = time.time()
elapsed_time = end_time - start_time # 경과시간
print('append(+) x %d 경과시간 %s' % (num, timedelta(seconds=elapsed_time)))

# str(+) x 10 경과시간 0:00:00
# str(+) x 10 경과시간 0:00:00

# str(+) x 1000000 경과시간 0:00:00.181523
# append(+) x 1000000 경과시간 0:00:00.110704

# str(+) x 4000000 경과시간 0:00:01.387290
# append(+) x 4000000 경과시간 0:00:00.475569

# str(+) x 8000000 경과시간 0:00:04.188704
# append(+) x 8000000 경과시간 0:00:00.890645