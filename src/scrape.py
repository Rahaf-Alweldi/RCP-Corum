from bs4 import BeautifulSoup
import requests
import pandas as pd


data = {'reference_number':[],
        'watch_URL':[],
         'type':[],
         'brand':[],
         'year_introduced':[],
         'parent_model':[],
         'specific_model':[],
         'nickname':[],
         'marketing_name':[],
         'style':[],
         'currency':[],
         'price':[],
         'image_URL':[],
         'made_in':[],
         'case_shape':[],
         'case_material':[],
         'case_finish':[],
         'caseback':[],
         'diameter':[],
         'between_lugs':[],
         'lug_to_lug':[],
         'case_thickness':[],
         'bezel_material':[],
         'bezel_color':[],
         'crystal':[],
         'water_resistance':[],
         'weight':[],
         'dial_color':[],
         'numerals':[],
         'bracelet_material':[],
         'bracelet_color':[],
         'clasp_type':[],
         'movement':[],
         'caliber':[],
         'power_reserve':[],
         'frequency':[],
         'jewels':[],
         'features':[],
         'description':[],
         'short_description': []}


url = 'https://www.corum-watches.com/'
collections = ['golden-bridge', 'admiral', 'lab', 'heritage', 'bubble']
links = []

for collection in collections:
    req = requests.get(f'https://www.corum-watches.com/collections/{collection}/')
    content = req.content
    soup = BeautifulSoup(content, 'html.parser')

    for link in soup.find_all("div", class_="row_2"):
        for a in link("a"):
            links.append(a.get('href'))


for i in range(len(links)):
    req = requests.get(links[i])
    content = req.content
    soup = BeautifulSoup(content, 'html.parser')

    # reference_number
    reference_number = soup.find(class_='p_infos').find('h4').text.replace("Ref. ", "")

    # watch_URL
    watch_url = req.url
    
    # brand
    brand = soup.find(class_='meta_infos').find('h2').text
    brand = brand[16:21]

    # parent_model
    parent_model = soup.find(class_='p_infos').find('h2').text

    # specific_model
    specific_model = soup.find(class_='p_infos').find('span').text

    # nickname
    try:
        Extract_nickname = soup.find(class_='p_infos').find('h1')
        nickname = ''.join(Extract_nickname.find('br').next_siblings)
    except AttributeError:
        nickname = None

    # marketing_name
    try:
        marketing_name = soup.select_one('.p_p_content p:nth-of-type(3)').text
        if marketing_name.find("Limited") == -1:
            marketing_name = soup.select_one('.p_p_content p:nth-of-type(4)').text
    except AttributeError:
        marketing_name = None


    # currency
    try:
        currency = soup.find(class_='p_button_preis').text
        currency = currency[0:3]
        
    except AttributeError:
        currency = None

    # price
    try:
        price = soup.find(class_='p_button_preis').text
        price = price[4:]
    except AttributeError:
        price = None

    # image_URL
    image_URL = soup.find(class_='w_z_w w_z_show').find("a").attrs['href']

    # made_in
    made_in = "Switzerland"


    # case_material, diameter, case_thickness, water_resistance
    try:
        case = soup.find('ul', attrs={"class": "p_t_ul", "class": "case"})
        case_info = case.find_all("li")
        if case and case_info is not None:
            for li in range(len(case_info)):
                diameter = (case_info[0].text).split(':')[1]
                case_thickness = (case_info[1].text).split(':')[1]
                case_material = (case_info[2].text).split(':')[1]
                water_resistance = (case_info[3].text).split(':')[1]

        else:
            diameter = None
            case_thickness = None
            case_material = None
            water_resistance = None
    except AttributeError:
            diameter = None
            case_thickness = None
            case_material = None
            water_resistance = None

    # between_lugs, bracelet_material, bracelet_color
    bracelet_records = []
    bracelet_column_list = []
    try:
        bracelet = soup.find_all('ul', attrs={"class": "p_t_ul", "class": "strap"})
        for result in bracelet:
            span_name = result.find_all("span", attrs={"class": "p_name"})
            span_results = result.find_all("span", attrs={"class": "p_value"})
            
            for span in span_results:
                bracelet_records.append(span.text)
            
            for span in span_name:
                bracelet_column_list.append(span.text)
                
        bracelet_material = bracelet_records[0]
        bracelet_color = bracelet_records[1]
        between_lugs = bracelet_records[2]

    except AttributeError:
        bracelet_material = None
        bracelet_color = None
        between_lugs = None

    except IndexError:
        if links[i] == links[41]:
            bracelet_material = None
            bracelet_color = None
            between_lugs = None

        elif bracelet_column_list[1] != 'Color:  ':
            bracelet_color = None
            between_lugs = bracelet_records[1]

        else:
            bracelet_color = None
            between_lugs = None

    # clasp_type
    Buckle_records =[]
    Buckle_column_list = []
    try:
        Buckle = soup.find_all('ul', attrs={"class": "p_t_ul", "class": "buckle"})
        for result in Buckle:
            span_name = result.find_all("span", attrs={"class": "p_name"})
            span_results = result.find_all("span", attrs={"class": "p_value"})
            
            for span in span_results:
                Buckle_records.append(span.text)
            
            for span in span_name:
                Buckle_column_list.append(span.text)
                
        clasp_type = Buckle_records[0]
            
    except AttributeError:
        clasp_type = None

    except IndexError:
        if links[i] == links[41]:
            clasp_type = None

    # movement, caliber, power_reserve, frequency, jewels, features
    movement_records =[]
    try:
        movement_section = soup.find_all('ul', attrs={"class": "p_t_ul", "class": "movement"})
        for result in movement_section:
            span_name = result.find_all("span", attrs={"class": "p_name"})
            span_results = result.find_all("span", attrs={"class": "p_value"})
            
            for span in span_results:
                movement_records.append(span.text)
                
        movement = movement_records[5]
        caliber = movement_records[0]
        power_reserve = movement_records[1]
        frequency = movement_records[2]
        jewels = movement_records[4]
        features = movement_records[6]

            
    except AttributeError:
        movement = None
        caliber = None
        power_reserve = None
        frequency = None
        jewels = None
        features = None

    except IndexError:
        if links[i] == links[41]:
            movement = None
            caliber = None
            power_reserve = None
            frequency = None
            jewels = None
            features = None
    
    # description
    try:
        description = soup.find(class_='p_p_content').find_all('p')[0:2]
        description = description[0].text + description[1].text
    except IndexError:
        if links[i] == links[41]:
            description = None



    data['reference_number'].append(reference_number)
    data['watch_URL'].append(watch_url)
    data['brand'].append(brand)
    data['parent_model'].append(parent_model)
    data['specific_model'].append(specific_model)
    data['nickname'].append(nickname)
    data['marketing_name'].append(marketing_name)
    data['currency'].append(currency)
    data['price'].append(price)
    data['image_URL'].append(image_URL)
    data['made_in'].append(made_in)
    data['case_material'].append(case_material)
    data['diameter'].append(diameter)
    data['between_lugs'].append(between_lugs)
    data['case_thickness'].append(case_thickness)
    data['water_resistance'].append(water_resistance)
    data['bracelet_material'].append(bracelet_material)
    data['bracelet_color'].append(bracelet_color)
    data['clasp_type'].append(clasp_type)
    data['movement'].append(movement)
    data['caliber'].append(caliber)
    data['power_reserve'].append(power_reserve)
    data['frequency'].append(frequency)
    data['jewels'].append(jewels)
    data['features'].append(features)
    data['description'].append(description)


# Store the dictionary into a dataframe
Data_Set = pd.DataFrame.from_dict(data, orient='index')
Data_Set = Data_Set.transpose()
Data_Set.head()

 
# saving the dataframe into CSV file
Data_Set.to_csv('data/Corum_timestamp.csv', index=False)