from model import build_model

'''
Generate a sorted list of predictions.  
 
'''

def predict(so_far, num_predictions=10):

    prediction_list = [] #List to capture pred words & frequencies
    pred_word_list = [] #Just prediciton words
    counter = 0

    #Create trie model
    word_trie = build_model("data.txt")

    #Returns sorted list of tuples based on text typed so_far
    result = sorted(word_trie.search(so_far, prediction_list), key=lambda tup: int(tup[1]), reverse = True)

    #Strips out frequences from prediction list
    for word in result:
        if counter < num_predictions:
            pred_word_list.append(word[0])
            counter += 1
        else:
            break

    return pred_word_list
