# # -*- coding: utf-8 -*-
# """
# Created on Thu May  5 12:47:06 2022

# @author: nariman


# Preperaing Attribute ID:
# In Roof_Rafters File, the recoverability and reusibility is devided in 2parts(Reuse,ReCover)
# In Exterior file, it is devided just for wall_cover 
# In Interior file, those 2 addition attributes of exterior walls has missing value
# """

import itertools as it
import pandas as pd
import csv
import numpy as np   

# Family_Code_Dict1={"I":"Interior","E":"Exterior","R":"Roof","F":"Floor"}
# Family_Code_Dict2={"D":"Door","W":"Wall","RB":"Bottom Runner","RT":"Top Runner",\
#             "Wi":"Window","In":"Insulation","St":"Stud","Sh":"Sheating","Cl":"Cladding",\
#     "RC":"Cover","Ra":"Rafters","Tr":"Truss","S":"Structure","GS":"Ground_Level_Structure","F":"Finishing","J":"Joist"}
    
# ##attribute ID preperation 
# Col_Names=["Family_Name","Family_Code","Quantity","Connection_Type","De_con","De_mov","De_Pre"\
#           ,"De_tol","Re_use","Re_sec","Re_Tox","Re_rec"]
# Col_Names_Roof_rafters=["Family_Name","Family_Code","Quantity","Connection_Type","De_con","De_mov","De_Pre"\
#            ,"De_tol","Re_use","Re_sec","Re_Tox","Re_rec","Re_rec_cover","Re_use_cover",\
#                "Re_tox_cover","Re_rec_sheat","Re_use_sheat","Re_tox_sheat",\
#                    "Re_rec_insul","Re_use_insul","Re_tox_insul"]  
# Col_Names_Interior=["Family_Name","Family_Code","Quantity","Connection_Type","De_con","De_mov","De_Pre"\
#           ,"De_tol","Re_use","Re_sec","Re_Tox","Re_rec","Connection_Type_S","De_con_S","De_mov_S","De_Pre_S"\
#                     ,"De_tol_S","Re_use_S","Re_sec_S","Re_Tox_S","Re_rec_S","Connection_Type_Co","De_con_Co","De_mov_Co","De_Pre_Co"\
#                               ,"De_tol_Co","Re_use_Co","Re_sec_Co","Re_Tox_Co","Re_rec_Co"]
# ##Reading the input files from revit model
# df_interior=pd.read_csv("Interior.csv",names=Col_Names_Interior)
# df_exterior=pd.read_csv("Exterior.csv",names=Col_Names)
# df_roof=pd.read_csv("Roof.csv",names=Col_Names)
# df_floor=pd.read_csv("floor.csv",names=Col_Names)

# df_exterior["De_con"]=df_exterior["De_con"].mask(df_exterior["De_con"]=="NN",np.nan)
# df_exterior["De_con"]=df_exterior["De_con"].astype(float)

# def akinade(x):
#     # checking if it is intrior assembly or not!
#     if x.loc[0,"Family_Code"].split("_")[0]!="I":
#         x=x.drop("De_mov,De_tol".split(","),axis=1,inplace=True)
#     else:
#         x.drop("De_mov,De_tol,De_mov_S,De_tol_S,De_tol_Co,De_mov_Co".split(","),axis=1,inplace=True)
#         # x["Quantity_Co"]=x["Quantity"]
        
#         # x=x[['Family_Name', 'Family_Code', 'Quantity', 'Connection_Type','De_con', 'De_Pre', 'De_tol','R_Score', 'Connection_Type_S','De_con_S', 'De_Pre_S', 'De_tol_S','R_Score_Structure', 'Connection_Type_Co','De_con_Co', 'De_Pre_Co', 'De_tol_Co', 'R_Score_Cover']]
#     # material=[]
#     # for family in x["Family_Code"]:
#     #    material=material+family.split("_")[2:]
#     #    material_count=len(set(material))


       
# akinade(df_interior)
# akinade(df_exterior)
# akinade(df_roof)
# akinade(df_floor)
# # print(list(df_interior.columns))
# # df_interior=df_interior[['Family_Name', 'Family_Code', 'Quantity', 'Connection_Type','De_con', 'De_Pre','R_Score', 'Connection_Type_S','De_con_S', 'De_Pre_S','R_Score_Structure', 'Connection_Type_Co','De_con_Co', 'De_Pre_Co', 'R_Score_Cover']]

# # b=akinade(df_exterior)
# # def compute(x):
# #    ##calculates D_Score and R_Score
# #    ##Since some attributes have missing values for some files, the average is
# #    ##takenbased on number of attribtes without Null
# #    # x["De_con"]=x["De_con"].mask(x["De_con"]=="NN",np.nan)
# #    # x["De_con"].astype(float)
# #    x['R_atr_Count'] = len(x.iloc[1,8:])
# #    x["Null_Count"]=x.iloc[:,8:].apply(lambda x:x.isnull().sum(), axis=1)
# #    x["Sum_De"]=x[["De_con","De_mov","De_Pre","De_tol"]].sum(axis=1)
# #    x["Sum_Re"]=x.iloc[:,8:-3].sum(axis=1)
# #    x["R_Score"]=(x["Sum_Re"]/(x["R_atr_Count"]-x["Null_Count"]))
# #    x["D_Score"]=(x["Sum_De"]/4).mask(x["De_con"].isna(),other=x["Sum_De"]/3)
# #    x["D_Score"]=round(x["D_Score"],3)
# #    x["R_Score"]=round(x["R_Score"],3)
# #    x.drop(["Sum_De","Sum_Re","R_atr_Count","Null_Count"],axis=1,inplace=True)
   
# def List_Prep(x,y):  
#     ##Prepers the output file for developing the combinations
    
#     (a,b)=x.shape 
#     info=[]
#     Family_code=x.loc[0,"Family_Code"].split("_")[1]
#     for i in range(a):
#       if Family_code==x.loc[i,"Family_Code"].split("_")[1]:
#           info.append([x.iloc[i,j] for j in range (1,b)])
#       else:
#           y.append(info)
#           info=[]
#           info.append([x.iloc[i,j] for j in range (1,b)])
#       Family_code=x.loc[i,"Family_Code"].split("_")[1]
#     y.append(info)


# def combination(x)    :
#     b=it.product(*x)
#     with open("D:\\aa\\Akinade_DAS\\Akinade_out.csv","w") as out:
#         writer=csv.writer(out)
#         # writer.writerows([["Family","Quantity","Connection_Type","D_Score","R_Score"]*17])
#         writer.writerows(b)
    
# def Statistic(x):
#     ##Generates a brief overview of each Category (D_Score,R_Score,number of Families)
#     temp2=pd.DataFrame()
#     temp=pd.DataFrame
#     for i in range(len(x)):
#        temp=pd.DataFrame(x[i]).describe().transpose()
#        temp["Category"]=[x[i][0][0],x[i][0][0],x[i][0][0]]
#        temp["Index"]=["Quantity","D_Score","R_Score"]
#        temp.set_index("Index",inplace=True) 
#        temp["mean"]=round(temp["mean"],3)
#        temp.drop(["Quantity"],inplace=True)
#        temp2=temp2.append(temp)
#     temp2["Category"]=temp2["Category"].apply(lambda x:Family_Code_Dict1[x.split("_")[0]]\
#                                               +" "+Family_Code_Dict2[x.split("_")[1]])
    
#     return temp2


    
# # compute(df_interior)
# # compute(df_exterior)
# # compute(df_floor)
# # compute(df_roof) 


# # df_interior.to_csv("D:\\aa\\Akinade_DAS\\Excel_Output\\Akinade_interior.csv")
# # df_exterior.to_csv("D:\\aa\\Akinade_DAS\\Excel_Output\\Akinade_exterior.csv")
# # df_roof.to_csv("D:\\aa\\Akinade_DAS\\Excel_Output\\Akinade_roof.csv")
# # df_floor.to_csv("D:\\aa\\Akinade_DAS\\Excel_Output\\Akinade_floor.csv")


# interior_output=[]
# exterior_output=[]
# floor_output=[]
# roof_output=[]

# List_Prep(df_interior,interior_output)
# List_Prep(df_exterior,exterior_output)
# List_Prep(df_floor,floor_output)
# List_Prep(df_roof,roof_output)
# # c=combination(interior_output)

# New=it.product(exterior_output[0],exterior_output[1],exterior_output[2],exterior_output[3],exterior_output[4],exterior_output[5])
# rows_gen=(L_1+L_2+L_3+L_4+L_5+L_6 for L_1,L_2,L_3,L_4,L_5,L_6 in New)

# with open("D:\\aa\\Akinade_DAS\\Exterior_output.csv","w") as out:
#       writer=csv.writer(out)
#       writer.writerows(rows_gen)
# # interior=Statistic(interior_output)
# # exterior=Statistic(exterior_output)

# # roof=Statistic(roof_output)312
# # floor=Statistic(floor_output)

# # interior.to_csv("D:\\aa\\Akinade_DAS\\Excel_Output\\Statistic\\Akinade_interior.csv")
# # exterior.to_csv("D:\\aa\\Akinade_DAS\\Excel_Output\\Statistic\\Akinade_exterior.csv")
# # roof.to_csv("D:\\aa\\Akinade_DAS\\Excel_Output\\Statistic\\Akinade_roof.csv")
# # floor.to_csv("D:\\aa\\Akinade_DAS\\Excel_Output\\Statistic\\Akinade_floor.csv")
# # b=df_interior[df_interior["D_Score"]>df_interior["R_Score"]]
# # a=len(df_interior[df_interior["D_Score"]==df_interior["R_Score"]]["D_Score"])
# # a=a+len(df_exterior[df_exterior["D_Score"]==df_exterior["R_Score"]]["D_Score"])
# # a=a+len(df_floor[df_floor["D_Score"]==df_floor["R_Score"]]["D_Score"])
# # a=a+len(df_roof[df_roof["D_Score"]==df_roof["R_Score"]]["D_Score"])
# # c=len(df_interior["D_Score"])+len(df_exterior["D_Score"])+len(df_floor["D_Score"])+len(df_roof["D_Score"])
# # Creating the combinations and output file of combinations

# # d=len(interior_output)

# # a = [[['a','b'],2,3]],[4,5,6],[7,8,9,10]]
# # b=list(it.product(*a))

    
    

# # with open("D:\\aa\\Akinade_DAS\\Akinade_out.csv","w") as out:
# #     writer=csv.writer(out)
# #      # writer.writerows([["Family","Quantity","Connection_Type","D_Score","R_Score"]*17])
# #     writer.writerows(b)

# df_output=pd.read_csv("D:\\aa\\Akinade_DAS\\Akinade_out.csv")
# a=df_output.iloc[1,:]
# df_output.replace(to_replace="nan",value=np.nan)
# df_output.dropna(axis=1, how="all",inplace=True)
# # (z,x)=df_output.shape
# # L=list(df_output.loc[1])
# # # new=list(it.chain(*L))
# L=list(np.concatenate(L).flat)
# for i in range (z): 
    # df_output.iloc[i,:]= list(np.concatenate(df_output.iloc[i,:]). flat)
col_name=['Family_Code', 'Quantity', 'Connection_Type', 'De_con', 'De_Pre', 'Re_use', 'Re_sec', 'Re_Tox', 'Re_rec', 'Family_Code2', 'Quantity2', 'Connection_Type2', 'De_con2', 'De_Pre2', 'Re_use2', 'Re_sec2', 'Re_Tox2', 'Re_rec2', 'Family_Code3', 'Quantity3', 'Connection_Type3', 'De_con3', 'De_Pre3', 'Re_use3', 'Re_sec3', 'Re_Tox3', 'Re_rec3', 'Family_Code4', 'Quantity4', 'Connection_Type4', 'De_con4', 'De_Pre4', 'Re_use4', 'Re_sec4', 'Re_Tox4', 'Re_rec4']
a=len (col_name)
Exterior=pd.read_csv("Exterior_output.csv",header=None)

