def gen_get_set(params):

    for i in range(len(params)):
        
        cur = params[i]
        
        print('@property')
        print('def %s(self):' % cur)
        print('    return self._%s' % cur)
        print()
        print('@%s.setter' % cur)
        print('def %s(self, %s):' % (cur, cur))
        print('    self._%s = %s' % (cur, cur))
        print()
        print()

            
    
        

gen_get_set(['mp'])