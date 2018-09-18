import unittest
from firewall import FireWall


class TestFirewall(unittest.TestCase):
    fw = FireWall()

    def test_wrong_ip(self):
        t1 = self.__class__.fw.accept_packet('inbound','tcp',80,"192.168.1.1")
        t2 = self.__class__.fw.accept_packet('inbound','udp',53,"192.168.1.0")
        t3 = self.__class__.fw.accept_packet('outbound','tcp',10000,"192.168.10.10")
        t4 = self.__class__.fw.accept_packet('outbound','udp',1000,"52.12.48.91")

        t5 = self.__class__.fw.accept_packet('inbound','tcp',80,"192.168.1.3")
        t6 = self.__class__.fw.accept_packet('inbound','udp',53,"192.168.2.6")
        t7 = self.__class__.fw.accept_packet('outbound','tcp',10000,"192.168.10.12")
        t8 = self.__class__.fw.accept_packet('outbound','udp',1000,"52.12.48.93")

        self.assertFalse(t1)
        self.assertFalse(t2)
        self.assertFalse(t3)
        self.assertFalse(t4)
        self.assertFalse(t5)
        self.assertFalse(t6)
        self.assertFalse(t7)
        self.assertFalse(t8)

    def test_wrong_range(self):
        t1 = self.__class__.fw.accept_packet('inbound','tcp',79,"192.168.1.2")
        t2 = self.__class__.fw.accept_packet('inbound','udp',52,"192.168.1.1")
        t3 = self.__class__.fw.accept_packet('outbound','tcp',9999,"192.168.10.11")
        t4 = self.__class__.fw.accept_packet('outbound','udp',999,"52.12.48.92")

        t5 = self.__class__.fw.accept_packet('inbound','tcp',81,"192.168.1.2")
        t6 = self.__class__.fw.accept_packet('inbound','udp',54,"192.168.1.1")
        t7 = self.__class__.fw.accept_packet('outbound','tcp',20001,"192.168.10.11")
        t8 = self.__class__.fw.accept_packet('outbound','udp',2001,"52.12.48.92")


        self.assertFalse(t1)
        self.assertFalse(t2)
        self.assertFalse(t3)
        self.assertFalse(t4)
        self.assertFalse(t5)
        self.assertFalse(t6)
        self.assertFalse(t7)
        self.assertFalse(t8)

    def test_opposite_protocol(self):
        t1 = self.__class__.fw.accept_packet('inbound','udp',80,"192.168.1.2")
        t2 = self.__class__.fw.accept_packet('inbound','tcp',53,"192.168.1.1")
        t3 = self.__class__.fw.accept_packet('outbound','udp',10000,"192.168.10.11")
        t4 = self.__class__.fw.accept_packet('outbound','tcp',1000,"52.12.48.92")

        self.assertFalse(t1)
        self.assertFalse(t2)
        self.assertFalse(t3)
        self.assertFalse(t4)

    def test_opposite_dir(self):

        t1 = self.__class__.fw.accept_packet('outbound','tcp',80,"192.168.1.2")
        t2 = self.__class__.fw.accept_packet('outbound','udp',53,"192.168.1.1")
        t3 = self.__class__.fw.accept_packet('inbound','tcp',10000,"192.168.10.11")
        t4 = self.__class__.fw.accept_packet('inbound','udp',1000,"52.12.48.92")

        self.assertFalse(t1)
        self.assertFalse(t2)
        self.assertFalse(t3)
        self.assertFalse(t4)




if __name__ == '__main__':
    unittest.main()
