def format_features(stock_dict):
    # using list comprehension loop on list to find individual stock item 
    # and then loop again on features key to seperate out individual features
    features_list = [[feature] for stock_item in stock_dict for feature in stock_item.get('features', '')]
    if len(features_list) == 1:
        return features_list
    else:
        # remove any repeate feature in the list of lists of features 
        unique_features_list = [features_list[i] for i in range(len(features_list)) if features_list[i] not in features_list[i + 1:]]
        return unique_features_list
