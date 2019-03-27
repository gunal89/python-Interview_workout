class clsstatic():
        var1 = 'PARAMAGURU'
        var2 = 'JAVA'

        def set_ins(self):
            self.var1 = "MUTHU"
        def print_ins(self):
            print "varl : ",self.var1

        @classmethod
        def set_cls(cls):
            cls.var2 = 'PYTHON'
        @classmethod
        def print_cls(cls):
            print "Var2 :", cls.var2

        @staticmethod
        def stst_mtd(buildver):
            if buildver == '3.7.0.22':
                print "Current build version {}".format(buildver)
            else :
                print "{} is not Current build version".format(buildver)

print "\n ### Instance Method ###\n"
obj_c = clsstatic()
print "1st check (ins_mtd) obj_c ::", obj_c.var1
obj_c.print_ins()
obj_set = clsstatic()
obj_set.set_ins()
print "Recheck (ins_mtd) obj_c ::", obj_c.var1

print "\n ### Class metod ###\n"

obj_x = clsstatic()
print "1st check(cls method) the obj_x ::",obj_x.var2
obj_y=clsstatic()
obj_y.set_cls()
print obj_y.var2
print "Recheck (cls method) the obj_x ::",obj_x.var2

print " \n### Static Method ### \n"
obj_s = clsstatic()
obj_s.stst_mtd('3.7.0.21')



