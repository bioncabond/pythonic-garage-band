class Band:
 
    instances = []

    def __init__(self, name, members=[]):
        self.name = name
        self.members = members 
        Band.instances.append(self.name) 
        
        # self.__class__.all_band.append(self)
        
    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}" 
            
    def play_solos(self): 
        solo_list = []
        for i in self.members: 
            solo_list.append(i.solo)
        return solo_list

    def add_member(self, player): 
        self.members.append(player) 
    
    @staticmethod
    def to_list(): 
        return Band.instances 
        

class Musician: 

    def __init__(self,name, members = []):
        self.name = name 
        self.members = members
                
    def get_instrument(self):
        return f'{self.instrument}'

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}" 

    def play_solo(self):
        return f'{self.solo}'


class Guitarist(Musician):
    def __init__(self,name):
        super().__init__(name)
        self.instrument = "guitar" 
        self.solo ='face melting guitar solo'


class Bassist(Musician):
    def __init__(self,name):
        super().__init__(name)
        self.instrument = "bass" 
        self.solo ='bom bom buh bom'
        


class Drummer(Musician):
    def __init__(self,name):
        super().__init__(name)
        # self.members = members 
        self.instrument = "drums" 
        self.solo ='rattle boom crash'



# pookie = Band('Pookie')
# # print(pookie)

# pookie.add_member('Pookie2') 
# # print(pookie.members)

# solos_list = pookie.play_solos()
# print(solos_list)