def format_stock_feature(stock_new, features_new, stock_orig):
    item_feature = []
    if not stock_new or not features_new or not stock_orig:
        return item_feature
    
    # from stock_orig list of stock item dicts, prepare a list of list, 
    # comprising a paired list of item_name and a single feature for each stock feature
    item_feature = [[stock['item_name'], feature] for stock in stock_orig 
                    for feature in stock.get('features', '')]
    
    # replace item_name in above with corresponding item_id
    item_feature = [[stock['stock_id'], item_feature[i][1]] for i in range(len(item_feature))
                    for stock in stock_new if stock['item_name'] == item_feature[i][0]]
    
    # replace feature_name in above with feature_id to arrive at the desired list
    item_feature = [[item_feature[i][0], feature['feature_id']] for i in range(len(item_feature))
                    for feature in features_new if feature['feature_name'] == item_feature[i][1]]
    return item_feature