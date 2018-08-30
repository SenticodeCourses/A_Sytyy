import os
import time
import hashlib

class FolderMonitor:
    state_dir = [] #dir, hash
    def __init__(self, path):
        self.path = path
        self.listdir = []
        self.list_hash = []

    def _check_listdir(self):
        self.listdir = os.listdir(self.path)

    def check_state(self):
        self.listdir = os.listdir(self.path)
        now_state = []
        for name in self.listdir:
            now_state.append((name, self._calc_hash(name)))
        # print(now_state)
        if not self.state_dir:
            self.state_dir = now_state
        state_1 = set(self.state_dir)
        state_2 = set(now_state)
        if state_1.difference(state_2):
            print(state_1.difference(state_2))
            self.state_dir = now_state
        elif state_2.difference(state_1):
            print(state_2.difference(state_1))
            self.state_dir = now_state

    def _calc_hash(self,name):
        md5 = hashlib.md5()
        f = open(r'{}\{}'.format(self.path, name), 'br')
        md5.update(f.read())
        return md5.hexdigest()


if __name__ == '__main__':
    f = FolderMonitor(r'F:\ntcn')
    while True:
        f.check_state()
        # print(f.state_dir)
        time.sleep(4)

