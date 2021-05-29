import uuid
import random as rng
import subprocess
import time
my_uuid = uuid.uuid4()
commit_count = 0
while(True):
    added_lines = ''
    num_of_added_line = rng.random(1, 20)
    sleep_time = rng.randint(1000, 9000) / 1000
    for idx in range(num_of_added_line):
        added_lines += str(my_uuid) + '\n'
    with open("guid_lib.txt", "a") as f:
        f.write(added_lines)
        
    Process = subprocess.check_call(['./script/commit-push.sh', 'Added ' + str(num_of_added_line) + ' GUID'])
    print('Commit No. {0}, sleep for {1}s'.format(commit_count, str(sleep_time)))
    commit_count += 1
    time.sleep(sleep_time)
    
    