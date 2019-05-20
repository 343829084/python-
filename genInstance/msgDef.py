import struct


class PktTest():
    def __init__(self, content):
        self.num_trades_f = ["int32_t", "num", "数量", '100']
        self.fields = []
        self.msg=[]
        self.content=content

    def process(self):
        self.fields += self.num_trades_f,
        return self.fields

    def unpack(self):
        tmp, = struct.unpack('!i', self.content[0:])
        print("unpack %d" %tmp)
        self.msg.append(('数量', tmp))
        self.content = self.content[4:]
        return self.msg


def GetInstance(class_name, content):
    name=class_name+"("+repr(content)+")"
    return eval(name)

if __name__ == "__main__":
    buffer = struct.pack("!i", 33)
    print(repr(buffer))

    myInstance = GetInstance("PktTest", buffer)
    msg = myInstance.unpack()

    print("myinstance field %s"%msg)

    msg_content=[]
    for i in range(len(msg)):
        if isinstance(msg[i], list):
            print("list instatnce")
        else:
            msg_content +=[msg[i]]

    print(msg_content)


