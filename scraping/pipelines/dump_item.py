import json
import os


class DumpItem:
    def open_spider(self, spider):
        self.file = open(os.path.join('result', 'items.json'), 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(item) + "\n"
        self.file.write(line)
        return item
