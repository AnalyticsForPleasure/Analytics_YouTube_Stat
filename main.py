import pandas as pd

if __name__ == '__main__':

    pd.set_option('display.max_rows', 500)
    df = pd.read_csv(r'C:\Users\Gil\PycharmProjects\YouTube_Stat\data\Global_YouTube_Statistics.csv')
    res = df.loc[:, ['Youtuber']]
    print('*')


    histogram_by_country = df['Country'].value_counts()
    top_10_Country = histogram_by_country.head(n=10)
    print('*')

    res = df.loc[:, ['Youtuber', 'uploads', 'Country']]
    grouping_by_Country = res.groupby('Country')

    for Country_name, mini_df_Country_name in grouping_by_Country:
        print(Country_name)
        print(mini_df_Country_name)

        amount_of_uploads_for_each_country =  mini_df_Country_name['uploads'].sum()
        print('*')


    # Top uploads in each country
    group_by_country = df


