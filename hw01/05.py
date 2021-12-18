import subprocess
args = ['ping', 'yandex.ru']
args2 = ['ping', 'youtube.com']


def test_ping(args):

    subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)

    for line in subproc_ping.stdout:
                line = line.decode('cp866').encode('utf-8')
                # line = line.decode('utf-8').encode('utf-8')
                print(line.decode('utf-8'))


test_ping(args);
test_ping(args2);
