from collections import Counter
import pandas as pd
import csv
def Filter_Gender(Column_to_Filter,Input_to_Filter):
    Filtered_Data = df[~df[Column_to_Filter].isin([Input_to_Filter])]
    return Filtered_Data

def Calculate_By_Province(Month_Data,Province_Data,CSV_to_Read):
    df = pd.read_csv(CSV_to_Read, sep=',',index_col=[0])
    df[Month_Data] = pd.to_datetime(df[Month_Data])
    df['Month'] = df[Month_Data].dt.strftime('%B')
    data = df.groupby(['Month',Province_Data]).size().reset_index(name='count').sort_values(['Month','count'],ascending = [True,False],ignore_index=True).head(6)
    return data

df = pd.read_csv('TMAQ1.csv', sep=',',index_col=[0])
#Convert Column 'report_week' to datetime format
df['report_week'] = pd.to_datetime(df['report_week'])
#Calculate Number of Female Infectors Each Month
Data_Month_Female_Only = Filter_Gender('sex','Male')
Data_Month_Female_Only = Data_Month_Female_Only['report_week'].dt.strftime('%b')
Data_Month_Female_Only =list(Counter(Data_Month_Female_Only).values())

#Calculate Number of Male Infectors Each Month
Data_Month_Male_Only = Filter_Gender('sex','Female')
Data_Month_Male_Only = Data_Month_Male_Only['report_week'].dt.strftime('%b')
Data_Month_Male_Only =list(Counter(Data_Month_Male_Only).values())

print('Total Number of Male and Female Infectors for each month:')
print('February: Males: {0}  Females: {1}'.format(Data_Month_Male_Only[0],Data_Month_Female_Only[0]))
print('March: Males: {0}  Females: {1}'.format(Data_Month_Male_Only[1],Data_Month_Female_Only[1]))
print('April: Males: {0}  Females: {1}\n'.format(Data_Month_Male_Only[2],Data_Month_Female_Only[2]))

# Age Groups of Female Infectors in Descending Order
data_Female_Only = Filter_Gender('sex','Male')
data_Female_Only_AgeRange = data_Female_Only.groupby('age')['age'].count()                            .reset_index(name='No. of Female Infectors:')                            .sort_values(['age'],ascending = False)
print(data_Female_Only_AgeRange)

# Top 2 Months for Age 50 and above Infectors
Data_Age = df[~df['age'].isin(['0-19','20-29','30-39','40-49'])]
Data_Age = Data_Age[~Data_Age['has_travel_history'].isin(['t'])]
Data_Age = Data_Age['report_week'].dt.strftime('%b')
Data_Age =list(Counter(Data_Age).values())
print('\nTop 2 Months for Those Older than 50')
print('          April: {0}               '.format(Data_Age[2]))
print('          March: {0}               '.format(Data_Age[1]))
print('\nFebruary only has {0} infectors older than 50'.format(Data_Age[0]))

# Top 6 Months based on province
Calculate_By_Province('report_week','province','TMAQ1.csv')

