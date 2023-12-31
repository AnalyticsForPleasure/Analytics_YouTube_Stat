import pandas as pd

if __name__ == '__main__':
    pd.set_option('display.max_rows', 500)
    df = pd.read_csv(r'C:\Users\Gil\PycharmProjects\YouTube_Stat\data\Global_YouTube_Statistics.csv')
    res = df.loc[:, ['Youtuber']]
    print('*')


    histogram_by_country = df['Country'].value_counts()
    top_10_Country = histogram_by_country.head(n=35)
    print('*')

    # res = df.loc[:, ['Youtuber', 'uploads', 'Country']]
    # grouping_by_Country = res.groupby('Country')
    #
    # for Country_name, mini_df_Country_name in grouping_by_Country:
    #     print(Country_name)
    #     print(mini_df_Country_name)
    #
    #     amount_of_uploads_for_each_country =  mini_df_Country_name['uploads'].sum()
    #     print('*')
    #
    #
    # # Top uploads in each country
    # group_by_country = df


    # Number of youtube categories : We are talking about 18 categories
    # 'Music', 'Film & Animation', 'Entertainment', 'Education', 'Shows', 'People & Blogs', 'Gaming', 'Sports',
    # 'Howto & Style', 'News & Politics', 'Comedy', 'Trailers', 'Nonprofits & Activism', 'Science & Technology',
    # 'Movies', 'Pets & Animals', 'Autos & Vehicles', 'Travel & Events']
    list_of_unique_categories = list(pd.unique(df['category']))
    print('*')
    output_res = df.loc[:, ['Youtuber', 'subscribers', 'category']]

    grouping_by_category = output_res.groupby('category')
    for category_name , mini_df_by_category in grouping_by_category:
        print(category_name)
        print(mini_df_by_category)
        print(f'Number of channels from the same category: {mini_df_by_category.shape[0]}')
        print('*')








