# -*- coding: utf-8 -*-
"""
Created on Thu May  5 12:47:06 2022

@author: nariman


Preperaing Attribute ID:
In Roof_Rafters File, the recoverability and reusibility is devided in 2parts(Reuse,ReCover)
In Exterior file, it is devided just for wall_cover 
In Interior file, those 2 addition attributes of exterior walls has missing value
"""

import itertools as it
import pandas as pd
import csv
import numpy as np   

Family_Code_Dict1={"I":"Interior","E":"Exterior","R":"Roof","F":"Floor"}
Family_Code_Dict2={"D":"Door","W":"Wall","RB":"Bottom Runner","RT":"Top Runner",\
            "Wi":"Window","In":"Insulation","St":"Stud","Sh":"Sheating","Cl":"Cladding",\
    "RC":"Cover","Ra":"Rafters","Tr":"Truss","S":"Structure","GS":"Ground_Level_Structure","F":"Finishing","J":"Joist"}
    
##attribute ID preperation 
Col_Names=["Family_Name","Family_Code","Quantity","Connection_Type","De_con","De_mov","De_Pre"\
          ,"De_tol","Re_use","Re_sec","Re_Tox","Re_rec","Re_rec_wallboard","Re_use_wallboard"]
Col_Names_Roof_rafters=["Family_Name","Family_Code","Quantity","Connection_Type","De_con","De_mov","De_Pre"\
           ,"De_tol","Re_use","Re_sec","Re_Tox","Re_rec","Re_rec_cover","Re_use_cover",\
               "Re_tox_cover","Re_rec_sheat","Re_use_sheat","Re_tox_sheat",\
                   "Re_rec_insul","Re_use_insul","Re_tox_insul"]   
##Reading the input files from revit model
df_interior=pd.read_csv("Interior.csv",names=Col_Names)
df_exterior=pd.read_csv("Exterior.csv",names=Col_Names)
df_roof=pd.read_csv("Roof_Rafters.csv",names=Col_Names_Roof_rafters)
df_floor=pd.read_csv("floor.csv",names=Col_Names)

df_exterior["De_con"]=df_exterior["De_con"].mask(df_exterior["De_con"]=="NN",np.nan)
df_exterior["De_con"]=df_exterior["De_con"].astype(float)


def compute(x):
   ##calculates D_Score and R_Score
   ##Since some attributes have missing values for some files, the average is
   ##takenbased on number of attribtes without Null
   # x["De_con"]=x["De_con"].mask(x["De_con"]=="NN",np.nan)
   # x["De_con"].astype(float)
   x['R_atr_Count'] = len(x.iloc[1,8:])
   x["Null_Count"]=x.iloc[:,8:].apply(lambda x:x.isnull().sum(), axis=1)
   x["Sum_De"]=x[["De_con","De_mov","De_Pre","De_tol"]].sum(axis=1)
   x["Sum_Re"]=x.iloc[:,8:-3].sum(axis=1)
   x["R_Score"]=(x["Sum_Re"]/(x["R_atr_Count"]-x["Null_Count"]))
   x["D_Score"]=(x["Sum_De"]/4).mask(x["De_con"].isna(),other=x["Sum_De"]/3)
   x["D_Score"]=round(x["D_Score"],3)
   x["R_Score"]=round(x["R_Score"],3)
   x.drop(["Sum_De","Sum_Re","R_atr_Count","Null_Count"],axis=1,inplace=True)
   
   
def List_Pre(x,y):  
    ##Prepers the output file for developing the combinations
    (a,b)=x.shape 
    info=[]
    Family_code=x.loc[0,"Family_Code"].split("_")[1]
    for i in range(a):
      if Family_code==x.loc[i,"Family_Code"].split("_")[1]:
          info.append([x.loc[i,"Family_Code"],x.loc[i,"Quantity"],x.loc[i,"Connection_Type"], x.loc[i,"D_Score"],x.loc[i,"R_Score"]])
      else:
          y.append(info)
          info=[]
          info.append([x.loc[i,"Family_Code"],x.loc[i,"Quantity"],x.loc[i,"Connection_Type"], x.loc[i,"D_Score"],x.loc[i,"R_Score"]])
      Family_code=x.loc[i,"Family_Code"].split("_")[1]
    y.append(info)
    
    
def Statistic(x):
    ##Generates a brief overview of each Category (D_Score,R_Score,number of Families)
    temp2=pd.DataFrame()
    temp=pd.DataFrame
    for i in range(len(x)):
       temp=pd.DataFrame(x[i]).describe().transpose()
       temp["Category"]=[x[i][0][0],x[i][0][0],x[i][0][0]]
       temp["Index"]=["Quantity","D_Score","R_Score"]
       temp.set_index("Index",inplace=True) 
       temp["mean"]=round(temp["mean"],3)
       temp.drop(["Quantity"],inplace=True)
       temp2=temp2.append(temp)
    temp2["Category"]=temp2["Category"].apply(lambda x:Family_Code_Dict1[x.split("_")[0]]\
                                              +" "+Family_Code_Dict2[x.split("_")[1]])
    temp2.drop(["25%","50%","75%","std"],axis=1,inplace=True)
    return temp2


    
compute(df_interior)
compute(df_exterior)
compute(df_floor)
compute(df_roof) 


# df_interior.to_csv("D:\\aa\\Original_DAS\\Excel_Output\\interior.csv")
# df_exterior.to_csv("D:\\aa\\Original_DAS\\Excel_Output\\exterior.csv")
# df_roof.to_csv("D:\\aa\\Original_DAS\\Excel_Output\\roof.csv")
# df_floor.to_csv("D:\\aa\\Original_DAS\\Excel_Output\\floor.csv")


interior_output=[]
exterior_output=[]
floor_output=[]
roof_output=[]

List_Pre(df_interior,interior_output)
List_Pre(df_exterior,exterior_output)
List_Pre(df_floor,floor_output)
List_Pre(df_roof,roof_output)


interior=Statistic(interior_output)
exterior=Statistic(exterior_output)
roof=Statistic(roof_output)
floor=Statistic(floor_output)

interior.to_csv("D:\\aa\\Original_DAS\\Excel_Output\\Statistic\\interior.csv")
exterior.to_csv("D:\\aa\\Original_DAS\\Excel_Output\\Statistic\\exterior.csv")
roof.to_csv("D:\\aa\\Original_DAS\\Excel_Output\\Statistic\\roof.csv")
floor.to_csv("D:\\aa\\Original_DAS\\Excel_Output\\Statistic\\floor.csv")


# Creating the combinations and output file of combinations

d=len(interior_output)
New=it.product(interior_output[0],interior_output[1],interior_output[2],interior_output[3]\
    ,exterior_output[0],exterior_output[1],exterior_output[2],exterior_output[3]\
    ,exterior_output[4],exterior_output[5],floor_output[0],floor_output[1],floor_output[2],floor_output[3],roof_output[0]\
        ,roof_output[1]+roof_output[2])
rows_gen=(L_1+L_2+L_3+L_4+L_5+L_6+L_7+L_8+L_9+L_10+L_11+L_12+L_13+L_14+L15+L16 for \
          L_1,L_2,L_3,L_4,L_5,L_6,L_7,L_8,L_9,L_10,L_11,L_12,L_13,L_14,L15,L16 in New)
with open("D:\\aa\\Original_DAS\\out.csv","w") as out:
    writer=csv.writer(out)
    writer.writerows([["Family","Quantity","Connection_Type","D_Score","R_Score"]*17])
    writer.writerows(rows_gen)
