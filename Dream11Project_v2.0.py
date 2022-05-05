from itertools import combinations
class Dream11:
# Defining all variables to be used further in below program
    List1 = []
    List3 =[]
    List4 = [] 
    List5 = []
    List6 = []
    a = []
    c1=0
    c2=0
    D_Names_Teams = {}
    D_Names_Credits = {}
    #counter_PBKS = 0
    #counter_GT = 0
    BatsmanList = []
    BowlerList = []
    KeeperList = []
    AllrounderList = []
    comb1 = []
    emptylist = []
    All_Combinations_Of_Players_with_3_min_Batsman = []
    All_Combinations_Of_Players_with_3_min_Batsman = []
    All_Combinations_Of_Players_with_3_min_Batsman = []
    All_Combinations_Of_Players_with_3_min_Batsman = []
    All_Combinations_Of_Players_with_3_min_Bowler = []
    All_Combinations_Of_Players_with_4_min_Bowler = []
    All_Combinations_Of_Players_with_5_min_Bowler = []
    All_Combinations_Of_Players_with_6_min_Bowler = []
    All_Combinations_Of_Players_with_1_min_Keeper = []
    All_Combinations_Of_Players_with_2_min_Keeper = []
    All_Combinations_Of_Players_with_3_min_Keeper = []
    All_Combinations_Of_Players_with_4_min_Keeper = []
    All_Combinations_Of_Players_with_1_min_AllRounder = []
    All_Combinations_Of_Players_with_2_min_AllRounder = []
    All_Combinations_Of_Players_with_3_min_AllRounder = []
    All_Combinations_Of_Players_with_4_min_AllRounder = []
    Seq1_B3B3 = [] 
    Seq1_K1A4 = [] 
    Seq1_B3B3K1A4 = []  
    Seq1_B3B3K1A4_TEAMSIZE = []
    FinalListOfTeams = []
    FinalTeamList = []
    ObjNames = []
    Objteam = []
    Objspecialty = []
    Objcredits = []
    listf = []
    listg = []

    def __init__(self,name,team,specialty,credit):
        self.Name=name
        self.team=team
        self.specialty=specialty
        self.credit=credit
        
    def CollectInfo(self):
        Dream11.ObjNames.append(self.Name)
        Dream11.Objteam.append(self.team)
        Dream11.Objspecialty.append(self.specialty)
        Dream11.Objcredits.append(self.credit)
        return Dream11.ObjNames
        return Dream11.Objteam
        return Dream11.Objspecialty
        return Dream11.Objcredits
            
    def Segregate(self):
        #print (self.Name)
        for self.name in range(30):
            if self.specialty == 'Batsman':
                Dream11.BatsmanList.append(self.Name)
                break
            elif self.specialty == 'Bowler':
                Dream11.BowlerList.append(self.Name)
                break
            elif self.specialty == 'Keeper':
                Dream11.KeeperList.append(self.Name)
                break
            else:
                Dream11.AllrounderList.append(self.Name)
                break
        return (Dream11.BatsmanList)
        return (Dream11.BowlerList)
        return (Dream11.KeeperList)
        return (Dream11.AllrounderList)
    
    @staticmethod
    def CombinationsOfPlayers():
        print('Total Number Of Batsman is : ', len(Dream11.BatsmanList))
        print('Total Number Of Bowler is : ', len(Dream11.BowlerList))
        print('Total Number Of Keeper is : ', len(Dream11.KeeperList))
        print('Total Number Of All Rounder is :', len(Dream11.AllrounderList))

        #print (Dream11.ObjNames)
        #print (Dream11.Objteam)
        #print (Dream11.Objspecialty)
        #print (Dream11.Objcredits)

        #print ('-------------------------------')
        D1 = zip(Dream11.ObjNames,Dream11.Objteam)
        Dream11.D_Names_Teams = dict(D1)
        #print (dict(D1))
        #print ('-------------------------------')
        D2= zip(Dream11.ObjNames,Dream11.Objcredits)
        Dream11.D_Names_Credits = dict(D2)
        #print (dict(D2))


        Dream11.All_Combinations_Of_Players_with_3_min_Batsman = list(combinations(Dream11.BatsmanList, 3))
        Dream11.All_Combinations_Of_Players_with_4_min_Batsman = list(combinations(Dream11.BatsmanList, 4))
        Dream11.All_Combinations_Of_Players_with_5_min_Batsman = list(combinations(Dream11.BatsmanList, 5))
        Dream11.All_Combinations_Of_Players_with_6_min_Batsman = list(combinations(Dream11.BatsmanList, 6))

        #print (Dream11.All_Combinations_Of_Players_with_3_min_Batsman)

        Dream11.All_Combinations_Of_Players_with_3_min_Bowler = list(combinations(Dream11.BowlerList, 3))
        Dream11.All_Combinations_Of_Players_with_4_min_Bowler = list(combinations(Dream11.BowlerList, 4))
        Dream11.All_Combinations_Of_Players_with_5_min_Bowler = list(combinations(Dream11.BowlerList, 5))
        Dream11.All_Combinations_Of_Players_with_6_min_Bowler = list(combinations(Dream11.BowlerList, 6))
        
        #print (Dream11.All_Combinations_Of_Players_with_3_min_Bowler)

        Dream11.All_Combinations_Of_Players_with_1_min_Keeper = list(combinations(Dream11.KeeperList, 1))
        Dream11.All_Combinations_Of_Players_with_2_min_Keeper = list(combinations(Dream11.KeeperList, 2))
        Dream11.All_Combinations_Of_Players_with_3_min_Keeper = list(combinations(Dream11.KeeperList, 3))
        Dream11.All_Combinations_Of_Players_with_4_min_Keeper = list(combinations(Dream11.KeeperList, 4))
        
        #print (Dream11.All_Combinations_Of_Players_with_1_min_Keeper)
        
        Dream11.All_Combinations_Of_Players_with_1_min_AllRounder = list(combinations(Dream11.AllrounderList, 1))
        Dream11.All_Combinations_Of_Players_with_2_min_AllRounder = list(combinations(Dream11.AllrounderList, 2))
        Dream11.All_Combinations_Of_Players_with_3_min_AllRounder = list(combinations(Dream11.AllrounderList, 3))
        Dream11.All_Combinations_Of_Players_with_4_min_AllRounder = list(combinations(Dream11.AllrounderList, 4))
    
        #print (Dream11.All_Combinations_Of_Players_with_4_min_AllRounder)

        return Dream11.All_Combinations_Of_Players_with_3_min_Batsman
        return Dream11.All_Combinations_Of_Players_with_4_min_Batsman
        return Dream11.All_Combinations_Of_Players_with_5_min_Batsman
        return Dream11.All_Combinations_Of_Players_with_6_min_Batsman
        
        return Dream11.All_Combinations_Of_Players_with_3_min_Bowler
        return Dream11.All_Combinations_Of_Players_with_4_min_Bowler
        return Dream11.All_Combinations_Of_Players_with_5_min_Bowler
        return Dream1.All_Combinations_Of_Players_with_6_min_Bowler
    
        return Dream11.All_Combinations_Of_Players_with_1_min_Keeper
        return Dream11.All_Combinations_Of_Players_with_2_min_Keeper
        return Dream11.All_Combinations_Of_Players_with_3_min_Keeper
        return Dream11.All_Combinations_Of_Players_with_4_min_Keeper
    
        return Dream11.All_Combinations_Of_Players_with_1_min_AllRounder
        return Dream11.All_Combinations_Of_Players_with_2_min_AllRounder
        return Dream11.All_Combinations_Of_Players_with_3_min_AllRounder
        return Dream11.All_Combinations_Of_Players_with_4_min_AllRounder
    
    @staticmethod
    def CombinationsOfTeam_Batsman_Bowler(List1, List2):
        result1= []
        
        for sc1 in range(0, len(List1)):
            for sc2 in range(0, len(List2)):
                result1= list(List1[sc1]+List2[sc2])
                Dream11.List3.append(list(result1)) 
        return Dream11.List3
        
    @staticmethod
    def CombinationsOfTeam_Keeper_Allrounder(List1, List2):
        result1= []
        
        for sc1 in range(0, len(List1)):
            for sc2 in range(0, len(List2)):
                result1= list(List1[sc1]+List2[sc2])
                Dream11.List4.append(list(result1)) 
        return Dream11.List4
        
    @staticmethod
    def CombinationsOfTeamForDiffSequence(List1, List2):
        result1= []
        
        for sc1 in range(0, len(List1)):
            for sc2 in range(0, len(List2)):
                result1= list(List1[sc1]+List2[sc2])
                Dream11.List5.append(list(result1))
        return Dream11.List5

    @classmethod
    def SegregateMain(cls):
        P1.Segregate()
        P2.Segregate()
        P3.Segregate()
        P4.Segregate()
        P5.Segregate()
        P6.Segregate()
        P7.Segregate()
        P8.Segregate()
        P9.Segregate()
        P10.Segregate()
        P11.Segregate()
        P12.Segregate()
        P13.Segregate()
        P14.Segregate()
        P15.Segregate()
        P16.Segregate()
        P17.Segregate()
        P18.Segregate()
        #P19.Segregate()
        #P20.Segregate()
        #P21.Segregate()
        #P22.Segregate()
        
        print('Batsman''s', cls.BatsmanList)
        print('\n')
        print ('Bowlers',cls.BowlerList)
        print('\n')
        print ('WicktKeepers',cls.KeeperList)
        print('\n')
        print ('Allrounders',cls.AllrounderList)
        print('\n')

    class Dream11Team1_B3B3K1A4():
        def method1():
            Dream11.CombinationsOfTeam_Batsman_Bowler(Dream11.All_Combinations_Of_Players_with_3_min_Batsman, Dream11.All_Combinations_Of_Players_with_3_min_Bowler)
            Dream11.Seq1_B3B3 = Dream11.List3
            Dream11.CombinationsOfTeam_Keeper_Allrounder(Dream11.All_Combinations_Of_Players_with_1_min_Keeper, Dream11.All_Combinations_Of_Players_with_4_min_AllRounder)
            Dream11.Seq1_K1A4 = Dream11.List4
            Dream11.CombinationsOfTeamForDiffSequence(Dream11.List3, Dream11.List4)
            Dream11.Seq1_B3B3K1A4 = Dream11.List5
            Dream11.FinalListOfTeams = Dream11.Seq1_B3B3K1A4
            #print (Dream11.Seq1_B3B3)        print (Dream11.Seq1_K1A4)        print (Dream11.Seq1_B3B3K1A4)        
            #print (Dream11.FinalListOfTeams)
            #print ('-------------------------------------METHOD 1------------------------------------------')
            #for a in range(len(Dream11.FinalListOfTeams)):
            #    print(len(Dream11.FinalListOfTeams[a]))
            
    class Dream11Team2_B3B4K1A3():
        def method1():
            Dream11.CombinationsOfTeam_Batsman_Bowler(Dream11.All_Combinations_Of_Players_with_3_min_Batsman, Dream11.All_Combinations_Of_Players_with_4_min_Bowler)
            Dream11.Seq2_B3B4 = Dream11.List3
            Dream11.CombinationsOfTeam_Keeper_Allrounder(Dream11.All_Combinations_Of_Players_with_1_min_Keeper, Dream11.All_Combinations_Of_Players_with_3_min_AllRounder)
            Dream11.Seq2_K1A3 = Dream11.List4
            Dream11.CombinationsOfTeamForDiffSequence(Dream11.Seq2_B3B4, Dream11.Seq2_K1A3)
            Dream11.Seq2_B3B4K1A3 = Dream11.List5
            Dream11.FinalListOfTeams = Dream11.FinalListOfTeams + Dream11.Seq2_B3B4K1A3
            #print ('-------------------------------------METHOD 2------------------------------------------')
            #print (Dream11.Seq2_B3B4)
            #print (Dream11.Seq2_K1A3)
            #print (Dream11.Seq2_B3B4K1A3)
            #print (Dream11.FinalListOfTeams)
            #for a in range(len(Dream11.FinalListOfTeams)):
            #    print(len(Dream11.FinalListOfTeams[a]))
    class Dream11Team3_B3B5K1A2():
        def method1():
            Dream11.CombinationsOfTeam_Batsman_Bowler(Dream11.All_Combinations_Of_Players_with_3_min_Batsman, Dream11.All_Combinations_Of_Players_with_5_min_Bowler)
            Dream11.Seq3_B3B5 = Dream11.List3
            Dream11.CombinationsOfTeam_Keeper_Allrounder(Dream11.All_Combinations_Of_Players_with_1_min_Keeper, Dream11.All_Combinations_Of_Players_with_2_min_AllRounder)
            Dream11.Seq3_K1A2 = Dream11.List4
            Dream11.CombinationsOfTeamForDiffSequence(Dream11.Seq3_B3B5, Dream11.Seq3_K1A2)
            Dream11.Seq3_B3B5K1A2 = Dream11.List5
            Dream11.FinalListOfTeams = Dream11.FinalListOfTeams + Dream11.Seq3_B3B5K1A2
            '''
            print (Dream11.Seq2_B3B5)        print (Dream11.Seq2_K1A2)        print (Dream11.Seq3_B3B5K1A2)        print (Dream11.FinalListOfTeams)
            '''
    class Dream11Team4_B3B3K2A3():
        def method1():
            Dream11.CombinationsOfTeam_Batsman_Bowler(Dream11.All_Combinations_Of_Players_with_3_min_Batsman, Dream11.All_Combinations_Of_Players_with_3_min_Bowler)
            Dream11.Seq4_B3B3 = Dream11.List3
            Dream11.CombinationsOfTeam_Keeper_Allrounder(Dream11.All_Combinations_Of_Players_with_2_min_Keeper, Dream11.All_Combinations_Of_Players_with_3_min_AllRounder)
            Dream11.Seq4_K2A3 = Dream11.List4
            Dream11.CombinationsOfTeamForDiffSequence(Dream11.Seq4_B3B3, Dream11.Seq4_K2A3)
            Dream11.Seq4_B3B3K2A3 = Dream11.List5
            Dream11.FinalListOfTeams = Dream11.FinalListOfTeams + Dream11.Seq4_B3B3K2A3
            '''
            print (Dream11.Seq2_B3B3)        print (Dream11.Seq2_K3A3)        print (Dream11.Seq4_B3B3K2A3)        print (Dream11.FinalListOfTeams)
            '''
    class Dream11Team5_B3B3K3A2():
        def method1():
            Dream11.CombinationsOfTeam_Batsman_Bowler(Dream11.All_Combinations_Of_Players_with_3_min_Batsman, Dream11.All_Combinations_Of_Players_with_3_min_Bowler)
            Dream11.Seq5_B3B3 = Dream11.List3
            Dream11.CombinationsOfTeam_Keeper_Allrounder(Dream11.All_Combinations_Of_Players_with_3_min_Keeper, Dream11.All_Combinations_Of_Players_with_2_min_AllRounder)
            Dream11.Seq5_K3A2 = Dream11.List4
            Dream11.CombinationsOfTeamForDiffSequence(Dream11.Seq5_B3B3, Dream11.Seq5_K3A2)
            Dream11.Seq5_B3B3K3A2 = Dream11.List5
            Dream11.FinalListOfTeams = Dream11.FinalListOfTeams + Dream11.Seq5_B3B3K3A2
            '''
            print (Dream11.Seq2_B3B3)        print (Dream11.Seq2_K3A2)        print (Dream11.Seq5_B3B3K3A2)        print (Dream11.FinalListOfTeams)
            '''
    class Dream11Team6_B3B3K4A1():
        def method1():
            Dream11.CombinationsOfTeam_Batsman_Bowler(Dream11.All_Combinations_Of_Players_with_3_min_Batsman, Dream11.All_Combinations_Of_Players_with_3_min_Bowler)
            Dream11.Seq6_B3B3 = Dream11.List3
            Dream11.CombinationsOfTeam_Keeper_Allrounder(Dream11.All_Combinations_Of_Players_with_4_min_Keeper, Dream11.All_Combinations_Of_Players_with_1_min_AllRounder)
            Dream11.Seq6_K4A1 = Dream11.List4
            Dream11.CombinationsOfTeamForDiffSequence(Dream11.Seq6_B3B3, Dream11.Seq6_K4A1)
            Dream11.Seq6_B3B3K4A1 = Dream11.List5
            Dream11.FinalListOfTeams = Dream11.FinalListOfTeams + Dream11.Seq6_B3B3K4A1
            '''
            print (Dream11.Seq2_B3B3)        print (Dream11.Seq2_K4A1)        print (Dream11.Seq6_B3B3K4A1)        print (Dream11.FinalListOfTeams)
            '''
    class Dream11Team7_B3B4K2A2():
        def method1():
            Dream11.CombinationsOfTeam_Batsman_Bowler(Dream11.All_Combinations_Of_Players_with_3_min_Batsman, Dream11.All_Combinations_Of_Players_with_4_min_Bowler)
            Dream11.Seq7_B3B4 = Dream11.List3
            Dream11.CombinationsOfTeam_Keeper_Allrounder(Dream11.All_Combinations_Of_Players_with_2_min_Keeper, Dream11.All_Combinations_Of_Players_with_2_min_AllRounder)
            Dream11.Seq7_K2A2 = Dream11.List4
            Dream11.CombinationsOfTeamForDiffSequence(Dream11.Seq7_B3B4, Dream11.Seq7_K2A2)
            Dream11.Seq7_B3B4K2A2 = Dream11.List5
            Dream11.FinalListOfTeams = Dream11.FinalListOfTeams + Dream11.Seq7_B3B4K2A2
            '''
            print (Dream11.Seq2_B3B4)        print (Dream11.Seq2_K2A2)        print (Dream11.Seq7_B3B4K2A2)        print (Dream11.FinalListOfTeams)
            '''
    class Dream11Team8_B3B4K3A1():
        def method1():
            Dream11.CombinationsOfTeam_Batsman_Bowler(Dream11.All_Combinations_Of_Players_with_3_min_Batsman, Dream11.All_Combinations_Of_Players_with_4_min_Bowler)
            Dream11.Seq8_B3B4 = Dream11.List3
            Dream11.CombinationsOfTeam_Keeper_Allrounder(Dream11.All_Combinations_Of_Players_with_3_min_Keeper, Dream11.All_Combinations_Of_Players_with_1_min_AllRounder)
            Dream11.Seq8_K3A1 = Dream11.List4
            Dream11.CombinationsOfTeamForDiffSequence(Dream11.Seq8_B3B4, Dream11.Seq8_K3A1)
            Dream11.Seq8_B3B4K3A1 = Dream11.List5
            Dream11.FinalListOfTeams = Dream11.FinalListOfTeams + Dream11.Seq8_B3B4K3A1
            '''
            print (Dream11.Seq2_B3B4)        print (Dream11.Seq2_K3A1)        print (Dream11.Seq8_B3B4K3A1)        print (Dream11.FinalListOfTeams)
            '''
    class Dream11Team9_B3B5K2A1():
        def method1():
            Dream11.CombinationsOfTeam_Batsman_Bowler(Dream11.All_Combinations_Of_Players_with_3_min_Batsman, Dream11.All_Combinations_Of_Players_with_5_min_Bowler)
            Dream11.Seq9_B3B5 = Dream11.List3
            Dream11.CombinationsOfTeam_Keeper_Allrounder(Dream11.All_Combinations_Of_Players_with_2_min_Keeper, Dream11.All_Combinations_Of_Players_with_1_min_AllRounder)
            Dream11.Seq9_K2A1 = Dream11.List4
            Dream11.CombinationsOfTeamForDiffSequence(Dream11.Seq9_B3B5, Dream11.Seq9_K2A1)
            Dream11.Seq9_B3B5K2A1 = Dream11.List5
            Dream11.FinalListOfTeams = Dream11.FinalListOfTeams + Dream11.Seq9_B3B5K2A1
            '''
            print (Dream11.Seq2_B3B5)        print (Dream11.Seq2_K2A1)        print (Dream11.Seq9_B3B5K2A1)        print (Dream11.FinalListOfTeams)
            '''
    class Dream11Team10_B3B6K1A1():
        def method1():
            Dream11.CombinationsOfTeam_Batsman_Bowler(Dream11.All_Combinations_Of_Players_with_3_min_Batsman, Dream11.All_Combinations_Of_Players_with_6_min_Bowler)
            Dream11.Seq10_B3B6 = Dream11.List3
            Dream11.CombinationsOfTeam_Keeper_Allrounder(Dream11.All_Combinations_Of_Players_with_1_min_Keeper, Dream11.All_Combinations_Of_Players_with_1_min_AllRounder)
            Dream11.Seq10_K1A1 = Dream11.List4
            Dream11.CombinationsOfTeamForDiffSequence(Dream11.Seq10_B3B6, Dream11.Seq10_K1A1)
            Dream11.Seq10_B3B6K1A1 = Dream11.List5
            Dream11.FinalListOfTeams = Dream11.FinalListOfTeams + Dream11.Seq10_B3B6K1A1
            '''
            print (Dream11.Seq2_B3B6)        print (Dream11.Seq2_K1A1)        print (Dream11.Seq10_B3B6K1A1)        print (Dream11.FinalListOfTeams)
            '''
    class Dream11Team11_B4B3K1A3():
        def method1():
            Dream11.CombinationsOfTeam_Batsman_Bowler(Dream11.All_Combinations_Of_Players_with_4_min_Batsman, Dream11.All_Combinations_Of_Players_with_3_min_Bowler)
            Dream11.Seq11_B4B3 = Dream11.List3
            Dream11.CombinationsOfTeam_Keeper_Allrounder(Dream11.All_Combinations_Of_Players_with_1_min_Keeper, Dream11.All_Combinations_Of_Players_with_3_min_AllRounder)
            Dream11.Seq11_K1A3 = Dream11.List4
            Dream11.CombinationsOfTeamForDiffSequence(Dream11.Seq11_B4B3, Dream11.Seq11_K1A3)
            Dream11.Seq11_B4B3K1A3 = Dream11.List5
            Dream11.FinalListOfTeams = Dream11.FinalListOfTeams + Dream11.Seq11_B4B3K1A3
            '''
            print (Dream11.Seq2_B4B3)        print (Dream11.Seq2_K1A3)        print (Dream11.Seq11_B4B3K1A3)        print (Dream11.FinalListOfTeams)
            '''
    class Dream11Team12_B4B3K2A2():
        def method1():
            Dream11.CombinationsOfTeam_Batsman_Bowler(Dream11.All_Combinations_Of_Players_with_4_min_Batsman, Dream11.All_Combinations_Of_Players_with_3_min_Bowler)
            Dream11.Seq12_B4B3 = Dream11.List3
            Dream11.CombinationsOfTeam_Keeper_Allrounder(Dream11.All_Combinations_Of_Players_with_2_min_Keeper, Dream11.All_Combinations_Of_Players_with_2_min_AllRounder)
            Dream11.Seq12_K2A2 = Dream11.List4
            Dream11.CombinationsOfTeamForDiffSequence(Dream11.Seq12_B4B3, Dream11.Seq12_K2A2)
            Dream11.Seq12_B4B3K2A2 = Dream11.List5
            Dream11.FinalListOfTeams = Dream11.FinalListOfTeams + Dream11.Seq12_B4B3K2A2
            '''
            print (Dream11.Seq2_B4B3)        print (Dream11.Seq2_K2A2)        print (Dream11.Seq12_B4B3K2A2)        print (Dream11.FinalListOfTeams)
            '''
    class Dream11Team13_B4B3K3A1():
        def method1():
            Dream11.CombinationsOfTeam_Batsman_Bowler(Dream11.All_Combinations_Of_Players_with_4_min_Batsman, Dream11.All_Combinations_Of_Players_with_3_min_Bowler)
            Dream11.Seq13_B4B3 = Dream11.List3
            Dream11.CombinationsOfTeam_Keeper_Allrounder(Dream11.All_Combinations_Of_Players_with_3_min_Keeper, Dream11.All_Combinations_Of_Players_with_1_min_AllRounder)
            Dream11.Seq13_K3A1 = Dream11.List4
            Dream11.CombinationsOfTeamForDiffSequence(Dream11.Seq13_B4B3, Dream11.Seq13_K3A1)
            Dream11.Seq13_B4B3K3A1 = Dream11.List5
            Dream11.FinalListOfTeams = Dream11.FinalListOfTeams + Dream11.Seq13_B4B3K3A1
            '''
            print (Dream11.Seq2_B4B3)        print (Dream11.Seq2_K3A1)        print (Dream11.Seq13_B4B3K3A1)        print (Dream11.FinalListOfTeams)
            '''
    class Dream11Team14_B4B4K1A2():
        def method1():
            Dream11.CombinationsOfTeam_Batsman_Bowler(Dream11.All_Combinations_Of_Players_with_4_min_Batsman, Dream11.All_Combinations_Of_Players_with_4_min_Bowler)
            Dream11.Seq14_B4B4 = Dream11.List3
            Dream11.CombinationsOfTeam_Keeper_Allrounder(Dream11.All_Combinations_Of_Players_with_1_min_Keeper, Dream11.All_Combinations_Of_Players_with_2_min_AllRounder)
            Dream11.Seq14_K1A2 = Dream11.List4
            Dream11.CombinationsOfTeamForDiffSequence(Dream11.Seq14_B4B4, Dream11.Seq14_K1A2)
            Dream11.Seq14_B4B4K1A2 = Dream11.List5
            Dream11.FinalListOfTeams = Dream11.FinalListOfTeams + Dream11.Seq14_B4B4K1A2
            '''
            print (Dream11.Seq2_B4B4)        print (Dream11.Seq2_K1A2)        print (Dream11.Seq14_B4B4K1A2)        print (Dream11.FinalListOfTeams)
            '''
    class Dream11Team15_B4B4K2A1():
        def method1():
            Dream11.CombinationsOfTeam_Batsman_Bowler(Dream11.All_Combinations_Of_Players_with_4_min_Batsman, Dream11.All_Combinations_Of_Players_with_4_min_Bowler)
            Dream11.Seq15_B4B4 = Dream11.List3
            Dream11.CombinationsOfTeam_Keeper_Allrounder(Dream11.All_Combinations_Of_Players_with_2_min_Keeper, Dream11.All_Combinations_Of_Players_with_1_min_AllRounder)
            Dream11.Seq15_K2A1 = Dream11.List4
            Dream11.CombinationsOfTeamForDiffSequence(Dream11.Seq15_B4B4, Dream11.Seq15_K2A1)
            Dream11.Seq15_B4B4K2A1 = Dream11.List5
            Dream11.FinalListOfTeams = Dream11.FinalListOfTeams + Dream11.Seq15_B4B4K2A1
            '''
            print (Dream11.Seq2_B4B4)        print (Dream11.Seq2_K2A1)        print (Dream11.Seq15_B4B4K2A1)        print (Dream11.FinalListOfTeams)
            '''
    class Dream11Team16_B4B5K1A1():
        def method1():
            Dream11.CombinationsOfTeam_Batsman_Bowler(Dream11.All_Combinations_Of_Players_with_4_min_Batsman, Dream11.All_Combinations_Of_Players_with_5_min_Bowler)
            Dream11.Seq16_B4B5 = Dream11.List3
            Dream11.CombinationsOfTeam_Keeper_Allrounder(Dream11.All_Combinations_Of_Players_with_1_min_Keeper, Dream11.All_Combinations_Of_Players_with_1_min_AllRounder)
            Dream11.Seq16_K1A1 = Dream11.List4
            Dream11.CombinationsOfTeamForDiffSequence(Dream11.Seq16_B4B5, Dream11.Seq16_K1A1)
            Dream11.Seq16_B4B5K1A1 = Dream11.List5
            Dream11.FinalListOfTeams = Dream11.FinalListOfTeams + Dream11.Seq16_B4B5K1A1
            '''
            print (Dream11.Seq16_B4B5)        print (Dream11.Seq16_K1A1)        print (Dream11.Seq16_B4B5K1A1)        print (Dream11.FinalListOfTeams)
            '''
    class Dream11Team17_B5B3K1A2():
        def method1():
            Dream11.CombinationsOfTeam_Batsman_Bowler(Dream11.All_Combinations_Of_Players_with_5_min_Batsman, Dream11.All_Combinations_Of_Players_with_3_min_Bowler)
            Dream11.Seq17_B5B3 = Dream11.List3
            Dream11.CombinationsOfTeam_Keeper_Allrounder(Dream11.All_Combinations_Of_Players_with_1_min_Keeper, Dream11.All_Combinations_Of_Players_with_2_min_AllRounder)
            Dream11.Seq17_K1A2 = Dream11.List4
            Dream11.CombinationsOfTeamForDiffSequence(Dream11.Seq17_B5B3, Dream11.Seq17_K1A2)
            Dream11.Seq17_B5B3K1A2 = Dream11.List5
            Dream11.FinalListOfTeams = Dream11.FinalListOfTeams + Dream11.Seq17_B5B3K1A2
            '''
            print (Dream11.Seq17_B5B3)        print (Dream11.Seq17_K1A2)        print (Dream11.Seq17_B5B3K1A2)        print (Dream11.FinalListOfTeams)
            '''
    class Dream11Team18_B5B3K2A1():
        def method1():
            Dream11.CombinationsOfTeam_Batsman_Bowler(Dream11.All_Combinations_Of_Players_with_5_min_Batsman, Dream11.All_Combinations_Of_Players_with_3_min_Bowler)
            Dream11.Seq18_B5B3 = Dream11.List3
            Dream11.CombinationsOfTeam_Keeper_Allrounder(Dream11.All_Combinations_Of_Players_with_2_min_Keeper, Dream11.All_Combinations_Of_Players_with_1_min_AllRounder)
            Dream11.Seq18_K2A1 = Dream11.List4
            Dream11.CombinationsOfTeamForDiffSequence(Dream11.Seq18_B5B3, Dream11.Seq18_K2A1)
            Dream11.Seq18_B5B3K2A1 = Dream11.List5
            Dream11.FinalListOfTeams = Dream11.FinalListOfTeams + Dream11.Seq18_B5B3K2A1
            '''
            print (Dream11.Seq18_B5B3)        print (Dream11.Seq18_K2A1)        print (Dream11.Seq18_B5B3K2A1)        print (Dream11.FinalListOfTeams)
            '''
    class Dream11Team19_B5B4K1A1():
        def method1():
            Dream11.CombinationsOfTeam_Batsman_Bowler(Dream11.All_Combinations_Of_Players_with_5_min_Batsman, Dream11.All_Combinations_Of_Players_with_4_min_Bowler)
            Dream11.Seq19_B5B4 = Dream11.List3
            Dream11.CombinationsOfTeam_Keeper_Allrounder(Dream11.All_Combinations_Of_Players_with_1_min_Keeper, Dream11.All_Combinations_Of_Players_with_1_min_AllRounder)
            Dream11.Seq19_K1A1 = Dream11.List4
            Dream11.CombinationsOfTeamForDiffSequence(Dream11.Seq19_B5B4, Dream11.Seq19_K1A1)
            Dream11.Seq19_B5B4K1A1 = Dream11.List5
            Dream11.FinalListOfTeams = Dream11.FinalListOfTeams + Dream11.Seq19_B5B4K1A1
            '''
            print (Dream11.Seq19_B5B4)        print (Dream11.Seq19_K1A1)        print (Dream11.Seq19_B5B4K1A1)        print (Dream11.FinalListOfTeams)
            '''
    class Dream11Team20_B6B3K1A1():
        def method1():
            Dream11.CombinationsOfTeam_Batsman_Bowler(Dream11.All_Combinations_Of_Players_with_6_min_Batsman, Dream11.All_Combinations_Of_Players_with_3_min_Bowler)
            Dream11.Seq20_B6B3 = Dream11.List3
            Dream11.CombinationsOfTeam_Keeper_Allrounder(Dream11.All_Combinations_Of_Players_with_1_min_Keeper, Dream11.All_Combinations_Of_Players_with_1_min_AllRounder)
            Dream11.Seq20_K1A1 = Dream11.List4
            Dream11.CombinationsOfTeamForDiffSequence(Dream11.Seq20_B6B3, Dream11.Seq20_K1A1)
            Dream11.Seq20_B6B3K1A1 = Dream11.List5
            Dream11.FinalListOfTeams = Dream11.FinalListOfTeams + Dream11.Seq20_B6B3K1A1
            
            #print (Dream11.Seq20_B6B3)
            #print (Dream11.Seq20_K1A1)
            #print (Dream11.Seq20_B6B3K1A1)
            #print (Dream11.FinalListOfTeams)
            
            
    @staticmethod
    def CombinationsOfTeam1WithProperTeamSizeTeam():
        #print (dict(Dream11.D_Names_Teams))
        for x in range (0,len(Dream11.FinalListOfTeams)): 
            Dream11.c1 = 0
            Dream11.c2 = 0
            for key in Dream11.D_Names_Teams:
                if key in Dream11.FinalListOfTeams[x]:
                    #print (b)
                    if (Dream11.D_Names_Teams)[key] == 'PBKS':
                        Dream11.c1+=1
                        continue
                    elif (Dream11.D_Names_Teams)[key] == 'CSK':
                        Dream11.c2+=1
                        continue
                elif key not in Dream11.FinalListOfTeams[x]:
                    #print ('not in the list')
                    continue
            #print (Dream11.c1,Dream11.c2)
            if Dream11.c1 >7 or Dream11.c1 < 4:
                Dream11.FinalListOfTeams[x] = []
            elif Dream11.c2 > 7 or Dream11.c2 < 4:
                Dream11.FinalListOfTeams[x] = []
        #print (Dream11.FinalListOfTeams)
        
        #print (Dream11.Seq1_B3B3K1A4)
        #return Dream11.Seq1_B3B3K1A4  
        #Dream11.Seq1_B3B3K1A4_TEAMSIZE = Dream11.Seq1_B3B3K1A4
        #B3B3K1A4_PROPER_TEAMSIZE =  open("C:\\Users\\ag26235\\OneDrive - Anthem\\Desktop\\Lessons\\ProjectDream11Learning\\Dream11PlayersList\\Seq1\\B3B3K1A4_PROPER_TEAMSIZE.txt", 'w+')
        #B3B3K1A4_PROPER_TEAMSIZE.writelines(str(Dream11.Seq1_B3B3K1A4_TEAMSIZE))
        #B3B3K1A4_PROPER_TEAMSIZE.close()
        
    @staticmethod        
    def CombinationsOfTeam1WithProperCreditPointTeam():
        #print (Dream11.D_Names_Credits)
        for x in range (0,len(Dream11.FinalListOfTeams)): 
            Dream11.Player_Credit = 0.0
            for key in Dream11.D_Names_Credits:
                if key in Dream11.FinalListOfTeams[x]:
                    #print (Dream11.D_Names_Credits[key])
                    Dream11.Player_Credit = Dream11.Player_Credit + (Dream11.D_Names_Credits)[key]
                    continue
                elif key not in Dream11.FinalListOfTeams[x]:
                    #print ('not in the list')
                    continue
            #print (Dream11.Player_Credit)
            if Dream11.Player_Credit >100:
                Dream11.FinalListOfTeams[x] = []
            elif Dream11.Player_Credit <= 100:
                continue
        #print (Dream11.FinalListOfTeams)
        for a in range(len(Dream11.FinalListOfTeams)):
            if (len(Dream11.FinalListOfTeams[a]) <11):
                continue
            else:
                Dream11.FinalTeamList.append(Dream11.FinalListOfTeams[a])
        print ('Valid combination of team count is: ', len(Dream11.FinalTeamList))
        #for a in range(len(Dream11.FinalTeamList)):
        #    print (len(Dream11.FinalTeamList[a]))
        print (Dream11.FinalTeamList)    
        B3B3K1A4_PROPER_TEAMSIZE_CREDITS =  open("C:\\Users\\ag26235\\OneDrive - Anthem\\Desktop\\Lessons\\ProjectDream11Learning\\Dream11PlayersList\\FinalCombination\\FinalTeamList.txt", 'w+')
        B3B3K1A4_PROPER_TEAMSIZE_CREDITS.writelines(str(Dream11.FinalTeamList))
        B3B3K1A4_PROPER_TEAMSIZE_CREDITS.close()
    

P1 = Dream11('M.S.DHONI','CSK','Keeper',8.5)
P2 = Dream11('J.Sharma','PBKS','Keeper',8.5)
P3 = Dream11('J.Bairstow','PBKS','Keeper',9)

P4 = Dream11('M.Agarwal','PBKS','Batsman',9.5)
P5 = Dream11('S.Dhawan','PBKS','Batsman',9.5)
P6 = Dream11('R.Gaikwad','CSK','Batsman',9.5)
P7 = Dream11('A.Rayudu','CSK','Batsman',9.5)
P8 = Dream11('S.Dube','CSK','Batsman',9.5)
P9 = Dream11('S.Khan','PBKS','Batsman',9)
P10 = Dream11('R.Uthappa','CSK','Batsman',9)

P11 = Dream11('L.Livingstone','PBKS','Allrounder',10)
P12 = Dream11('M.Santner','CSK','Allrounder',9.5)
P13 = Dream11('O.Smith','PBKS','Allrounder',9.5)
#P14 = Dream11('R.Jadeja','CSK','Allrounder',9)
#P15 = Dream11('D.Pretorius','CSK','Allrounder',9.5)

P14 = Dream11('K.Rabada','PBKS','Bowler',8.5)
P15 = Dream11('D.Bravo','CSK','Bowler',9.5)
P16 = Dream11('M.Theekshna','CSK','Bowler',9.5)
P17 = Dream11('N.Ellis','PBKS','Bowler',9.5)
P18 = Dream11('M.Choudhary','CSK','Bowler',9)
#P21 = Dream11('A.Singh','PBKS','Bowler',9)
#P22 = Dream11('R.Chahar','PBKS','Bowler',9.5)


P1.CollectInfo()
P2.CollectInfo()
P3.CollectInfo()
P4.CollectInfo()
P5.CollectInfo()
P6.CollectInfo()
P7.CollectInfo()
P8.CollectInfo()
P9.CollectInfo()
P10.CollectInfo()
P11.CollectInfo()
P12.CollectInfo()
P13.CollectInfo()
P14.CollectInfo()
P15.CollectInfo()
P16.CollectInfo()
P17.CollectInfo()
P18.CollectInfo()
#P19.CollectInfo()
#P20.CollectInfo()
#P21.CollectInfo()
#P22.CollectInfo()


Dream11.SegregateMain()
Dream11.CombinationsOfPlayers()
Dream11.Dream11Team1_B3B3K1A4.method1()
Dream11.Dream11Team2_B3B4K1A3.method1()
Dream11.Dream11Team3_B3B5K1A2.method1() 
Dream11.Dream11Team4_B3B3K2A3.method1() 
Dream11.Dream11Team5_B3B3K3A2.method1() 
Dream11.Dream11Team6_B3B3K4A1.method1() 
Dream11.Dream11Team7_B3B4K2A2.method1() 
Dream11.Dream11Team8_B3B4K3A1.method1() 
Dream11.Dream11Team9_B3B5K2A1.method1() 
Dream11.Dream11Team10_B3B6K1A1.method1() 
Dream11.Dream11Team11_B4B3K1A3.method1() 
Dream11.Dream11Team12_B4B3K2A2.method1() 
Dream11.Dream11Team13_B4B3K3A1.method1() 
Dream11.Dream11Team14_B4B4K1A2.method1() 
Dream11.Dream11Team15_B4B4K2A1.method1() 
Dream11.Dream11Team16_B4B5K1A1.method1() 
Dream11.Dream11Team17_B5B3K1A2.method1() 
Dream11.Dream11Team18_B5B3K2A1.method1() 
Dream11.Dream11Team19_B5B4K1A1.method1() 
Dream11.Dream11Team20_B6B3K1A1.method1() 
Dream11.CombinationsOfTeam1WithProperTeamSizeTeam()
Dream11.CombinationsOfTeam1WithProperCreditPointTeam()