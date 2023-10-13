def format_features(stock_dict):

    features_list = []
    features_list = [stock_item.get('features', 'Key not supplied') for stock_item in stock_dict]

    return features_list
